"""
----------------------------------------------------------------------
English: 
A taxi company has 30 cars, numbered from 1 to 30. 
For each trip made by the cars, the following data are available:
- Car number. (integer nr. between 1 and 30)
- Cost of the trip (real value.)

The number of journeys made is not known, 
Each car could have made one trip, more than one, or none at all. 
The data are not sorted. By entering a
car number equal to 0 indicates the end of the data.

You want to obtain a list showing for each car 
the total accumulated cost

Spanish: 
Una compañía de remises tiene 30 coches, numerados de 1 a 30. 
Por cada viaje realizado de los coches se tienen los siguientes datos:
• Nro. de coche (nro. entero entre 1 y 30)
• Costo del viaje (nro. real)

No se sabe la cantidad de viajes realizados, 
cada coche pudo haber realizado un viaje, más de uno, o ninguno. 
Los datos no están ordenados. Con el ingreso de un
número de coche igual a 0 se indica fin de datos

Se desea obtener un listado donde se muestre para cada coche 
el costo total acumulado
----------------------------------------------------------------------

Type: 
    a = array [1..30] of integer
Var:
    taxis: a
"""

# pylint: disable=missing-function-docstring
def init_array(taxi_number, tam):
    for i in range(0, tam):
        taxi_number[i] = 0


def no_name_yet(taxi_number):
    i = int(input("Ingrese numero de taxi: "))
    while i != 0:
        acum_costo_total = 0
        costo_del_viaje = int(input("Ingresar Costo del viaje: "))
        acum_costo_total += costo_del_viaje
        taxi_number[i] += acum_costo_total
        print("Costo total hasta el momento del taxi:", i, "es", taxi_number[i])
        message = str(input("Desea ingresar otro numero de taxi? (y/n): "))
        while message != "y" and message != "n":
            print("Solo se admiten y/n")
            message = str(input("Desea ingresar otro numero de taxi? (y/n): "))
        if message == "y":
            i = int(input("Ingrese numero de taxi: "))
        else:
            i = int(input("Ingrese 0 para salir: "))


def bubble_sort_by_ammount(taxi_number, tam):
    aux = 0
    for i in range(0, tam-1):
        for j in range(i+1, tam):
            if taxi_number[i] > taxi_number[j]:
                aux = taxi_number[i]
                taxi_number[i] = taxi_number[j]
                taxi_number[j] = aux


def display(taxi_number, tam):
    for i in range (0, tam):
        print("Nro de Coche: ", i, "Costo del Viaje: ", taxi_number[i])


#----------------------------------------------------------------------
# Main Program

T = 30
array = [0] * T
init_array(array, T)
no_name_yet(array)
#bubble_sort_by_ammount(array, T)
display(array, T)
