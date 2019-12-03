# Este programa convierte el valor de un monto en dolares USD a guaranies PYG

# ingreso por el usuario del monto que quiere cambiar y lo convertimos a int
monto_usd = float(input("Ingrese el monto en USD que quiere convertir a PYG: "))

# cotizacion actual de 1USD
cotizacion_compra = 6200
cotizacion_venta = 6300

# calculo de conversion
pyg_compra = monto_usd * cotizacion_compra
pyg_venta = monto_usd * cotizacion_venta

# imprimimos el monto calculado
print(f"A la compra equivale a PYG {pyg_compra}")
print(f"A la venta equivale a PYG {pyg_venta}")

