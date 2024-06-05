from django.db import models

from app.clases.models import Clase
from app.usuarios.models import Usuario

class Asistencia(models.Model): 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mis_asistencias")
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name="asistencias")
