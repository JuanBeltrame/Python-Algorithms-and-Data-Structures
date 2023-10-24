"""
Practica 1 - For Loops - Inconditional - Exercise 03
----------------------------------------------------------------------
English:
Entering a sequence of 300 whole numbers, 
determine the quantity of positive numbers within it.

Spanish: 
Ingresando una sucesión de 300 números enteros, 
determinar la cantidad de números.
positivos que hay en ella.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
begin = 0
end = 5
contador = 0
for i in range(begin,end):
    number = int(input("Ingresar un numero: "))
    if number > 0:
        contador +=1
    else: 
        None
print("Se encontraron:",contador,"numeros positivos")
