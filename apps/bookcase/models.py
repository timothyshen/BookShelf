from django.db import models
from users.models import Reader
from users.models import Book
from django.contrib.auth import get_user_model


# Create your models here.


class Bookcase(models.Model):
    user = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name='User bookcase')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = 'Bookcase'
        verbose_name_plural = verbose_name
        unique_together = ('user', "book")

    def __str__(self):
        return self.user.user.username
