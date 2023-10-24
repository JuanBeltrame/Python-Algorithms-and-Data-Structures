"""
Exercise 02 - Arreglo de Registros 
----------------------------------------------------------------------
English: 
A 3rd-year department at the university opened registration for its 5 sections. 
Each section has a capacity of 50 students.

To register each student, the following information is requested:
Student ID (integer)
Desired section number for enrollment (from 0 to 4)
Name (string)
If there are no available spots in the chosen section, the student cannot be registered.

A list is desired to display, for each of the 5 sections:
The total number of registered students
The names and student IDs of the students in the order they registered.


Spanish: 
Una cátedra de 3º año de la facultad abrió la inscripción para sus 5 comisiones. 
El cupo de cada una de ellas es de 50 alumnos. 

Para inscribir a cada alumno se le solicita:
Número de legajo (entero)
Número de comisión en la cual desea anotarse (de 0 a 4) 
Nombre (cadena ) 
Si no hay cupo en dicha comisión no se lo anota. 

Se desea un listado que muestre para cada una de las 5 comisiones,
la cantidad total de inscriptos y los nombres y números de legajo 
de los alumnos en el orden en que se fueron inscribiendo.
----------------------------------------------------------------------
Solucion Matriz de Registros
----------------------------------------------------------------------
CONSTANTES
N = 5;   // 5 Comisiones
A = 3;  // El enunciado dice 50 alumnos -


Alumno = RECORD
         legajo: integer;
         nombre: string;
   
Cont= array [1..5]of integer;

Als :arreglo bidimensional de tipo alumno;
"""
class Alumno:
        def __init__(self):
                #self.comision= 0  OBSERVAR!!! la comisión no la guardo como campo porque es la fila de la matriz
                self.legajo = 0
                self.nombre = " "


def Cargar(Als,Tam):
        i= -1
        rta='s'
        while rta=='s' and i<Tam:
                i= i+1
                comi= int(input('ingrese comisión entre 0 y 4:'))  #valido el número de comisión FILA
                while (comi <0)  or (comi>4):
                    comi= int(input('Incorrecto, ingrese comisión:'))
                if Cont[comi]< 3:
                    Cont[comi]= Cont[comi]+ 1
                     
                    leg= int(input ('Ingrese Legajo del alumno 1000-9999 : ')) #valido el número de legajo
                    while   (leg >9999) or (leg <1000):
                        leg= int(input ('Incorrecto- Ingrese Legajo del alumno 1000-9999 '))
                    Als[comi][Cont[comi]].legajo= leg    
                    nom = input("Nombre: ")
                    Als[comi][Cont[comi]].nombre= nom
                else:
                    print ('Esta comision no tiene mas lugar')
                
                rta= str(input('desea ingresar otro alumno s ó n '))  
                while (rta !='s')  and (rta!='n'):
                    rta= str(input('Incorrecto, ingrese respuesta s ó n:'))
        return i+1

def Mostrar(Als,Tam):  #OBSERVAR, no necesito filtrar por cada comisión sino que directamente muestro la matriz
    for i in range(5):
       print()
       print('Comision: ', i, '             Cantidad de inscriptos: ', Cont[i])
       print('---------------         -------------------------')
       if  Cont[i]==0:
           print('No hay alumnos cargados en esta comision')
       else:
           for j in range( Cont[i]) :   #recorro columnas hasta la cantidad que se hayan inscripto
               print (' ',Als[i][j].nombre,'   ',Als[i][j].legajo)


#Programa Principal

A=3 #puedo guardar hasta 3 alumnos por comisión, lo hacemos constante para simplificar la carga
FIL = 5  #5 comisiones de 0 a 4 ...FILAS
COL = A  # cuantos alumnos se inscriben en cada comisión
Als = [None]* FIL  # declaro un arreglo vacío de cualquier tipo de elemento

for i in range(FIL):   
	Als[i] = [Alumno()] * COL  #declaro que cada celda de la matriz de registros es de tipo Alumno  

Cont=[0]*A*FIL   # este es el arreglo único donde voy contando cuantos alumnos hay en cada comisión


print('Ingrese los registros del arreglo')
cuantos=Cargar(Als,FIL) 
print("se ingresaron", cuantos, "alumnos")
Mostrar(Als,cuantos)

