# Generated by Django 2.2.10 on 2020-06-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0026_auto_20200623_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='last update'),
        ),
    ]