# Generated by Django 2.2.4 on 2020-05-25 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_auto_20200525_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='chapter_count',
        ),
        migrations.RemoveField(
            model_name='book',
            name='total_words',
        ),
        migrations.RemoveField(
            model_name='book',
            name='weekly_vote',
        ),
    ]
