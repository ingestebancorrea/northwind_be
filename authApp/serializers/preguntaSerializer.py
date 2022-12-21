from rest_framework import serializers
from authApp.models import Pregunta

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ['id','respuesta','orden','prueba']