# miapp/serializers.py
from rest_framework import serializers
from .models import *  # Reemplaza con tu modelo

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

class EgresadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Egresado
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class EstadoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoServicio
        fields = '__all__'

class EstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estatus
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'

class NombreTallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NombreTaller
        fields = '__all__'

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class PlanAcadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanAcad
        fields = '__all__'

class PracticaProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticaProf
        fields = '__all__'

class ProEduSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProEdu
        fields = '__all__'

class ServicioSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioSocial
        fields = '__all__'

class SituacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situacion
        fields = '__all__'

class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = '__all__'

class TutoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutoria
        fields = '__all__'

class VinculacionAcadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VinculacionAcad
        fields = '__all__'
