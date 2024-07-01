"""
Test custom Django management commands.
"""

from unittest.mock import MagicMock, patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase  # without database
from psycopg import OperationalError as PsycopgError


@patch("management.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """Test commands."""

    # django.test.testcases.DatabaseOperationForbidden: Database queries
    # to 'default' are not allowed in SimpleTestCase subclasses
    # add 'default' to core.tests.test_commands.CommandTest.databases to
    # silence this failure.
    # we are using the database in the command to wait_for_db to check
    # that it is connected, this is why we have to silence it here
    databases = ["default"]

    def test_wait_for_db_ready(self, patched_check: MagicMock) -> None:
        """Test waiting for database if database ready."""
        patched_check.return_value = True

        call_command("wait_for_db")

        patched_check.assert_called_once_with(databases=["default"])

    # patching sleep so we dont have to wait each time 1 sec
    @patch("time.sleep")
    def test_wait_for_db_delay(
        self, patched_sleep: MagicMock, patched_check: MagicMock
    ) -> None:
        """Test waiting for databse when getting OperationalError."""
        patched_check.side_effect = [PsycopgError] * 2 + [OperationalError] * 3 + [True]

        call_command("wait_for_db")

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=["default"])
