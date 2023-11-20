import logging
import random
import string

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

logger = logging.getLogger(__name__)

def send_email_with_html_body(subjet: str, receivers: list, template: str, context: dict):
    """ this function send a customize email to pecif user

    try:
        message = render_to_string(template, context)
        send_mail(
            subjet,
            message,
            settings.EMAIL_HOST_USER,
            receivers,
            fail_silently=True,
            html_message=message
        )
        return True
    except Exception as e:
        logger.error(e)
    """
    try:
        message = render_to_string(template, context)
        send_mail(
            subjet,
            message,
            settings.EMAIL_HOST_USER,
            receivers,
            fail_silently=True,
            html_message=message
        )
        return True
    except Exception as e:
        logger.error(e)
    return False




def Car_Id(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    chaine_aleatoire = ''.join(random.choice(caracteres) for _ in range(longueur))
    return chaine_aleatoire

# Exemple d'utilisation avec une chaîne de longueur 12
chaine_resultat = Car_Id(12)
print(chaine_resultat)