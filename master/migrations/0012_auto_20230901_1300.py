# Generated by Django 3.2.19 on 2023-09-01 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0011_auto_20230901_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estimatioresourcedetail',
            old_name='grossTotal',
            new_name='gross_total',
        ),
        migrations.RenameField(
            model_name='estimatioresourceheader',
            old_name='InquiryDetail',
            new_name='inquiry_detail',
        ),
    ]