CREATE TABLE IF NOT EXISTS "tipousuarios" (
	"id_tipo_usuario" serial NOT NULL UNIQUE,
	"tipo" varchar(255) NOT NULL,
	PRIMARY KEY ("id_tipo_usuario")
);

CREATE TABLE IF NOT EXISTS "usuario" (
	"id_usuario" serial NOT NULL UNIQUE,
	"nombre" varchar(30) NOT NULL,
	"apellido_pat" varchar(30) NOT NULL,
	"apellido_mat" varchar(30) NOT NULL,
	"correo" varchar(40) NOT NULL,
	"id_contrasena" int NOT NULL,
	"id_tipo_usuario" int NOT NULL,
	"id_departamento" int NOT NULL,
	PRIMARY KEY ("id_usuario")
);

CREATE TABLE IF NOT EXISTS "contrasea" (
	"id_contrasena" serial NOT NULL UNIQUE,
	"contrasena" varchar(255) NOT NULL,
	PRIMARY KEY ("id_contrasena")
);

CREATE TABLE IF NOT EXISTS "proyecto" (
	"id_proyecto" serial NOT NULL UNIQUE,
	"nombre_proyecto" varchar(255) NOT NULL,
	"tipo_proyecto" int NOT NULL,
	"objetivo" varchar(255) NOT NULL,
	"etapa" varchar(255) NOT NULL,
	"financiamiento" varchar(255) NOT NULL,
	PRIMARY KEY ("id_proyecto")
);

CREATE TABLE IF NOT EXISTS "tipo_estancia" (
	"id_tipo_estancia" serial NOT NULL UNIQUE,
	"tipo_estancia" varchar(255) NOT NULL,
	PRIMARY KEY ("id_tipo_estancia")
);

CREATE TABLE IF NOT EXISTS "asesoria" (
	"id_asesoria" int NOT NULL UNIQUE,
	"tipo_asesoria" boolean NOT NULL,
	"id_grado_asesoria" int NOT NULL,
	"id_fases_proyecto" int NOT NULL,
	"institucion" varchar(255) NOT NULL,
	"fecha_inicio" date NOT NULL,
	"fecha_final" date NOT NULL,
	"recursos" boolean NOT NULL,
	PRIMARY KEY ("id_asesoria")
);

CREATE TABLE IF NOT EXISTS "estancia" (
	"id_estancia" serial NOT NULL UNIQUE,
	"id_tipo_estancia" int NOT NULL,
	"id_ciudad" int NOT NULL,
	PRIMARY KEY ("id_estancia")
);

CREATE TABLE IF NOT EXISTS "tutoria" (
	"id_tutoria" serial NOT NULL UNIQUE,
	"tipo_tutoria" boolean NOT NULL,
	"id_profesor" int NOT NULL,
	"id_estudiante" int NOT NULL,
	"carta_asignacion" bytea NOT NULL,
	"motivo_tutoria" varchar(255) NOT NULL,
	"atencion_seguimiento" varchar(255) NOT NULL,
	"evidencia" bytea NOT NULL,
	"fecha_inicio" date NOT NULL,
	"fecha_final" date NOT NULL,
	PRIMARY KEY ("id_tutoria")
);

CREATE TABLE IF NOT EXISTS "tipo_producto" (
	"id_tipo_producto" serial NOT NULL UNIQUE,
	"tipo_producto" varchar(255) NOT NULL,
	PRIMARY KEY ("id_tipo_producto")
);

CREATE TABLE IF NOT EXISTS "investigacion" (
	"id_investigacion" serial NOT NULL UNIQUE,
	"tipo_producto" int NOT NULL,
	"isbn" varchar(255) NOT NULL,
	"objeto_estudio" varchar(255) NOT NULL,
	"fecha_publicacion" date NOT NULL,
	"numero_edicion" varchar(255) NOT NULL,
	"lugar_publicacion" varchar(255) NOT NULL,
	"nombre_institucion" varchar(255) NOT NULL,
	PRIMARY KEY ("id_investigacion")
);

