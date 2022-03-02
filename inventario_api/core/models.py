from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import  MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from multiselectfield import MultiSelectField
# Create your models here.



class Cities(models.Model):
    dane=models.CharField(max_length=30)
    description=models.CharField(max_length=50)
    class Meta:
        verbose_name = ("Ciudades")
    def __str__(self):
        return self.description

class Dependency(models.Model):
    description=models.CharField(max_length=100, primary_key = True,verbose_name="Nombre dependencia")
    buy_group=models.CharField(max_length=40,blank=True,verbose_name="Grupo Compras")
    man_group=models.CharField(max_length=40,blank=True,verbose_name="Grupo Gestor")
    class Meta:
        verbose_name = ("Dependencia")
    def __str__(self):
        return self.description

class Provider(models.Model):
    name=models.CharField(max_length=40, primary_key = True,verbose_name="Nombre")
    address=models.CharField(max_length=40,blank=True,verbose_name="Direccion")
    email=models.CharField(max_length=40,blank=True,verbose_name="Correo")
    web =  models.CharField(max_length=100,blank=True)
    telephone=models.CharField(max_length=40,blank=True,verbose_name="Telefono")
    city = models.ForeignKey(Cities, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Ciudad")
    class Meta:
        verbose_name = ("Proveedor")
    def __str__(self):
        return self.name

class AdqType(models.Model):
    description=models.CharField(max_length=100, primary_key = True)
    class Meta:
        verbose_name = ("Tipo de adquisicion")
    def __str__(self):
        return self.description

class Category(models.Model):
    description=models.CharField(max_length=100, primary_key = True)
    class Meta:
        verbose_name = ("Categoria")
    def __str__(self):
        return self.description

class Disponibility(models.Model):
    description=models.CharField(max_length=100, primary_key = True)
    class Meta:
        verbose_name = ("Disponibilidad")
    def __str__(self):
        return self.description

class Status(models.Model):
    description=models.CharField(max_length=100, primary_key = True)
    class Meta:
        verbose_name = ("Estado")
    def __str__(self):
        return self.description

class Master(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Maestro")
    def __str__(self):
        return self.description

class Position(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Cargo")
    def __str__(self):
        return self.description

class Area(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Area")
    def __str__(self):
        return self.description

class Work_environment(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Ambiente de trabajo")
    def __str__(self):
        return self.description

class Storage_server(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Servidor de Alojamiento")
    def __str__(self):
        return self.description

class Comm_protocol(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Protocolo de comunicación")
    def __str__(self):
        return self.description

class App_type(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Tipo de Aplicativo")
    def __str__(self):
        return self.description

class App_purpose(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Propósito de la Aplicación")
    def __str__(self):
        return self.description

class Web_server(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Servidor Web")
    def __str__(self):
        return self.description

class Client_code(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Código ejecutado en el cliente")
    def __str__(self):
        return self.description

class Server_code(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Código ejecutado en el servidor")
    def __str__(self):
        return self.description

class Dbs(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Base de datos")
    def __str__(self):
        return self.description

class Languages(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Idiomas")
    def __str__(self):
        return self.description

class Report_mannager(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Manejador de reportes")
    def __str__(self):
        return self.description

class Data_export(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Exportar Datos")
    def __str__(self):
        return self.description

class Arch_type(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Tipo arquitectura")
    def __str__(self):
        return self.description

class Licence(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Licenciamiento")
    def __str__(self):
        return self.description

class Interface(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Interface")
    def __str__(self):
        return self.description

class Os(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Sistema Operativo")
    def __str__(self):
        return self.description

class Version(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Version")
    def __str__(self):
        return self.description

class Architecture(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Arquitectura")
    def __str__(self):
        return self.description

class Db_mannager(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Manejador Base de datos")
    def __str__(self):
        return self.description

class Backup_method(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Metodo Backup")
    def __str__(self):
        return self.description

class Periodicity_backup(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Periodicidad Backup")
    def __str__(self):
        return self.description

class Storage(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Almacenamiento")
    def __str__(self):
        return self.description

class Db_licences(models.Model):
    description=models.CharField(max_length=50, primary_key = True)
    class Meta:
        verbose_name = ("Licenciamiento Bases de Datos")
    def __str__(self):
        return self.description

class UserManager(BaseUserManager):
    def create_user(self,email,password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('El usuario debe contener email')
        user = self.model(email = self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        """Creates and saves a new superuser"""
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    document=models.CharField(max_length=20,verbose_name="Numero de documento")
    class DocType(models.TextChoices):
        CC = "CC"
        CE = "CE"
        NIT = "NIT"
        PAS = "PAS"
    document_type = models.CharField(choices = DocType.choices, max_length=50,verbose_name="Tipo de documento")
    full_name=models.CharField(max_length=50,verbose_name="Nombre completo")
    address=models.CharField(max_length=40,blank=True,verbose_name="Direccion")
    email=models.EmailField(max_length=80, unique=True,verbose_name="Correo")
    city = models.ForeignKey(Cities, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Ciudad")
    cellphone=models.CharField(max_length=20,blank=True,verbose_name="Telefono")
    position= models.ForeignKey(Position, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Cargo")
    init_date = models.DateField(blank=True, null = True,verbose_name="Fecha de inicio de contrato")
    end_date = models.DateField(blank=True, null = True,verbose_name="Fecha de fin de contrato")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'


class Inventario_Software(models.Model):
    """General Data"""
    nombre = models.CharField(max_length=100)
    idenfiticador = models.CharField(max_length=500,blank=True)
    descripcion = models.CharField(max_length=500)
    sigla = models.CharField(max_length=40,blank=True)
    version_inicial = models.CharField(max_length=40,blank=True)
    version_actual = models.CharField(max_length=40,blank=True)
    fabricante = models.ForeignKey(Provider, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Proveedor")
    url_interna = models.CharField(max_length=60,blank=True)
    url_externa =  models.CharField(max_length=60,blank=True)
    adqType = models.ForeignKey(AdqType, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Tipo de adquisicion")
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Categoria")
    init_lic_date = models.DateField(blank=True, null = True)
    end_lic_date = models.DateField(blank=True, null = True)
    lic_number = models.IntegerField(blank=True, null = True)
    disponibility = models.ForeignKey(Disponibility, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Disponibilidad")
    status = models.ForeignKey(Status, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Estado")
    fecha_inactivo = models.DateField(blank=True, null = True)
    observations = models.TextField(max_length=500,blank=True,verbose_name="Observaciones")


    """Guarantee"""
    guarantee = models.TextField(max_length=500,blank=True,verbose_name="Garantia")

    """Actualization"""

    actualization = models.TextField(max_length=500,blank=True,verbose_name="Actualizacion")

    """Datos Basicos"""

    YESNOCHOICE = (
     ('SI', 'SI'),
     ('NO', 'NO'),
   )
    work_environment = models.ForeignKey(Work_environment, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Ambiente de trabajo")
    fecha_prod = models.DateField(blank=True, null = True, verbose_name="Fecha de puesta en produccion")
    fecha_act = models.DateField(blank=True, null = True, verbose_name="Fecha ultima actualizacion")
    host_server = models.ForeignKey(Storage_server, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Servidor de alojamiento")
    server_name = models.CharField(verbose_name="Nombre del servidor",max_length=258,blank=True)
    ipv = models.ForeignKey(Comm_protocol, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Protocolo de comunicacion")
    ipv4_address = models.CharField(verbose_name="Direccion ipv4",max_length=258,blank=True)
    ipv6_address = models.CharField(verbose_name="Direccion ipv6",max_length=258,blank=True)
    app_type = models.ForeignKey(App_type, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Tipo de aplicativo")
    app_purpose = models.ForeignKey(App_purpose, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Propósito de aplicación")
    web_server = models.ForeignKey(Web_server, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Servidor Web")
    web_server_version = models.CharField(verbose_name="Version",max_length=258,blank=True)
    client_code = models.ManyToManyField(Client_code, verbose_name="Código ejecutado en el cliente",blank=True,related_name='Cliente')
    server_code = models.ManyToManyField(Server_code, verbose_name="Código ejecutado en el servidor",blank=True,related_name='Servidor')
    required_db  = models.ManyToManyField(Languages, verbose_name="Bases de datos",blank=True,related_name='Db')
    language = models.ManyToManyField(Languages, verbose_name="Idiomas",blank=True,related_name='Idioma')
    other_language = models.CharField(verbose_name="Cual?",max_length=258,blank=True)
    reports = models.ManyToManyField(Report_mannager, verbose_name="Manejadores de reportes",blank=True,related_name='Reporte')
    imports = models.ManyToManyField(Data_export, verbose_name="¿Permite importar datos?",blank=True,related_name='Importar')
    exports = models.ManyToManyField(Data_export, verbose_name="¿Permite exportar datos?",blank=True,related_name='Exportar')
    interact_choice = models.ManyToManyField("self", verbose_name="¿Interactúa con otra aplicación?",blank=True,related_name='Otra_app')
    architecture = models.ManyToManyField(Architecture, verbose_name="Tipo de arquitectura software",blank=True,related_name='Arquitectura')
    font_code = models.CharField(verbose_name="Ubicacion codigo fuente",max_length=258,blank=True)
    lic_scheme_choice = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='Esquema de licenciamiento')
    lic_number2 = models.IntegerField(blank=True, null = True)
    lic_observations = models.TextField(max_length=500,blank=True,verbose_name="Observacion")
    app_interface = models.ManyToManyField(Interface, verbose_name="Interface del Aplicativo",blank=True,related_name='Interface')
    online_help = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='Ayudas en linea')
    roles = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Tiene esquema de roles y perfiles?')
    auditoria = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Tiene esquema de auditorías?')
    admin_usuarios = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Tiene esquema de administración de usuarios?')
    parametrizable = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Es parametrizable?')
    ssl = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Tiene certificado de sitio seguro?')
    logos = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Tiene Logos Institucionales?')
    firewall = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Controlada por Firewall?')
    responsive = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Es responsive (para el caso de los sistemas web)?')
    criterios = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Aplica criterios de usabilidad y accesibilidad?')
    admin_user = models.CharField(verbose_name="Usuario administrador",max_length=258,blank=True)
    MEDIUMCHOICE = (
     ('Fisico', 'Fisico'),
     ('Digital', 'Digital'),
   )
    proyect_plan_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    proyect_plan_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    proyect_plan_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    proyect_plan_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    definition_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    definition_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    definition_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    definition_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    req_doc_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    req_doc_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    req_doc_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    req_doc_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    design_doc_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    design_doc_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    design_doc_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    design_doc_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    test_doc_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    test_doc_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    test_doc_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    test_doc_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    tec_manual_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    tec_manual_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    tec_manual_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    tec_manual_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    admin_manual_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    admin_manual_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    admin_manual_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    admin_manual_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    user_manual_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    user_manual_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    user_manual_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    user_manual_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    sec_manual_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    sec_manual_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    sec_manual_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    sec_manual_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    soft_arch_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    soft_arch_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    soft_arch_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    soft_arch_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    data_dic_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    data_dic_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    data_dic_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    data_dic_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    unit_test_doc_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    unit_test_doc_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    unit_test_doc_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    unit_test_doc_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    pers_doc_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    pers_doc_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    pers_doc_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    pers_doc_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    acta_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    acta_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    acta_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    acta_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    prod_plan_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    prod_plan_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    prod_plan_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    prod_plan_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    service_agr_choice1 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se entregó?')
    service_agr_choice2 = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='¿Se aprobó?')
    service_agr_choice3 = MultiSelectField(choices=MEDIUMCHOICE,max_choices=1,blank=True, verbose_name='Medio')
    service_agr_location = models.CharField(verbose_name="Ubicación",max_length=258,blank=True)

    deliveder_mediums = models.CharField(verbose_name="¿Se entregó medios de instalación?",max_length=258,blank=True)
    DIGMEDCHOICE = (
     ('Fuentes', 'Fisico'),
     ('Ejecutables', 'Digital'),
   )
    dig_med_choice = MultiSelectField(choices=DIGMEDCHOICE,max_choices=1,blank=True, verbose_name='Contenido del medio digital')
    last_version_location= models.CharField(verbose_name="Ubicación última versión código fuente",max_length=258,blank=True)
    observations_documentation = models.TextField(max_length=500,blank=True,verbose_name="Observaciones")


    class Meta:
        verbose_name = ("Inventario de software")


class ObjectivePoblation(models.Model):
    inventary_id = models.ForeignKey(Inventario_Software, on_delete=models.CASCADE)
    dependencia = models.ForeignKey(Dependency, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Dependencia")
    maestro = models.ForeignKey(Master, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Maestro")
    class Meta:
        verbose_name = ("Poblacion Objetivo")

class WebService(models.Model):
    inventary_id = models.ForeignKey(Inventario_Software, on_delete=models.CASCADE)
    web_service  = models.CharField(verbose_name="Descripcion",max_length=258,blank=True)
    url  = models.CharField(verbose_name="Url",max_length=258,blank=True)
    class Meta:
        verbose_name = ("Web Service")

class Modules(models.Model):
    YESNOCHOICE = (
     ('SI', 'SI'),
     ('NO', 'NO'),
   )
    inventary_id = models.ForeignKey(Inventario_Software, on_delete=models.CASCADE)
    name  = models.CharField(verbose_name="Nombre",max_length=258,blank=True)
    descripcion  = models.CharField(verbose_name="Description",max_length=258,blank=True)
    installed = MultiSelectField(choices=YESNOCHOICE,max_choices=1,blank=True, verbose_name='Está Instalado')
    observation = models.TextField(max_length=500,blank=True,verbose_name="Observacion")
    class Meta:
        verbose_name = ("Modulos")

class SoftwareRequirements(models.Model):
    inventary_id = models.ForeignKey(Inventario_Software, on_delete=models.CASCADE)
    type  = models.ForeignKey(Os, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Tipo")
    version  = models.ForeignKey(Version, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Version")
    architecture= models.ForeignKey(Architecture, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Arquitectura")
    class Meta:
        verbose_name = ("Requerimientos de software")

class AppRequirements(models.Model):
    inventary_id = models.ForeignKey(Inventario_Software, on_delete=models.CASCADE)
    language  = models.CharField(verbose_name="Lenguaje",max_length=258,blank=True)
    version  = models.CharField(verbose_name="Version",max_length=258,blank=True)
    libraries= models.CharField(verbose_name="Bibliotecas",max_length=258,blank=True)
    observation = models.TextField(max_length=500,blank=True,verbose_name="Observaciones")
    class Meta:
        verbose_name = ("De aplicacion")

class BdRequirements(models.Model):
    inventary_id = models.ForeignKey(Inventario_Software, on_delete=models.CASCADE)
    mannager  = models.CharField(verbose_name="Manejador",max_length=258,blank=True)
    version  = models.CharField(verbose_name="Version",max_length=258,blank=True)
    port= models.CharField(verbose_name="Puerto",max_length=258,blank=True)
    observation = models.TextField(max_length=500,blank=True,verbose_name="Observaciones")
    class Meta:
        verbose_name = ("De base de datos")


class BdInformation(models.Model):
    inventary_id = models.ForeignKey(Inventario_Software, on_delete=models.CASCADE)
    mannager  = models.ForeignKey(Db_mannager, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Manejador")
    db_name_server  = models.CharField(verbose_name="Nombre Servidor de BD",max_length=258,blank=True)
    db_name  = models.CharField(verbose_name="Nombre BD",max_length=258,blank=True)
    user  = models.CharField(verbose_name="Usuario",max_length=258,blank=True)
    route  = models.CharField(verbose_name="Ruta",max_length=258,blank=True)
    disk_space  = models.CharField(verbose_name="Espacio en disco (actual)",max_length=258,blank=True)
    proyection  = models.CharField(verbose_name="Proyección a 3 años",max_length=258,blank=True)
    backup_method = models.ForeignKey(Backup_method, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Método de Backup")
    backup_policy  = models.CharField(verbose_name="Política de Backup",max_length=258,blank=True)
    periodicity = models.ForeignKey(Periodicity_backup, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Periodicidad")
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Medio de almacenamiento")
    licence = models.ForeignKey(Db_licences, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Licenciamiento de DB")
    db_location  = models.CharField(verbose_name="Ubicación de la DB",max_length=258,blank=True)
    observation = models.TextField(max_length=500,blank=True,verbose_name="Observaciones")
    class Meta:
        verbose_name = ("INFORMACIÓN DE BASES DE DATOS ASOCIADA/S A LA APLICACIÓN")

class Support(models.Model):
    inventary_id = models.ForeignKey(Inventario_Software, on_delete=models.CASCADE)
    class Supp_Type(models.TextChoices):
        Funcional = "Funcional"
        Tecnico = "Tecnico"
    supp_type = models.CharField(choices = Supp_Type.choices, max_length=50,verbose_name="Tipo de soporte")
    area= models.ForeignKey(Area, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Area")
    responsible = models.ManyToManyField(User, verbose_name="Responsables",blank=True)
    contact_telephone = models.CharField(verbose_name="Telefono de contacto",max_length=258,blank=True)
    web =  models.CharField(max_length=100,blank=True)
    disponibility = models.ForeignKey(Disponibility, on_delete=models.CASCADE,blank=True,null = True, default = None,verbose_name="Disponibilidad")
    observations = models.TextField(max_length=500,blank=True)
    venc_fecha = models.DateField(blank=True, null = True)
    class Meta:
        verbose_name = ("Soporte")
