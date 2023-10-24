"""
Practica 3 - One-Dimensional Array- Exercise 07
----------------------------------------------------------------------
English:
You have a set of 10 integers. The task is to modify this set in the following way: 
If the last number read is even, change to zero the numbers in the even positions of the set; 
if the last number read is odd, change to zero the numbers in the odd positions of the set.

Spanish: 
Se dispone de un conjunto de 10 numeros enteros. Se pide modificar ese conjunto de la siguiente forma: 
Si el ultimo numero leido es par, cambiar por cero los numeros contenidos en las posiciones par del conjutno; 
si el ultimo numero leido es impar, cambiar por cero los numeros contenidos en las posiciones impar del conjunto. 
----------------------------------------------------------------------
"""

def load_array(array, size):
    begin = 0
    for i in range(begin, size):
        array[i] = int(input("Enter Number: "))

def modify_array_0(array, num):
    begin = 0
    for i in range(begin, 5):
        array[(i*2) - num] = 0

def modify_array_1(array, num):
    begin = 0
    for i in range(begin, 5):
        array[(i*2) + num] = 1

#----------------------------------------------------------------------
# Main Program

T = 10
v = [0] * T
load_array(v, 10)
if (v[9] % 2) == 0:
    modify_array_0(v, 0)
else:
    modify_array_1(v, 1)

print("El arreglo queda modificado de la siguiente manera:", v)
