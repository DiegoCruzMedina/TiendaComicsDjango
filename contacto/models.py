from django.db import models

# Create your models here.

opciones_consultas= [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"],
    {4, "Problemas Iniciar sesion"}
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje= models.TextField()
    avisos= models.BooleanField()

    def __str__(self):
        return self.nombre
