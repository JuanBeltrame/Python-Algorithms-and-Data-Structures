"""
Practica 3 - Multidimensional Array- Ejercicio 02
----------------------------------------------------------------------
English:
Enter 20 sets of 20 integer elements each into a two-dimensional array. 
Calculate and display the sum of their main diagonal and the sum of their secondary diagonal.

Spanish:
Ingresar 20 conjuntos de 20 elementos enteros cada uno en un arreglo bidimensional.
Calcular y exhibir la suma de su diagonal principal y la de su diagonal secundaria.
----------------------------------------------------------------------
"""
def inicializar(Matrix,row,colum):
    for fil in range(row):
        for col in range(colum):
            Matrix[fil][col] = 0

def carga(Matrix,row,colum):
    for fil in range(row):
        for col in range(colum):
            Matrix[fil][col] = int(input("Ingresar valores a la matriz: "))

def diagonales(Matrix,row):
    sp = 0
    ss = 0
    j = row - 1
    for fil in range(row):
        sp += Matrix[fil][fil]
        ss += Matrix[j][fil]
        j -= 1
    print("Suma Principal: ", sp)
    print("Suma secundaria: ", ss)


#----------------------------------------------------------------------
# Main Program
FILA = 3
COL = 3

M = [None] * FILA
for f in range(FILA):
    M[f] = [None] * COL

inicializar(M,FILA,COL)
carga(M,FILA,COL)
diagonales(M,FILA)
