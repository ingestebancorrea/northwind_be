from django.contrib import admin
from .models.estudiante import Estudiante
from .models.pregunta import Pregunta
from .models.prueba import Prueba
from .models.resultado import Resultado

admin.site.register(Estudiante)
admin.site.register(Pregunta)
admin.site.register(Prueba)
admin.site.register(Resultado)