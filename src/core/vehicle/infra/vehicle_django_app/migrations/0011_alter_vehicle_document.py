# Generated by Django 5.1.2 on 2024-11-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader_django_app', '0001_initial'),
        ('vehicle_django_app', '0010_remove_vehicle_document_vehicle_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='document',
            field=models.ManyToManyField(blank=True, related_name='document', to='uploader_django_app.document'),
        ),
    ]
