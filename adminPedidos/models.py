from django.db import models

class Cliente(models.Model):
    nombre= models.CharField(max_length=100)
    direccion= models.CharField(max_length=200)
    email= models.EmailField()
    telefono = models.CharField(max_length=12)


class TipoArticulo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    tipo = models.ForeignKey(TipoArticulo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    numero_pedido = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    articulos_pedidos = models.ManyToManyField(Articulo)

class Devoluciones(models.Model):
    numero_pedido = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    articulos_pedidos = models.ManyToManyField(Articulo)

class DatosAdmin(models.Model):
    nombre= models.CharField(max_length=120)
    email= models.EmailField()
    telefono = models.CharField(max_length=12)

