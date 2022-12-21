from django.db import models

class Prueba(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=30)
    año = models.DateField('Año')