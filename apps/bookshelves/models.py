# Create your models here.
from django.db import models

from users.models import User
from books.models import Chapter, Book


# Create your models here.


class BookMark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', blank=True, null=True,
                             related_name='user_marked')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book', blank=True, null=True,
                             related_name='marked_book')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name='Chapter',
                                related_name='marked_chapter')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="added time")

    class Meta:
        verbose_name = 'Bookmark'
        db_table = 'Bookmark'

    def __str__(self):
        return "{0}".format(self.chapter.chapter_title)


class Bookcase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User bookcase')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book', blank=True, null=True)
    bookmark = models.ForeignKey(BookMark, on_delete=models.CASCADE, verbose_name='bookmark',
                                 related_name='marked_book', blank=True, null=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"Added time")

    class Meta:
        verbose_name = 'Bookcase'
        verbose_name_plural = verbose_name
        db_table = 'Bookcase'

    def __str__(self):
        return self.user.username
