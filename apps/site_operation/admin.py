from django.contrib import admin
from .models import *
from django import forms

# Register your models here.

admin.site.register(IndexImage)
admin.site.register(IndexPage)
admin.site.register(CategoryImagePage)
admin.site.register(CategoryPage)
admin.site.register(ContentType)
