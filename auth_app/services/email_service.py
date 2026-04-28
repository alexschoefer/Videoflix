from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

def send_activation_email(user, activation_link):
    """
    Send an account activation email to the user.
    Args:
        user: The user object for whom the activation email is being sent.
        token: The activation token to be included in the email.
    """
    subject = 'Confirm your email'
    from_email = settings.DEFAULT_FROM_EMAIL
    user_name = user.first_name if user.first_name else user.email
    to_email = user.email

    # Render the email template with the user's information and token
    html_content = render_to_string('activation_email.html', {
        'user_name': user_name,
        'activation_link': activation_link,
    })

    # Create the email message
    email = EmailMultiAlternatives(subject, '', from_email, [to_email])
    email.attach_alternative(html_content, "text/html")

    # Send the email
    email.send()