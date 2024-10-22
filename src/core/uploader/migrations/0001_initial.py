# Generated by Django 5.1.2 on 2024-10-22 16:38

import core.uploader.models.document
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_key', models.UUIDField(default=uuid.uuid4, help_text='Used to attach the document to another object. Cannot be used to retrieve the document file.', unique=True)),
                ('public_id', models.UUIDField(default=uuid.uuid4, help_text='Used to retrieve the document file itself. Should not be readable until the document is attached to another object.', unique=True)),
                ('file', models.FileField(upload_to=core.uploader.models.document.document_file_path)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('PDF', 'PDF'), ('IMG', 'IMG')], default='PDF', max_length=3)),
            ],
        ),
    ]
