# Generated by Django 3.0.2 on 2020-01-29 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200129_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='vip_validate',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Validate Until'),
        ),
    ]
