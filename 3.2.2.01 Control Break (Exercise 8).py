"""
Practica 1 - While Loops - Pre-Conditional - Exercise 01/08
----------------------------------------------------------------------
English: 
We want to know the total sales for each of the sellers in a company. 
To this end, we have the following data: the seller's code and the amount of each sale.

A seller may have made more than one sale. 
We don't know the number of sellers the company has or the number of sales made by each seller 
(a seller code equal to zero marks the end of data). 
THIS DATA IS SORTED BY SELLER CODE. 
Display each seller's code and their corresponding total, 
and finally, the seller code with the highest total sales and that total amount."

Spanish: 
Se desea saber el total de ventas de cada uno de los vendedores de una empresa. 
A tal fin se tienen como datos: el código de vendedor y el importe de cada una de las ventas;

Un vendedor puede haber realizado más de una venta. 
No se sabe la cantidad de vendedores que tiene la empresa ni la cantidad de ventas hechas por cada vendedor 
(un código de vendedor igual a cero es fin de datos). 
ESTOS DATOS ESTAN ORDENADOS POR CODIGO DE VENDEDOR. 
Exhibir cada código de vendedor y su total correspondiente 
y al final, el código de vendedor con mayor importe vendido y dicho importe.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
mayorImporteGlobal = 0
codigoVendedor = int(input("Ingrese codigo de vendedor (0 para finalizar): "))
while codigoVendedor != 0:
    importe_total_vendedor = 0 # Variable que acumula el total de ventas por cada vendedor
    vendedorAnterior = codigoVendedor # Variable para tener guardado el ultimo vendedor
    while codigoVendedor == vendedorAnterior: # Mientras el nuevo vendedor sea el mismo al vendedor anterior 
        importe_venta = float(input("Ingrese el importe de la venta realizada: "))
        importe_total_vendedor = importe_total_vendedor + importe_venta
        codigoVendedor = int(input("Ingrese codigo de vendedor (0 para finalizar): "))
        if importe_total_vendedor > mayorImporteGlobal: 
            mayorImporteGlobal = importe_total_vendedor
            mejor_vendedor = vendedorAnterior
    print("El importe total del vendedor:",vendedorAnterior,"es de:",importe_total_vendedor)

print("El vendedor con la mayor venta fue el vendedor:",mejor_vendedor,"con importe de:",mayorImporteGlobal)
        
