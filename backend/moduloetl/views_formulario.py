from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Proyecto, TipoEstancia, Capacitacion, EventoAcad, FaseProyecto,
    TipoCapacitacion, TipoEvento, EventoSubcategoria, Profesor, Usuario,
    Contrasena, Departamento, Tipousuarios, GradoAcademico, ProEdu,
    TipoProfesor, Estudios, Actividadesinactivo
)
from datetime import date

@api_view(['POST'])
def guardar_formulario(request):
    data = request.data
    print("Datos recibidos:", data)
    try:
        from django.db import connection, transaction
        
        with transaction.atomic():
            # Variables necesarias
            usuario = Usuario.objects.first()
            grado, _ = GradoAcademico.objects.get_or_create(grado_academico="Licenciatura")
            proedu, _ = ProEdu.objects.get_or_create(nombre_pro_edu="UPQ")
            tipo_profesor, _ = TipoProfesor.objects.get_or_create(tipo_profesor=1)
            hoy = date.today()
            
            # 1. Insertar directamente en la tabla estudios y actividadesinactivo con id_profesor nulo
            with connection.cursor() as cursor:
                # Para PostgreSQL, deshabilitar restricciones temporalmente
                cursor.execute("SET CONSTRAINTS ALL DEFERRED;")
                
                # Insertar un estudio sin id_profesor
                cursor.execute(
                    """
                    INSERT INTO estudios (grado_actual, grado_estudiando, fecha_inicio, fecha_final, nombre_institucion, id_profesor)
                    VALUES (%s, %s, %s, %s, %s, NULL) RETURNING id_estudios
                    """, 
                    ["Licenciatura", "Maestría", hoy, hoy, "UPQ"]
                )
                estudio_id = cursor.fetchone()[0]
                
                # Insertar actividad sin id_profesor
                cursor.execute(
                    """
                    INSERT INTO "actividadesInactivo" (cartaautorizacion, institucion, cartaaceptacioninst, nombproyecto, fechainicio, fechafinal, cartareincorporacion, id_profesor)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, NULL) RETURNING id_actividad
                    """, 
                    [bytes(), "UPQ", bytes(), "Proyecto Prueba", hoy, hoy, bytes()]
                )
                actividad_id = cursor.fetchone()[0]
                
                # Crear profesor con las referencias a estudio y actividad
                cursor.execute(
                    """
                    INSERT INTO profesor (nombre, apellido_pat, apellido_mat, correo, id_usuario_id, id_grado_academico_id, id_pro_edu_id, jefe_departamento, id_tipo_profesor_id, id_estudio_id, activo, id_actividad_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_profesor
                    """, 
                    [data.get("nombreProfesor"), "-", "-", "correo@prueba.com", usuario.id, grado.id, proedu.id, False, tipo_profesor.id, estudio_id, True, actividad_id]
                )
                profesor_id = cursor.fetchone()[0]
                
                # Actualizar estudio y actividad con el id del profesor
                cursor.execute("UPDATE estudios SET id_profesor = %s WHERE id_estudios = %s", [profesor_id, estudio_id])
                cursor.execute("UPDATE \"actividadesInactivo\" SET id_profesor = %s WHERE id_actividad = %s", [profesor_id, actividad_id])
                
                # Confirmar las transacciones
                cursor.execute("SET CONSTRAINTS ALL IMMEDIATE;")
            
            # Obtener los objetos para usarlos en el resto del código
            profesor = Profesor.objects.get(id_profesor=profesor_id)
            
            # El resto del código como estaba...
            Proyecto.objects.create(
                nombre_proyecto=data.get("proyectoNombre"),
                tipo_proyecto_id=1,
                objetivo="Objetivo no especificado",
                etapa=data.get("faseProyecto"),
                financiamiento="Sin financiamiento"
            )
            
            TipoEstancia.objects.get_or_create(tipo_estancia=data.get("tipoEstancia"))
            
            Capacitacion.objects.create(
                evento=data.get("capacitacion"),
                sede="Por definir",
                organizador="Por definir",
                id_profesor=profesor,
                id_tipo_capacitacion=TipoCapacitacion.objects.get_or_create(tipo=data.get("tipoCapacitacion"))[0],
                fecha_inicio=hoy,
                fecha_final=hoy
            )
            
            EventoAcad.objects.create(
                nombre_evento=data.get("evento"),
                id_profesor=profesor,
                id_tipo_evento=TipoEvento.objects.get_or_create(tipo_evento="Otro")[0],
                id_evento_subcategoria=EventoSubcategoria.objects.get_or_create(subcategoria="General")[0],
                fecha_inicio=hoy,
                fecha_final=hoy
            )
            
        return Response({"mensaje": "Formulario recibido y datos guardados"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        print("Error:", e)
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)