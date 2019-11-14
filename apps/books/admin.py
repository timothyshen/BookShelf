# Register your models here.
from django import forms
from django.contrib import admin

from .models import BookCategory, Book


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    # fields = (
    #     ('Book Info', {'fields': (
    #         'book_name'
    #     )}),
    #     # ('Data Info', {'fields': (
    #     #
    #     # )})
    # )
    list_display = ["book_name", 'book_author']
    search_fields = ['book_name', ]
    # list_editable = ["is_hot", ]
    list_filter = ["book_name"]
    # style_fields = {"goods_desc": "ueditor"}

    # class GoodsImagesInline(object):
    #     model = GoodsImage
    #     exclude = ["add_time"]
    #     extra = 1
    #     style = 'tab'

    # inlines = [GoodsImagesInline]
    pass

admin.site.register(BookCategory)
