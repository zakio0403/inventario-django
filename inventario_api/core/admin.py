from django.contrib import admin
from tabbed_admin import TabbedModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
#from .models import Inventario_Software, Dependency, Support, Cities, AdqType, Category, Disponibility, Status, Master, Position, Area, User
from core import models
#from core import models



class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display=['email','full_name']
    fieldsets = (
        (None, {'fields':('email','password')}),
        (_('Informacion personal'), {'fields':('document_type','document',  'full_name', 'address','city','cellphone', 'position')}),
        (
        _('Permissions'),
            {'fields':('is_active', 'is_staff','is_superuser')}
        ),
        (_('Fechas'),{'fields':('init_date','end_date','last_login')})
    )
    add_fieldsets=(
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1','password2','full_name', 'document_type', 'document')
            }),
    )
    model = models.User
    search_fields = ['email']

class DependencyAdmin(admin.ModelAdmin):
    list_display=['description','buy_group',"man_group"]
    model = models.Dependency
    search_fields = ['description']

class AreaAdmin(admin.ModelAdmin):
    list_display=['description',]
    model = models.Area
    search_fields = ['description']

class ProviderAdmin(admin.ModelAdmin):
    list_display=['name','address','email','web','telephone','city']
    model = models.Provider
    search_fields = ['name']

class SupportAdmin(admin.StackedInline):
    model = models.Support
    autocomplete_fields = ['responsible',"area"]
    fields = ('supp_type', 'area',"responsible",'contact_telephone','web','disponibility','observations', 'venc_fecha')

class PoblationAdmin(admin.StackedInline):
    model = models.ObjectivePoblation
    raw_id_fields=['dependencia']
    fields = ('dependencia', 'maestro')

class WebServiceAdmin(admin.StackedInline):
    model = models.WebService
    fields =  ('web_service', 'url')

class ModuleAdmin(admin.StackedInline):
    model = models.Modules
    fields = ('name', 'descripcion','installed','observation')

class AppRequirementsAdmin(admin.StackedInline):
    model = models.AppRequirements
    fields = ('language', 'version','libraries','observation')

class BdRequirementsAdmin(admin.StackedInline):
    model = models.BdRequirements
    fields = ('mannager', 'version','port','observation')
class SoftwareRequirementsAdmin(admin.StackedInline):
    model = models.SoftwareRequirements
    fields = ('type', 'version','architecture')

class BdInformationAdmin(admin.StackedInline):
    model = models.BdInformation
    fields = (('db_name_server','mannager'),('db_name','user'),('route','disk_space'),('proyection','backup_method'),('backup_policy','periodicity'),('db_location','storage'),'licence','observation')

