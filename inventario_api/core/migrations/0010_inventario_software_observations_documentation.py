# Generated by Django 3.1.14 on 2022-03-01 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20220301_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario_software',
            name='observations_documentation',
            field=models.TextField(blank=True, max_length=500, verbose_name='Observaciones'),
        ),
    ]
