# Generated by Django 5.1.2 on 2024-10-31 21:44

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company_django_app', '0001_initial'),
        ('product_django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementUnit',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=45)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company_django_app.company')),
            ],
            options={
                'verbose_name_plural': 'measurement units',
                'db_table': 'measurement_unit',
            },
        ),
        migrations.CreateModel(
            name='Packing',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company_django_app.company')),
            ],
            options={
                'verbose_name_plural': 'packings',
                'db_table': 'packing',
            },
        ),
        migrations.CreateModel(
            name='PurchaseSaleOrder',
            fields=[
                ('deleted_at', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('balance', models.FloatField(blank=True, null=True)),
                ('operation_type', models.CharField(choices=[('CARGA', 'Carga'), ('DESCARGA', 'Descarga')], max_length=255)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_orders', to='company_django_app.company')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company_django_app.company')),
                ('measurement_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='measurement_unit_orders', to='order_django_app.measurementunit')),
                ('operation_terminal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='operation_terminal_orders', to='company_django_app.company')),
                ('packing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='packing_orders', to='order_django_app.packing')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product_django_app.product')),
            ],
            options={
                'verbose_name_plural': 'purchase_sale_orders',
                'db_table': 'purchase_sale_order',
            },
        ),
        migrations.CreateModel(
            name='TransportContract',
            fields=[
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('balance', models.FloatField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('carrier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='carrier_contracts', to='company_django_app.company')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transport_contracts', to='company_django_app.company')),
                ('purchase_sale_order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order_django_app.purchasesaleorder')),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]
