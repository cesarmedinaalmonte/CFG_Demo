from django.db import models


# Create your models here.
class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    telefono = models.CharField(max_length=15, verbose_name="Telefóno")
    publica = models.BooleanField(default=True, verbose_name="Público")

    def __str__(self):
        return  '%s' % (self.nombre)


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

    def __str__(self):
        return  '%s %s' % (self.nombre, self.apellidos)
