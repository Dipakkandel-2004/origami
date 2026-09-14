

from django.core.mail import send_mail
from django.conf import settings


def send_contact_email(inquiry):

    subject = f"New Contact Inquiry from {inquiry.name}"

    message = f"""
New inquiry received.

Name: {inquiry.name}
Email: {inquiry.email}
Travel Dates: {inquiry.travel_dates}

Message:
{inquiry.message}
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.ADMIN_EMAIL],
        fail_silently=False,
    )