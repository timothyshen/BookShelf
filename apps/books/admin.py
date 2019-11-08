# Register your models here.
from django import forms
from django.contrib import admin

from.models import BookCategory, Book

admin.site.register(BookCategory)
admin.site.register(Book)