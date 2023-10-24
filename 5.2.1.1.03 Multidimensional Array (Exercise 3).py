"""
Practica 3 - Multidimensional Array- Ejercicio 03
----------------------------------------------------------------------
English:
Enter integers into a two-dimensional array A of 10 rows by 5 columns; 
then enter integers into another array B of equal dimension. 
Obtain an array C, where C = A + B. 
(each element of C is obtained as the sum of the counterpart elements of A and B).

- Show A, B and C, one array below the other.
- Show A, B and C, one array next to the other.

Spanish:
Ingresar números enteros en un arreglo bidimensional A de 10 filas por 5 columnas; 
luego ingresar números enteros en otro arreglo B de igual dimensión. 
Obtener un arreglo C, siendo C = A + B. 
(cada elemento de C se obtiene como la suma de los elementos homólogos de A y B).

• Mostrar A, B y C, un arreglo debajo del otro
• Mostrar A, B y C, un arreglo al lado del otro
----------------------------------------------------------------------

Type 
Values= array[1..ROW,1..COL]
Variables
array_A,array_B,array_C: values
ROW, COL
"""
def carga(name, array):
    print()
    print("Ingrese datos del arreglo: ", name)
    for r in range(ROW):
        for c in range(COL):
            print ("Ingrese Valor de fila", r, "Columna ", c)
            array[r][c] = int(input(array[r][c]))

def crear_C(array1, array2, array3):
    for r in range(ROW):
        for c in range(COL):
            array3[r][c] = array1[r][c] + array2[r][c]

def muestro(array_name, r):
    for c in range(COL):
        print(array_name[r][c], end= "")

def muestro1():
    print()
    print(" Los arreglos A, B, C uno debajo del otro")
    print()
    for r in range(ROW):
        muestro(array_A, r)
        print()
    print()

    for r in range(ROW):
        muestro(array_B, r)
        print()
    print()

    for r in range(ROW):
        muestro(array_C, r)
        print()
    print()

def muestro2():
    print()
    print(" Los arreglos A, B, C uno al lado del otro")
    print()
    for r in range(ROW):
        muestro(array_A, r)
        print(end = "")
        muestro(array_B, r)
        print(end = "")
        muestro(array_C, r)
        print()
    print()
#----------------------------------------------------------------------
# Main Program
ROW = 3 # Constants
COL = 2 # Constants
# Definir las listas en Python a trabajarlas como arreglos
# crea las columnas para cada fila
array_A  = [0] * ROW # Pueden ser cero o "none", que vendria ser cargalos con cero o bien con vacio
for r in range(ROW): # El extremo superior no lo toma python por lo tanto es COL-1
    # crea la columnas para cada fila
    array_A[r] = [0] * COL

array_B  = [0] * ROW
for r in range(ROW): # Sino no pongo nada, por defecto el inicio del arreglo es 0
    # crea la columnas para cada fila
    array_B[r] = [0] * COL

array_C  = [0] * ROW
for r in range(ROW):
    # crea la columnas para cada fila
    array_C[r] = [0] * COL    

carga("Arreglo A", array_A)
carga("Arreglo B", array_B)
crear_C(array_A, array_B, array_C)
muestro1()
muestro2()
