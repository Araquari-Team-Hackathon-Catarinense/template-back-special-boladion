import os

from celery import shared_task
from django.core.mail import send_mail
from django.utils.html import strip_tags

from django_project.settings import BASE_DIR, EMAIL_HOST_USER


@shared_task
def send_forget_password_email(email, token):
    from_email = EMAIL_HOST_USER

    # Renderizando o template HTML
    with open(
        os.path.join(BASE_DIR, "emails/send_forget_password_email_template.html"),
        "r",
    ) as file:
        html = file.read()
        html = html.replace("token", token)

    recipient_list = [email]

    subject = "Recuperação de Senha"
    plain_message = strip_tags(html)

    send_mail(subject, plain_message, from_email, recipient_list, html_message=html)
