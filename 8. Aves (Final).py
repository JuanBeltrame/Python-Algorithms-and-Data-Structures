#------------------- IMPORTAR LIBRERIAS ----------------------------------
import os
import pickle
import os.path
import datetime

#----------------------- DEFINICION DE CLASES/REGISTROS ----------------------------------
class Ave:
    def __init__(self):  
        self.nro = 0 
        self.desc= "" 

class Socio:
    def __init__(self):  
        self.nro = 0 
        self.nom = "" 
        self.cant = 0 

class Avistaje:
    def __init__(self):  
        self.nroAve = 0 
        self.nroSocio = 0 
        self.fecha = ""  
        self.lugar = "" 

#----------------------------- VALIDACIONES DATOS DE ENTRADA + FORMATEO -----------------------------------------  
def validaRangoEntero(nro, min,max):
    try:              
        nro = int(nro)      
        if nro >= min and nro <= max:
            return False 
        else:
            return True  
    except:
        return True  

def validarChar(min, max):
    letra = input("Ingrese opcion ['a'-'f']: ").lower()
    while letra >max or letra <min:
        letra = input("Ingrese opcion ['a'-'f']: ").lower()
    return letra

def validarFecha():
    flag = True
    while flag:
        try:
            fecha = input("Ingresa una fecha en el formato DD/MM/AAAA: ")
            datetime.datetime.strptime(fecha, '%d/%m/%Y')
            print("Fecha valida")
            flag = False
        except ValueError:
            print("Fecha invalida")
    return fecha

def formatearAve(vrAve): 
    vrAve.nro= str(vrAve.nro)
    vrAve.nro= vrAve.nro.ljust(4, ' ') 
    vrAve.desc= vrAve.desc.ljust(30, ' ')

def formatearSocio(vrSocio): 
    vrSocio.nro= str(vrSocio.nro)
    vrSocio.nro= vrSocio.nro.ljust(4, ' ') 
    vrSocio.nom= vrSocio.nom.ljust(30, ' ')
    vrSocio.cant= str(vrSocio.cant)
    vrSocio.cant= vrSocio.cant.ljust(3, ' ')

def formatearAvistajes(vrAvistajes):
    vrAvistajes.nroAve= str(vrAvistajes.nroAve)
    vrAvistajes.nroAve= vrAvistajes.nroAve.ljust(4, ' ') 
    vrAvistajes.nroSocio= str(vrAvistajes.nroSocio)
    vrAvistajes.nroSocio= vrAvistajes.nroSocio.ljust(4, ' ') 
    vrAvistajes.lugar= vrAvistajes.lugar.ljust(30, ' ')
    vrAvistajes.fecha= str(vrAvistajes.fecha)
    vrAvistajes.fecha= vrAvistajes.fecha.ljust(12, ' ') 

#----------------------------- BUSQUEDAS Y ORDENAMIENTO -----------------------------------------  
#busqueda Secuencial por archivo Ave  con bandera
def buscaAve(nA):
    global ArcFisiAves, ArcLogAves 
    t = os.path.getsize(ArcFisiAves)
    rAve = Ave()
    band = False
    ArcLogAves.seek(0) 
    while ArcLogAves.tell()<t and band== False:
        pos = ArcLogAves.tell()
        rAve = pickle.load(ArcLogAves)
        if int(rAve.nro) == nA:
            band = True
    if band:
        return pos
    else:
        return -1

#busqueda Secuencial por archivo Socio con bandera
def buscaSocio(nS):
    global ArcFisiSocios, ArcLogSocios
    t = os.path.getsize(ArcFisiSocios)
    rSocio = Socio()
    band = False
    ArcLogSocios.seek(0,0) 
    while ArcLogSocios.tell()<t and band== False:
        pos = ArcLogSocios.tell()
        rSocio = pickle.load(ArcLogSocios)
        if int(rSocio.nro) == nS:
            band = True
    if band:
        return pos
    else:
        return -1