CREATE TABLE IF NOT EXISTS "servicio_social" (
	"id_servicio" serial NOT NULL UNIQUE,
	"id_estudiante" int NOT NULL,
	"id_estado" int NOT NULL,
	"tipo_proyecto" varchar(255) NOT NULL,
	"nombre_proyecto" varchar(255) NOT NULL,
	"beneficiarios" varchar(255) NOT NULL,
	"evidencias" bytea NOT NULL,
	"fecha_inicio" date NOT NULL,
	"fecha_final" date NOT NULL,
	"horas_acreditdas" int NOT NULL,
	"horas_pendientes" int NOT NULL,
	"horas_proyecto" int NOT NULL,
	"fecha_ultimo_reporte" date NOT NULL,
	PRIMARY KEY ("id_servicio")
);

CREATE TABLE IF NOT EXISTS "estado_servicio" (
	"id_estado" serial NOT NULL UNIQUE,
	"estado" varchar(15) NOT NULL,
	PRIMARY KEY ("id_estado")
);

CREATE TABLE IF NOT EXISTS "vinculacion_acad" (
	"id_vinculacion_acad" serial NOT NULL UNIQUE,
	"id_estudiante" int NOT NULL,
	"institucion" varchar(255) NOT NULL,
	"fecha_inicio" date NOT NULL,
	"fecha_final" date NOT NULL,
	"acreditado" boolean NOT NULL,
	"beca" boolean NOT NULL,
	"nombre_beca" varchar(255) NOT NULL,
	"tipo_vinculacion" boolean NOT NULL,
	"id_ciudad" int NOT NULL,
	PRIMARY KEY ("id_vinculacion_acad")
);

CREATE TABLE IF NOT EXISTS "situacion" (
	"id_situacion" serial NOT NULL UNIQUE,
	"situacion" varchar(30) NOT NULL,
	PRIMARY KEY ("id_situacion")
);

CREATE TABLE IF NOT EXISTS "taller" (
	"id_taller" serial NOT NULL UNIQUE,
	"id_estudiante" int NOT NULL,
	"tipo_taller" boolean NOT NULL,
	"id_nombre_taller" int NOT NULL,
	"representante" boolean NOT NULL,
	"selectivo" boolean NOT NULL,
	"acreditado" boolean NOT NULL,
	"club" varchar(255) NOT NULL,
	PRIMARY KEY ("id_taller")
);

CREATE TABLE IF NOT EXISTS "nombre_taller" (
	"id_nombre_taller" serial NOT NULL UNIQUE,
	"nombre" varchar(30) NOT NULL,
	PRIMARY KEY ("id_nombre_taller")
);

CREATE TABLE IF NOT EXISTS "idioma" (
	"id_idioma" serial NOT NULL UNIQUE,
	"estudiante" int NOT NULL,
	"idioma" varchar(255) NOT NULL,
	"nivel" int NOT NULL,
	"acreditado" boolean NOT NULL,
	"asesorias" boolean NOT NULL,
	"certificacion" varchar(60) NOT NULL,
	PRIMARY KEY ("id_idioma")
);

CREATE TABLE IF NOT EXISTS "practica_prof" (
	"id_practica_prof" serial NOT NULL UNIQUE,
	"id_estudiante" int NOT NULL,
	"num_practica" int NOT NULL,
	"fecha_inicio" date NOT NULL,
	"fecha_final" date NOT NULL,
	"empresa" varchar(255) NOT NULL,
	"telefon_empresa" varchar(15) NOT NULL,
	"contratado" boolean NOT NULL,
	PRIMARY KEY ("id_practica_prof")
);

CREATE TABLE IF NOT EXISTS "estatus" (
	"id_estatus" serial NOT NULL UNIQUE,
	"estatus" varchar(15) NOT NULL,
	PRIMARY KEY ("id_estatus")
);

