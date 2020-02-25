# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '04/12/2019 22:44'

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from users.models import Profile
from .models import Bookcase


@receiver(post_save, sender=Bookcase)
def create_bookcase(sender, instance=None, created=False, **kwargs):
    if created:
        book = instance.Book
        book.is_added = True
        book.save()


@receiver(post_delete, sender=Bookcase)
def delete_bookcase(sender, instance=None, created=False, **kwargs):
    book = instance.Book
    book.is_added = False
    book.save()
