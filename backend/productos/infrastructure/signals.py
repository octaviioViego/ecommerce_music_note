"""
    Señales para generar slug
"""
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from productos.domain.models import Producto
from django.db.models import Q

@receiver(pre_save, sender=Producto)
def generar_slug(sender, instance, **kwargs):
    if not instance.slug and instance.nombre:
        base = slugify(instance.nombre)[:200]
        slug = base
        n = 1

        while Producto.objects.filter(Q(slug=slug)).exclude(pk=instance.pk).exists():
            slug = f"{base}-{n}"
            n += 1

        instance.slug = slug
