# miapp/urls.py
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import *
from .procesamiento import RecibirArchivo
from .views_formulario import guardar_formulario
from .formato_archivo import FormatoArchivo

router = routers.DefaultRouter()


""" <----------------------- ESTUDIANTES --------------------------> """
router.register(r'ciudad', CiudadViewSet)
router.register(r'egresado', EgresadoViewSet)
router.register(r'estado', EstadoViewSet)
router.register(r'estadoServicio', EstadoServicioViewSet)
router.register(r'estatus', EstatusViewSet)
router.register(r'estudiante', EstudianteViewSet)
router.register(r'idioma', IdiomaViewSet)
router.register(r'nombreTaller', NombreTallerViewSet)
router.register(r'pais', PaisViewSet)
router.register(r'planAcad', PlanAcadViewSet)
router.register(r'practicaProf', PracticaProfViewSet)
router.register(r'proEdu', ProEduViewSet)
router.register(r'servicioSocial', ServicioSociaLViewSet)
router.register(r'situacion', SituacionViewSet)
router.register(r'taller', TallerViewSet)
router.register(r'tutoria', TutoriaViewSet)
router.register(r'tipoingreso', TipoIngresoViewSet)
router.register(r'vinculacionAcad', VinculacionAcadViewSet)


""" <----------------------- PROFESORES --------------------------> """
router.register(r'profesores', ProfesorViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'tipo_estancia', TipoEstanciaViewSet)
router.register(r'asesorias', AsesoriaViewSet)
router.register(r'estancias', EstanciaViewSet)
router.register(r'tipo_producto', TipoProductoViewSet)
router.register(r'investigaciones', InvestigacionViewSet)
router.register(r'excursiones', ExcursionViewSet)
router.register(r'asignaturas', AsignaturaViewSet)
router.register(r'capacitaciones', CapacitacionViewSet)
router.register(r'tipo_capacitacion', TipoCapacitacionViewSet)
router.register(r'tipo_evento', TipoEventoViewSet)
router.register(r'evento_subcategoria', EventoSubcategoriaViewSet)
router.register(r'tipo_proyecto', TipoProyectoViewSet)
router.register(r'profesor_proyecto', ProfesorProyectoViewSet)
router.register(r'fase_proyecto', FaseProyectoViewSet)
router.register(r'asesoria_int', AsesoriaIntViewSet)
router.register(r'asesoria_ext', AsesoriaExtViewSet)
router.register(r'profesor_estancia', ProfesorEstanciaViewSet)
router.register(r'profesor_investigacion', ProfesorInvestigacionViewSet)
router.register(r'tipo_profesor', TipoProfesorViewSet)
router.register(r'evento_academico', EventoAcadViewSet)
router.register(r'grado_academico', GradoAcademicoViewSet)
router.register(r'estudios', EstudiosViewSet)
router.register(r'grado_asesoria', GradoAsesoriaViewSet)
router.register(r'actividades_inactivo', ActividadesinactivoViewSet)


urlpatterns = [
    path('', include(router.urls)), 
    path('docs/', include_docs_urls(title="API DOCS")),
    path('ProcesarExcel/', RecibirArchivo),
    path('guardar_formulario/', guardar_formulario, name='guardar-formulario'),

    path('FormatoArchivo/', FormatoArchivo),
 ]