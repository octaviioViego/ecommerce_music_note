"""
  En esta clase vas los servicios (Lógica de dominio) como: 
    - Aplicar descuentos.
    - Actualizar inventario.
    - Reglas del negocio.
    - Validaciones.
"""
def calcular_precio_con_descuento(producto, porcentaje):
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("Descuento inválido")

    descuento = producto.precio * (porcentaje / 100)
    return producto.precio - descuento