CREATE TABLE IF NOT EXISTS "estudiante" (
	"id_estudiante" serial NOT NULL UNIQUE,
	"matricula" varchar(10) NOT NULL UNIQUE,
	"nombre" varchar(40) NOT NULL,
	"curp" varchar(20) NOT NULL,
	"direccion" varchar(60) NOT NULL,
	"email_personal" varchar(30) NOT NULL,
	"telefono" varchar(10) NOT NULL,
	"iems_procedencia" varchar(255) NOT NULL,
	"generacion" varchar(255) NOT NULL,
	"id_tipo_ingreso" int NOT NULL,
	"fecha_ingreso" int NOT NULL,
	"discapacidad" boolean NOT NULL,
	"nombre_discapacidad" varchar(255) NOT NULL,
	"id_pro_edu" int NOT NULL,
	"id_situacion" int NOT NULL,
	"motivo_situacion" varchar(255) NOT NULL,
	"id_estatus" int NOT NULL,
	"beca" boolean NOT NULL,
	"tipo_beca" varchar(255) NOT NULL,
	"creditos" double precision NOT NULL,
	"derecho_servicio_social" boolean NOT NULL,
	"fecha_nac" date NOT NULL,
	"sexo" boolean NOT NULL,
	"hablante_indigena" boolean NOT NULL,
	"nombre_lengua" varchar(255) NOT NULL,
	"promedio" double precision NOT NULL,
	PRIMARY KEY ("id_estudiante")
);

CREATE TABLE IF NOT EXISTS "egresado" (
	"id_egresado" serial NOT NULL UNIQUE,
	"id_estudiante" int NOT NULL,
	"email" varchar(50) NOT NULL,
	"telefono" varchar(10) NOT NULL,
	"telefono_casa" varchar(10) NOT NULL,
	"red_social" varchar(255) NOT NULL,
	PRIMARY KEY ("id_egresado")
);

CREATE TABLE IF NOT EXISTS "profesor" (
	"id_profesor" serial NOT NULL UNIQUE,
	"id_usuario" int NOT NULL,
	"nombre" varchar(30) NOT NULL,
	"apellido_pat" varchar(30) NOT NULL,
	"apellido_mat" varchar(30) NOT NULL,
	"correo" varchar(50) NOT NULL,
	"id_grado_academico" int NOT NULL,
	"id_pro_edu" int NOT NULL,
	"jefe_departamento" boolean NOT NULL,
	"id_tipo_profesor" int NOT NULL,
	"id_estudio" int NOT NULL,
	"activo" boolean NOT NULL,
	"id_actividad" int NOT NULL,
	PRIMARY KEY ("id_profesor")
);

CREATE TABLE IF NOT EXISTS "excursion" (
	"id_excursion" serial NOT NULL UNIQUE,
	"tipo_excursion" boolean NOT NULL,
	"id_asignatura" int NOT NULL,
	"id_profesor" int NOT NULL,
	"destino" varchar(255) NOT NULL,
	"objetivo" varchar(255) NOT NULL,
	"evidencias" bytea NOT NULL,
	"fecha_inicio" date NOT NULL,
	"fecha_final" date NOT NULL,
	PRIMARY KEY ("id_excursion")
);

CREATE TABLE IF NOT EXISTS "asignatura" (
	"id_asignatura" serial NOT NULL UNIQUE,
	"nombre_asignatura" varchar(255) NOT NULL,
	"id_plan_acad" int NOT NULL,
	"clave" varchar(255) NOT NULL,
	PRIMARY KEY ("id_asignatura")
);

CREATE TABLE IF NOT EXISTS "capacitacion" (
	"id_capacitacion" serial NOT NULL UNIQUE,
	"id_profesor" int NOT NULL,
	"id_tipo_capacitacion" int NOT NULL,
	"evento" varchar(30) NOT NULL,
	"sede" varchar(255) NOT NULL,
	"organizador" varchar(255) NOT NULL,
	"fecha_inicio" date NOT NULL,
	"fecha_final" date NOT NULL,
	PRIMARY KEY ("id_capacitacion")
);

CREATE TABLE IF NOT EXISTS "tipo_capacitacion" (
	"id_tipo_capacitacion" serial NOT NULL UNIQUE,
	"tipo" varchar(15) NOT NULL,
	PRIMARY KEY ("id_tipo_capacitacion")
);

CREATE TABLE IF NOT EXISTS "tipo_evento" (
	"id_tipo_evento" serial NOT NULL UNIQUE,
	"tipo_evento" varchar(30) NOT NULL,
	PRIMARY KEY ("id_tipo_evento")
);

CREATE TABLE IF NOT EXISTS "pro_edu" (
	"id_pro_edu" serial NOT NULL UNIQUE,
	"nombre_pro_edu" varchar(60) NOT NULL,
	PRIMARY KEY ("id_pro_edu")
);

