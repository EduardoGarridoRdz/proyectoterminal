# miapp/urls.py
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
# <----------------------- ESTUDIANTES --------------------------> #
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
router.register(r'vinculacionAcad', VinculacionAcadViewSet)

# <----------------------- PROFESORES --------------------------> #
router.register(r'profesores', ProfesorViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('docs/', include_docs_urls(title="API DOCS")),
    #Prueba para subir archivos excel
    path('recibirDatos/', recibir_json, name='recibir_json')
]