"""
Practica 1 - If Conditional - Exercise 01
----------------------------------------------------------------------
English:
Given two distinct numbers,
show them sorted in increasing order.

Spanish: 
Dados dos números distintos, 
mostrarlos ordenados en forma creciente.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
a = int(input())
b = int(input())
if a > b:
    print("Entro al if")
    print("En orden creciente: ", b, a)
elif b > a:
    print("Entro al elif")
    print("En orden creciente: ", a, b)
else: 
    print("Entro al else")
    print("Los numeros ingresados son iguales")
