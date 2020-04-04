# Generated by Django 3.0.2 on 2020-03-10 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='chapter',
        ),
        migrations.AddField(
            model_name='chapter',
            name='Book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='Book'),
        ),
    ]