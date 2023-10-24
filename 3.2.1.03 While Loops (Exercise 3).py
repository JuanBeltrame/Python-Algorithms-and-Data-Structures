"""
Practica 1 - While Loops - Pre-Conditional - Exercise 03
----------------------------------------------------------------------
English: 
Distinct numbers, except for the last value, are being entered. 
Calculate their sum.

Spanish: 
Se van ingresando números distintos de cero, 
salvo el último valor. 
Determinar su suma.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
acumNumeros = 0
numero = int(input("Ingrese un numero: "))
while numero != 0:
    acumNumeros = acumNumeros + numero
    numero = int(input("Ingrese otro numero: "))
print("La suma de todos los numeros ingresados es: ",acumNumeros)
