from django.db import models
from .estudiante import Estudiante
from .prueba import Prueba
from .pregunta import Pregunta

class Resultado(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, related_name='fk_estudiantes_resultados', on_delete=models.CASCADE)
    prueba = models.ForeignKey(Prueba, related_name='fk_pruebas_resultados', on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, related_name='fk_pregunta_resultados', on_delete=models.CASCADE)