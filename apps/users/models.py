# Create your models here.

from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from books.models import *


class User(AbstractUser):
    role_choice = (
        ('Reader', u'Reader'),
        ('Author', u'Author'),
        ('Editor', u'Editor'),
        ('Admin', u'Admin')
    )
    user_mobile = PhoneNumberField(null=True, unique=True, verbose_name='Mobile')
    user_gender = models.CharField(choices=(("male", u"Male"), ("female", u"Female")),
                                   default="Female",
                                   max_length=150, verbose_name='Gender')
    user_birthday = models.DateField(null=True, blank=True, verbose_name="Birthday")
    user_icon = models.ImageField(upload_to="media/image/%Y/%m",
                                  default=u"media/image/default.png",
                                  max_length=1000,
                                  verbose_name=u"User icon", null=True)
    user_role = models.CharField(choices=role_choice,
                                 max_length=150,
                                 default='Admin',
                                 verbose_name='Role')

    def __str__(self):
        return self.username

    def get_user_role_display(self):
        return self.role_choice

    class Meta:
        verbose_name_plural = "user"
        verbose_name = verbose_name_plural
        db_table = 'User'


class Admin(User):

    def __str__(self):
        template = '{0.username}'
        return template.format(self)

    class Meta:
        verbose_name_plural = "Admin"
        verbose_name = verbose_name_plural
        db_table = 'Admin'


class Reader(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reader')
    is_user_vip = models.CharField(choices=(('normal', u'Normal'), ('vip', u'VIP')),
                                   default='Normal',
                                   max_length=10,
                                   verbose_name=u'Vip status',
                                   editable=False)
    vip_validate = models.DateField(verbose_name=u"Validate Until",
                                    default='', null=True,
                                    editable=False)

    def __str__(self):
        template = '{0.user.email} {0.user_mobile}'
        return template.format(self)

    class Meta:
        verbose_name_plural = "Reader"
        verbose_name = verbose_name_plural
        db_table = 'Reader'


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_author')
    contract_number = models.IntegerField(verbose_name= 'Contact number', null=True, blank=True, max_length=100)
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Author'
        verbose_name = verbose_name_plural
        db_table = 'Author'
