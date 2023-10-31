#------------------- IMPORTAR LIBRERIAS ----------------------------------
"""
Examen Final 06/02/2018

"""
import os
import pickle
import os.path

#----------------------- DEFINICION DE CLASES/REGISTROS ----------------------------------
class Propiedad:
    def __init__(self):  
        self.cod = 0    #5 caracteres
        self.tipo = ""  #1 caracteres
        self.zona = 0   #2 caracteres-- posicion relativa con el archivo Zonas 
        self.dir = ""   #30 caracteres
        self.cantAmb = 0  #2 caracteres
        self.precio = 0 #5 caracteres
        self.alquilado = [['D','D'] for x in range(3)]
        #mes 1er indice, quincena 2do indice

class Zona:
    def __init__(self):
        self.nro: 0 #3 caracteres
        self.nombre: "" #15 caracteres

#----------------------------- VALIDACIONES DATOS DE ENTRADA + FORMATEO ----------------------------------------- 
def validarEnteros(min, max):
    nro = int(input("Ingrese nro : "))
    while nro > max or nro < min:
        nro = int(input("Ingrese nro : "))
    return nro
 
def formatearPropiedad(rPropiedad): #seria un parametro variable el que recibe aca
    global afPropiedades, alPropiedades, afZonas, alZonas
    rPropiedad.cod = str(rPropiedad.cod).ljust(5)    #5 caracteres
    #el tipo no hace falta porque es un solo caracter siempre
    rPropiedad.zona =  str(rPropiedad.zona).ljust(2)  #2 caracteres-- posicion relativa con el archivo Zonas 
    rPropiedad.dir = (rPropiedad.dir).ljust(30)  #30 caracteres
    rPropiedad.cantAmb = str(rPropiedad.cantAmb).ljust(2)  #2 caracteres
    rPropiedad.precio = str(rPropiedad.precio).ljust(5) #5 caracteres
    for i in range(3):
        for j in range(2):
            rPropiedad.alquilado[i][j] = str(rPropiedad.alquilado[i][j]).ljust(1)

#----------------------------- BUSQUEDAS Y ORDENAMIENTO -----------------------------------------  
def buscaPropiedad(codigo):   # método de búsqueda dicotómica
    global afPropiedades, alPropiedades
    alPropiedades.seek(0)
    tamanio = os.path.getsize(afPropiedades)
    if tamanio == 0:
        return -1
    aux = pickle.load(alPropiedades)
    tamReg = alPropiedades.tell()
    cantReg = tamanio // tamReg
    inicio = 0
    fin = cantReg-1
    encontrado = False
    while not encontrado and inicio <= fin:
        medio = (inicio + fin) // 2
        alPropiedades.seek(medio*tamReg, 0)
        rPropiedad = pickle.load(alPropiedades)
        if int(rPropiedad.cod) == codigo:
            encontrado = True
        else:
            if codigo < int(rPropiedad.cod):
                fin = medio - 1
            else:
                inicio = medio + 1
    if int(rPropiedad.cod) == codigo:
        return (medio*tamReg)
    else:
        return -1

def ordenar():   # método ordenamiento falso burbuja
    global afPropiedades, alPropiedades, afZonas, alZonas
    alPropiedades.seek (0)
    aux = Propiedad()
    aux = pickle.load(alPropiedades)
    tamReg = alPropiedades.tell() 
    tamArch = os.path.getsize(afPropiedades)
    cantReg = int(tamArch / tamReg)  
    for i in range(0, cantReg-1):
        for j in range (i+1, cantReg):
            alPropiedades.seek (i*tamReg)
            auxi = Propiedad()
            auxi = pickle.load(alPropiedades)
            alPropiedades.seek (j*tamReg)
            auxj = Propiedad()
            auxj = pickle.load(alPropiedades)
            if (int(auxi.cod) > int(auxj.cod)):
                alPropiedades.seek (i*tamReg)
                pickle.dump(auxj, alPropiedades)
                alPropiedades.seek (j*tamReg)
                pickle.dump(auxi,alPropiedades)
                alPropiedades.flush()

#----------------------------- INICIALIZAR ----------------------------------------- 

