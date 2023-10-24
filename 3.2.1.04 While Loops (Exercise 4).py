"""
Practica 1 - While Loops - Pre-Conditional - Exercise 04
----------------------------------------------------------------------
English: 
We have information provided by a group of salespeople.
For each of them, we enter their code (a character different from *) and the total amount of their sales.
Determine the code of the salesperson with the highest sales amount and that amount.

Spanish: 
Se cuenta con la información brindada por un conjunto de vendedores. 
Por cada uno de ellos se ingresa su código (un carácter distinto de *) y el importe total de sus ventas.
Determinar el código del vendedor con mayor importe vendido y dicho importe.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
maximoImporteEnVentasGlobal = 0
codVendedor = input("Ingrese el codigo de vendedor: , (*), para salir: ")
while codVendedor != "*":
    print("Ingresar el importe total en ventas realizadas por el vendedor: ",codVendedor)
    totalVentas = float(input("Importe total en ventas realizadas: ")) 
    if totalVentas > maximoImporteEnVentasGlobal:
        bestSellerGlobal = codVendedor
        maximoImporteEnVentasGlobal = totalVentas
    else: 
        print()
    codVendedor = input("Ingrese el codigo de vendedor: , (*), para salir: ")
print("El codigo de vendedor con mayor importe vendido es el vendedor: ", bestSellerGlobal)
print("El importe de dicho vendedor es: ",maximoImporteEnVentasGlobal)
