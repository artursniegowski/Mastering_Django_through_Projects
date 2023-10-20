"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections
from typing import Any
import time
from psycopg import OperationalError as PsycopgError


class Command(BaseCommand):
    """Django command to wait for database."""
    help = "Django command to wait for database."

    def handle(self, *args: Any, **options: Any) -> str | None:
        """Entry point for command."""

        self.stdout.write("Waiting for database...")
        db_conn = None
        time_to_wait_s = 1

        while not db_conn:
            try:
                self.check(databases=['default'])
                # the  above  check was not enough, github actions raised
                # an error that the databases was not redy yet
                # this is why we adding extra check
                # Try to establish a connection by executing a test query
                connections['default'].cursor().execute('SELECT 1')
                db_conn = True  # if the check is succeesful
            except (PsycopgError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(time_to_wait_s)

        self.stdout.write(self.style.SUCCESS("Database available!"))
