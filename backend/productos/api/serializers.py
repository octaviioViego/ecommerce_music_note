"""
    Convertimos del modelo a json.
"""

from rest_framework import serializers
from productos.domain.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        read_only_fields = ['id', 'creado_en', 'actualizado_en', 'slug']
