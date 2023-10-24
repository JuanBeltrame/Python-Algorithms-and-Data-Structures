"""
Exercise 02 - Arreglo de Registros 
----------------------------------------------------------------------
English: 
A 3rd-year department at the university opened registration for its 5 sections. Each section has a capacity of 50 students.

To register each student, the following information is requested:
Student ID (integer)
Desired section number for enrollment (from 0 to 4)
Name (string)
If there are no available spots in the chosen section, the student cannot be registered.

A list is desired to display, for each of the 5 sections:
The total number of registered students
The names and student IDs of the students in the order they registered.


Spanish: 
Una cátedra de 3º año de la facultad abrió la inscripción para sus 5 comisiones. El cupo de cada una de ellas es de 50 alumnos. 

Para inscribir a cada alumno se le solicita:
Número de legajo (entero)
Número de comisión en la cual desea anotarse (de 0 a 4) 
Nombre (cadena ) 
Si no hay cupo en dicha comisión no se lo anota. 

Se desea un listado que muestre para cada una de las 5 comisiones,
la cantidad total de inscriptos y los nombres y números de legajo de los alumnos en el orden en que se fueron inscribiendo.
----------------------------------------------------------------------
Solucion SIN matriz registro
----------------------------------------------------------------------
CONSTANTES
A = 3 hasta 3 alumnos por comisión en vez de 50
T = 5 * A  5 comisiones en un arreglo de registro

TIPOS
Cont : arreglo [1..T*A]de enteros aca voy a ir guardando la cantidad de alumnos inscriptos en cada comisión
Alumno = Registro
         comisión: entero
         legajo: entero
	     nombre: string 
	

VARIABLES
Als: Arreglo[T] de Alumnos
"""
# una función para inicializar un registro de tipo Alumno
class Alumno:
        def __init__(self):
                self.comision= 0
                self.legajo = 0
                self.nombre = " "
 		

def Cargar(Als,Tam):
        i= -1
        rta='s'
        while rta=='s' and i<Tam:
                i= i+1
                
                comi= int(input('ingrese comisión entre 0 y 4:'))  #valido el número de comisión
                while (comi <0)  or (comi>4):
                    comi= int(input('Incorrecto, ingrese comisión:'))
                if Cont[comi]< 3:
                    Cont[comi]= Cont[comi]+ 1
                    Als[i].comision= comi    
                    leg= int(input ('Ingrese Legajo del alumno 1000-9999 : ')) #valido el número de legajo
                    while   (leg >9999) or (leg <1000) :
                        leg= int(input ('Ingrese Legajo del alumno 1000-9999 : '))
                    Als[i].legajo= leg    
                    nom = input("Nombre: ")
                    Als[i].nombre= nom
                else:
                    print ('Esta comision no tiene mas lugar')
                
                rta= str(input('desea ingresar otro alumno s ó n '))  
                while (rta !='s')  and (rta!='n'):
                    rta= str(input('Incorrecto, ingrese respuesta s ó n:'))
        return i+1
 
def MostrarTodo(Als, Tam):
    print("   comisión    Legajo    Nombre  ")
    print("----------------------------------------------------")
    #i=-1
    #while  i<= Tam :
    for i in range (Tam):
        print("   ",Als[i].comision,"       ",Als[i].legajo,"    ",Als[i].nombre)  
       # i=i+1
        
     
def Mostrar(Als, Tam):
    for j in range (5):    
       print()
       print ('Comision: ', j, '             Cantidad de inscriptos: ', Cont[j])
       print('---------------         -------------------------')
       if  Cont[j]==0:
           print('No hay alumnos cargados en esta comision')
       else:
           for k in range (Tam):
               if Als[k].comision == j:
                   print (' ',Als[k].nombre,'   ',Als[k].legajo)
    
#Programa Principal
# declaración de un tipo de registro Alumno vacío 

A=3 #puedo guardar hasta 3 alumnos por comisión
T = 5*A  #5 comisiones de 0 a 4 con hasta 3 inscriptos x comisión

Als = [None]* T  # declaro un arreglo vacío de cualquier tipo de elemento

for i in range(T):   # acá digo que los elementos del arreglo serán de tipo registro Alumno
	Als[i] = Alumno()

Cont=[0]*A*T   # este es el arreglo único donde voy contando cuantos alumnos hay en cada comisión

cuantos=Cargar(Als,T)
print("se ingresaron", cuantos, "alumnos")
MostrarTodo(Als,cuantos)
Mostrar(Als,cuantos)





   
