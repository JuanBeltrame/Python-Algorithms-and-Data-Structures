"""
Practica 3 - One-Dimensional Array- Exercise 08
----------------------------------------------------------------------
English: 
From an array called X of 50 integer elements, create and display:
a. Another array DX such that the first element is the difference between the second and
the first element of X, the second element of DX is the difference between
the third and the second of X and so on.

b. idem section (a) but on itself, that is, without generating an array DX.

Spanish: 
A partir de un arreglo llamado X de 50 elementos enteros, crear y exhibir:
a. Otro arreglo DX tal que el primer elemento sea la diferencia entre el segundo y
el primer elemento de X, el segundo elemento de DX sea la diferencia entre
el tercero y el segundo de X y así sucesivamente.

b. ídem apartado (a) pero sobre sí mismo, o sea sin generar un arreglo DX.
----------------------------------------------------------------------
"""

def load_array(arr_a, size): 
    begin = 0
    for i in range(begin, size):
        arr_a[i] = input("Enter values in array")

def get_second_array(arr_b, arr_a, size): 
    begin = 0
    for i in range(begin, size):
        arr_b[i] = arr_a[i+1] - arr_a[i]

def sobre_si_mismo(array_a,size):
    begin = 0 
    for i in range(begin,size):
        array_a[i] = array_a[i+1] - array_a[i]

#----------------------------------------------------------------------
# Main Program

T = 5
x = [0] * T
dx = [0] * T
load_array(x, T)
get_second_array(dx, x[:], T)
sobre_si_mismo(x,T)
