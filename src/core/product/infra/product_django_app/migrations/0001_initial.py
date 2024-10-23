# Generated by Django 5.1.2 on 2024-10-23 22:44

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company_django_app', '0003_alter_employee_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('internal_code', models.CharField(max_length=45)),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='company_django_app.company')),
            ],
            options={
                'verbose_name_plural': 'products',
                'db_table': 'product',
            },
        ),
    ]