def ordenarSocios():
    global ArcFisiSocios,ArcLogSocios
    ArcLogSocios.seek (0)
    aux = pickle.load(ArcLogSocios) #para con el tell saber cuanto pesa un registro
    tamReg = ArcLogSocios.tell() 
    tamArch = os.path.getsize(ArcFisiSocios)
    cantReg = int(tamArch / tamReg)  
    for i in range(0, cantReg-1):
        for j in range (i+1, cantReg):
            ArcLogSocios.seek (i*tamReg, 0)
            auxi = pickle.load(ArcLogSocios)
            ArcLogSocios.seek (j*tamReg, 0)
            auxj = pickle.load(ArcLogSocios)
            if (auxi.cant < auxj.cant):
                ArcLogSocios.seek (i*tamReg, 0)
                pickle.dump(auxj, ArcLogSocios)
                ArcLogSocios.seek (j*tamReg, 0)
                pickle.dump(auxi,ArcLogSocios)

#----------------------------- INICIALIZAR ----------------------------------------- 

#----------------------------- CARGAS/ALTAS -----------------------------------------

def grabar (nroA, nroS, fecha, lugar):
    global ArcLogAvistajes
    rAvistaje=Avistaje()
    rAvistaje.nroAve = str(nroA).ljust(5)   #5
    rAvistaje.nroSocio = str(nroS).ljust(5) #5
    rAvistaje.fecha = fecha  #12
    rAvistaje.lugar = lugar  #30
    ArcLogAvistajes.seek(0,2)
    pickle.dump(rAvistaje, ArcLogAvistajes)
    ArcLogAvistajes.flush()

def ActualizarSocio(nS):
    pos = buscaSocio(nS)
    ArcLogSocios.seek(pos,0)
    rSocio = pickle.load(ArcLogSocios)
    rSocio.cant = str(int(rSocio.cant) + 1).ljust(3)
    ArcLogSocios.seek(pos,0) ##tengo que volver a pararme adelante del registro a actualizar
    pickle.dump(rSocio, ArcLogSocios)
    ArcLogSocios.flush()

def registrarAvistaje():
    nroAve = int(input('Ingrese nro de Ave: '))
    if buscaAve(nroAve) == -1:
        print(" El nro de Ave ingresado NO EXISTE")
    else: 
        nroSocio = int(input('Ingrese nro de Socio: '))
        if buscaSocio(nroSocio) == -1:
            print(" El número de socio ingresado NO EXISTE")

        else:
            fecha = validarFecha().ljust(12)
            lugar = input("Ingrese lugar: ").lower().ljust(30)
            grabar(nroAve,nroSocio,fecha,lugar)
            ActualizarSocio(nroSocio)
            print('Registro grabado exitosamente \n')

def historiaMigratoria():
    global ArcLogAves, ArcFisiAvistajes,ArcLogAvistajes
    rAvistaje=Avistaje()
    rAve= Ave()
    nroAve = int(input('Ingrese nro de Ave: '))
    pos= buscaAve(nroAve)
    if pos == -1:
        print('nro de Ave NO EXISTE:  ')
    else:
        ArcLogAves.seek(pos,0)
        rAve=pickle.load(ArcLogAves)
        print('.......Historia migratoria: ',rAve.desc)
        print("-------------------------------------------------------")
        print(" Socio      Lugar de avistaje                    Fecha")
        print("-------------------------------------------------------")
        ArcLogAvistajes.seek(0,0)
        t = os.path.getsize(ArcFisiAvistajes)
        while ArcLogAvistajes.tell() < t:
            rAvistaje = pickle.load(ArcLogAvistajes)
            if int(rAvistaje.nroAve) == int(nroAve):
                print (" ",rAvistaje.nroSocio," ",rAvistaje.lugar," ", rAvistaje.fecha)

def observaciones():
    global ArcFisiSocios, ArcLogSocios
    ordenarSocios()
    cont=0
    ArcLogSocios.seek(0,0)
    t = os.path.getsize(ArcFisiSocios)
    print("--------------------------------------------------------")
    print(" socio    Nombre               cantidad de observaciones")
    print("--------------------------------------------------------")
    while (ArcLogSocios.tell() < t)and cont<=15: 
        rSocio = pickle.load(ArcLogSocios)
        print(" ",rSocio.nro, " ",rSocio.nom," ", rSocio.cant)
        cont=cont+1
    input()

