from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import *


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance)
        instance.profile.save()
        if profile.get_user_role_display() == 'Reader':
            reader = Reader(user=instance.profile)
            instance.profile.reader.save()
        if profile.get_user_role_display() == 'Author':
            author = Author(user=instance.profile)
            instance.profile.author.save()
