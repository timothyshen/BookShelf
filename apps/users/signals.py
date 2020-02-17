from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from .models import *


@receiver(post_save, sender=Profile)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        if Profile.get_user_role_display() == 'Reader':
            reader = Reader(user=instance.profile)
            instance.profile.reader.save()
        if Profile.get_user_role_display() == 'Author':
            author = Author(user=instance.profile)
            instance.profile.author.save()
