from rest_framework import serializers
from authApp.models import Resultado

class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = ['id','estudiante','prueba','pregunta']