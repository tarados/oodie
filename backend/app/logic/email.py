from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_email(to, subject, message):
    send_mail(subject, '', settings.FROM_EMAIL, to, html_message=message)


def send_email_template(to, subject, template_name, template_context):
    message = render_to_string(template_name, template_context)
    send_email(to, subject, message)
