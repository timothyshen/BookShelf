# Register your models here.
from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Reader, User, Author, Admin


class ReaderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReaderForm, self).__init__(*args, **kwargs)
        excluded_user = Reader.objects.all()
        if self.instance:
            excluded_user = excluded_user.exclude(pk=self.instance.pk)
        self.fields['user'].queryset = User.objects.exclude(id__in=excluded_user.values('user_id'))


class UserInline(admin.TabularInline):
    model = User


class ReaderAdmin(admin.ModelAdmin):
    inlines = [UserInline]


admin.site.register(Reader, UserAdmin)
admin.site.register(Admin)
