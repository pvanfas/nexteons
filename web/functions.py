# send contact mail using data(form.cleaned_data:name,email,phone,subject,message,timestamp)
from django.core.mail import send_mail
from django.conf import settings


def send_contact_mail(data):
    print(data)
    subject = f"New Contact Form Submission from {data.name}"
    message = f"""
    You have received a new contact form submission from {data.name} with the following details:
        Name: {data.name}
        Email: {data.email}
        Phone: {data.phone}
        Subject: {data.subject}
        Message: {data.message}
        Timestamp: {data.timestamp}
    """
    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, ["anfasperingavu@gmail.com"])
    except Exception as e:
        print(e)
