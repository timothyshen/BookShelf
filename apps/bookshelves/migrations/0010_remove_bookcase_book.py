# Generated by Django 2.2.10 on 2020-06-21 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelves', '0009_auto_20200621_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcase',
            name='book',
        ),
    ]