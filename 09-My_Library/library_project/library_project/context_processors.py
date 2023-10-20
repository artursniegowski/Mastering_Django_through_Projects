"""Global context - adding current_year to the context"""
import datetime
from django.http import HttpRequest


def get_current_year_context(request: HttpRequest) -> dict[str, int]:
    return {
        'current_year': datetime.datetime.now().year
    }
