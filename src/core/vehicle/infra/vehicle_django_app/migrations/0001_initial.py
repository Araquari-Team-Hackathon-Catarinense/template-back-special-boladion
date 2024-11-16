# Generated by Django 5.1.3 on 2024-11-16 22:47

import core.vehicle.domain.value_objects
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uploader_django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name_plural': 'bodies',
                'db_table': 'body',
            },
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('axle', models.IntegerField()),
                ('gross_weight', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'compositions',
                'db_table': 'composition',
            },
        ),
        migrations.CreateModel(
            name='Modality',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=45)),
                ('axle', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'modalities',
                'db_table': 'modality',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('license', models.CharField(max_length=10, unique=True)),
                ('chassis', models.CharField(blank=True, max_length=45, null=True, unique=True)),
                ('renavam', models.CharField(blank=True, max_length=45, null=True)),
                ('axle', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('gross_weight', models.IntegerField(blank=True, null=True)),
                ('vehicle_type', models.CharField(choices=[('TRACIONADORA', 'Tracionadora'), ('CARRETA', 'Carreta'), ('DOLLY', 'Dolly'), ('MOTO', 'Moto'), ('CARRO', 'Carro'), ('CAMIONETA', 'Camioneta')], default=core.vehicle.domain.value_objects.VehicleType['CARRO'], max_length=45)),
                ('body', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='body', to='vehicle_django_app.body')),
                ('documents', models.ManyToManyField(related_name='+', to='uploader_django_app.document')),
                ('modality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modality', to='vehicle_django_app.modality')),
            ],
            options={
                'verbose_name_plural': 'vehicles',
                'db_table': 'vehicle',
            },
        ),
        migrations.CreateModel(
            name='VehicleComposition',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sequence', models.IntegerField()),
                ('composition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='composition', to='vehicle_django_app.composition')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='vehicle_django_app.vehicle')),
            ],
            options={
                'verbose_name_plural': 'vehicles_compositions',
                'db_table': 'vehicle_composition',
            },
        ),
    ]
