"""
Healt Check of the web app
"""
from django.http import JsonResponse, HttpRequest


def health_check(request: HttpRequest) -> JsonResponse:
    """Checking the health of the applicaiton"""
    # TODO: add any relevant health checks as:
    # database queries, API checks, or any other checks relevant to your application's health # noqa
    return JsonResponse({'status': 'healthy'})
