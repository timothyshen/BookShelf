# Generated by Django 2.2.4 on 2019-10-05 19:42

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(
                    choices=[(1, 'reader'), (2, 'author'), (3, 'editor'), (4, 'admin'), (5, 'anonymous')], default=1,
                    primary_key=True, serialize=False, verbose_name='Role')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                                              help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                              max_length=150, unique=True,
                                              validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                                              verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                                                 help_text='Designates whether the user can log into this admin site.',
                                                 verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True,
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                  verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.Permission', verbose_name='user permissions')),
                ('user_type', models.ManyToManyField(related_name='Role', to='users.Role', verbose_name='User Type')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='users.User')),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admin',
                'db_table': 'Admin',
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mobile',
                 phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True,
                                                                verbose_name='Mobile')),
                ('user_gender',
                 models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Female', max_length=150,
                                  verbose_name='Gender')),
                ('user_icon', models.ImageField(default='media/image/default.png', max_length=1000, null=True,
                                                upload_to='media/image/%Y/%m', verbose_name='User icon')),
                ('is_user_vip',
                 models.CharField(choices=[('normal', 'Normal'), ('vip', 'VIP')], default='Normal', max_length=10,
                                  verbose_name='Vip status')),
                ('vip_validate', models.DateField(default='', null=True, verbose_name='Validate Until')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_reader',
                                              to='users.User')),
            ],
            options={
                'verbose_name': 'Reader',
                'verbose_name_plural': 'Reader',
                'db_table': 'Reader',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_author',
                                              to='users.User')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Author',
                'db_table': 'Author',
            },
        ),
    ]
