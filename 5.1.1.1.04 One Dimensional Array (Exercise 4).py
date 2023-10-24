"""
Practica 3 - One-Dimensional Array- Exercise 04
----------------------------------------------------------------------
English:
Enter 30 elements of type char into an array, 
and then display only the elements that are not equal to '*', 
indicating the position that each of these elements occupies in the array

Spanish: 
Ingresar 30 elementos de tipo char en un arreglo 
y luego mostrar sólo los elementos que sean distintos de *, 
indicando la posición que dicho elemento ocupa en el arreglo.
----------------------------------------------------------------------
"""
def incializar_arreglo(arreglo, tam):
    for i in range(0, tam):
        arreglo[i] = 0

def cargar_arreglo(arreglo, tam):
    for i in range(0, tam):
        arreglo[i] = str((input("Ingrese un caracter:")))

def mostrar_arreglo(arreglo, tam):
    for i in range (0, tam):
        if arreglo[i] != '*':
            print(arreglo[i])
            print("Se ingreso en la posicion: ", i)
        else:
            print("El simbolo * se ingreso en la posicion :", i)


#----------------------------------------------------------------------
# Main Program
T = 3
A = [0] * T

incializar_arreglo(A, T)
cargar_arreglo(A, T)
mostrar_arreglo(A, T)
