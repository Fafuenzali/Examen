from django.db import models
import datetime

class Producto(models.Model):
    sku = models.CharField(max_length=7, null=False, unique=True, verbose_name='Sku')
    nombre = models.CharField(max_length=255, null=False, unique=True, verbose_name='nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class contacto(models.Model):
    run = models.CharField(max_length=10, null=False, verbose_name='Run')
    nombre = models.CharField(max_length=100, null=False, verbose_name='Nombre completo')
    correoe = models.CharField(max_length=50, null=False, verbose_name='Correo Electronico')
    telefono = models.CharField(max_length=15, null=False, verbose_name='Numero de telefono')
    mensaje = models.CharField(max_length=200, null=False, verbose_name='Mensaje')
    fecha =models.DateField(("Fecha"), default=datetime.date.today) 

    def __date__(self):
        return self.fecha

        
