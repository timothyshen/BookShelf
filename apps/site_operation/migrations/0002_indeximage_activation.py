# Generated by Django 2.2.4 on 2020-06-14 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indeximage',
            name='activation',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Active', 'Active')], default='Inactive', max_length=1000, verbose_name='Publish status'),
        ),
    ]
