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
    html_content = render_to_string('emails/account_activation_email.html', {
        'user_name': user_name,
        'activation_link': activation_link,
    })
    email = EmailMultiAlternatives(subject, '', from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()


def send_password_reset_email(user, reset_link):
    """
    Send a password reset email to the user.
    Args:
        user: The user object for whom the password reset email is being sent.
        reset_link: The password reset link to be included in the email.
    """
    subject = 'Reset your Password'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = user.email

    # Render the email template with the user's information and reset link
    html_content = render_to_string('password_reset_email.html', {
        'reset_link': reset_link,
    })

    # Create the email message
    email = EmailMultiAlternatives(subject, '', from_email, [to_email])
    email.attach_alternative(html_content, "text/html")

    # Send the email
    email.send()