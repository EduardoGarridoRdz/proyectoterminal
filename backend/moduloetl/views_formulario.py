from django.db.models import Value, CharField
from django.db.models.functions import Concat
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Profesor, Proyecto, ProfesorProyecto, Investigacion, TipoProyecto, Estudios,
    Capacitacion, FaseProyecto, TipoCapacitacion, EventoAcad
)
import re
from datetime import datetime

@api_view(['POST'])
def guardar_formulario_unificado(request):
    data = request.data
    nombre_profesor = data.get("nombreProfesor")

    if not nombre_profesor:
        return Response({"error": "Campo 'nombreProfesor' requerido"}, status=status.HTTP_400_BAD_REQUEST)

    # Limpiar prefijos como Dr., Mtro., etc.
    nombre_profesor = re.sub(r'^(Dr\.|Dra\.|Mtro\.|Mtra\.)\s+', '', nombre_profesor).strip()

    # Buscar al profesor por nombre completo
    profesor = Profesor.objects.annotate(
        nombre_completo=Concat('nombre', Value(' '), 'apellido_pat', Value(' '), 'apellido_mat', output_field=CharField())
    ).filter(nombre_completo__icontains=nombre_profesor).first()

    if not profesor:
        return Response({"error": "Profesor no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # 1. Formación Personal Académica
    if "formacionAcademica" in data:
        formacion = data["formacionAcademica"]
        Estudios.objects.create(
            id_profesor=profesor,
            grado_actual=formacion["gradoActual"],
            grado_estudiando=formacion["gradoEstudiando"],
            fecha_inicio=formacion["fechaInicio"],
            fecha_final=formacion["fechaFinal"],
            nombre_institucion=formacion["nombreInstitucion"]
        )
        if "fase" in formacion:
            FaseProyecto.objects.get_or_create(fase=formacion["fase"])

    # 2. Proyecto de Investigación
    if "proyectoInvestigacion" in data:
        proj = data["proyectoInvestigacion"]
        tipo = TipoProyecto.objects.filter(tipo__iexact=proj["tipoProyecto"]).first()
        if tipo:
            proyecto = Proyecto.objects.create(
                nombre_proyecto=proj["proyectoNombre"],
                tipo_proyecto=tipo,
                objetivo=proj["resultadosImpactos"],
                etapa="",
                financiamiento=""
            )
            ProfesorProyecto.objects.create(
                id_profesor=profesor,
                id_proyecto=proyecto,
                fecha_inicio=datetime.now().date(),
                fecha_final=datetime.now().date()
            )

    # 3. Actividad de Vinculación
    if "actividadVinculacion" in data:
        vinc = data["actividadVinculacion"]
        Investigacion.objects.create(
            tipo_producto_id=1,
            isbn="",
            objeto_estudio=vinc["descripcionActividad"],
            fecha_publicacion=vinc["fechaVinculacion"],
            numero_edicion="",
            lugar_publicacion=vinc["institucionVinculada"],
            nombre_institucion=vinc["resultadoVinculacion"]
        )

    # 4. Dirección de Proyectos Terminales
    if "proyectoTerminal" in data:
        pt = data["proyectoTerminal"]
        EventoAcad.objects.create(
            id_profesor=profesor,
            id_tipo_evento_id=1,
            id_evento_subcategoria_id=1,
            nombre_evento=pt["nombrePT"],
            fecha_inicio=pt["fechaPT"],
            fecha_final=pt["fechaPT"]
        )

    # 5. Actividades Anuales Académicas
    if "actividadAnual" in data:
        act = data["actividadAnual"]
        Investigacion.objects.create(
            tipo_producto_id=2,
            isbn=act["linkProducto"],
            objeto_estudio=act["productosAcademicos"],
            fecha_publicacion=f"{act['anioPublicacion']}-01-01",
            numero_edicion="",
            lugar_publicacion=act["sedeActividad"],
            nombre_institucion=""
        )

    # 6. Capacitación
    if "capacitacion" in data:
        cap = data["capacitacion"]
        tipo_cap = TipoCapacitacion.objects.filter(tipo__iexact=cap["tipo"]).first()
        if tipo_cap:
            Capacitacion.objects.create(
                id_profesor=profesor,
                id_tipo_capacitacion=tipo_cap,
                evento=cap["evento"],
                sede="",
                organizador="",
                fecha_inicio=datetime.now().date(),
                fecha_final=datetime.now().date()
            )

    return Response({"mensaje": "Formulario completo guardado exitosamente"}, status=status.HTTP_201_CREATED)
