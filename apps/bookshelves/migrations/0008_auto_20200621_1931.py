# Generated by Django 2.2.10 on 2020-06-21 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelves', '0007_auto_20200621_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcase',
            name='bookmark',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marked_book', to='bookshelves.BookMark', verbose_name='bookmark'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='bookmark',
            name='bookcase',
        ),
    ]
