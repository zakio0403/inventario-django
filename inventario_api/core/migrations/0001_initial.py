# Generated by Django 3.1.14 on 2022-02-28 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('document', models.CharField(max_length=20, verbose_name='Numero de documento')),
                ('document_type', models.CharField(choices=[('CC', 'Cc'), ('CE', 'Ce'), ('NIT', 'Nit'), ('PAS', 'Pas')], max_length=50, verbose_name='Tipo de documento')),
                ('full_name', models.CharField(max_length=50, verbose_name='Nombre completo')),
                ('address', models.CharField(blank=True, max_length=40, verbose_name='Direccion')),
                ('email', models.EmailField(max_length=80, unique=True, verbose_name='Correo')),
                ('cellphone', models.CharField(blank=True, max_length=20, verbose_name='Telefono')),
                ('init_date', models.DateField(blank=True, null=True, verbose_name='Fecha de inicio de contrato')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Fecha de fin de contrato')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdqType',
            fields=[
                ('description', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Tipo de adquisicion',
            },
        ),
        migrations.CreateModel(
            name='App_purpose',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Propósito de la Aplicación',
            },
        ),
        migrations.CreateModel(
            name='App_type',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Tipo de Aplicativo',
            },
        ),
        migrations.CreateModel(
            name='Arch_type',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Tipo arquitectura',
            },
        ),
        migrations.CreateModel(
            name='Architecture',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Arquitectura',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Area',
            },
        ),
        migrations.CreateModel(
            name='Backup_method',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Metodo Backup',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('description', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dane', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Client_code',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Código ejecutado en el cliente',
            },
        ),
        migrations.CreateModel(
            name='Comm_protocol',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Protocolo de comunicación',
            },
        ),
        migrations.CreateModel(
            name='Data_export',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Exportar Datos',
            },
        ),
        migrations.CreateModel(
            name='Db_licences',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Licenciamiento Bases de Datos',
            },
        ),
        migrations.CreateModel(
            name='Db_mannager',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Manejador Base de datos',
            },
        ),
        migrations.CreateModel(
            name='Dbs',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Base de datos',
            },
        ),
        migrations.CreateModel(
            name='Dependency',
            fields=[
                ('description', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Nombre dependencia')),
                ('buy_group', models.CharField(blank=True, max_length=40, verbose_name='Grupo Compras')),
                ('man_group', models.CharField(blank=True, max_length=40, verbose_name='Grupo Gestor')),
            ],
            options={
                'verbose_name': 'Dependencia',
            },
        ),
        migrations.CreateModel(
            name='Disponibility',
            fields=[
                ('description', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Disponibilidad',
            },
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Interface',
            },
        ),
        migrations.CreateModel(
            name='Inventario_Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('sigla', models.CharField(blank=True, max_length=40)),
                ('version_inicial', models.CharField(blank=True, max_length=40)),
                ('version_actual', models.CharField(blank=True, max_length=40)),
                ('fabricante', models.CharField(blank=True, max_length=60)),
                ('url_interna', models.CharField(blank=True, max_length=60)),
                ('url_externa', models.CharField(blank=True, max_length=60)),
                ('adqType', models.CharField(choices=[('Comprado', 'Comprado'), ('Alquilado', 'Alquilado'), ('Des.propio', 'Des.propio'), ('Donado', 'Donado'), ('Comodato', 'Comodato'), ('Licencia de uso', 'Licencia de uso')], max_length=50)),
                ('categoria', models.CharField(blank=True, choices=[('Misional', 'Misional'), ('Estrategico', 'Estrategico'), ('Operativo', 'Operativo')], max_length=258, null=True)),
                ('otra_categoria', models.CharField(blank=True, max_length=258, verbose_name='Otro?')),
                ('init_lic_date', models.DateField(blank=True, null=True)),
                ('end_lic_date', models.DateField(blank=True, null=True)),
                ('lic_number', models.IntegerField(blank=True, null=True)),
                ('disponibility', models.CharField(blank=True, choices=[('7x24', '7x24'), ('5x9', '5x9')], max_length=50)),
                ('status', models.CharField(blank=True, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('En desarrollo', 'En desarrollo'), ('En pruebas', 'En pruebas')], max_length=50)),
                ('fecha_inactivo', models.DateField(blank=True, null=True)),
                ('observations', models.TextField(blank=True, max_length=500)),
                ('maestro', models.CharField(blank=True, choices=[('M', 'M'), ('R', 'R')], max_length=50)),
                ('guarantee', models.TextField(blank=True, max_length=500, verbose_name='Garantia')),
                ('actualization', models.TextField(blank=True, max_length=500, verbose_name='Actualizacion')),
                ('dependencia', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.dependency', verbose_name='Dependencia')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Idiomas',
            },
        ),
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Licenciamiento',
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Maestro',
            },
        ),
        migrations.CreateModel(
            name='Os',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Sistema Operativo',
            },
        ),
        migrations.CreateModel(
            name='Periodicity_backup',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Periodicidad Backup',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Cargo',
            },
        ),
        migrations.CreateModel(
            name='Report_mannager',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Manejador de reportes',
            },
        ),
        migrations.CreateModel(
            name='Server_code',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Código ejecutado en el servidor',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('description', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Almacenamiento',
            },
        ),
        migrations.CreateModel(
            name='Storage_server',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Servidor de Alojamiento',
            },
        ),
        migrations.CreateModel(
            name='Web_server',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Servidor Web',
            },
        ),
        migrations.CreateModel(
            name='Work_environment',
            fields=[
                ('description', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Ambiente de trabajo',
            },
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supp_type', models.CharField(choices=[('Funcional', 'Funcional'), ('Tecnico', 'Tecnico')], max_length=50, verbose_name='Tipo de soporte')),
                ('contact_telephone', models.CharField(blank=True, max_length=258, verbose_name='Telefono de contacto')),
                ('web', models.CharField(blank=True, max_length=100)),
                ('observations', models.TextField(blank=True, max_length=500)),
                ('venc_fecha', models.DateField(blank=True, null=True)),
                ('area', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.area', verbose_name='Area')),
                ('disponibility', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.disponibility', verbose_name='Disponibilidad')),
                ('inventary_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.inventario_software')),
                ('responsible', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Responsables')),
            ],
            options={
                'verbose_name': 'Soporte',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('address', models.CharField(blank=True, max_length=40, verbose_name='Direccion')),
                ('email', models.CharField(blank=True, max_length=40, verbose_name='Correo')),
                ('web', models.CharField(blank=True, max_length=100)),
                ('telephone', models.CharField(blank=True, max_length=40, verbose_name='Telefono')),
                ('city', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cities', verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Proveedor',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cities', verbose_name='Ciudad'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.position', verbose_name='Cargo'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
