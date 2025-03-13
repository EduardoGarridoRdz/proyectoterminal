# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actividadesinactivo(models.Model):
    id_actividad = models.IntegerField(primary_key=True)
    id_profesor = models.IntegerField()
    cartaautorizacion = models.BinaryField()
    institucion = models.CharField(max_length=255)
    cartaaceptacioninst = models.BinaryField()
    nombproyecto = models.CharField(max_length=255)
    fechainicio = models.DateField()
    fechafinal = models.DateField()
    cartareincorporacion = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'actividadesInactivo'


class Asesoria(models.Model):
    id_asesoria = models.IntegerField(primary_key=True)
    tipo_asesoria = models.BooleanField()
    id_grado_asesoria = models.IntegerField()
    id_fases_proyecto = models.IntegerField()
    institucion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    recursos = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'asesoria'


class AsesoriaExt(models.Model):
    id_asesoria = models.IntegerField(primary_key=True)
    id_profesor = models.IntegerField()
    nombre_asesorado = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'asesoria_ext'


class AsesoriaInt(models.Model):
    id_asesoria = models.IntegerField(primary_key=True)
    id_profesor = models.IntegerField()
    id_estudiante = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'asesoria_int'


class Asignatura(models.Model):
    id_asignatura = models.IntegerField(primary_key=True)
    nombre_asignatura = models.CharField(max_length=255)
    id_plan_acad = models.IntegerField()
    clave = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'asignatura'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Capacitacion(models.Model):
    id_capacitacion = models.IntegerField(primary_key=True)
    id_profesor = models.IntegerField()
    id_tipo_capacitacion = models.IntegerField()
    evento = models.CharField(max_length=30)
    sede = models.CharField(max_length=255)
    organizador = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'capacitacion'


class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    id_estado = models.IntegerField()
    id_pais = models.IntegerField()
    nombre_ciudad = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Contrasea(models.Model):
    id_contrasena = models.IntegerField(primary_key=True)
    contrasena = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'contrasea'


class Departamento(models.Model):
    id_departamento = models.IntegerField(primary_key=True)
    nombre_departamento = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'departamento'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Egresado(models.Model):
    id_egresado = models.IntegerField(primary_key=True)
    id_estudiante = models.IntegerField()
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    telefono_casa = models.CharField(max_length=10)
    red_social = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'egresado'


class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    nombre_estado = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'estado'


class EstadoServicio(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'estado_servicio'


class Estancia(models.Model):
    id_estancia = models.IntegerField(primary_key=True)
    id_tipo_estancia = models.IntegerField()
    id_ciudad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'estancia'


class Estatus(models.Model):
    id_estatus = models.IntegerField(primary_key=True)
    estatus = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'estatus'


class Estudiante(models.Model):
    id_estudiante = models.IntegerField(primary_key=True)
    matricula = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=40)
    apellido_pat = models.CharField(max_length=30)
    apellido_mat = models.CharField(max_length=30)
    fecha_nac = models.DateField()
    sexo = models.BooleanField()
    curp = models.CharField(max_length=20)
    email_personal = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    discapacidad = models.BooleanField()
    nombre_discapacidad = models.CharField(max_length=255)
    hablante_indigena = models.BooleanField()
    nombre_lengua = models.CharField(max_length=255)
    iems_procedencia = models.CharField(max_length=255)
    id_estatus = models.IntegerField()
    promedio = models.FloatField()
    id_pro_edu = models.IntegerField()
    id_situacion = models.IntegerField()
    generacion = models.CharField(max_length=255)
    creditos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'estudiante'


class Estudios(models.Model):
    id_estudios = models.IntegerField(primary_key=True)
    id_profesor = models.IntegerField()
    grado_actual = models.CharField(max_length=255)
    grado_estudiando = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    nombre_institucion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'estudios'


class EventoAcad(models.Model):
    id_evento_acad = models.IntegerField(primary_key=True)
    id_profesor = models.IntegerField()
    id_tipo_evento = models.IntegerField()
    id_evento_subcategoria = models.IntegerField()
    nombre_evento = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'evento_acad'


class EventoSubcategoria(models.Model):
    id_evento_subcategoria = models.IntegerField(primary_key=True)
    subcategoria = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'evento_subcategoria'


class Excursion(models.Model):
    id_excursion = models.IntegerField(primary_key=True)
    tipo_excursion = models.BooleanField()
    id_asignatura = models.IntegerField()
    id_profesor = models.IntegerField()
    destino = models.CharField(max_length=255)
    objetivo = models.CharField(max_length=255)
    evidencias = models.BinaryField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'excursion'


class FaseProyecto(models.Model):
    id_fase_proyecto = models.IntegerField(primary_key=True)
    fase = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'fase_proyecto'


class GradoAcademico(models.Model):
    id_grado_academico = models.IntegerField(primary_key=True)
    grado_academico = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'grado_academico'


class GradoAsesoria(models.Model):
    id_grado_asesoria = models.IntegerField(primary_key=True)
    grado = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'grado_asesoria'


class Idioma(models.Model):
    id_idioma = models.IntegerField(primary_key=True)
    estudiante = models.IntegerField()
    nivel = models.IntegerField()
    acreditado = models.BooleanField()
    asesorias = models.BooleanField()
    certificacion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'idioma'


