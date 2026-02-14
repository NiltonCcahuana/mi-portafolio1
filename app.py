"""
Sistema de Control de Ventas Diarias para una MYPE en Perú
"""
total_dia=0
mayor_cantidad=0
producto_mas_vendido=""
meta_diaria=int(input("Ingrese la meta diaria por favor: "))

while True:
    continuar=input("¿Desea registrar una venta?(si/no): ")
    if continuar.lower() == "no":
        break
    nombre_producto=input("Escriba el nombre del producto: ")
    precio_unitario=float(input("Ingrese su precio unitario: "))
    cantidad=int(input("Ingrese la cantidad por favor: "))

    ingreso=precio_unitario*cantidad
    total_dia+=ingreso
    
    if cantidad>mayor_cantidad:
        mayor_cantidad=cantidad
        producto_mas_vendido=nombre_producto
    
print(total_dia)
print(producto_mas_vendido)

if total_dia>=meta_diaria:
    print("Meta alcanzada")
else:
    print("Meta no alcanzada")




