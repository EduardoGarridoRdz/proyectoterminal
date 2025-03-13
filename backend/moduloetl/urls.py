# miapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
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



urlpatterns = [
    path('', include(router.urls)),  # Las URLs quedarán en /api/categorias/, /api/productos/, etc.
]