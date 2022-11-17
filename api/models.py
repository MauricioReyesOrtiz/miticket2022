from django.db import models
from datetime import datetime
# Create your models here.
class Cliente (models.Model):
    nombre=models.CharField(max_length=50)
    paterno=models.CharField(max_length=50)
    materno=models.CharField(max_length=50)
    fechanac = models.DateTimeField(max_length=50)

class Ticket (models.Model):
    numticket=models.CharField(max_length=50)
    servicio=models.CharField(max_length=50)
    fecha=models.DateTimeField(max_length=50)
    idcliente=models.PositiveIntegerField()
    
