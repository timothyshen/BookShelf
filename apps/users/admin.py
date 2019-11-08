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
            excluded_user = excluded_user.exclude(pk=self.instance.pk)
        self.fields['user'].queryset = User.objects.exclude(id__in=excluded_user.values('user_id'))


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    form = ReaderForm
    fieldsets = (
        ('User Info', {'fields': ('user', 'user_mobile', 'user_gender', 'user_icon', 'user_birthday')}),
        ('VIP status', {'fields': ('is_user_vip', 'vip_validate')})
    )
    # inlines = [UserList]


class UserList(admin.StackedInline):
    model = User


admin.site.register(Role)
admin.site.register(Author)
admin.site.register(Admin)
