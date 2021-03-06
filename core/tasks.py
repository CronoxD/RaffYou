
from __future__ import absolute_import, unicode_literals

from celery import shared_task

# Django
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# Utilities
import requests


@shared_task
def send_email_html(subject, template, from_email, recipient_list):
    html_message = render_to_string(template)
    plain_message = strip_tags(html_message)
    send_mail(
        subject,
        plain_message,
        from_email,
        recipient_list,
        html_message=html_message
    )

    return {
        'subjects': subject,
        'template': template,
        'recipients': recipient_list,
    }


@shared_task
def send_email_text(subject, content, from_email, recipient_list):

    send_mail(
        subject,
        content,
        from_email,
        recipient_list
    )

    return {
        'subjects': subject,
        'recipients': recipient_list,
    }


@shared_task
def send_telegram_message(text):
    data = {
        'text': text,
        'parse_mode': 'MarkdownV2',
        'chat_id': settings.TELEGRAM_CHAT_ID
    }
    url = f'{settings.TELEGRAM_URL}/sendMessage'
    res = requests.post(url, data=data)
    return res.text


@shared_task
def debug_task(x, y):
    print(f'Debug task celery args: {x} + {y}')
    return x + y
