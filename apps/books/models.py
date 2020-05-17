from django.conf import settings
from django.db import models


# from tinymce.models import HTMLField
# Create your models here.


class BookCategory(models.Model):
    # CATEGORY_TYPE = (
    #     (1, "Primary type"),
    #     (2, "Secondary genre"),
    # )
    category_name = models.CharField(default="", max_length=30, verbose_name='Category name')
    category_code = models.CharField(default="", max_length=30, verbose_name='Category code')
    # category_type = models.IntegerField(default='', verbose_name='Category Type')
    # parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="Parent category",
    #                                     help_text="Parent list",
    #                                     related_name="sub_cat", on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name='is Navigate')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Added time')
    total_number = models.BigIntegerField(default=0, verbose_name='Total Number', editable=False)

    class Meta:
        verbose_name = 'Type Category'
        verbose_name_plural = verbose_name
        db_table = 'Book Genre'

    def __str__(self):
        return self.category_name


# TODO add django-tinymce

class Book(models.Model):
    BOOK_STATUS = (
        ('Ongoing', u'Ongoing'),
        ('Completed', u'Completed')
    )
    book_name = models.CharField(default="", max_length=30, verbose_name='Book name', unique=True)
    book_image = models.ImageField(default="", max_length=30, verbose_name='Book image')
    book_status = models.CharField(choices=BOOK_STATUS, default='Ongoing', verbose_name='Book Status', max_length=150,
                                   null=True)
    # contract_status = models.BooleanField()
    book_author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.SET_NULL,
                                    verbose_name='author',
                                    related_name='author',
                                    null=True)
    book_type = models.ForeignKey(BookCategory,
                                  on_delete=models.CASCADE,
                                  verbose_name='book type',
                                  related_name='book_type',
                                  null=True)
    # book_genre = models.ForeignKey()
    book_short_description = models.TextField(verbose_name='Short description', default='')
    book_description = models.TextField(verbose_name='Book Description', default='')
    # non-editable values
    total_words = models.IntegerField(verbose_name='Total_words', default=0, editable=False)
    chapter_count = models.IntegerField(verbose_name='Chapter Count', default=0, editable=False)
    total_vote = models.IntegerField(verbose_name='Total vote', default=0, editable=False)
    weekly_vote = models.IntegerField(verbose_name='Weekly vote', default=0, editable=False)
    total_click = models.IntegerField(verbose_name='Total Click', default=0, editable=False)
    fav_num = models.IntegerField(verbose_name='Total favorite number', default=0, editable=False)
    added_time = models.DateTimeField(verbose_name='Added time', auto_now_add=True, editable=False)
    last_update = models.DateTimeField(verbose_name='last update', auto_now=True, editable=False)

    def get_chapter_number(self):
        chapter_count = Chapter.objects.filter(self.id).count()
        return chapter_count

    def get_book_name(self):
        return self.book_name

    class Meta:
        db_table = 'Books'
        verbose_name = 'Novel'
        verbose_name_plural = verbose_name


class Chapter(models.Model):
    PUBLISH_STATUS = (
        ('Published', u'Published'),
        ('Draft', u'Draft'),
        ('Unpublished', u'Unpublished'),
    )
    chapter_title = models.CharField(verbose_name='Chapter title', default='', max_length=150)
    chapter_body = models.TextField(verbose_name='Chapter text', default='')
    word_count = models.IntegerField(verbose_name='Word count', default=0)
    created_time = models.DateTimeField(verbose_name='Created time', auto_now_add=True, editable=False)
    last_update = models.DateTimeField(verbose_name='last update', auto_now=True, editable=False)
    publish_status = models.CharField(choices=PUBLISH_STATUS, default='Published', max_length=150)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='chapter', null=True, related_name='chapter')
