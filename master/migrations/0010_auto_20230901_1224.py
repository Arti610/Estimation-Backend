# Generated by Django 3.2.19 on 2023-09-01 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0009_alter_inquirydetail_inquiryno'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalouge',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inquiry_tax', to='master.tax'),
        ),
        migrations.AddField(
            model_name='catalouge',
            name='unit_of_measurement',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='EstimatioResourceHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('InquiryDetail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.inquirydetail')),
            ],
        ),
        migrations.CreateModel(
            name='EstimatioResourceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('grossTotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vat_percentage', models.IntegerField(blank=True, null=True)),
                ('vat_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estimation_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estresource', to=settings.AUTH_USER_MODEL)),
                ('estimation_res_header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.estimatioresourceheader')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.catalouge')),
            ],
        ),
        migrations.CreateModel(
            name='EstimatioHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimation_date', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estimationheader', to=settings.AUTH_USER_MODEL)),
                ('inquiry_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.inquiryheader')),
            ],
        ),
        migrations.CreateModel(
            name='EstimatioDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimation_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('salesprice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('markup', models.CharField(blank=True, max_length=10, null=True)),
                ('markup_value', models.CharField(blank=True, max_length=50, null=True)),
                ('gross_price', models.CharField(blank=True, max_length=15, null=True)),
                ('taxable', models.CharField(blank=True, max_length=25, null=True)),
                ('NetTotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estimation_number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.estimatioheader')),
                ('inquirydetail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.inquirydetail')),
                ('vat_tax', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.tax')),
            ],
        ),
    ]
