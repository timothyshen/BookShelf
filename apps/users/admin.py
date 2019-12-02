# Register your models here.
from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Reader, User, Author, Admin


class ReaderInlines(admin.StackedInline):
    model = Reader
    extra = 0
    readonly_fields = ['is_user_vip', 'vip_validate']


class AuthorInlines(admin.TabularInline):
    model = Author
    extra = 0
    readonly_fields = ['contract_number']


class UserAdmin(UserAdmin):
    model = User

    # inlines = []
    list_filter = ('user_role',)

    date_hierarchy = 'date_joined'
    ordering = ('date_joined',)

    def get_inline_instances(self, request, obj=None):
        if obj.user_role == 'Reader':
            return ReaderInlines(self.model, self.admin_site)

admin.site.register(User, UserAdmin)
# admin.site.register(Admin)