#----------------------------- CARGAS/ALTAS -----------------------------------------
def alta():
    global afPropiedades, alPropiedades, afZonas, alZonas
    #valida que el codigo este disponible
    codigo = int(input('Ingrese codigo de la Propiedad: '))
    #tengo que poner la condicion del getsize tb porque sino en la dicotomica al hacer el load sobre algo vacio falla
    if os.path.getsize(afPropiedades) != 0:
        while buscaPropiedad(codigo) != -1:
            codigo = int(input('No puede usarse ese codigo. Ingrese otro codigo para dicha Propiedad: '))
    rPropiedad = Propiedad()
    rPropiedad.cod = codigo
    #valida el tipo
    rPropiedad.tipo = input('Ingrese el tipo de la Propiedad: ').upper()
    while rPropiedad.tipo != "C" and rPropiedad.tipo != "X" and rPropiedad.tipo != "D" :
        rPropiedad.tipo = input('Tipo no valido. Ingrese el tipo de la Propiedad: ').upper()
    #valida la zona.
    #deberia ser de 1 a 10, deje solo de 1 a 3 dado que solo cargue 3 en el archivo al comienzo
    rPropiedad.zona = validarEnteros(1,3)
    rPropiedad.dir = input('Ingrese la direccion: ')  
    rPropiedad.cantAmb = int(input('Ingrese la cantidad de ambientes: '))
    rPropiedad.precio = float(input('Ingrese el precio de Diciembre(base): '))
    formatearPropiedad(rPropiedad)
    alPropiedades.seek(os.path.getsize(afPropiedades))
    pickle.dump(rPropiedad,alPropiedades)
    alPropiedades.flush()
    ordenar() #no hacia falta desarrollar pero esta desarrolada para que funcione todo
    print('Alta registrada. ')

def modificar():
    global afPropiedades, alPropiedades, afZonas, alZonas
    #valida que al menos haya alguna propiedad cargada
    if os.path.getsize(afPropiedades) != 0:
        codigo = int(input('Ingrese codigo de la Propiedad: '))
        while buscaPropiedad(codigo) == -1:
            codigo = int(input('Codigo inexistente. Ingrese otro codigo de Propiedad: '))
        pos = buscaPropiedad(codigo)
        alPropiedades.seek(pos)
        rPropiedad = Propiedad()
        rPropiedad = pickle.load(alPropiedades)
        rPropiedad.precio = float(input('Ingrese el nuevo precio de Diciembre(base): '))
        formatearPropiedad(rPropiedad)
        alPropiedades.seek(pos)
        pickle.dump(rPropiedad,alPropiedades)
        alPropiedades.flush()
        print('Modificación registrada. ')
    else:
        print('No hay propiedades cargadas. ') 

def pantalla1():
    global afPropiedades, alPropiedades, afZonas, alZonas
    print("Listado de Zonas: ")
    alZonas.seek(0)
    tamanio = os.path.getsize(afZonas)
    while alZonas.tell() < tamanio:
        rZona = pickle.load(alZonas)
        print(rZona.nro, rZona.nombre)
    print("Fin del listado.")

#necesitamos esta funcion porque los indices en Python son numericos, no del tipo char
def nroMes(mes):
    if mes == "D":
        return 0
    elif mes == "E":
        return 1
    elif mes == "F":
        return 2

#para traer el nombre de la Zona por posicion relativa
def nombreZona(i):
    global  afZonas, alZonas
    i = int(i)
    alZonas.seek(0)
    aux = pickle.load(alZonas)
    tamReg = alZonas.tell() 
    pos = i*tamReg
    #print(pos, type(pos))
    alZonas.seek(pos)
    rZona = pickle.load(alZonas)
    return rZona.nombre

def calcularImporte(mes,quincena,precio):
    precio = float(precio)
    if mes == "D":
        if quincena != 0:
            return round(precio * 0.6,2)
        else:
            return round(precio,2)
    elif mes == "E":
        if quincena != 0:
            return round(precio*0.20 + (precio * 0.6),2)
        else:
            return round(precio*0.20 + precio,2)
    elif mes == "F":
        if quincena != 0:
            return round(precio * 0.10 + (precio * 0.6),2)
        else:
            return round(precio*0.10 + precio,2)

def pantalla2(tipo,mes,quincena,zona):
    global afPropiedades, alPropiedades, afZonas, alZonas
    print("Listado de Propiedades que coinciden: ")
    #hay que mostrar el nombre de la Zona por lo tanto por posicion relativa tengo que traerlo
    nombre = nombreZona(zona)
    print("Tipo ",tipo," Zona: ", nombre, " Mes: ", mes, " Quincena: ", quincena)
    alPropiedades.seek(0)
    tamanio = os.path.getsize(afPropiedades)
    indiceMes = nroMes(mes)
    rPropiedad = Propiedad()
    while alPropiedades.tell() < tamanio:
        rPropiedad = pickle.load(alPropiedades)
        if ((rPropiedad.tipo == tipo) and (int(rPropiedad.zona) == int(zona)) and ((quincena == 0 and rPropiedad.alquilado[indiceMes][0] == 'D' and rPropiedad.alquilado[indiceMes][1] == 'D') or (quincena != 0 and rPropiedad.alquilado[indiceMes][quincena-1] == 'D'))):
            total = calcularImporte(mes,quincena,rPropiedad.precio)
            print(rPropiedad.cod, rPropiedad.dir, rPropiedad.cantAmb, total)
    print("Fin del listado.")

