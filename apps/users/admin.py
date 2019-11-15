# Register your models here.
from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Reader, Role, User, Author, Admin


class ReaderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReaderForm, self).__init__(*args, **kwargs)
        excluded_user = Reader.objects.all()
        if self.instance:
            excluded_user = excluded_user.exclude(pk = self.instance.pk)
        self.fields['user'].queryset = User.objects.exclude(id__in = excluded_user.values('user_id'))


class UserInline(admin.TabularInline):
    model = User


class RoleInline(admin.TabularInline):
    model = Role


@admin.register(Reader, Author)
class ReaderAdmin(admin.ModelAdmin):
    form = ReaderForm

    inlines = [RoleInline, UserInline]


admin.site.register(Role)
admin.site.register(Admin)
