from django.db import models
from users.models import Author


# Create your models here.
class BookCategory(models.Model):
    category_name = models.CharField(default="", max_length=30)
    category_code = models.CharField(default="", max_length=30)
    cetegory_type = models.CharField(default="", max_length=30)
    is_tab = models.BooleanField(default=False)
    add_time = models.DateTimeField()
    total_number =

    class Meta:
        verbose_name = 'Type Category'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name


# TODO add django-tinymce
class Book(models.Model):
    book_name = models.CharField()
    book_image = models.ImageField()
    book_author = models.OneToOneField(Author)
    book_status = models.BooleanField()
    contract_status = models.BooleanField()
    book_type = models.ForeignKey()
    book_genre = models.ForeignKey()
    book_short_description = models.TextField(verbose_name='Short descritpion')
    book_description = models.Ueditor
    total_words = models.IntegerField(verbose_name='Total_words', default=0, editable=False)
    chapter_count = models.IntegerField(verbose_name='Chapter Count', default=0, editable=False)
    total_vote = models.IntegerField(verbose_name='Total vote', default=0, editable=False)
    weekly_vote = models.IntegerField(verbose_name='Weekly vote', default=0, editable=False)
    total_click = models.IntegerField(verbose_name='Total Click', default=0, editable=False)
    added_time = models.DateTimeField(verbose_name='Added time', auto_now_add=True, editable=False)
    last_update = models.DateTimeField(verbose_name='last update', auto_now=True, editable=False)


class Chapter(models.Model):
    book_id = models.ForeignKey(Book)
    chapter_title = models.CharField
    chapter_body = models.Ueditor
