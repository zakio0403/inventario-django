# Generated by Django 3.1.14 on 2022-03-01 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_apprequirements_bdrequirements_softwarerequirements_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='softwarerequirements',
            options={'verbose_name': 'Requerimientos de software'},
        ),
        migrations.RemoveField(
            model_name='apprequirements',
            name='soft_req_id',
        ),
        migrations.RemoveField(
            model_name='bdrequirements',
            name='soft_req_id',
        ),
        migrations.AddField(
            model_name='apprequirements',
            name='inventary_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.inventario_software'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bdrequirements',
            name='inventary_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.inventario_software'),
            preserve_default=False,
        ),
    ]