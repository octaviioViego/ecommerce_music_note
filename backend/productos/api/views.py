from rest_framework import generics
from productos.domain.models import Producto
from .serializers import ProductoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
class ProductoAPIView(APIView):
    def get(self, request):
        productos = Producto.objects.filter(activo=True)
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=ProductoSerializer 
    )
    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

