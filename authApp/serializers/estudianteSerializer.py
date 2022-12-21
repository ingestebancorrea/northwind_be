from rest_framework import serializers
from authApp.models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['id','nombres','grado','salon']