# Generated by Django 2.2.10 on 2020-06-22 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0024_auto_20200621_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='favoured',
        ),
    ]
