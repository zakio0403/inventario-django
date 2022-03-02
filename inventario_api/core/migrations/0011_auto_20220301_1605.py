# Generated by Django 3.1.14 on 2022-03-01 21:05

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_inventario_software_observations_documentation'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario_software',
            name='deliveder_mediums',
            field=models.CharField(blank=True, max_length=258, verbose_name='¿Se entregó medios de instalación?'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='dig_med_choice',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Fuentes', 'Fisico'), ('Ejecutables', 'Digital')], max_length=19, verbose_name='Contenido del medio digital'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='last_version_location',
            field=models.CharField(blank=True, max_length=258, verbose_name='Ubicación última versión código fuente'),
        ),
    ]
