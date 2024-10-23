# Generated by Django 5.1.2 on 2024-10-22 23:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_django_app', '0003_alter_employee_user'),
        ('uploader_django_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='pic',
        ),
        migrations.AddField(
            model_name='company',
            name='avatar',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='uploader_django_app.document'),
        ),
    ]
