"""
  Esta clase podemos crear los casos de uso:
    - Crear productos
    - Actualizar
    - Etc
"""

from productos.domain.models import Producto

def crear_producto(data):
    producto = Producto(
        nombre=data["nombre"],
        descripcion=data.get("descripcion", ""),
        precio=data["precio"],
        stock=data.get("stock", 0),
        sku=data.get("sku", None)
    )
    producto.save()
    return producto