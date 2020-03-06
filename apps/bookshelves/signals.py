from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Bookcase


@receiver(post_save, sender=Bookcase)
def create_bookfav(sender, instance=None, created=False, **kwargs):
    if created:
        book = instance.book
        book.fav_num += 1
        book.save()

