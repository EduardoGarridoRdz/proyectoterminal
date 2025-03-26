# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# las tablas están listadas en orden alfabético

from django.db import models


class Actividadesinactivo(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    id_profesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profesor')
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
    id_grado_asesoria = models.ForeignKey('GradoAsesoria', models.DO_NOTHING, db_column='id_grado_asesoria')
    id_fases_proyecto = models.ForeignKey('FaseProyecto', models.DO_NOTHING, db_column='id_fases_proyecto')
    institucion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    recursos = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'asesoria'


class AsesoriaExt(models.Model):
    id_asesoria = models.OneToOneField(Asesoria, models.DO_NOTHING, db_column='id_asesoria', primary_key=True)
    id_profesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profesor')
    nombre_asesorado = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'asesoria_ext'


class AsesoriaInt(models.Model):
    id_asesoria = models.OneToOneField(Asesoria, models.DO_NOTHING, db_column='id_asesoria', primary_key=True)
    id_profesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profesor')
    id_estudiante = models.ForeignKey('Estudiante', models.DO_NOTHING, db_column='id_estudiante')

    class Meta:
        managed = False
        db_table = 'asesoria_int'


class Asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True)
    nombre_asignatura = models.CharField(max_length=255)
    id_plan_acad = models.ForeignKey('PlanAcad', models.DO_NOTHING, db_column='id_plan_acad')
    clave = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'asignatura'


class Capacitacion(models.Model):
    id_capacitacion = models.AutoField(primary_key=True)
    id_profesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profesor')
    id_tipo_capacitacion = models.ForeignKey('TipoCapacitacion', models.DO_NOTHING, db_column='id_tipo_capacitacion')
    evento = models.CharField(max_length=30)
    sede = models.CharField(max_length=255)
    organizador = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'capacitacion'


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    id_estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='id_estado')
    id_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='id_pais')
    nombre_ciudad = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'ciudad'


class Contrasea(models.Model):
    id_contrasena = models.AutoField(primary_key=True)
    contrasena = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'contrasea'


class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'departamento'


class Egresado(models.Model):
    id_egresado = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey('Estudiante', models.DO_NOTHING, db_column='id_estudiante')
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    telefono_casa = models.CharField(max_length=10)
    red_social = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'egresado'


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'estado'


class EstadoServicio(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'estado_servicio'


class Estancia(models.Model):
    id_estancia = models.AutoField(primary_key=True)
    id_tipo_estancia = models.ForeignKey('TipoEstancia', models.DO_NOTHING, db_column='id_tipo_estancia')
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad')

    class Meta:
        managed = False
        db_table = 'estancia'


class Estatus(models.Model):
    id_estatus = models.AutoField(primary_key=True)
    estatus = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'estatus'


class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
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
    id_estatus = models.ForeignKey(Estatus, models.DO_NOTHING, db_column='id_estatus')
    promedio = models.FloatField()
    id_pro_edu = models.ForeignKey('ProEdu', models.DO_NOTHING, db_column='id_pro_edu')
    id_situacion = models.ForeignKey('Situacion', models.DO_NOTHING, db_column='id_situacion')
    generacion = models.CharField(max_length=255)
    creditos = models.IntegerField()

    class Meta:
        managed =   True
        db_table = 'estudiante'


class Estudios(models.Model):
    id_estudios = models.AutoField(primary_key=True)
    id_profesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profesor')
    grado_actual = models.CharField(max_length=255)
    grado_estudiando = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    nombre_institucion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'estudios'


class EventoAcad(models.Model):
    id_evento_acad = models.AutoField(primary_key=True)
    id_profesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profesor')
    id_tipo_evento = models.ForeignKey('TipoEvento', models.DO_NOTHING, db_column='id_tipo_evento')
    id_evento_subcategoria = models.ForeignKey('EventoSubcategoria', models.DO_NOTHING, db_column='id_evento_subcategoria')
    nombre_evento = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'evento_acad'


class EventoSubcategoria(models.Model):
    id_evento_subcategoria = models.AutoField(primary_key=True)
    subcategoria = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'evento_subcategoria'


class Excursion(models.Model):
    id_excursion = models.AutoField(primary_key=True)
    tipo_excursion = models.BooleanField()
    id_asignatura = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='id_asignatura')
    id_profesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profesor')
    destino = models.CharField(max_length=255)
    objetivo = models.CharField(max_length=255)
    evidencias = models.BinaryField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'excursion'


class FaseProyecto(models.Model):
    id_fase_proyecto = models.AutoField(primary_key=True)
    fase = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'fase_proyecto'


class GradoAcademico(models.Model):
    id_grado_academico = models.AutoField(primary_key=True)
    grado_academico = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'grado_academico'


class GradoAsesoria(models.Model):
    id_grado_asesoria = models.AutoField(primary_key=True)
    grado = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'grado_asesoria'


class Idioma(models.Model):
    id_idioma = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='estudiante')
    nivel = models.CharField(max_length=10)
    acreditado = models.BooleanField()
    asesorias = models.BooleanField()
    certificacion = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'idioma'


class Investigacion(models.Model):
    id_investigacion = models.AutoField(primary_key=True)
    tipo_producto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='tipo_producto')
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
    id_nombre_taller = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'nombre_taller'


class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'pais'


class PlanAcad(models.Model):
    id_plan_acad = models.AutoField(primary_key=True)
    id_pro_edu = models.ForeignKey('ProEdu', models.DO_NOTHING, db_column='id_pro_edu')
    nombre_plan_acad = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'plan_acad'


