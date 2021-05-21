import datetime
from asgiref.sync import sync_to_async
# ADDITIONAL
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    print(reset_password_token.user.email)

    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    year = datetime.date.today().year
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.get_fullname,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(reverse('account:password_reset:reset-password-request'), reset_password_token.key),
        'token': reset_password_token.key,
        'life_time':settings.DJANGO_REST_MULTITOKENAUTH_RESET_TOKEN_EXPIRY_TIME,
        'year': year,
    }

    # render email text
    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Şifrəni yenilə - {title}".format(title="Tech.az"),
        # message:
        email_plaintext_message,
        # from:
        "info@tech.az",
        # to:
        [reset_password_token.user.email]
    )
    
    msg.attach_alternative(email_html_message, "text/html")
    sync_to_async(msg.send())
