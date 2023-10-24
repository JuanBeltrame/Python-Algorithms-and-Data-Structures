"""
Practica 1 - If Conditional - Exercise 05
----------------------------------------------------------------------
English:
Determine if the first of a set of three given numbers 
is smaller than the other two.

Spanish: 
Determinar si el primero de un conjunto de tres números dados, 
es menor que los otros dos.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
n1 = int(input("Ingresar el primer numero: "))
n2 = int(input("Ingresar el segundo numero: "))
n3 = int(input("Ingresar el tercer numero: "))
menor = n1

if n2 < menor:
    menor = n2
    print("El primero de los tres numeros ingresados NO fue el menor")
elif n3 < menor:
    menor = n3
    print("El primero de los tres numeros ingresados NO fue el menor")
else:
    print("El primero de los tres numeros ingresados fue el menor de los tres")

 