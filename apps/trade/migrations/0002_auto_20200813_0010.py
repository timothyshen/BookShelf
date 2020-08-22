# Generated by Django 2.2.13 on 2020-08-13 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatus',
            name='level',
            field=models.IntegerField(default=0, verbose_name='VIP level'),
        ),
        migrations.AlterField(
            model_name='userstatus',
            name='valid_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Valid date'),
        ),
    ]