class PracticaProf(models.Model):
    id_practica_prof = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='id_estudiante')
    num_practicas = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    empresa = models.CharField(max_length=255)
    contratado = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'practica_prof'


class ProEdu(models.Model):
    id_pro_edu = models.AutoField(primary_key=True)
    nombre_pro_edu = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'pro_edu'


class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    nombre = models.CharField(max_length=30)
    apellido_pat = models.CharField(max_length=30)
    apellido_mat = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    id_grado_academico = models.ForeignKey(GradoAcademico, models.DO_NOTHING, db_column='id_grado_academico')
    id_pro_edu = models.ForeignKey(ProEdu, models.DO_NOTHING, db_column='id_pro_edu')
    jefe_departamento = models.BooleanField()
    id_tipo_profesor = models.ForeignKey('TipoProfesor', models.DO_NOTHING, db_column='id_tipo_profesor')
    id_estudio = models.ForeignKey(Estudios, models.DO_NOTHING, db_column='id_estudio')
    activo = models.BooleanField()
    id_actividad = models.ForeignKey(Actividadesinactivo, models.DO_NOTHING, db_column='id_actividad')

    class Meta:
        managed = False
        db_table = 'profesor'


class ProfesorEstancia(models.Model):
    id_estancia = models.OneToOneField(Estancia, models.DO_NOTHING, db_column='id_estancia', primary_key=True)
    id_profesor = models.ForeignKey(Profesor, models.DO_NOTHING, db_column='id_profesor')
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
    id_investigacion = models.OneToOneField(Investigacion, models.DO_NOTHING, db_column='id_investigacion', primary_key=True)
    id_profesor = models.ForeignKey(Profesor, models.DO_NOTHING, db_column='id_profesor')
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'profesor_investigacion'


class ProfesorProyecto(models.Model):
    id_proyecto = models.OneToOneField('Proyecto', models.DO_NOTHING, db_column='id_proyecto', primary_key=True)
    id_profesor = models.ForeignKey(Profesor, models.DO_NOTHING, db_column='id_profesor')
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'profesor_proyecto'


class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=255)
    tipo_proyecto = models.ForeignKey('TipoProyecto', models.DO_NOTHING, db_column='tipo_proyecto')
    objetivo = models.CharField(max_length=255)
    etapa = models.CharField(max_length=255)
    financiamiento = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'proyecto'


class ServicioSocial(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='id_estudiante')
    id_estado = models.ForeignKey(EstadoServicio, models.DO_NOTHING, db_column='id_estado')
    tipo_proyecto = models.CharField(max_length=255)
    nombre_proyecto = models.CharField(max_length=255)
    beneficiarios = models.CharField(max_length=255)
    
    evidencias = models.BinaryField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = True
        db_table = 'servicio_social'


class Situacion(models.Model):
    id_situacion = models.AutoField(primary_key=True)
    situacion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'situacion'


class Taller(models.Model):
    id_taller = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='id_estudiante')
    tipo_taller = models.BooleanField()
    id_nombre_taller = models.ForeignKey(NombreTaller, models.DO_NOTHING, db_column='id_nombre_taller')
    representante = models.BooleanField()
    selectivo = models.BooleanField()
    acreditado = models.BooleanField()
    club = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'taller'


class TipoCapacitacion(models.Model):
    id_tipo_capacitacion = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tipo_capacitacion'


class TipoEstancia(models.Model):
    id_tipo_estancia = models.AutoField(primary_key=True)
    tipo_estancia = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_estancia'


class TipoEvento(models.Model):
    id_tipo_evento = models.AutoField(primary_key=True)
    tipo_evento = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_evento'


class TipoProducto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    tipo_producto = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoProfesor(models.Model):
    id_tipo_profesor = models.AutoField(primary_key=True)
    tipo_profesor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_profesor'


class TipoProyecto(models.Model):
    id_tipo_proyecto = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_proyecto'


class Tipousuarios(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'tipousuarios'


class Tutoria(models.Model):
    id_tutoria = models.AutoField(primary_key=True)
    tipo_tutoria = models.BooleanField()
    id_profesor = models.ForeignKey(Profesor, models.DO_NOTHING, db_column='id_profesor')
    id_estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='id_estudiante')
    carta_asignacion = models.BinaryField()
    motivo_tutoria = models.CharField(max_length=255)
    atencion_seguimiento = models.CharField(max_length=255)
    evidencia = models.BinaryField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = True
        db_table = 'tutoria'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido_pat = models.CharField(max_length=30)
    apellido_mat = models.CharField(max_length=30)
    correo = models.CharField(max_length=40)
    id_contrasena = models.ForeignKey(Contrasea, models.DO_NOTHING, db_column='id_contrasena')
    id_tipo_usuario = models.ForeignKey(Tipousuarios, models.DO_NOTHING, db_column='id_tipo_usuario')
    id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_departamento')

    class Meta:
        managed = True
        db_table = 'usuario'


class VinculacionAcad(models.Model):
    id_vinculacion_acad = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='id_estudiante')
    institucion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    acreditado = models.BooleanField()
    beca = models.BooleanField()
    nombre_beca = models.CharField(max_length=255)
    tipo_vinculacion = models.BooleanField()
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad')

    class Meta:
        managed = True
        db_table = 'vinculacion_acad'
