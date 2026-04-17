"""
Users app Celery tasks.

Run worker:  celery -A config.celery_app worker -l info
"""

import logging

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

logger = logging.getLogger(__name__)
User   = get_user_model()


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_welcome_email_task(self, user_id):
    """Send a welcome email to a newly registered user."""
    try:
        user = User.objects.get(pk=user_id)
        context = {"user": user, "site_name": settings.SITE_NAME, "site_url": settings.SITE_URL}
        html_message = render_to_string("emails/welcome.html", context)
        plain_message = strip_tags(html_message)

        send_mail(
            subject=f"Welcome to {settings.SITE_NAME}!",
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            html_message=html_message,
        )
        logger.info("Welcome email sent to %s", user.email)
    except User.DoesNotExist:
        logger.error("send_welcome_email_task: user %s not found", user_id)
    except Exception as exc:
        logger.exception("send_welcome_email_task failed for user %s", user_id)
        raise self.retry(exc=exc)


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_email_verification_task(self, user_id, verification_url):
    """Send an email address verification link."""
    try:
        user = User.objects.get(pk=user_id)
        context = {
            "user": user,
            "verification_url": verification_url,
            "site_name": settings.SITE_NAME,
        }
        html_message = render_to_string("emails/verify_email.html", context)
        plain_message = strip_tags(html_message)

        send_mail(
            subject=f"Verify your email — {settings.SITE_NAME}",
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            html_message=html_message,
        )
        logger.info("Verification email sent to %s", user.email)
    except Exception as exc:
        raise self.retry(exc=exc)
