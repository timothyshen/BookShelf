from django.db import models

from books.models import Book
from users.models import Reader


# Create your models here.


class Bookcase(models.Model):
    user = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name='User bookcase')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"Added time")

    class Meta:
        verbose_name = 'Bookcase'
        verbose_name_plural = verbose_name
        unique_together = ('user', "book")

    def __str__(self):
        return self.user.user.username
