# Generated by Django 5.1.3 on 2024-11-16 22:47

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uploader_django_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('trade_name', models.CharField(blank=True, max_length=255, null=True)),
                ('person_type', models.CharField(choices=[('PJ', 'PJ'), ('PF', 'PF')], max_length=2)),
                ('document_number', models.CharField(max_length=14, unique=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('system_admin', models.BooleanField(blank=True, default=False, null=True)),
                ('address', models.JSONField(blank=True, null=True)),
                ('contacts', models.JSONField(blank=True, null=True)),
                ('avatar', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='uploader_django_app.document')),
                ('documents', models.ManyToManyField(blank=True, related_name='company_document', to='uploader_django_app.document')),
            ],
            options={
                'verbose_name_plural': 'companies',
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contract_type', models.CharField(choices=[('FORNECEDOR', 'FORNECEDOR'), ('CLIENTE', 'CLIENTE'), ('TRANSPORTADORA', 'TRANSPORTADORA'), ('ARMAZEM', 'ARMAZEM'), ('TERMINAL', 'TERMINAL')], max_length=255)),
                ('source_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_contracts', to='company_django_app.company')),
                ('target_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_contracts', to='company_django_app.company')),
            ],
            options={
                'verbose_name_plural': 'contracts',
                'db_table': 'contract',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_django_app.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'employees',
                'db_table': 'employee',
            },
        ),
    ]
