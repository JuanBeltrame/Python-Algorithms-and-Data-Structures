class Empleado:
    def __init__(self): # Constructor del Registro Empleado
        self.legajo = 0
        self.nombre = ""
        self.sueldo = [0.00] * 3
        self.antiguedad  = 0


def carga_empleado(rEmp): # En el caso de querer cargar un solo registro
    rEmp.legajo = input("Legajo: ")
    rEmp.nombre = input("Nombre: ")
    for j in range(12):
        rEmp.sueldo[j]=float(input("Sueldo mes"+ str(j+1) +":"))
    rEmp.antiguedad = int(input("Antiguedad: "))    

def mostrar_empleado(rEmp): # En el caso de querer mostrar un solo registro
    print("\nLegajo: ", rEmp.legajo)
    print("Nombre: ", rEmp.nombre)
    for j in range(12):
        print("Sueldo mes",j+1,":",rEmp.sueldo[j],end='\t')
    print("\nAntiguedad: ",rEmp.antiguedad,end='\n\n')


def carga_empleados(rEmp,tam): # Para cargar un arreglo de Empleados
    for i in range(tam):
       rEmp[i].legajo = input("Legajo: ")
    rEmp[i].nombre = input("Nombre: ")
    for j in range(12):
        rEmp[i].sueldo[j]=float(input("Sueldo mes"+ str(j+1) +":"))
    rEmp[i].antiguedad = int(input("Antiguedad: ")) 

def mostrar_empleados(rEmp,tam): # Para mostrar un arreglo de registros
    for i in range(tam):
        print("\nLegajo: ", rEmp.legajo)
        print("Nombre: ", rEmp.nombre)
        for j in range(12):
            print("Sueldo mes",j+1,":",rEmp.sueldo[j],end='\t')
        print("\nAntiguedad: ",rEmp.antiguedad,end='\n\n')

#----------------------------------------------------------------------
# Main Program
T = 3
regEmp = [None] * T # Arreglo undimensional de Tamano T 
for j in range(T):
    regEmp[j]= Empleado() #definimos una variable tipo registro
carga_empleado(regEmp)
mostrar_empleado(regEmp)
carga_empleados(regEmp,T)
mostrar_empleados(regEmp,T)