def registrarAlquiler(nR,quincena,mes):
    global afPropiedades, alPropiedades, afZonas, alZonas
    pos = buscaPropiedad(nR)
    alPropiedades.seek(pos)
    rPropiedad = Propiedad()
    rPropiedad = pickle.load(alPropiedades)
    if quincena == 0:
        rPropiedad.alquilado[nroMes(mes)][0] = 'A'
        rPropiedad.alquilado[nroMes(mes)][1] = 'A'
    else:
        rPropiedad.alquilado[nroMes(mes)][quincena-1] = 'A'
    alPropiedades.seek(pos)
    formatearPropiedad(rPropiedad)
    pickle.dump(rPropiedad,alPropiedades)
    alPropiedades.flush()
    print('Alquiler registrado. ') 

def alquilar():
    global afPropiedades, alPropiedades, afZonas, alZonas
    #valido el tipo o * para salir
    tipo = input('Ingrese el tipo de la Propiedad: ').upper()
    while tipo != "C" and tipo != "X" and tipo != "D" and tipo != "*":
        tipo = input('Tipo no valido. Ingrese el tipo de la Propiedad: ').upper()
    while tipo != "*":
        mes = input('Ingrese el mes (D,E,F): ').upper()
        while mes != "D" and mes != "E" and mes != "F":
            mes = input('Mes no valido. Ingrese un mes correcto: ').upper()
        quincena = validarEnteros(0,2)
        pantalla1()
        zona = validarEnteros(1,10)
        #mostramos las coincidencias
        pantalla2(tipo,mes,quincena,zona)
        nroRef = int(input('Ingrese el nro de referencia: '))
        while nroRef != 0 and buscaPropiedad(nroRef) == -1:
            nroRef = int(input('Ingrese el nro de referencia: '))
        if nroRef != 0:
            registrarAlquiler(nroRef,quincena,mes)
        tipo = input('Ingrese el tipo de la Propiedad: ').upper()
        while tipo != "C" and tipo != "X" and tipo != "D" and tipo != "*":
            tipo = input('Tipo no valido. Ingrese el tipo de la Propiedad: ').upper()

def listado():
    global afPropiedades, alPropiedades, afZonas, alZonas
    alPropiedades.seek(0)
    tamanio = os.path.getsize(afPropiedades)
    while alPropiedades.tell() < tamanio:
        rPropiedad = pickle.load(alPropiedades)
        nombre = nombreZona(rPropiedad.zona)
        print(rPropiedad.cod, nombre, rPropiedad.dir)
        print ("M Q1 Q2")
        for i in range(3):
            print(i,rPropiedad.alquilado[i][0],rPropiedad.alquilado[i][1])

def abrir():
    global afPropiedades, alPropiedades, afZonas, alZonas
    afPropiedades = "./propiedades.dat"
    rZona = Zona()
    if not os.path.exists(afPropiedades):   
        alPropiedades = open(afPropiedades, "w+b")   
    else:
        alPropiedades = open(afPropiedades, "r+b")   
    afZonas = "./zonas.dat" 
    if not os.path.exists(afZonas):   
        alZonas = open(afZonas, "w+b")
        ##Hardcodeo algo de contenido dentro para cuando lo crea por primera vez
        rZona.nro = str(0).ljust(2) 
        rZona.nombre = ("Sur Playa").ljust(15) 
        pickle.dump(rZona, alZonas)
        alZonas.flush()
        rZona.nro = str(1).ljust(2) 
        rZona.nombre = ("Norte").ljust(15) 
        pickle.dump(rZona, alZonas)
        alZonas.flush()
        rZona.nro = str(2).ljust(2) 
        rZona.nombre = ("Golf").ljust(15) 
        pickle.dump(rZona, alZonas)
        alZonas.flush()

    else:
        alZonas = open(afZonas, "r+b")

def mostrarMenu():
    print("ALQUILERES DE VACACIONES")
    print("----------------\n")
    print("1 - Alta")
    print("2 - Modificación")
    print("3 - Alquilar")
    print("4 - Listado")
    print("0 - Salir \n\n")

def main():
    global afPropiedades, alPropiedades, afZonas, alZonas
    ### Programa principal ###
    abrir()
    opc = -1
    while opc != 0:
        mostrarMenu()
        opc = validarEnteros(0,4)
        if opc == 1:
            alta()
        elif opc == 2:
            modificar()
        elif opc == 3:
            alquilar()
        elif opc == 4:
            listado()
        else:
            print("\n\nGracias por visitarnos ...\n\n")
            alPropiedades.close()
            alZonas.close()

main()