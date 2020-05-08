# Create your models here.

from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser, User
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from . import managers


class Profile(models.Model):
    role_choice = (
        ('Reader', u'Reader'),
        ('Author', u'Author'),
        ('Editor', u'Editor'),
        ('Admin', u'Admin')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='user')
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
                            verbose_name='Role')

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