CREATE TABLE IF NOT EXISTS "plan_acad" (
	"id_plan_acad" serial NOT NULL UNIQUE,
	"id_pro_edu" int NOT NULL,
	"nombre_plan_acad" varchar(30) NOT NULL,
	PRIMARY KEY ("id_plan_acad")
);

CREATE TABLE IF NOT EXISTS "pais" (
	"id_pais" serial NOT NULL UNIQUE,
	"nombre_pais" varchar(255) NOT NULL,
	PRIMARY KEY ("id_pais")
);

CREATE TABLE IF NOT EXISTS "estado" (
	"id_estado" serial NOT NULL UNIQUE,
	"nombre_estado" varchar(255) NOT NULL,
	PRIMARY KEY ("id_estado")
);

CREATE TABLE IF NOT EXISTS "ciudad" (
	"id_ciudad" serial NOT NULL UNIQUE,
	"id_estado" int NOT NULL,
	"id_pais" int NOT NULL,
	"nombre_ciudad" varchar(50) NOT NULL,
	PRIMARY KEY ("id_ciudad")
);

CREATE TABLE IF NOT EXISTS "evento_subcategoria" (
	"id_evento_subcategoria" serial NOT NULL UNIQUE,
	"subcategoria" varchar(30) NOT NULL,
	PRIMARY KEY ("id_evento_subcategoria")
);

CREATE TABLE IF NOT EXISTS "tipo_proyecto" (
	"id_tipo_proyecto" serial NOT NULL UNIQUE,
	"tipo" varchar(30) NOT NULL,
	PRIMARY KEY ("id_tipo_proyecto")
);

CREATE TABLE IF NOT EXISTS "profesor_proyecto" (
	"id_proyecto" int NOT NULL UNIQUE,
	"id_profesor" int NOT NULL,
	"fecha_inicio" date NOT NULL,
	"fecha_final" date NOT NULL,
	PRIMARY KEY ("id_proyecto")
);

CREATE TABLE IF NOT EXISTS "fase_proyecto" (
	"id_fase_proyecto" serial NOT NULL UNIQUE,
	"fase" varchar(30) NOT NULL,
	PRIMARY KEY ("id_fase_proyecto")
);

CREATE TABLE IF NOT EXISTS "asesoria_int" (
	"id_asesoria" int NOT NULL UNIQUE,
	"id_profesor" int NOT NULL,
	"id_estudiante" int NOT NULL,
	PRIMARY KEY ("id_asesoria")
);

CREATE TABLE IF NOT EXISTS "asesoria_ext" (
	"id_asesoria" int NOT NULL UNIQUE,
	"id_profesor" int NOT NULL,
	"nombre_asesorado" varchar(255) NOT NULL,
	PRIMARY KEY ("id_asesoria")
);

CREATE TABLE IF NOT EXISTS "profesor_estancia" (
	"id_estancia" int NOT NULL UNIQUE,
	"id_profesor" int NOT NULL,
	"id_tipo_institucion" varchar(255) NOT NULL,
	"motivo" varchar(255) NOT NULL,
	"objetivo" varchar(255) NOT NULL,
	"resultados" varchar(255) NOT NULL,
	"fecha_inicio" date NOT NULL,
	"fecha_final" date NOT NULL,
	PRIMARY KEY ("id_estancia")
);

CREATE TABLE IF NOT EXISTS "profesor_investigacion" (
	"id_investigacion" int NOT NULL UNIQUE,
	"id_profesor" int NOT NULL,
	"fecha_inicio" date NOT NULL,
	"fecha_final" date NOT NULL,
	PRIMARY KEY ("id_investigacion")
);

CREATE TABLE IF NOT EXISTS "tipo_profesor" (
	"id_tipo_profesor" serial NOT NULL UNIQUE,
	"tipo_profesor" int NOT NULL,
	PRIMARY KEY ("id_tipo_profesor")
);

CREATE TABLE IF NOT EXISTS "departamento" (
	"id_departamento" serial NOT NULL UNIQUE,
	"nombre_departamento" varchar(255) NOT NULL,
	PRIMARY KEY ("id_departamento")
);

