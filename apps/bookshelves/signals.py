from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Bookcase


@receiver(post_save, sender=Bookcase)
def create_bookfav(sender, instance=None, created=False, **kwargs):
    if created:
        book = instance.book
        book.fav_num += 1
        book.save()


@receiver(post_delete, sender=Bookcase)
def delete_bookfav(sender, instance=None, created=False, **kwargs):
    goods = instance.goods
    if goods.fav_num != 0:
        goods.fav_num -= 1
    else:
        goods.fav_num = 0
    goods.save()
