"""
Sistema de Control de Ventas Diarias para una MYPE en Perú
"""
total_dia=0
mayor_cantidad=0
producto_mas_vendido=""
meta_soles=int(input("Ingrese la meta diaria en soles por favor: "))

while True:
    continuar=input("¿Desea registrar una venta?(si/no): ")
    if continuar.lower() == "no":
        break
    nombre_producto=input("Escriba el nombre del producto: ")
    precio_unitario=float(input("Ingrese su precio unitario: "))
    cantidad=int(input("Ingrese la cantidad de productos vendidos por favor: "))

    ingreso=precio_unitario*cantidad
    total_dia+=ingreso

    if cantidad>mayor_cantidad:
        mayor_cantidad=cantidad
        producto_mas_vendido=nombre_producto
    
print("Total vendido en el día: ",total_dia)
print("Producto más vendido: ", producto_mas_vendido)

if total_dia>=meta_soles:
    print("Meta alcanzada")
else:
    print("Meta no alcanzada")




