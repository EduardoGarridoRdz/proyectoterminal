from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# <----------------------- ESTUDIANTES --------------------------> #
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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def recibir_json(request):
    if request.method == 'POST':
        try:
            # Leer el cuerpo de la solicitud (el JSON enviado desde el frontend)
            data = json.loads(request.body)
            
            # Imprimir el JSON en la consola del servidor
            print("JSON recibido:", data)
            

            # Responder con un mensaje de éxito
            return JsonResponse({'status': 'success', 'message': 'JSON recibido correctamente.'})
        except Exception as e:
            # Manejar errores
            print("Error al procesar el JSON:", str(e))
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)


# <----------------------- PROFESORES --------------------------> #
class ProfesorViewSet(viewsets.ModelViewSet):
        queryset = Profesor.objects.all()
        serializer_class = ProfesorSerializer