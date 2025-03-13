from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class EgresadoViewSet(viewsets.ModelViewSet):
        queryset = Egresado.objects.all()
        serializer_class = CiudadSerializer

class EstadoViewSet(viewsets.ModelViewSet):
        queryset = Estado.objects.all()
        serializer_class = EstadoSerializer

class EstadoServicioViewSet(viewsets.ModelViewSet):
        queryset = EstadoServicio.objects.all()
        serializer_class = EstadoServicioSerializer

class EstatusViewSet(viewsets.ModelViewSet):
        queryset = Estatus.objects.all()
        serializer_class = EstatusSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
        queryset = Estudiante.objects.all()
        serializer_class = EstudianteSerializer

class IdiomaViewSet(viewsets.ModelViewSet):
        queryset = Idioma.objects.all()
        serializer_class = IdiomaSerializer

class NombreTallerViewSet(viewsets.ModelViewSet):
        queryset = NombreTaller.objects.all()
        serializer_class = NombreTallerSerializer

class PaisViewSet(viewsets.ModelViewSet):
        queryset = Pais.objects.all()
        serializer_class = PaisSerializer

class PlanAcadViewSet(viewsets.ModelViewSet):
        queryset = PlanAcad.objects.all()
        serializer_class = PlanAcadSerializer

class PracticaProfViewSet(viewsets.ModelViewSet):
        queryset = PracticaProf.objects.all()
        serializer_class = PracticaProfSerializer

class ProEduViewSet(viewsets.ModelViewSet):
        queryset = ProEdu.objects.all()
        serializer_class = ProEduSerializer

class ServicioSociaLViewSet(viewsets.ModelViewSet):
        queryset = ServicioSocial.objects.all()
        serializer_class = ServicioSocialSerializer

class SituacionViewSet(viewsets.ModelViewSet):
        queryset = Situacion.objects.all()
        serializer_class = SituacionSerializer

class TallerViewSet(viewsets.ModelViewSet):
        queryset = Taller.objects.all()
        serializer_class = TallerSerializer

class TutoriaViewSet(viewsets.ModelViewSet):
        queryset = Tutoria.objects.all()
        serializer_class = TutoriaSerializer

class VinculacionAcadViewSet(viewsets.ModelViewSet):
        queryset = VinculacionAcad.objects.all()
        serializer_class = VinculacionAcadSerializer
