# Generated by Django 2.2.4 on 2019-11-08 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='user_birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Birthday'),
        ),
    ]
