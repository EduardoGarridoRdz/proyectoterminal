from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *

from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action

import pandas as pd
import io

########## ESTUDIANTES #####################
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

import pandas as pd
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

class ExcelUploadViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser]

    @action(detail=False, methods=['post'])
    def upload_excel(self, request):
        if 'file' not in request.FILES:
            return Response({'status': 'error', 'message': 'No file uploaded'}, status=400)

        excel_file = request.FILES['file']
        try:
            # Leer el archivo Excel con Pandas
            df = pd.read_excel(excel_file)

            # Convertir el DataFrame a un diccionario
            data = df.to_dict(orient='records')  # 'records' devuelve una lista de diccionarios

            # Respuesta exitosa
            return Response({
                'status': 'success',
                'message': 'File processed successfully',
                'data': data,
            })
        except Exception as e:
            # Manejo de errores
            return Response({
                'status': 'error',
                'message': str(e),
            }, status=400)
#---------------------------------------------------------#