def CargaSocios():
    global ArcFisiSocios, ArcLogSocios
    os.system("cls")
    RegSocio= Socio()
    print("OPCION  e - Carga de Socios")
    print("----------------------------\n")
    ns = input("Ingrese el numero de socio entre 1 y 9999 [0- para Volver]: ")
    while validaRangoEntero(ns, 0, 9999):
        ns = input("Incorrecto - Entre 1 y 9999 [0 para Volver]: ")
    while int(ns) != 0:
        if buscaSocio(int(ns)) == -1:
            RegSocio.nom = input("Nombre del Socio: ")
            while len(RegSocio.nom)<1 or len(RegSocio.nom)>30:
                RegSocio.nom = input("Incorrecto - Nombre <hasta 30 caracteres>: ")
            RegSocio.nro=ns
            RegSocio.cant=0
            formatearSocio(RegSocio)
            ArcLogSocios.seek(0,2)
            pickle.dump(RegSocio, ArcLogSocios)
            print("-----------------------")
            print("Alta de Socio exitosa")
            print("------------------------")
            ArcLogSocios.flush()
        else:
            print("Número de Socio ya existe...")
        ns = input("Ingrese el numero de socio entre 1 y 9999 [0- para Volver]: ")
        while validaRangoEntero(ns, 0, 9999):
            ns = input("Incorrecto - Entre 1 y 9999 [0 para Volver]: ")

def CargaAves():
    global ArcFisiAves, ArcLogAves
    os.system("cls")
    RegAve= Ave()
    print("OPCION  d - Carga de Aves")
    print("----------------------------\n")
    na = input("Ingrese el numero de ave entre 1 y 9999 [0- para Volver]: ")
    while validaRangoEntero(na, 0, 9999):
        na = input("Incorrecto - Entre 1 y 9999 [0 para Volver]: ")
    while int(na) != 0:
        if buscaAve(int(na)) == -1:
            #ingresa(cod,RegAve)
            RegAve.desc = input("Descripción del Ave: ")
            while len(RegAve.desc)<1 or len(RegAve.desc)>30:
                RegAve.desc = input("Incorrecto - descripción <hasta 30 caracteres>: ")
            RegAve.nro=na
            formatearAve(RegAve)
            ArcLogAves.seek(0,2)
            pickle.dump(RegAve, ArcLogAves)
            print("-----------------------")
            print("Alta de Ave exitosa")
            print("------------------------")
            ArcLogAves.flush()
        else:
            print("Número de Ave ya existe...")
        na = input("Ingrese el numero de ave entre 1 y 9999 [0- para Volver]: ")
        while validaRangoEntero(na, 0, 9999):
            na = input("Incorrecto - Entre 1 y 9999 [0 para Volver]: ")

def Pantalla():
    print("")
    print("FINAL AVES")
    print("----------------\n")
    print("a - Registro de avistaje")
    print("b - Listado de historia migratoria")
    print("c - Listado cantidad de observaciones")
    print("d - Alta AVES")
    print("e - Alta SOCIOS")
    print("f - Salir \n")

# programa principal 
ArcFisiAves = "D:\\AEDD\\aves.dat" 
ArcFisiAvistajes = "D:\\AEDD\\avistajes.dat" 
ArcFisiSocios = "D:\\AEDD\\socios.dat" 
if not os.path.exists(ArcFisiAves):   
    ArcLogAves = open(ArcFisiAves, "w+b")   
else:
    ArcLogAves = open(ArcFisiAves, "r+b")
if not os.path.exists(ArcFisiSocios):   
    ArcLogSocios = open(ArcFisiSocios, "w+b")   
else:
    ArcLogSocios = open(ArcFisiSocios, "r+b")
if not os.path.exists(ArcFisiAvistajes):   
    ArcLogAvistajes = open(ArcFisiAvistajes, "w+b")   
else:
    ArcLogAvistajes = open(ArcFisiAvistajes, "r+b")
##variables auxiliares
RegAve = Ave()
RegSocio = Socio()
RegAje = Avistaje()
##menu
opc = 'a'
while opc != 'f':
    Pantalla()
    opc = validarChar('a','f')
    if opc == 'a':
        registrarAvistaje()
    elif opc == 'b':
        historiaMigratoria()
    elif opc == 'c':
        observaciones()
    elif (opc == 'd'):
        CargaAves()
    elif (opc == 'e'):
        CargaSocios()
    elif opc == 'f':
        print("Gracias por visitarnos ...\n")
        ArcLogAves.close()
        ArcLogSocios.close()
        ArcLogAvistajes.close()
        print(" archivos cerrados ..Fin del programa!!")
        input()
