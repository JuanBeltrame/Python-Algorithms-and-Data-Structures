"""
Practica 1 - While Loops - Pre-Conditional - Exercise 02
----------------------------------------------------------------------
English: 
The following data is available:
The amounts of all the invoices for the just-ended month from a store (the number of invoices is unknown). The objective is to find out:

• How many sales were made.
• The average amount of the sales.
• How many of the amounts exceed 300 pesos.

Spanish: 
Se tienen como dato
los importes de todas las facturas correspondientes al mes que acaba de finalizar de un comercio (no se sabe cuántas son). 
Se desea conocer:

• Cuántas ventas se realizaron
• Importe promedio de las mismas
• Cuántos son los importes que superan los 300 pesos
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
contCantidadVentas = 0
contImportesCaros = 0
sumaDeImportes = 0
promedio = 0
importeFactura = float(input("Ingresar el valor de una factura: "))
while importeFactura != 0:
    contCantidadVentas = contCantidadVentas + 1
    sumaDeImportes = sumaDeImportes + importeFactura
    if importeFactura >= 300:
        contImportesCaros +=1
    else: 
        print()
    importeFactura = float(input("Ingrese nuevamente otro valor de factura (0 para salir): "))

if contCantidadVentas > 0:  # Verificar si hubo ventas
    promedio = sumaDeImportes / contCantidadVentas
print("Se realizaron la siguiente cantidad de ventas: ", contCantidadVentas)
print("La cantiadad de importes/ventas mayores a 300 pesos fueron:", contImportesCaros)
print("El importe promedio de las facturas es de: ", promedio)
