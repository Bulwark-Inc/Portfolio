from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def send_custom_email(subject, template_name, context, recipient_list, sender=None, fail_silently=False):
    """
    Sends an HTML email rendered from a template.
    
    Parameters:
    - subject: Subject of the email
    - message_body: Body of the email
    - recipient_list: List of recipients
    - sender: Optional custom sender email. Defaults to EMAIL_HOST_USER.
    - fail_silently: If True, suppress errors.
    """
    sender_email = sender or settings.EMAIL_HOST_USER
    html_message = render_to_string(template_name, context)

    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=sender_email,
        to=recipient_list,
    )
    email.content_subtype = 'html' 
    email.send(fail_silently=fail_silently)
