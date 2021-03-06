# Generated by Django 3.0 on 2019-12-06 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True, verbose_name='Mobile')),
                ('user_gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Female', max_length=150, verbose_name='Gender')),
                ('user_birthday', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('user_icon', models.ImageField(default='media/image/default.png', max_length=1000, null=True, upload_to='media/image/%Y/%m', verbose_name='User icon')),
                ('user_role', models.CharField(choices=[('Reader', 'Reader'), ('Author', 'Author'), ('Editor', 'Editor'), ('Admin', 'Admin')], default='Admin', max_length=150, verbose_name='Role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profile',
                'db_table': 'Profile',
            },
        ),
    ]
