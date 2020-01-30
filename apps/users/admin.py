# Register your models here.
from django.contrib import admin
from django.http import request
from django import forms

from .models import *



class ReaderInlines(admin.StackedInline):
    model = Reader
    extra = 0
    max_num = 1
    readonly_fields = ['is_user_vip', 'vip_validate']


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    model = Profile
    extra = 0
    # fields = ('user.username', 'user.password')
    inlines = [ReaderInlines]

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if isinstance(inline, ReaderInlines) and obj.get_user_role_display() == 'Reader':
                yield inline.get_formset(request, obj), inline

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     super().save_model(request, obj, form, change)

