# Generated by Django 3.2.19 on 2023-08-21 11:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='First Name ')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='Last Name ')),
                ('date_joined', models.DateTimeField(default=datetime.datetime.now)),
                ('phone_number', models.PositiveBigIntegerField(blank=True, help_text='Optional', null=True, verbose_name='Phone Number ')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Address')),
                ('profile_image', models.FileField(blank=True, default='', null=True, upload_to='profile image', verbose_name='Profile Image')),
                ('user_type', models.CharField(blank=True, choices=[('AD', 'Admin'), ('OP', 'Operator'), ('Customer', 'Customer')], max_length=30, null=True)),
                ('account_status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Closed', 'Closed'), ('Suspended', 'Suspended')], default='Active', max_length=30, null=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'All Users',
                'verbose_name_plural': 'All Users',
            },
        ),
        migrations.CreateModel(
            name='MultiToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'abstract': False,
            },
        ),
    ]
