"""
Practica 1 - While Loops - Pre-Conditional - Exercise 06
----------------------------------------------------------------------
English: 
A company has 50 traveling salesmen working for it. 
At the end of the month, each of the salesmen reports their number and the amounts of each of the sales made. 
The number of sales made by each of them is not known, 
so a sales value equal to zero indicates that there are no more sales by that salesman.
It is requested to display, for each of the salesmen, 
the salesman's number and the amount of the largest sale made by them

Spanish: 
Una empresa tiene 50 viajantes que trabajan en ella. 
A fin de mes cada uno de los viajantes informa su número y los importes de cada una de las ventas realizadas. 
No se sabe la cantidad de ventas que realizó cada uno de ellos 
por lo que un valor de venta igual a cero indica que no hay más ventas de ese vendedor.
Se pide exhibir, para cada uno de los viajantes, 
el Nro. del viajante y el importe de la mayor venta realizada por el mismo.
"""
#----------------------------------------------------------------------
# Main Program
begin = 0
end = 2
for i in range(begin,end):
    codV = int(input("Ingresar el codigo del viajante: "))
    importe = int(input("Ingresar importe de la ventas realizada: "))
    maximoImporte = 0
    while importe != 0:     
        if importe > maximoImporte:
            maximoImporte = importe
        else:
            print()
        importe = int(input("Ingresar un nuevo importe de la venta realizada: "))
    print("El numero de viajante es:",i+1, "y su mayor venta fue:",maximoImporte)
