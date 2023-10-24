"""
Practica 1 - While Loops - Pre-Conditional - Exercise 07
----------------------------------------------------------------------
English: 
"At the end of each day, the sellers of a store 
submit their sales to the owner to calculate the commission they will receive. 
There are 8 sellers, coded from A to H, 
and it is not known how many sales each one made.

The data is ordered and grouped by seller. 
For each seller, the amounts of their sales are entered. 
To indicate the end of each sale, a sale value of 0 is entered. 
It is requested to display for each of the sellers: 
their code and the commission they will receive, which is 2.5% of the sum of their sales.

Spanish: 
Al finalizar cada día, los vendedores de un comercio 
rinden al dueño sus ventas para calcular la comisión que cobrarán. 
Los vendedores son 8, codificados de la A a la H, 
y no se sabe cuántas ventas realizó cada uno.

Los datos vienen ordenados y agrupados por vendedor. 
Por cada vendedor se ingresan cada uno de los importes de sus ventas. 
Para indicar el fin de cada uno de ellos se ingresa un valor de venta igual a 0. 
Se solicita mostrar para cada uno de los vendedores:
su código y la comisión que cobrará, que es el 2,5 % de la suma de sus ventas.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
for codVendedor in ('A','B','C','D','E','F','G','H'):
    print("Codigo de Venderdor:", codVendedor)
    montoTotalenVentas = 0
    importe_venta = float(input("Ingresar importe de venta: "))
    while importe_venta != 0:
        montoTotalenVentas = montoTotalenVentas + importe_venta
        comision = montoTotalenVentas * 0.025
        importe_venta = float(input("Ingresar importe de venta: "))
    print("La comision del vendedor",codVendedor,"es de:",comision)

