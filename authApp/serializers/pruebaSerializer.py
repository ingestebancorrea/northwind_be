from rest_framework import serializers
from authApp.models import Prueba

class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = ['id','nombre','año']