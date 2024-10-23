# Generated by Django 5.1.2 on 2024-10-23 00:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_django_app', '0003_company_document_alter_employee_user'),
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='document',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='uploader.document'),
        ),
    ]
