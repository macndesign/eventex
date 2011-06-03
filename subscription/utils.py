# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_subscription_email(subscription):
    if subscription is None:
        raise ValueError('This function must be conected to: post_save of Subscription')

    subject = u'Inscrição no Eventex realizada com sucesso.'
    message = render_to_string(
        'subscription/email.txt',
        {'subscription': subscription}
    )

    send_mail(
        subject = subject,
        message = message,
        from_email = settings.DEFAULT_FROM_EMAIL,
        recipient_list = [subscription.email]
    )
