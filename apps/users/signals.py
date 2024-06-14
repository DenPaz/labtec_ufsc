from allauth.account.models import EmailAddress
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            UserProfile.objects.create(user=instance)
        except Exception as e:
            if settings.DEBUG:
                raise e
            else:
                pass


@receiver(post_save, sender=User)
def create_email_address(sender, instance, created, **kwargs):
    if created:
        try:
            EmailAddress.objects.create(user=instance, email=instance.email, primary=True, verified=False)
        except Exception as e:
            if settings.DEBUG:
                raise e
            else:
                pass
