from django.db import models

# Create your models here.

class Categoria (models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria

#Modelo para cliente 
class Colaborador(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='Rut')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.rut

#Modelo inventario
class Inventario(models.Model):
    codigo = models.CharField(primary_key=True,max_length=6)
    nombreIn = models.CharField(max_length=50, verbose_name='Nombre')
    Cantidad = models.PositiveSmallIntegerField()
    imagen = models.ImageField(upload_to="inventario",null=True, blank=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombreIn, self.Cantidad)