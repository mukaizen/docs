"""
User signals.

Signals let you react to model events without coupling code.
Add any post-save / post-delete hooks here.
"""

import logging

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

logger = logging.getLogger(__name__)

User = get_user_model()


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Auto-create a DRF auth token whenever a new user is created."""
    if created:
        Token.objects.get_or_create(user=instance)
        logger.debug("Auth token created for new user: %s", instance.email)


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance=None, created=False, **kwargs):
    """
    Send a welcome email after registration.
    Uses Celery so it doesn't block the request.
    Uncomment once you have email configured.
    """
    if created:
        pass
        # from apps.users.tasks import send_welcome_email_task
        # send_welcome_email_task.delay(instance.pk)
