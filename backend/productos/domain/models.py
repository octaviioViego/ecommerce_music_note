"""
    Modelo de un producto con sus respectivos campos.
"""

from django.db import models

class Producto(models.Model):
    nombre = models.CharField('nombre', max_length=200)
    descripcion = models.TextField('descripción', blank=True)
    precio = models.DecimalField('precio', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('stock', default=0)

    slug = models.SlugField('slug', max_length=220, unique=True, blank=True)
    sku = models.CharField('SKU', max_length=50, unique=True, null=True, blank=True)

    destacado = models.BooleanField('destacado', default=False)
    activo = models.BooleanField('activo', default=True)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-creado_en']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['sku']),
        ]

    def __str__(self):
        return f"{self.nombre} — {self.sku or self.id}"
