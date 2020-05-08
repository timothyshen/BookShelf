# Register your models here.
from django.contrib import admin
from django.http import request
from django import forms

from .models import *



@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    model = Profile
    extra = 0
    # fields = ('user.username', 'user.password')
