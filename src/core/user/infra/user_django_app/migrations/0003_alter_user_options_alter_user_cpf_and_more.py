# Generated by Django 5.1.2 on 2024-10-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_django_app', '0002_delete_evaluator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-date_joined'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=14, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='document_number',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
