import time
from typing import Any

from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    """Django test command."""

    help = (
        "Description of the test command"
    )

    def handle(self, *args: Any, **options: Any) -> str | None:
        """Entry point for command."""

        self.stdout.write("This is my test command")