@admin.register(models.Inventario_Software)
class InventarioAdmin(TabbedModelAdmin):
    model = models.Inventario_Software
    list_display = ['id','nombre','sigla','version_actual', "url_interna", "url_externa",'status']
    search_fields = ('nombre', 'fabricante')
    autocomplete_fields = ['fabricante',]
    tab_1 = (
        ('Datos Generales', {
            'fields': (('nombre', 'idenfiticador'), ('descripcion', 'sigla'), ('version_inicial', 'version_actual'), "fabricante",('url_interna', 'adqType'),('url_externa','categoria'),('init_lic_date', 'end_lic_date'), ('lic_number', 'disponibility','status'),  'fecha_inactivo', 'observations')
        }),

    )
    tab_2 = (
        PoblationAdmin,

    )
    tab_3 = (
        SupportAdmin,
    )
    tab_4 = (
        ('Garantia', {
            'fields': ('guarantee', )
        }),
    )
    tab_5 = (
        ('Actualizacion', {
            'fields': ('actualization', )
        }),
    )
    tab_6 = (
        ('Ambiente de trabajo', {
            'fields': ('work_environment',)
        }),('Fechas', {
            'fields': ( ('fecha_prod', 'fecha_act',), )
        }),('Informacion del Servidor', {
            'fields': ( "host_server",'server_name' )
        }),('Protocolo de comunicacion', {
            'fields': ( ('ipv', 'ipv4_address','ipv6_address'),)
        }),('Tipo de aplicativo', {
            'fields': ( 'app_type', )
        }),('Proposito de aplicacion', {
            'fields': ( 'app_purpose', )
        }),('Servidor web', {
            'fields': ( ('web_server', 'web_server_version'),)
        }),('Código ejecutado en el cliente', {
            'fields': ( 'client_code', )
        }),('Código ejecutado en el servidor', {
            'fields': ( 'server_code', )
        }),('¿Requiere base de datos?', {
            'fields': ("required_db", )
        }),('¿Maneja varios idiomas?', {
            'fields': ("language",)
        }),('¿Utiliza Manejador de Reportes?', {
            'fields': ("reports", )
        }),('¿Permite exportar datos?', {
            'fields': ("imports", )
        }),('¿Permite importar datos?', {
            'fields': ("exports", )
        }),('¿Interactúa con otra aplicación?', {
            'fields': ("interact_choice", )
        }),('Tipo de arquitectura software', {
            'fields': ("architecture", )
        }),('¿Se tiene código fuente?', {
            'fields': ("font_code",)
        }),('Esquema de licenciamiento', {
            'fields': (("lic_scheme_choice","lic_number2" ),"lic_observations")
        }),('Interface del Aplicativo', {
            'fields': ("app_interface", )
        }),(None, {
            'fields': (("online_help","roles",'auditoria') ,('admin_usuarios','parametrizable','ssl'),('logos','firewall','responsive'),('criterios','admin_user'))
        }),(
            WebServiceAdmin
        ),(
            ModuleAdmin
        )

    )
    tab_7 = (
        SoftwareRequirementsAdmin,
        BdRequirementsAdmin,
        AppRequirementsAdmin


    )
    tab_8 = (
        BdInformationAdmin,
    )
    tab_9 = (
        ('Plan de proyecto', {
            'fields': (("proyect_plan_choice1","proyect_plan_choice2") ,('proyect_plan_choice3','proyect_plan_location'))
        }),
        ('Definición y Alcance', {
            'fields': (("definition_choice1","definition_choice2") ,('definition_choice3','definition_location'))
        }),
        ('Documento de requerimientos', {
            'fields': (("req_doc_choice1","req_doc_choice2") ,('req_doc_choice3','req_doc_location'))
        }),
        ('Documento de Diseño', {
            'fields': (("design_doc_choice1","design_doc_choice2") ,('design_doc_choice3','design_doc_location'))
        }),
        ('Documentos de Pruebas', {
            'fields': (("test_doc_choice1","test_doc_choice2") ,('test_doc_choice3','test_doc_location'))
        }),
        ('Manual Técnico y de instalación', {
            'fields': (("tec_manual_choice1","tec_manual_choice2") ,('tec_manual_choice3','tec_manual_location'))
        }),
        ('Manual de Administración', {
            'fields': (("admin_manual_choice1","admin_manual_choice2") ,('admin_manual_choice3','admin_manual_location'))
        }),
        ('Manual de Usuario', {
            'fields': (("user_manual_choice1","user_manual_choice2") ,('user_manual_choice3','user_manual_location'))
        }),
        ('Manual de copias de seguridad', {
            'fields': (("sec_manual_choice1","sec_manual_choice2") ,('sec_manual_choice3','sec_manual_location'))
        }),
        ('Arquitectura de software', {
            'fields': (("soft_arch_choice1","soft_arch_choice2") ,('soft_arch_choice3','soft_arch_location'))
        }),
        ('Diccionario de datos', {
            'fields': (("data_dic_choice1","data_dic_choice2") ,('data_dic_choice3','data_dic_location'))
        }),
        ('Documentación de pruebas unitarias e integrales', {
            'fields': (("unit_test_doc_choice1","unit_test_doc_choice2") ,('unit_test_doc_choice3','unit_test_doc_location'))
        }),
        ('Documento de política de protección de datos personales', {
            'fields': (("pers_doc_choice1","pers_doc_choice2") ,('pers_doc_choice3','pers_doc_location'))
        }),
        ('Acta de aceptación de entrega del proyecto a entera satisfacción por el área dueña del proceso que soporta el proyecto', {
            'fields': (("acta_choice1","acta_choice2") ,('acta_choice3','acta_location'))
        }),
        ('Plan de salida en producción', {
            'fields': (("prod_plan_choice1","prod_plan_choice2") ,('prod_plan_choice3','prod_plan_location'))
        }),
        ('Acuerdo de Niveles de Servicio', {
            'fields': (("service_agr_choice1","service_agr_choice2") ,('service_agr_choice3','service_agr_location'))
        }),
        (None,{
        'fields': (('deliveder_mediums','dig_med_choice'),('last_version_location','observations_documentation'))
        })


    )

    tabs = [
        ('Datos Generales', tab_1),
        ('Poblacion objetivo', tab_2),
        ('Soportes', tab_3),
        ('Garantia', tab_4),
        ('Actualizacion', tab_5),
        ('Datos Basicos Aplicacion', tab_6),
        ('Requerimientos de software para el servidor', tab_7),
        ('Informacion de bases de datos asociadas a la aplicacion', tab_8),
        ('Documentacion', tab_9),

    ]

admin.site.register(models.User,UserAdmin)
admin.site.register(models.Dependency,DependencyAdmin)
admin.site.register(models.Area,AreaAdmin)
admin.site.register(models.Provider,ProviderAdmin)
admin.site.register(models.BdInformation)
admin.site.register(models.Cities)
admin.site.register(models.AdqType)
admin.site.register(models.Category)
admin.site.register(models.Disponibility)
admin.site.register(models.Status)
admin.site.register(models.Master)
admin.site.register(models.Work_environment)
admin.site.register(models.Storage_server)
admin.site.register(models.Comm_protocol)
admin.site.register(models.App_type)
admin.site.register(models.App_purpose)
admin.site.register(models.Web_server)
admin.site.register(models.Client_code)
admin.site.register(models.Server_code)
admin.site.register(models.Dbs)
admin.site.register(models.Languages)
admin.site.register(models.Report_mannager)
admin.site.register(models.Data_export)
admin.site.register(models.Arch_type)
admin.site.register(models.Licence)
admin.site.register(models.Interface)
admin.site.register(models.Os)
admin.site.register(models.Db_mannager)
admin.site.register(models.Backup_method)
admin.site.register(models.Periodicity_backup)
admin.site.register(models.Storage)
admin.site.register(models.Position)
admin.site.register(models.Architecture)
admin.site.register(models.Db_licences)


"""('Requerimientos de software para el servidor', tab_2),
('Requerimientos de hardware para el servidor', tab_2),
('Archivos de configuracion o parametrizacion', tab_2),
('Parametros de configuracion', tab_2),
('Informacion de bases de datos asociadas a la aplicacion', tab_2),
('Aplicaciones o plugins externos requeridos', tab_2),
('Directorios de la aplicacion', tab_2),
('Usuarios administradores o privilegiados', tab_2),
('Concepto tecnico', tab_2),
('Documentacion', tab_2),
('Fortalezas', tab_2),
('Debilidades', tab_2),"""
