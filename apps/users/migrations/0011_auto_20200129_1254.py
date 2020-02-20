# Generated by Django 3.0.2 on 2020-01-29 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200129_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Reader', 'Reader'), ('Author', 'Author'), ('Editor', 'Editor'), ('Admin', 'Admin')], default='Admin', editable=False, max_length=150, verbose_name='Role'),
        ),
    ]