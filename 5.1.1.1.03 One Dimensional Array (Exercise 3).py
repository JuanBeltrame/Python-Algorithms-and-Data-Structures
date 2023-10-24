"""
Practica 3 - One-Dimensional Array- Exercise 03
----------------------------------------------------------------------
English:
Enter 25 integer type elements in an array and then obtain the sum of the values
positive within the set. Use the same LOAD procedure as the previous exercise
(include parameters).

Spanish: 
Ingresar 25 elementos de tipo entero en un arreglo y luego obtener la suma de los valores
positivos dentro del conjunto. Utilizar el mismo procedimiento CARGA del ejercicio
anterior (incluir parámetros).
----------------------------------------------------------------------
Declarativa
TYPE
    arreglo = array [0..24] of integer
VAR
    suma: integer
    lista: arreglo
    T: int
"""
def cargar(l, TAM):
    global T
    for i in range(0, TAM):
        l[i] = int(input(str(i + 1) + ". Ingreso: "))

def sumar_positivos(x, TAM):
    global T
    acum = 0
    for i in range(0, TAM):
        if x[i] > 0:
            acum = acum + x[i]
    return acum

#----------------------------------------------------------------------
# Main Program

T = 3  # Constante para el tamano del arreglo, aunque pyton no maneja el concepto de constante # Las constantes se declaran en Mayusculas
lista = [0] * T  # La lista se representa por medio de corchetes, A una lista que va a tener de valor 0, la voy a reproducir 25 veces  Esto significa que adentro de lista habra 3 casilleros empezando en el indice 0 y adentro tendra todos valores 0
cargar(lista, T)
suma = sumar_positivos(lista[:], T)
print("La suma de los numeros positivos ingresados es: ", suma)
