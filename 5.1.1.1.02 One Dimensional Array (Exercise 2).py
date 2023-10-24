"""
Practica 3 - One-Dimensional Array- Exercise 02
----------------------------------------------------------------------
English:
Enter 20 real type elements in an array
and perform the sum of them.
Use the LOAD and SUM procedures.


Spanish:
Ingresar 20 elementos de tipo real en un arreglo
y realizar la suma de los mismos. 
Utilizar los procedimientos Carga y Suma.
----------------------------------------------------------------------

Declarativa
Type:
    vec: array [0..19] of real
Var:
    a: vec
"""

def initialize_array(array, size):
    begin = 0
    for i in range(begin, size):
        array[i] = 0
    
def load_array(array, size):
    begin = 0
    for i in range(begin,size):
        array[i] = float(input())

def sum(array, ac, size):
    begin = 0
    for i in range(begin,size):
        ac += array[i]

    return ac

def show_results(ac):
    print(ac)

#----------------------------------------------------------------------
# Main Program
T = 5
arreglo = [0] * T
acum = 0
initialize_array(arreglo, T)
print ("Enter ", T , "array values")
load_array(arreglo, T)
sum_result = sum(arreglo[:], acum, T)
print("The sum is being made") 
print("The sum of the array values is: ")
show_results(sum_result)
