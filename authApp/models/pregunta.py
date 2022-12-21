from django.db import models
from .prueba import Prueba

class Pregunta(models.Model):
    id = models.AutoField(primary_key=True)
    respuesta = models.CharField('Respuesta', max_length=2)
    orden = models.IntegerField('Orden')
    prueba = models.ForeignKey(Prueba, related_name='fk_pruebas_preguntas', on_delete=models.CASCADE)