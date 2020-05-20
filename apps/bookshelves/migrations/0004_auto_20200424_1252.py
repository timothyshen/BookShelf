# Generated by Django 2.2.4 on 2020-04-24 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelves', '0003_auto_20200421_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User bookcase'),
        ),
    ]