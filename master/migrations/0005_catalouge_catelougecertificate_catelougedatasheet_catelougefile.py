# Generated by Django 3.2.19 on 2023-08-23 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0004_auto_20230822_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalouge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('type', models.CharField(blank=True, max_length=225, null=True)),
                ('category', models.CharField(blank=True, max_length=225, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=225, null=True)),
                ('type_sub_category', models.CharField(blank=True, max_length=225, null=True)),
                ('origin', models.CharField(blank=True, max_length=225, null=True)),
                ('finish', models.CharField(blank=True, max_length=225, null=True)),
                ('brand', models.CharField(blank=True, max_length=225, null=True)),
                ('series', models.CharField(blank=True, max_length=225, null=True)),
                ('model', models.CharField(blank=True, max_length=225, null=True)),
                ('size', models.CharField(blank=True, max_length=225, null=True)),
                ('specification', models.TextField(blank=True, null=True)),
                ('list_price', models.CharField(blank=True, max_length=100, null=True)),
                ('currency', models.CharField(blank=True, max_length=100, null=True)),
                ('discount', models.CharField(blank=True, max_length=100, null=True)),
                ('base_of_pricing', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('primary_image', models.FileField(blank=True, null=True, upload_to='catalogueImage')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CreatedCatelouge', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CatelougeFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='Catalougefiles')),
                ('catalogue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.catalouge')),
            ],
        ),
        migrations.CreateModel(
            name='CatelougeDataSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasheet', models.FileField(blank=True, null=True, upload_to='catalogueSheet')),
                ('catalogue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.catalouge')),
            ],
        ),
        migrations.CreateModel(
            name='CatelougeCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='Catalouge_certificate')),
                ('catalogue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.catalouge')),
            ],
        ),
    ]
