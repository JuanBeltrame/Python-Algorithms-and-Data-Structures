"""
Practica 3 - One-Dimensional Array- Exercise 05
----------------------------------------------------------------------
English:
Enter integer numbers into an array A of 10 elements, 
and enter integer numbers into another array B of the same size (using the LOAD procedure with parameters). 
Obtain an array C, where C = A + B 
(each element of C is obtained as the sum of the corresponding elements of A and B).
a. Display A, B, and C one below the other.
b. Display A, B, and C side by side.

Spanish: 
Ingresar números enteros en un arreglo A de 10 elementos 
e ingresar números enteros en otro arreglo B de igual dimensión (utilizar procedure CARGA con parámetros).
Obtener, un arreglo C, siendo C = A + B. 
(cada elemento de C se obtiene como la suma de los elementos homólogos de A y B).
a. Mostrar A, B y C, uno debajo del otro.
b. Mostrar A, B y C, uno al lado del otro.
----------------------------------------------------------------------
"""
def inicializarArray(arr, size):
    begin = 0
    for i in range (begin, size):
        arr[i] = 0

def cargarArray(arr,size):
    begin = 0
    for i in range(begin,size):
        arr[i] = int(input("Ingresar valores al arreglo: "))

def obtener_c(arrayA, arrayB, arrayC, size):
    begin = 0
    for i in range(begin,size):
        arrayC[i] = arrayA[i] + arrayB[i]
    return arrayC

def mostrar(arrayA, arrayB, arrayC, size):
    for i in range(size):
        print(arrayA[i])
        print(arrayB[i])
        print(arrayC[i])
        print()
        print(arrayA[i],arrayB[i],arrayC[i])
#----------------------------------------------------------------------
# Main Program

TAM = 3
A = [0] * TAM
B = [0] * TAM
C = [0] * TAM

inicializarArray(A, TAM)
inicializarArray(B, TAM)
inicializarArray(C, TAM)
print("Ingresar valores en el Arreglo A:")
cargarArray(A,TAM)
print("Ingresar valores en el Arreglo B:")
cargarArray(B,TAM)
C = obtener_c(A[:],B[:],C[:],TAM)
print("Mostrando arreglo....")
mostrar(A[:],B[:],C[:],TAM)
