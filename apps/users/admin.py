# Register your models here.
from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Reader, User, Author, Admin


class ReaderInlines(admin.TabularInline):
    model = Reader
    extra = 0
    readonly_fields = ['is_user_vip', 'vip_validate']


class AuthorInlines(admin.TabularInline):
    model = Author
    extra = 0
    readonly_fields = ['contract_number']


class ReaderAdmin(UserAdmin):
    inlines = []

# admin.site.register(Reader, ReaderAdmin)
# admin.site.register(Admin)
