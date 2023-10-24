"""
Practica 1 - Sequential - Exercise 03
----------------------------------------------------------------------
English:
Given five numbers, 
calculate their average 
and report the result

Spanish: 
Dados como datos cinco números 
obtener el promedio de los mismos 
e informar el resultado.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
n1 = int(input("Ingresar el primer numero: "))
n2 = int(input("Ingresar el segundo numero: "))
n3 = int(input("Ingresar el tercer numero: "))
n4 = int(input("Ingresar el cuarto numero: "))
n5 = int(input("Ingresar el quinto numero: "))

average = (n1 + n2 + n3 + n4 + n5) / 5
print("El promedio es:",average)
