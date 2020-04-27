from django.db import models
from django.utils import timezone

class Cancha(models.Model):
    nombre = models.TextField()
    codigo = models.TextField()
    tipo = models.TextField()
    vestuario = models.BooleanField()
    iluminacion = models.BooleanField()
    cesped = models.BooleanField()

    def __str__(self):
        return self.nombre	

class Alquiler(models.Model):
	cancha = models.ForeignKey(Cancha , on_delete=models.CASCADE , related_name='alquileres')
	cliente = models.TextField()
	empleado = models.TextField()
	fechaReserva = models.DateTimeField(default=timezone.now)
	fechaHora = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.cliente
		