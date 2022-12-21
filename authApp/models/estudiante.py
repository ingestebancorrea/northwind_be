from django.db import models

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombre', max_length=40)
    grado = models.IntegerField('Grado')
    salon = models.CharField('Salon', max_length=20)