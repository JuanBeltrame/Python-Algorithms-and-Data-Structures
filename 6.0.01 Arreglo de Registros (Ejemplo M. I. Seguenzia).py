"""
Exercise 01 - Arreglo de Registros
----------------------------------------------------------------------
English: 
For a subject in the basic cycle of a faculty, the following data for 50 students are available: 
Student ID, section, student's name, major code, 3 midterm grades. 
It is desired to obtain a list of the 50 students with all the data, ordered in decreasing order by the average of the 3 grades.

Spanish: 
Para una materia del ciclo básico de una facultad se tiene los siguientes datos de 50 alumnos: 
Legajo, comisión, nombre del alumno, código de carrera, 3 notas de parciales.
Se desea obtener un listado de los 50 alumnos con todos los datos ordenado en forma decreciente por promedio de las 3 notas
----------------------------------------------------------------------
DECLARATIVA
TIPOS 
Alumno = Registro
        legajo: entero 
        comision: entero
        nombre: string 
        carrera: string
        notas: array[3] de enteros
        promedio: flotante

CONSTANTES
T= 3 Dimension 3 para almacenar 3 alumnos en un arreglo de registro

VARIABLES
Als: Arreglo[T] de Alumno
"""
class Alumno:
 	def __init__(self):  # constructor dentro de la clase Alumno
 		self.legajo = 0
 		self.comision= 0
 		self.nombre = " "
 		self.carrera = " "
 		self.notas = [0]*3
 		self.promedio = 0.00

"""def Cargar(Als,tam):  # carga datos sin validar
    for i in range(tam):
        acum=0
        print("alumno", i+1, ":")
        Als[i].legajo = int(input(" Legajo: "))
        Als[i].comision = int(input(" Comisión : ")) 
        Als[i].nombre = str(input(" Nombre: "))
        Als[i].carrera = str(input(" Carrera: ")) 
        for k in range(3):
            Als[i].notas[k] = int(input(" Ingrese nota: "))
            acum = acum + Als[i].notas[k]
        Als[i].promedio = acum/3
        print() """

def validaRangoEntero(nro, desde, hasta):
    try:              
        nro = int(nro)      
        if nro >= desde and nro <= hasta:
            return True 
        else:
            return False  
    except:
        return False        

def Cargar(Als,tam):   #carga datos con validación usando las funciones 
        for i in range(tam):
            acum=0
            print("alumno", i+1, ":")
            leg= input ('Ingrese Legajo del alumno 1000-9999 : ') #valido el número de legajo
            while   validaRangoEntero(leg,1000,9999)== False :
                leg= input ('Incorrecto. Ingrese Legajo del alumno 1000-9999  : ')
            Als[i].legajo=int(leg)
            
            comi= input('ingrese comisión entre 0 y 4:')  #valido el número de comisión
            while validaRangoEntero(comi,0,4)== False:
                comi =input('Incorrecto. Ingrese comisión:')
            Als[i].comision=int(comi)
            
            Als[i].nombre = input(" nombre: ")

            Als[i].carrera = str(input(" Carrera- S-sistemas  M-mecánica  Q-Química ")) 
            while (Als[i].carrera !='S')and (Als[i].carrera !='M')and (Als[i].carrera !='Q'):
                Als[i].carrera = str(input('Incorrecto. Ingrese carrera :'))

            for k in range(3):
                    nota = input("ingrese nota entre 0 y 10:")
                    while validaRangoEntero(nota,0,10)== False:
                        nota= input('Incorrecto. Ingrese nota:')
                    Als[i].notas[k]= int(nota)
                    acum = acum + Als[i].notas[k]

            Als[i].promedio = acum/3
            print() 

def Mostrar(Als, Tam):
    print("comisión    Legajo    Nombre       carrera  Nota1 Nota2  Nota3    Promedio  ")
    print("----------------------------------------------------------------------------")
    for i in range (Tam):
         print("   ",Als[i].comision,"       ",Als[i].legajo,"    ",Als[i].nombre,"    ",Als[i].carrera,"    ",Als[i].notas[0]," ",Als[i].notas[1]," ",Als[i].notas[2],"   ",round(Als[i].promedio,2))
      
def Ordenar(Bls,tam):  #notar que le puedo cambiar el nombre al parámetro formal
    for i in range (tam-1): 
       for j in range (i+1,tam): 
          if Bls[i].promedio < Bls[j].promedio:  #ordeno decreciente, de mayor a menor
              a= Bls[i]
              Bls[i]= Bls[j]
              Bls[j]= a

#Programa Principal
# declaración de un tipo de registro Alumno vacío 

T = 3

Als = [None]* T
for i in range(T):
	Als[i] = Alumno()

Cargar(Als,T)
print('---------------------------')
print('    muestra desordenado')
print('---------------------------')
Mostrar(Als,T)
print('---------------------------')
print('muestra ordenado por promedio')
print('---------------------------')
Ordenar(Als,T)
Mostrar(Als,T)
