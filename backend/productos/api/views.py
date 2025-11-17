from rest_framework import generics
from productos.domain.models import Producto
from .serializers import ProductoSerializer

class ProductoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Producto.objects.filter(activo=True)
    serializer_class = ProductoSerializer
