from allauth.account.models import EmailAddress
from django.conf import settings
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, UserProfile


@receiver(post_save, sender=User)
def create_user_related_objects(sender, instance, created, **kwargs):
    if created:
        try:
            UserProfile.objects.create(
                user=instance,
            )
        except Exception as e:
            if settings.DEBUG:
                raise e
            else:
                pass
