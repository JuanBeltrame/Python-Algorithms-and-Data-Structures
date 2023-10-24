"""
Practica 3 - Multidimensional Array- Exercise 01
----------------------------------------------------------------------
English:
Enter real elements into a two-dimensional array of 30 rows by 12 columns. 
Then enter an integer data corresponding to a row number (validate its consistency). 
The objective is to calculate and display the sum of all elements in that row.

Spanish:
Ingresar elementos reales en un arreglo bidimensional de 30 filas por 12 columnas. 
Luego ingresar un dato entero que corresponde al número de una fila (validar que sea consistente).
Se desea obtener y exhibir la suma de todos los elementos de dicha fila.
----------------------------------------------------------------------
"""
def initialize_matrix(matrix, filas, columnas): # matrix is a reference value. r and c are value types
    for fila in range(filas):
        for columna in range(columnas):
            matrix[fila][columna] = 0

def load_matrix(matrix, filas, columnas): #matrix is a reference value, r and c are value types
    for fila in range(filas):
        print("Fila: ",fila)
        for columna in range(columnas):
            matrix[fila][columna] = int(input("Enter values: "))

def sum_row(matrix, nro_fila, columnas):
    suma = 0
    for columna in range(columnas):
        suma = suma + matrix[nro_fila][columna]
    return suma

#----------------------------------------------------------------------
# Main Program
ROWS = 2
COLUMNS = 3

M = [0] * ROWS
for f in range(ROWS):
    M[f] = [0] * COLUMNS

initialize_matrix(M, ROWS, COLUMNS)
load_matrix(M, ROWS, COLUMNS) 

row_number = int(input("Enter a row number: "))
while row_number < 0 and row_number > ROWS:
    print("The row number must be between 0 and ", ROWS)
    row = int(input("Enter a row number: "))

sum_result = sum_row(M, row_number, COLUMNS)
print("the sum of the row", row_number, "is: ", sum_result) 
