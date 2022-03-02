# Generated by Django 3.1.14 on 2022-03-01 16:21

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventario_software',
            options={'verbose_name': 'Inventario de software'},
        ),
        migrations.RemoveField(
            model_name='inventario_software',
            name='dependencia',
        ),
        migrations.RemoveField(
            model_name='inventario_software',
            name='maestro',
        ),
        migrations.RemoveField(
            model_name='inventario_software',
            name='otra_categoria',
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='app_interface',
            field=models.ManyToManyField(blank=True, related_name='Interface', to='core.Interface', verbose_name='Interface del Aplicativo'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='app_purpose',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.app_purpose', verbose_name='Propósito de aplicación'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='app_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.app_type', verbose_name='Tipo de aplicativo'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='architecture',
            field=models.ManyToManyField(blank=True, related_name='Arquitectura', to='core.Architecture', verbose_name='Tipo de arquitectura software'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='client_code',
            field=models.ManyToManyField(blank=True, related_name='Cliente', to='core.Client_code', verbose_name='Código ejecutado en el cliente'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='exports',
            field=models.ManyToManyField(blank=True, related_name='Exportar', to='core.Data_export', verbose_name='¿Permite exportar datos?'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='fecha_act',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha ultima actualizacion'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='fecha_prod',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de puesta en produccion'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='font_code',
            field=models.CharField(blank=True, max_length=258, verbose_name='Ubicacion codigo fuente'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='host_server',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.storage_server', verbose_name='Servidor de alojamiento'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='idenfiticador',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='imports',
            field=models.ManyToManyField(blank=True, related_name='Importar', to='core.Data_export', verbose_name='¿Permite importar datos?'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='interact_choice',
            field=models.ManyToManyField(blank=True, related_name='_inventario_software_interact_choice_+', to='core.Inventario_Software', verbose_name='¿Interactúa con otra aplicación?'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='ipv',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.comm_protocol', verbose_name='Protocolo de comunicacion'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='ipv4_address',
            field=models.CharField(blank=True, max_length=258, verbose_name='Direccion ipv4'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='ipv6_address',
            field=models.CharField(blank=True, max_length=258, verbose_name='Direccion ipv6'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='language',
            field=models.ManyToManyField(blank=True, related_name='Idioma', to='core.Languages', verbose_name='Idiomas'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='lic_number2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='lic_observations',
            field=models.TextField(blank=True, max_length=500, verbose_name='Observacion'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='lic_scheme_choice',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=5, verbose_name='Esquema de licenciamiento'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='other_language',
            field=models.CharField(blank=True, max_length=258, verbose_name='Cual?'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='reports',
            field=models.ManyToManyField(blank=True, related_name='Reporte', to='core.Report_mannager', verbose_name='Manejadores de reportes'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='required_db',
            field=models.ManyToManyField(blank=True, related_name='Db', to='core.Languages', verbose_name='Bases de datos'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='server_code',
            field=models.ManyToManyField(blank=True, related_name='Servidor', to='core.Server_code', verbose_name='Código ejecutado en el servidor'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='server_name',
            field=models.CharField(blank=True, max_length=258, verbose_name='Nombre del servidor'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='web_server',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.web_server', verbose_name='Servidor Web'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='web_server_version',
            field=models.CharField(blank=True, max_length=258, verbose_name='Version'),
        ),
        migrations.AddField(
            model_name='inventario_software',
            name='work_environment',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.work_environment', verbose_name='Ambiente de trabajo'),
        ),
        migrations.AlterField(
            model_name='inventario_software',
            name='adqType',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.adqtype', verbose_name='Tipo de adquisicion'),
        ),
        migrations.AlterField(
            model_name='inventario_software',
            name='categoria',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='inventario_software',
            name='disponibility',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.disponibility', verbose_name='Disponibilidad'),
        ),
        migrations.AlterField(
            model_name='inventario_software',
            name='fabricante',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.provider', verbose_name='Proveedor'),
        ),
        migrations.AlterField(
            model_name='inventario_software',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.status', verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='ObjectivePoblation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependencia', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.dependency', verbose_name='Dependencia')),
                ('inventary_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.inventario_software')),
                ('maestro', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.master', verbose_name='Maestro')),
            ],
            options={
                'verbose_name': 'Poblacion Objetivo',
            },
        ),
    ]
