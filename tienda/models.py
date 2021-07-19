from django.db import models

class Producto(models.Model):
    sku = models.CharField(max_length=7, null=False, unique=True, verbose_name='Sku')
    nombre = models.CharField(max_length=255, null=False, unique=True, verbose_name='nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']