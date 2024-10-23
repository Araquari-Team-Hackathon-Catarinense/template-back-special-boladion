# Generated by Django 5.1.2 on 2024-10-23 00:09

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company_django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=45)),
                ('slots', models.IntegerField(default=0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parking', to='company_django_app.company')),
            ],
            options={
                'verbose_name_plural': 'parkings',
                'db_table': 'parking',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operations', to='parking_django_app.parking')),
            ],
            options={
                'verbose_name_plural': 'operations',
                'db_table': 'operation',
            },
        ),
        migrations.CreateModel(
            name='ParkingSector',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=45)),
                ('qty_slots', models.IntegerField(default=0)),
                ('sector_type', models.CharField(choices=[('ROTATIVE', 'ROTATIVE'), ('CONTRACT', 'CONTRACT')], max_length=8)),
                ('contract', models.IntegerField(blank=True, null=True)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sectors', to='parking_django_app.parking')),
            ],
            options={
                'verbose_name_plural': 'parking_sectors',
                'db_table': 'parking_sector',
            },
        ),
    ]
