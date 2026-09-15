import os
import resend


def send_contact_email(inquiry):

    resend.api_key = os.getenv("RESEND_API_KEY")

    subject = f"New Contact Inquiry from {inquiry.name}"

    message = f"""
New inquiry received.

Name: {inquiry.name}
Email: {inquiry.email}
Travel Dates: {inquiry.travel_dates}

Message:
{inquiry.message}
"""

    resend.Emails.send({
        "from": "Origami Limousines <onboarding@resend.dev>",
        "to": [os.getenv("ADMIN_EMAIL")],
        "subject": subject,
        "text": message,
    })