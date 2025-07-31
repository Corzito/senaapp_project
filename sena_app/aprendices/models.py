from django.db import models

# Create your models here.
class Aprendiz(models.Model):
    documento_identidad = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100)
    programa = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.documento_identidad}"