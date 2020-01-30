# Create your models here.

from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser, User
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from books.models import *
from . import managers


class Profile(models.Model):
    role_choice = (
        ('Reader', u'Reader'),
        ('Author', u'Author'),
        ('Editor', u'Editor'),
        ('Admin', u'Admin')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='profile', verbose_name='user')
    gender = models.CharField(choices=(("male", u"Male"), ("female", u"Female")),
                                   default="Female",
                                   max_length=150, verbose_name='Gender')
    birthday = models.DateField(null=True, blank=True, verbose_name="Birthday")
    icon = models.ImageField(upload_to="media/image/%Y/%m",
                                  default=u"media/image/default.png",
                                  max_length=1000,
                                  verbose_name=u"User icon", null=True)
    role = models.CharField(choices=role_choice,
                                 max_length=150,
                                 default='Admin',
                                 verbose_name='Role', editable=False)

    @property
    def get_username(self):
        return self.user.username

    def get_user_role_display(self):
        return self.role


    class Meta:
        verbose_name_plural = "Profile"
        verbose_name = verbose_name_plural
        db_table = 'Profile'

    def __str__(self):
        return self.user.username

# class Admin(models.Model):
#
#     def __str__(self):
#         template = '{0.username}'
#         return template.format(self)
#
#     class Meta:
#         verbose_name_plural = "Admin"
#         verbose_name = verbose_name_plural
#         db_table = 'Admin'


class Reader(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='reader', verbose_name='user')
    is_user_vip = models.CharField(choices=(('normal', u'Normal'), ('vip', u'VIP')),
                                   default='normal',
                                   max_length=10,
                                   verbose_name=u'Vip status')
    vip_validate = models.DateField(verbose_name=u"Validate Until",
                                    auto_now_add=True, null=True,
                                    editable=False)

    def __str__(self):
        return (self.user.get_username)

    class Meta:
        verbose_name_plural = "Reader"
        verbose_name = verbose_name_plural
        db_table = 'Reader'


class Author(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='author')
    contract_number = models.IntegerField(verbose_name= 'Contact number', null=True, blank=True, max_length=100)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Author'
        verbose_name = verbose_name_plural
        db_table = 'Author'
