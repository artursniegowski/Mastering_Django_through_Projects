from django import template
from django.utils import timezone

register = template.Library()

@register.filter(name='format_datetime')
def format_datetime(value: str, arg: str):
    """returns data formated as ' 29-05-2023'
    the arg should be the valid format for the function strftime"""
    if value:
        return value.strftime(arg)
    return value

@register.filter(name='divide_to_num_percent')
def divide_to_num_percent(value: float, total: float) -> int:
    """this will take the value and devide it by the total and then return the percentage of the total, but it cant be greater than 100
    percentage will be rounded down to the whole num"""
    new_value = int(float(value)*100/float(total))
    if new_value >= 100:
        return 100
    return new_value

@register.filter(name='get_oldest_booking')
def get_oldest_booking(bookings):
    """returns the oldes booking, if the queryset is empty it will return None"""
    return bookings.order_by('booking_date').first()

@register.filter(name="timezone_localtime")
def timezone_localtime(date_time_object):
    """make sure the time will be outputed in the local time zone"""
    return timezone.localtime(date_time_object)

@register.filter(name='time_difference')
def time_difference(date_time_object):
    """calculates the difference in days hours and minutes to the given date from now, accomodates fro the timezone difference"""
    current_time = timezone.localtime(timezone.now())
    date_time_object = timezone.localtime(date_time_object)
    diff_days, diff_hours, diff_minutes = 0, 0, 0

    if current_time < date_time_object:
        time_difference = date_time_object - current_time
        diff_days, diff_hours, diff_minutes = time_difference.days, time_difference.seconds // 3600, (time_difference.seconds // 60) - ((time_difference.seconds // 3600) * 60)

    return {
        'days': diff_days,
        'hours': diff_hours,
        'minutes': diff_minutes, 
    }
    