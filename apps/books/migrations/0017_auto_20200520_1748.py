# Generated by Django 2.2.4 on 2020-05-20 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_chapter_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='publish_status',
            field=models.CharField(choices=[('Published', 'Published'), ('Draft', 'Draft'), ('Trash', 'Trash')], default='Published', max_length=150),
        ),
    ]