CREATE TABLE IF NOT EXISTS "evento_acad" (
	"id_evento_acad" serial NOT NULL UNIQUE,
	"id_profesor" int NOT NULL,
	"id_tipo_evento" int NOT NULL,
	"id_evento_subcategoria" int NOT NULL,
	"nombre_evento" varchar(255) NOT NULL,
	"fecha_inicio" date NOT NULL,
	"fecha_final" date NOT NULL,
	PRIMARY KEY ("id_evento_acad")
);

CREATE TABLE IF NOT EXISTS "grado_academico" (
	"id_grado_academico" serial NOT NULL UNIQUE,
	"grado_academico" varchar(255) NOT NULL,
	PRIMARY KEY ("id_grado_academico")
);

CREATE TABLE IF NOT EXISTS "estudios" (
	"id_estudios" serial NOT NULL UNIQUE,
	"id_profesor" int NOT NULL,
	"grado_actual" varchar(255) NOT NULL,
	"grado_estudiando" varchar(255) NOT NULL,
	"fecha_inicio" date NOT NULL,
	"fecha_final" date NOT NULL,
	"nombre_institucion" varchar(255) NOT NULL,
	PRIMARY KEY ("id_estudios")
);

CREATE TABLE IF NOT EXISTS "grado_asesoria" (
	"id_grado_asesoria" serial NOT NULL UNIQUE,
	"grado" varchar(255) NOT NULL,
	PRIMARY KEY ("id_grado_asesoria")
);

CREATE TABLE IF NOT EXISTS "actividadesInactivo" (
	"id_actividad" serial NOT NULL UNIQUE,
	"id_profesor" int NOT NULL,
	"cartaautorizacion" bytea NOT NULL,
	"institucion" varchar(255) NOT NULL,
	"cartaaceptacioninst" bytea NOT NULL,
	"nombproyecto" varchar(255) NOT NULL,
	"fechainicio" date NOT NULL,
	"fechafinal" date NOT NULL,
	"cartareincorporacion" bytea NOT NULL,
	PRIMARY KEY ("id_actividad")
);

CREATE TABLE IF NOT EXISTS "tipo_ingreso" (
	"id_tipo_ingreso" serial NOT NULL UNIQUE,
	"ingreso" varchar(255) NOT NULL,
	PRIMARY KEY ("id_tipo_ingreso")
);


ALTER TABLE "usuario" ADD CONSTRAINT "usuario_fk5" FOREIGN KEY ("id_contrasena") REFERENCES "contrasea"("id_contrasena");

ALTER TABLE "usuario" ADD CONSTRAINT "usuario_fk6" FOREIGN KEY ("id_tipo_usuario") REFERENCES "tipousuarios"("id_tipo_usuario");

ALTER TABLE "usuario" ADD CONSTRAINT "usuario_fk7" FOREIGN KEY ("id_departamento") REFERENCES "departamento"("id_departamento");

ALTER TABLE "proyecto" ADD CONSTRAINT "proyecto_fk2" FOREIGN KEY ("tipo_proyecto") REFERENCES "tipo_proyecto"("id_tipo_proyecto");

ALTER TABLE "asesoria" ADD CONSTRAINT "asesoria_fk2" FOREIGN KEY ("id_grado_asesoria") REFERENCES "grado_asesoria"("id_grado_asesoria");

ALTER TABLE "asesoria" ADD CONSTRAINT "asesoria_fk3" FOREIGN KEY ("id_fases_proyecto") REFERENCES "fase_proyecto"("id_fase_proyecto");
ALTER TABLE "estancia" ADD CONSTRAINT "estancia_fk1" FOREIGN KEY ("id_tipo_estancia") REFERENCES "tipo_estancia"("id_tipo_estancia");

ALTER TABLE "estancia" ADD CONSTRAINT "estancia_fk2" FOREIGN KEY ("id_ciudad") REFERENCES "ciudad"("id_ciudad");
ALTER TABLE "tutoria" ADD CONSTRAINT "tutoria_fk2" FOREIGN KEY ("id_profesor") REFERENCES "profesor"("id_profesor");

ALTER TABLE "tutoria" ADD CONSTRAINT "tutoria_fk3" FOREIGN KEY ("id_estudiante") REFERENCES "estudiante"("id_estudiante");

