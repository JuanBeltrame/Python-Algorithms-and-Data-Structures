"""
Practica 1 - While Loops - Pre-Conditional - Exercise 05
----------------------------------------------------------------------
English: 
A series of amounts is available,
and for each one, it is necessary to determine whether a discount is applied or not.
If the answer is yes, calculate the amount of the discount.

The criteria are as follows: 
for amounts less than or equal to 85, no discount is applied, 
and for larger amounts, a 5% discount is applied.

Report each amount (never zero) with its corresponding discount,
and, in the end, the percentage representing the number of
amounts that received a discount, relative to the total number of amounts

Spanish: 
Se dispone de una serie de importes
y para cada uno es necesario saber si se aplica o no un descuento. 
En caso afirmativo, calcular el importe del mismo. 

El criterio es el siguiente: 
para importes menores o iguales que 85, no se hace descuento 
y para importes mayores, se hace el 5 % de descuento. 

Informar cada importe (nunca cero) con su correspondiente descuento 
y, al final, el porcentaje que representa la cantidad de
importes que tuvieron descuento, con respecto a la cantidad total de importes.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
continuar = True
contadorImp = 0
contadorImpD = 0
while continuar:
    importe = int(input("Ingresar importe de venta:"))
    contadorImp = contadorImp + 1
    if importe > 85:
        contadorImpD +=1 
        descuento = importe * 0.95
        porcentaje = (100 * contadorImpD) / contadorImp
        print("El importe final con descuento es:", descuento)
        print("El porcentaje que representa la cantidad de importes que tuvieron descuento es:", porcentaje, "%")
    elif importe != 0:
        print("Por este importe de:", importe,"No se realiza descuento")
        print("El importe final con descuento es:", importe)
    else:
        print("Saliendo del programa...")
        continuar = False
