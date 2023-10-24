"""
Exercise - Arreglo de Registros - Juegos Sudamericanos
----------------------------------------------------------------------
English: 
For the South American Youth Games an iterative menu with the following options is requested:
1- Data upload
2- Medal list of a country
3- List of athletes
4- Exit

Notes:
Item 1-Load each one of the athletes, entering their name, the country to which they belong (in both cases
of 50 characters), and the number of medals of each type (integer) obtained by the athlete at the end of the game.
athlete at the end of the game.
The medal types are: 1 Gold, 2 Silver and 3 Bronze.
It is known that a maximum of 500 athletes participate.

Item 2-Enter a country, and inform its medal list, i.e. number of medals per type and total. For example:
           Gold Silver Bronze Total
Argentina    3    1       0     4

Item 3- To send the invitations to the closing party of the games, issue a list sorted alphabetically by name of the athlete.
alphabetically by athlete's name, also indicating the country to which he/she belongs.
To solve each menu item, use a different procedure with the appropriate parameters.

Spanish: 
Para los juegos sudamericanos para la juventud se solicita un menú iterativo con las siguientes opciones:
1- Carga de datos
2- Medallero de un país
3- Listado de deportistas
4- Salir

Notas:
Ítem 1-Cargar cada uno de los deportistas, ingresando su nombre, el país al que pertenece (en ambos casos
ninguno de los dos supera los 50 caracteres), y la cantidad de medallas de cada tipo (entero) obtenidas por el
deportista al finalizar el juego.
Los tipos de medalla son: 1 Oro, 2 Plata y 3 Bronce.
Se sabe que como máximo participan 500 deportistas.

Ítem 2-Ingresar un país, e informar su medallero, es decir, cantidad de medallas por tipo y el total. Por ejemplo:
            Oro Plata Bronce Total
Argentina    3    1     0      4

Ítem 3- Para cursar las invitaciones a la fiesta de cierre de los juegos, emitir un listado ordenado
alfabéticamente por nombre de deportista, indicando además el país al que pertenece.
Para resolver cada ítem del menú utilizar un procedimiento diferente con los parámetros adecuados.
----------------------------------------------------------------------
# Declarativa de variables y estructuras de datos
TYPE
   datosDeportista = RECORD
                       nombre: string[50];
                       pais: string[50];
                       oro: integer;
                       plata: integer;
                       bronce: integer;
                     END;
   deportista = array [1..500] of datosDeportista;

VAR
   medallero: deportista;
   opc, cant: integer;
"""

import os

class medallero:
    def __init__(self):  
        self.nombre = ""
        self.pais = ""
        self.oro = 0
        self.plata = 0
        self.bronce = 0

def menu():
    print('Menu');
    print('----');
    print()
    print('1-Alta de Deportistas')
    print('2-Listado de Medallas')
    print('3-Listado de Deportistas')
    print('4-Salir')
    print()

# función para cargar los deportistas con sus medallas y retornar la cantidad cargada hasta el momento
def carga(M, C):
    global TOPE
    os.system("cls");
    print('Ingrese los datos de los deportistas <* en nombre para terminar>');
    print()
    print()
    nom = input('Nombre: ')
    while (nom != '*' and C<TOPE):
        M[C].nombre = nom
        M[C].pais = input('País: ')
        M[C].oro = int(input('Cant. de Oro: '))
        M[C].plata = int(input('Cant. de Plata: '))
        M[C].bronce = int(input('Cant. de Bronce: '))
        C=C+1
        print("\n")
        nom = input('Nombre: ')
    return C

# Procedimiento para mostrar el medallero
def listaMedallas(M, C):
    os.system("cls");
    print('MEDALLERO POR PAIS')
    print('------------------\n')
    pais = input('Ingrese el pais: ');
    oro=0
    plata=0
    bronce=0
    for i in range (C):
        if (M[i].pais == pais):
            oro = oro + M[i].oro
            plata = plata + M[i].plata
            bronce = bronce + M[i].bronce
    print("\n")

    print('              ORO      PLATA     BRONCE    TOTAL')
    salida = ''
    salida += '{:<15}'.format(pais.strip())
    salida += '{:<10}'.format(str(oro).strip())
    salida += '{:<10}'.format(str(plata).strip())
    salida += '{:<10}'.format(str(bronce).strip())
    salida += '{:<10}'.format(str(oro+plata+bronce).strip())
    print(salida)
    os.system("pause")

# Procedimiento para mostrar la lista ordenada de participantes
def listaDeportistas(M, C):
    os.system("cls")
    if (C == 0):
        print('No hay deportistas inscriptos!!')
    else:
        #ordeno el arreglo por nombre
        for i in range(0, C-1):
            for j in range (i+1, C):
                if (M[i].nombre > M[j].nombre):
                   raux = M[i]
                   M[i] = M[j]
                   M[j] = raux
        # muestro el listado
        print('Deportistas de los Juegos Sudamericanos <ordenado por Nombre>')
        print()
        print('Nombre         Pais          Oro     Plata     Bronce')
        print('-----------------------------------------------------')
        for i in range(C):
            salida = ''
            salida += '{:<15}'.format(M[i].nombre.strip())
            salida += '{:<15}'.format(M[i].pais.strip())
            salida += '{:<10}'.format(str(M[i].oro).strip())
            salida += '{:<10}'.format(str(M[i].plata).strip())
            salida += '{:<10}'.format(str(M[i].bronce).strip())
            print(salida)
    os.system("pause")


### Programa Principal ###
TOPE = 10    # después cambiar a 500
deportistas = [None] * TOPE
for i in range (TOPE):
    deportistas[i] = medallero()
cant=0   # contador de cantidad de deportistas cargados
opc=99   # valor por defecto a la variable opc para forzar un primer ingreso al while
while (opc != 4):
    os.system("cls")
    menu()
    opc = int(input("Ingrese opcion <1 a 4>: "))
    while (opc<1 or opc>4):
        opc = int (input("Incorrecto. Ingrese opcion <1 a 4>: "))
    if (opc == 1):
        cant = carga(deportistas, cant)
    elif (opc == 2):
        listaMedallas(deportistas, cant)
    elif (opc == 3):
        listaDeportistas(deportistas, cant)
print("\n\nFin del programa!!")