ALTER TABLE "investigacion" ADD CONSTRAINT "investigacion_fk1" FOREIGN KEY ("tipo_producto") REFERENCES "tipo_producto"("id_tipo_producto");
ALTER TABLE "servicio_social" ADD CONSTRAINT "servicio_social_fk1" FOREIGN KEY ("id_estudiante") REFERENCES "estudiante"("id_estudiante");

ALTER TABLE "servicio_social" ADD CONSTRAINT "servicio_social_fk2" FOREIGN KEY ("id_estado") REFERENCES "estado_servicio"("id_estado");

ALTER TABLE "vinculacion_acad" ADD CONSTRAINT "vinculacion_acad_fk1" FOREIGN KEY ("id_estudiante") REFERENCES "estudiante"("id_estudiante");

ALTER TABLE "vinculacion_acad" ADD CONSTRAINT "vinculacion_acad_fk9" FOREIGN KEY ("id_ciudad") REFERENCES "ciudad"("id_ciudad");

ALTER TABLE "taller" ADD CONSTRAINT "taller_fk1" FOREIGN KEY ("id_estudiante") REFERENCES "estudiante"("id_estudiante");

ALTER TABLE "taller" ADD CONSTRAINT "taller_fk3" FOREIGN KEY ("id_nombre_taller") REFERENCES "nombre_taller"("id_nombre_taller");

ALTER TABLE "idioma" ADD CONSTRAINT "idioma_fk1" FOREIGN KEY ("estudiante") REFERENCES "estudiante"("id_estudiante");
ALTER TABLE "practica_prof" ADD CONSTRAINT "practica_prof_fk1" FOREIGN KEY ("id_estudiante") REFERENCES "estudiante"("id_estudiante");

ALTER TABLE "estudiante" ADD CONSTRAINT "estudiante_fk9" FOREIGN KEY ("id_tipo_ingreso") REFERENCES "tipo_ingreso"("id_tipo_ingreso");

ALTER TABLE "estudiante" ADD CONSTRAINT "estudiante_fk13" FOREIGN KEY ("id_pro_edu") REFERENCES "pro_edu"("id_pro_edu");

ALTER TABLE "estudiante" ADD CONSTRAINT "estudiante_fk14" FOREIGN KEY ("id_situacion") REFERENCES "situacion"("id_situacion");

ALTER TABLE "estudiante" ADD CONSTRAINT "estudiante_fk16" FOREIGN KEY ("id_estatus") REFERENCES "estatus"("id_estatus");
ALTER TABLE "egresado" ADD CONSTRAINT "egresado_fk1" FOREIGN KEY ("id_estudiante") REFERENCES "estudiante"("id_estudiante");
ALTER TABLE "profesor" ADD CONSTRAINT "profesor_fk1" FOREIGN KEY ("id_usuario") REFERENCES "usuario"("id_usuario");

ALTER TABLE "profesor" ADD CONSTRAINT "profesor_fk6" FOREIGN KEY ("id_grado_academico") REFERENCES "grado_academico"("id_grado_academico");

ALTER TABLE "profesor" ADD CONSTRAINT "profesor_fk7" FOREIGN KEY ("id_pro_edu") REFERENCES "pro_edu"("id_pro_edu");

ALTER TABLE "profesor" ADD CONSTRAINT "profesor_fk9" FOREIGN KEY ("id_tipo_profesor") REFERENCES "tipo_profesor"("id_tipo_profesor");

ALTER TABLE "profesor" ADD CONSTRAINT "profesor_fk10" FOREIGN KEY ("id_estudio") REFERENCES "estudios"("id_estudios");

ALTER TABLE "profesor" ADD CONSTRAINT "profesor_fk12" FOREIGN KEY ("id_actividad") REFERENCES "actividadesInactivo"("id_actividad");
ALTER TABLE "excursion" ADD CONSTRAINT "excursion_fk2" FOREIGN KEY ("id_asignatura") REFERENCES "asignatura"("id_asignatura");