class Investigacion(models.Model):
    id_investigacion = models.IntegerField(primary_key=True)
    tipo_producto = models.IntegerField()
    isbn = models.CharField(max_length=255)
    objeto_estudio = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    numero_edicion = models.CharField(max_length=255)
    lugar_publicacion = models.CharField(max_length=255)
    nombre_institucion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'investigacion'


class NombreTaller(models.Model):
    id_nombre_taller = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'nombre_taller'


class Pais(models.Model):
    id_pais = models.IntegerField(primary_key=True)
    nombre_pais = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pais'


class PlanAcad(models.Model):
    id_plan_acad = models.IntegerField(primary_key=True)
    id_pro_edu = models.IntegerField()
    nombre_plan_acad = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'plan_acad'


class PracticaProf(models.Model):
    id_practica_prof = models.IntegerField(primary_key=True)
    id_estudiante = models.IntegerField()
    num_practicas = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    empresa = models.CharField(max_length=255)
    contratado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'practica_prof'


class ProEdu(models.Model):
    id_pro_edu = models.IntegerField(primary_key=True)
    nombre_pro_edu = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'pro_edu'


class Profesor(models.Model):
    id_profesor = models.IntegerField(primary_key=True)
    id_usuario = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido_pat = models.CharField(max_length=30)
    apellido_mat = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    id_grado_academico = models.IntegerField()
    id_pro_edu = models.IntegerField()
    jefe_departamento = models.BooleanField()
    id_tipo_profesor = models.IntegerField()
    id_estudio = models.IntegerField()
    activo = models.BooleanField()
    id_actividad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profesor'


class ProfesorEstancia(models.Model):
    id_estancia = models.IntegerField(primary_key=True)
    id_profesor = models.IntegerField()
    id_tipo_institucion = models.CharField(max_length=255)
    motivo = models.CharField(max_length=255)
    objetivo = models.CharField(max_length=255)
    resultados = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'profesor_estancia'


class ProfesorInvestigacion(models.Model):
    id_investigacion = models.IntegerField(primary_key=True)
    id_profesor = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'profesor_investigacion'


class ProfesorProyecto(models.Model):
    id_proyecto = models.IntegerField(primary_key=True)
    id_profesor = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'profesor_proyecto'


class Proyecto(models.Model):
    id_proyecto = models.IntegerField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=255)
    tipo_proyecto = models.IntegerField()
    objetivo = models.CharField(max_length=255)
    etapa = models.CharField(max_length=255)
    financiamiento = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'proyecto'


class ServicioSocial(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    id_estudiante = models.IntegerField()
    id_estado = models.IntegerField()
    tipo_proyecto = models.CharField(max_length=255)
    nombre_proyecto = models.CharField(max_length=255)
    beneficiarios = models.CharField(max_length=255)
    evidencias = models.BinaryField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'servicio_social'


class Situacion(models.Model):
    id_situacion = models.IntegerField(primary_key=True)
    situacion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'situacion'


class Taller(models.Model):
    id_taller = models.IntegerField(primary_key=True)
    id_estudiante = models.IntegerField()
    tipo_taller = models.BooleanField()
    id_nombre_taller = models.IntegerField()
    representante = models.BooleanField()
    selectivo = models.BooleanField()
    acreditado = models.BooleanField()
    club = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'taller'


class TipoCapacitacion(models.Model):
    id_tipo_capacitacion = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tipo_capacitacion'


class TipoEstancia(models.Model):
    id_tipo_estancia = models.IntegerField(primary_key=True)
    tipo_estancia = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_estancia'


class TipoEvento(models.Model):
    id_tipo_evento = models.IntegerField(primary_key=True)
    tipo_evento = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_evento'


class TipoProducto(models.Model):
    id_tipo_producto = models.IntegerField(primary_key=True)
    tipo_producto = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoProfesor(models.Model):
    id_tipo_profesor = models.IntegerField(primary_key=True)
    tipo_profesor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_profesor'


class TipoProyecto(models.Model):
    id_tipo_proyecto = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_proyecto'


class Tipousuarios(models.Model):
    id_tipo_usuario = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tipousuarios'


class Tutoria(models.Model):
    id_tutoria = models.IntegerField(primary_key=True)
    tipo_tutoria = models.BooleanField()
    id_profesor = models.IntegerField()
    id_estudiante = models.IntegerField()
    carta_asignacion = models.BinaryField()
    motivo_tutoria = models.CharField(max_length=255)
    atencion_seguimiento = models.CharField(max_length=255)
    evidencia = models.BinaryField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'tutoria'


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido_pat = models.CharField(max_length=30)
    apellido_mat = models.CharField(max_length=30)
    correo = models.CharField(max_length=40)
    id_contrasena = models.ForeignKey(Contrasea, models.DO_NOTHING, db_column='id_contrasena')
    id_tipo_usuario = models.IntegerField()
    id_departamento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'


class VinculacionAcad(models.Model):
    id_vinculacion_acad = models.IntegerField(primary_key=True)
    id_estudiante = models.IntegerField()
    institucion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    acreditado = models.BooleanField()
    beca = models.BooleanField()
    nombre_beca = models.CharField(max_length=255)
    tipo_vinculacion = models.BooleanField()
    id_ciudad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vinculacion_acad'
