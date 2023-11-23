# Generated by Django 3.2.19 on 2023-08-25 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_company'),
        ('master', '0006_sourceofinquiry_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='InquiryHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inquirydate', models.DateField(blank=True, null=True)),
                ('client_reference_no', models.CharField(blank=True, max_length=50, null=True)),
                ('submission_date', models.DateField()),
                ('scope_of_work', models.CharField(blank=True, max_length=100, null=True)),
                ('attachments', models.FileField(blank=True, null=True, upload_to='inquiryheader')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inqheader', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.customers')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.departments')),
                ('employer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.employer')),
                ('estimator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estimator', to=settings.AUTH_USER_MODEL)),
                ('salesman', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salesman', to=settings.AUTH_USER_MODEL)),
                ('source_of_inquiry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.sourceofinquiry')),
            ],
        ),
        migrations.CreateModel(
            name='InquiryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boq_number', models.CharField(blank=True, max_length=100, null=True)),
                ('boq_description', models.TextField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('inquiryno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.inquiryheader')),
            ],
        ),
    ]