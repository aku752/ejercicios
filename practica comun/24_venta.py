print("--------Fabrica el cometa--------")
materia_prima = int(input("Materia prima: "))
clave = int(input("Clave del producto: "))
if clave == 3 or clave == 4:
    mano_obra = materia_prima*0.75
else:
    if clave == 1 or clave == 5:
        mano_obra = materia_prima*0.85
    else:
        mano_obra = materia_prima*0.80

if clave == 2 or clave ==5:
    gasto_fabricacion = materia_prima*0.30
else:
    if clave == 3 or clave == 6:
        gasto_fabricacion = materia_prima*0.35
    else:
        gasto_fabricacion = materia_prima*0.28

costo_produccion = materia_prima + mano_obra + gasto_fabricacion
precio_venta = costo_produccion + costo_produccion * 0.45
print("-----------------------------------------")
print("Costo de produccion: ", round(costo_produccion,2))
print("Precio de venta: ", round(precio_venta,2))
