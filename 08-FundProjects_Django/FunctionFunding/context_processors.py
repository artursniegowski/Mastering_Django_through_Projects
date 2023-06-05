import datetime

# this context needs to be registered in settings.py
def get_current_year_context(request):
    current_year = datetime.datetime.now().year
    return {
        'current_year': current_year
    }