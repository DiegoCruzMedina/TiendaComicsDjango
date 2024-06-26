from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column="id_genero",primary_key=True)
    categoria = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return str(self.categoria)


class Comic(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, db_column="id_categoria")
    precio = models.IntegerField()
    comentario = models.CharField(max_length=500)
    editorial = models.CharField(max_length=15)
    imagen = models.CharField(max_length=150)
    autor = models.CharField(max_length=20)
    fecha = models.DateField(blank=False,null=False)
    paginas = models.IntegerField()
    tamaño = models.CharField(max_length=25)
    cantidad = models.IntegerField()

    def __str__(self):
        return str(self.nombre) + " " + str(self.id_categoria)

    class Meta:
        ordering=['id']


# Create your models here.
