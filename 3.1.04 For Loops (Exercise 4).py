"""
Practica 1 - For Loops - Inconditional - Exercise 04
----------------------------------------------------------------------
English:
Given 200 integer numbers as data, obtain and display their sum.

Spanish: 
Dados como datos 200 números enteros, obtener y mostrar su suma.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
begin = 0 
end = 5
sumaTotal = 0
for i in range(begin,end):
    number = int(input("Ingresar numero:"))
    sumaTotal = sumaTotal + number
print("La suma todas de todos los numeros es:",sumaTotal)
