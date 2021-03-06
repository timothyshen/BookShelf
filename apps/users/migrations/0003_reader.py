# Generated by Django 2.2.4 on 2020-01-14 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200114_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_user_vip', models.CharField(choices=[('normal', 'Normal'), ('vip', 'VIP')], default='Normal', editable=False, max_length=10, verbose_name='Vip status')),
                ('vip_validate', models.DateField(default='', editable=False, null=True, verbose_name='Validate Until')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reader', to='users.Profile', verbose_name='user')),
            ],
            options={
                'verbose_name': 'Reader',
                'verbose_name_plural': 'Reader',
                'db_table': 'Reader',
            },
        ),
    ]
