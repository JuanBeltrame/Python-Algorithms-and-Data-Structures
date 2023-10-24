"""
Practica 1 - While Loops - Pre-Conditional - Exercise 01
----------------------------------------------------------------------
English: 
Given a set of integer numbers, 
determine how many of them are greater than or equal to 100. 
A number equal to zero indicates the end of data.

Spanish:
Dado un conjunto de números enteros, determinar cuántos de ellos son mayores o
iguales que 100. Un número igual a cero indica fin de datos.
"""
#----------------------------------------------------------------------
# Main Program

contador = 0
numero = int(input("Ingresar un numero: "))
while numero != 0:
    if numero >= 100:
        contador += 1
    else: 
        print()
    numero = int(input("Ingresar un numero: "))
print("La cantidad de numeros mayores o iguales a 100 son: ",contador)