ALTER TABLE "excursion" ADD CONSTRAINT "excursion_fk3" FOREIGN KEY ("id_profesor") REFERENCES "profesor"("id_profesor");
ALTER TABLE "asignatura" ADD CONSTRAINT "asignatura_fk2" FOREIGN KEY ("id_plan_acad") REFERENCES "plan_acad"("id_plan_acad");
ALTER TABLE "capacitacion" ADD CONSTRAINT "capacitacion_fk1" FOREIGN KEY ("id_profesor") REFERENCES "profesor"("id_profesor");

ALTER TABLE "capacitacion" ADD CONSTRAINT "capacitacion_fk2" FOREIGN KEY ("id_tipo_capacitacion") REFERENCES "tipo_capacitacion"("id_tipo_capacitacion");



ALTER TABLE "plan_acad" ADD CONSTRAINT "plan_acad_fk1" FOREIGN KEY ("id_pro_edu") REFERENCES "pro_edu"("id_pro_edu");


ALTER TABLE "ciudad" ADD CONSTRAINT "ciudad_fk1" FOREIGN KEY ("id_estado") REFERENCES "estado"("id_estado");

ALTER TABLE "ciudad" ADD CONSTRAINT "ciudad_fk2" FOREIGN KEY ("id_pais") REFERENCES "pais"("id_pais");


ALTER TABLE "profesor_proyecto" ADD CONSTRAINT "profesor_proyecto_fk0" FOREIGN KEY ("id_proyecto") REFERENCES "proyecto"("id_proyecto");

ALTER TABLE "profesor_proyecto" ADD CONSTRAINT "profesor_proyecto_fk1" FOREIGN KEY ("id_profesor") REFERENCES "profesor"("id_profesor");

ALTER TABLE "asesoria_int" ADD CONSTRAINT "asesoria_int_fk0" FOREIGN KEY ("id_asesoria") REFERENCES "asesoria"("id_asesoria");

ALTER TABLE "asesoria_int" ADD CONSTRAINT "asesoria_int_fk1" FOREIGN KEY ("id_profesor") REFERENCES "profesor"("id_profesor");

ALTER TABLE "asesoria_int" ADD CONSTRAINT "asesoria_int_fk2" FOREIGN KEY ("id_estudiante") REFERENCES "estudiante"("id_estudiante");
ALTER TABLE "asesoria_ext" ADD CONSTRAINT "asesoria_ext_fk0" FOREIGN KEY ("id_asesoria") REFERENCES "asesoria"("id_asesoria");

ALTER TABLE "asesoria_ext" ADD CONSTRAINT "asesoria_ext_fk1" FOREIGN KEY ("id_profesor") REFERENCES "profesor"("id_profesor");
ALTER TABLE "profesor_estancia" ADD CONSTRAINT "profesor_estancia_fk0" FOREIGN KEY ("id_estancia") REFERENCES "estancia"("id_estancia");

ALTER TABLE "profesor_estancia" ADD CONSTRAINT "profesor_estancia_fk1" FOREIGN KEY ("id_profesor") REFERENCES "profesor"("id_profesor");
ALTER TABLE "profesor_investigacion" ADD CONSTRAINT "profesor_investigacion_fk0" FOREIGN KEY ("id_investigacion") REFERENCES "investigacion"("id_investigacion");

ALTER TABLE "profesor_investigacion" ADD CONSTRAINT "profesor_investigacion_fk1" FOREIGN KEY ("id_profesor") REFERENCES "profesor"("id_profesor");


ALTER TABLE "evento_acad" ADD CONSTRAINT "evento_acad_fk1" FOREIGN KEY ("id_profesor") REFERENCES "profesor"("id_profesor");

ALTER TABLE "evento_acad" ADD CONSTRAINT "evento_acad_fk2" FOREIGN KEY ("id_tipo_evento") REFERENCES "tipo_evento"("id_tipo_evento");

ALTER TABLE "evento_acad" ADD CONSTRAINT "evento_acad_fk3" FOREIGN KEY ("id_evento_subcategoria") REFERENCES "evento_subcategoria"("id_evento_subcategoria");

ALTER TABLE "estudios" ADD CONSTRAINT "estudios_fk1" FOREIGN KEY ("id_profesor") REFERENCES "profesor"("id_profesor");

ALTER TABLE "actividadesInactivo" ADD CONSTRAINT "actividadesInactivo_fk1" FOREIGN KEY ("id_profesor") REFERENCES "profesor"("id_profesor");
