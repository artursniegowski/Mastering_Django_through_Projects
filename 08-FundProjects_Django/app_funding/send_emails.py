from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class TemplateEmails:
    BOOKING_REQUEST = 'app_funding/emails/booking_request.html'
    BOOKING_EXTENSION = 'app_funding/emails/booking_extension.html'

    @classmethod
    def is_included(cls, given_value: str) -> bool:
        """
        check if given value is part of the values in the class
        """ 
        return given_value in vars(cls).values()


def send_email_template(subject, recipient_list, context, template_version: TemplateEmails):
    """this will send one email including the list of recipies for all users - intended to send a email directly to a specific person"""
    assert TemplateEmails.is_included(template_version), f"Error: {template_version} is not included in defined TemplateEmails class"
    # Render the email template with the provided context
    html_message = render_to_string(template_version, context)
    plain_message = strip_tags(html_message)  # Strip HTML tags for the plain text version
    
    # Send the email
    num = send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL ,recipient_list,html_message=html_message)
    return num

# TODO: to finish , to test ! this would be for sednign multiple emails
# def send_multiple_email_template(subject, recipient_list, context, template_version: TemplateEmails):
#     """This is intended to send to all recipients seperate emails """
#     assert TemplateEmails.is_included(template_version), f"Error: {template_version} is not included in defined TemplateEmails class"
#     # Render the email template with the provided context
#     html_message = render_to_string(template_version, context)
#     plain_message = strip_tags(html_message)  # Strip HTML tags for the plain text version
    
#     for recipient in recipient_list:
#         pass
    
#     # Send the email
#     send_mass_mail()
#     num = send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL ,recipient_list,html_message=html_message)
#     return num
