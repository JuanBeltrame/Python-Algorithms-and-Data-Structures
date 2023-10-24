"""
Practica 1 - If Conditional - Exercise 04
----------------------------------------------------------------------
English:
Enter three distinct integer numbers. 
Determine and display if they were entered in ascending order.

Spanish: 
Ingresar tres números enteros distintos. 
Determinar y mostrar si ingresaron en orden creciente.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
n1 = int(input("Ingresar el primer numero: "))
n2 = int(input("Ingresar el segundo numero: "))
n3 = int(input("Ingresar el tercer numero: "))

if n1>n2 and n2<n3:
    print("Se ingresaron en orden creciente:")
else:
    print("Los numeros ingresados no estan en orden")
