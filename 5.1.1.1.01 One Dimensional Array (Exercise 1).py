"""
Practica 3 - One-Dimensional Array- Exercise 01
----------------------------------------------------------------------
English:
Given the following example
Enter 30 integer elements into an array and then display them.

Spanish: 
Dado el siguiente ejemplo:
Ingresar 30 elementos enteros en un arreglo y luego mostrarlos.
----------------------------------------------------------------------
"""
def inicializar_array(array, size):
    begin = 0
    for i in range(begin,size):
        array[i] = 0

def cargar_array(array, size):
    begin = 0
    for i in range(begin,size):
        array[i] = int(input("Ingresar elemento: "))

def mostrar_array(array,size):
    begin = 0
    for i in range(begin,size):
        print("Los elementos del arreglo son: ",array[i])

#----------------------------------------------------------------------
# Main Program
TAM = 5
a = [0]*TAM

inicializar_array(a,TAM)
cargar_array(a,TAM)
mostrar_array(a[:],TAM)
