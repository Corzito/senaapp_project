from django.db import models

# Create your models here.
class Instructor(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cedula de extranjeria'),
        ('TI', 'Tarjeta de identidad'),
        ('PAS', 'Pasaporte'),
    ]
    NIVEL_EDUCATIVO_CHOICES = [
        ('TEC', 'Tecnico'),
        ('TGL', 'Tecnologo'),
        ('PRE', 'Pregrado'),
        ('ESP', 'Especialización'),
        ('MAE', 'Maestria'),
        ('DOC', 'Doctorado'),
    ]
    
    documento_identidad = models.CharField(max_length=20, unique=True)
    tipo_documento = models.CharField(max_length=3, choices=TIPO_DOCUMENTO_CHOICES, default='CC')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100)
    nivel_educativo = models.CharField(max_length=3, choices=NIVEL_EDUCATIVO_CHOICES, default='TEC')
    especialidad = models.CharField(max_length=100)
    anos_experiencia = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_vinculacion = models.DateField()
    fecha_registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.especialidad}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    