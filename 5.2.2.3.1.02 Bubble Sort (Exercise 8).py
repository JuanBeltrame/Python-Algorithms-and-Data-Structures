"""
Practica 3 - Bubble Sort - Multidimensional Array- Exercise 08 
----------------------------------------------------------------------
English: 
The information from the latest tennis tournament of a club is available, in which 40 players participated.
For each of them, the following set of integer numerical data is available:

- Player number
- Number of matches won
- Number of matches lost

As this data is entered, the total score for each player must be calculated,
knowing that, for each match won, 3 points are assigned, and for each lost match, zero points are assigned.

A list is desired, sorted in decreasing order according to the total score,
in the following format:
Player Number   Matches Won   Matches Lost    Total Score
....            .....         .....           ......


Spanish: 
Se cuenta con la información del último torneo de tenis de un club, en el que participaron 40 jugadores. 
Por cada uno de ellos se tiene el siguiente juego de datos numéricos enteros:

- Nro de jugador
- Cantidad de partidos ganados
- Cantidad de partidos perdidos

A medida que se ingresan dichos datos, se debe ir calculando el puntaje total de cada jugador
sabiendo que, por cada partido ganado, se le asigna 3 puntos y por cada partido perdido cero puntos.

Se desea obtener un listado, ordenado en forma decreciente según puntaje total, 
de la siguiente forma:
Nro. de Jugador       Partidos Ganados   Partidos Perdidos   Puntaje Total
....                  .....              .....               ......
----------------------------------------------------------------------
"""

def inicializar(Matrix,filas,columnas):
    for f in range(filas):
        for c in range(columnas):
            Matrix[f][c] = 0

def cargar(Matrix):
    print("Ingrese datos de los jugadores: ")
    print("--------Carga Matriz------------")
    for f in range(FIL):
        Matrix[f][0] = int(input("Ingrese Numero de Jugador: "))
        Matrix[f][1] = int(input("Ingrese Cantidad de Partidos Ganados: "))
        Matrix[f][2] = int(input("Ingrese Cantidad de Partidos Perdidos: "))  
        Matrix[f][3] = Matrix[f][1] * 3 # Calcula y guarda el puntaje
        print()
        
def ordenar(Matrix,Columa):
    for i in range(FIL-1):
        for j in range(i+1,FIL):
            if Matrix[i][Columa] > Matrix[i][Columa]: 
                for k in range(COL):
                    aux = Matrix[i][k]
                    Matrix[i][k] = Matrix[j][k]
                    Matrix[j][k] = aux

def mostrar(Matrix):
    print("Nro  PG   PP  PJe")
    print("-----------------")
    for f in range(FIL):
        for c in range(COL):
            print(Matrix[f][c], end="     ")
        print() # baja de renglón cuando termina de mostrar la fila

#----------------------------------------------------------------------
# Main Program

FIL = 3 # Constantes // # Probamos con 3 Jugadores en vez de 40 para acelerar la prueba! 
COL = 4  

M = [None] * FIL # Definir las listas en Python a trabajarlas como arreglos
for f in range(FIL):
    M[f] = [None] * COL # Crear columnas para cada fila


inicializar(M,FIL,COL)
cargar(M)
Colum = int(input("Ingresar nro de Columna por el cual desea ordenar la matriz - Enunciado pedia x Puntaje Col 4: "))
Colum = Colum - 1
ordenar(M,Colum)
mostrar(M[:]) # Paso la Matriz por parametro por Valor
