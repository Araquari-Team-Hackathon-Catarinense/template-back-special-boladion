# Generated by Django 5.1.2 on 2024-10-22 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader_django_app', '0001_initial'),
        ('user_django_app', '0002_alter_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pic',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='uploader_django_app.document'),
        ),
    ]
