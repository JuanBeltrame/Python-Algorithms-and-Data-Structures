#------------------- IMPORTAR LIBRERIAS ----------------------------------
import os
import os.path
import pickle

#----------------------- DEFINICION DE CLASES/REGISTROS ----------------------------------
class Pais:
    def __init__(self):
        self.codigo = 0
        self.nombre = " "
        self.cantMedellas = [0]*3
        self.baja = False

class PuntajePar:
    def __init__(self):
        self.nomPartic = " "
        self.codigo_pais = 0
        self.categoria = " "
        self.puntos = [0] * 6
        self.puntaje_final = 0.0

#----------------------------- VALIDACIONES DATOS DE ENTRADA + FORMATEO -----------------------------------------
def validarExistArchivoPais():
    global arFiPais
    global arLoPais
    arFiPais = "paises.dat"
    if not os.path.exists(arFiPais):
        print("El archivo " + arFiPais + " NO existía y fue creado")
        arLoPais = open(arFiPais, "w+b")
    else:
        arLoPais = open(arFiPais, "r+b")

def validarExistArchivoPuntaje():
    global arFiPuntaje
    global arLoPuntaje
    arFiPuntaje = "puntajes.dat"
    if not os.path.exists(arFiPuntaje):
        print("El archivo " + arFiPuntaje + " NO existía y fue creado")
        arLoPuntaje = open(arFiPuntaje, "w+b")
    else:
        arLoPuntaje = open(arFiPuntaje, "r+b")

def validarIngresoEntero(x, y, z):
    try:
        valor = int(x)
        if valor >= y and valor <= z:
            return True
        else:
            print(f"Por favor, ingrese un valor entre {y} y {z}")
            return False
    except ValueError:
        print(f"Por favor, ingrese un valor entero")
        return False

#----------------------------- BUSQUEDAS Y ORDENAMIENTO -----------------------------------------
def buscarPais(codigo):
    global arFiPais
    global arLoPais
    t = os.path.getsize(arFiPais)
    arLoPais.seek(0, 0)
    pos = arLoPais.tell()
    if t == 0:
        return -1
    else:
        p = pickle.load(arLoPais)
        while arLoPais.tell() < t and int(p.codigo) != codigo:
            pos = arLoPais.tell()
            p = pickle.load(arLoPais)
        if int(p.codigo) == codigo:
            return pos
        else:
            return -1

def ordenarPorPuntaje():
    global arFiPuntaje
    global arLoPuntaje
    arLoPuntaje.seek(0, 0)
    pun = pickle.load(arLoPuntaje)
    tamReg = arLoPuntaje.tell()
    tamArc = os.path.getsize(arFiPuntaje)
    cantReg = tamArc // tamReg
    arLoPuntaje.seek(0, 0)
    for i in range(0, cantReg-1):
        for j in range(i+1,cantReg):
            arLoPuntaje.seek(i*tamReg, 0)
            a = pickle.load(arLoPuntaje)
            arLoPuntaje.seek(j*tamReg, 0)
            b = pickle.load(arLoPuntaje)
            if a.puntaje_final > b.puntaje_final:
                arLoPuntaje.seek(i * tamReg, 0)
                pickle.dump(b, arLoPuntaje)
                arLoPuntaje.seek(j * tamReg, 0)
                pickle.dump(a, arLoPuntaje)

def ordenarPorMedalla():
    global arFiPais
    global arLoPais
    arLoPais.seek(0, 0)
    pais = pickle.load(arLoPais)
    tamReg = arLoPais.tell()
    tamArc = os.path.getsize(arFiPais)
    cantReg = tamArc // tamReg
    arLoPais.seek(0, 0)
    for i in range(0, cantReg - 1):
        for j in range(i + 1, cantReg):
            arLoPais.seek(i * tamReg, 0)
            a = pickle.load(arLoPais)
            arLoPais.seek(j * tamReg, 0)
            b = pickle.load(arLoPais)
            if a.cantMedellas[0] > b.cantMedellas[0]:
                arLoPais.seek(i * tamReg, 0)
                pickle.dump(b, arLoPais)
                arLoPais.seek(j * tamReg, 0)
                pickle.dump(a, arLoPais)

#----------------------------- INICIALIZAR -----------------------------------------


def mostrarPais(p):
    print("Codigo:", p.codigo, "  Nombre del Pais:", p.nombre.strip())


def mostrarPaisCompleto(p):
    print("Codigo:", p.codigo, "  Nombre del Pais:", p.nombre.strip(),
          "Medallas de Oro: ", p.cantMedellas[0], "Medallas de Plata: ", p.cantMedellas[1], "Medallas de Bronce: ", p.cantMedellas[2])




def cargarPais():
    global arLoPais
    p = Pais()
    cod = int(input("Ingresa el código del pais, entre 0 y 999 [0 para Volver]: "))
    while not validarIngresoEntero(cod, 0, 999):
        cod = input("Por favor, un número entero entre 0 y 999: ")
    cod = int(cod)
    while cod != 0:
        if buscarPais(cod) == -1:
            p.codigo = cod
            p.nombre = input("Nombre del País: ").ljust(20, " ")
            while len(p.nombre) < 1 or len(p.nombre) > 20:
                p.nombre = input("Por favor no uses mas de 20 caracteres: ")
            p.baja = False
            for j in range(3):
                p.cantMedellas[j] = 0
            pickle.dump(p, arLoPais)
            arLoPais.flush()
            print("Producto dado de alto con éxito:")
            mostrarPais(p)
        else:
            print("Ya existe un pais con el código", cod)
        cod = int(input("Ingresa el código del pais, entre 0 y 999 [0 para Volver]: "))
        while not validarIngresoEntero(cod, 0, 999):
            cod = input("Por favor, un número entero entre 0 y 999: ")
        cod = int(cod)


def crearPais():
    global arFiPais
    global arLoPais
    os.system("cls")
    print("ALTA DE PAÍS\n")
    t = os.path.getsize(arFiPais)
    if t == 0:
        print("Aun no hay paises registrados")
    else:
        print("Lista de Productos")
        print("------------------")
        arLoPais.seek(0, 0)
        while arLoPais.tell() < t:
            p = pickle.load(arLoPais)
            if p.baja == False:
                mostrarPais(p)
                print("-----------------------------------------------------------------")
    print()
    cargarPais()


def eliminarPais():
    global arLoPais
    p = Pais()
    os.system("cls")
    print("BAJA LÓGICA DE UN PAÍS\n")
    print("Recordar que el país que se da de baja si ya fue utilizado no se eliminará del medallero")
    cod = input("Ingresa el código del pais, entre 1 y 999 [0 para Volver]: ")
    while not validarIngresoEntero(cod, 0, 999):
        cod = input("Por favor, un número entero entre 0 y 999: ")
    cod = int(cod)
    if cod != 0:
        pos = buscarPais(cod)
        if pos == -1:
            print("El producto no existe")
        else:
            arLoPais.seek(pos, 0)
            p = pickle.load(arLoPais)
            print("Pais a dar de baja:")
            mostrarPais(p)
            p.baja = True
            rpta = input("Confirma? (S o N): ")
            while rpta.upper() != "S" and rpta.upper() != "N":
                rpta = input("Incorrecto - Confirma? (S o N): ")
            if rpta.upper() == "S":
                arLoPais.seek(pos, 0)
                pickle.dump(p, arLoPais)
                arLoPais.flush()
                print("Eliminación exitosa")
                print("El producto eliminado es: ")
                mostrarPais(p)
        os.system("pause")


def listarPaises():
    global arLoPais
    global arFiPais
    p = Pais()
    t = os.path.getsize(arFiPais)
    if t == 0:
        print("No hay pais registrados")
    else:
        arLoPais.seek(0, 0)
        while arLoPais.tell() < t:
            p = pickle.load(arLoPais)
            if not p.baja:
                mostrarPais(p)

    print("---------------------------------------------------")
    input("Toque una tecla para continuar...")


def editarPais():
    global arLoPais
    p = Pais()
    os.system("cls")
    print("MODIFICAR EL NOMBRE DE UN PAïS\n")
    cod = input("Ingresa el código del país, entre 1 y 999 [0 para Volver]: ")
    while not validarIngresoEntero(cod, 0, 999):
        cod = input("Por favor, un número entero entre 0 y 999: ")
    cod = int(cod)
    if cod != 0:
        pos = buscarPais(cod)
        if pos == -1:
            print("El país no existe o fue dado de baja")
        else:
            arLoPais.seek(pos, 0)
            p = pickle.load(arLoPais)
            print("Producto a modificar el nombre: ")
            mostrarPais(p)
            s = input("Deseas Modificar el nombre de este país (S/N): ").upper()
            while s != "S" and s != "N":
                s = input("Por favor, solo contesta con S para Si o N para No ").upper()
            if s == "S":
                p.nombre = input(f"Nuevo Nombre: ").ljust(15, " ")
            rpta = input("¿Confirma actualización? (S o N): ")
            while rpta.upper() != "S" and rpta.upper() != "N":
                rpta = input("Incorrecto - Confirma? (S o N): ")
            if rpta.upper() == "S":
                arLoPais.seek(pos, 0)
                pickle.dump(p, arLoPais)
                arLoPais.flush()
                print("Modificación exitosa")
                print("El nombre del país fue actualizado:")
                mostrarPais(p)
        os.system("pause")


def ejecutarCase_2(accion):
    if accion == "A":
        crearPais()
    elif accion == "B":
        eliminarPais()
    elif accion == "C":
        listarPaises()
    elif accion == "M":
        editarPais()


def mostrarMenuPaises():
    os.system("cls")
    print("A - ALTA")
    print("B – BAJA")
    print("C – CONSULTA")
    print("M – MODIFICACION")
    print("V – VOLVER")


def mostrarOpciones():
    os.system("cls")
    print("1- CARGAR RESULATODOS DE PARTICIPANTES")
    print("2 – ARMAR EL PODIO")
    print("3 – MOSTRAR EL MEDALLERO")
    print("4 – EXTRA!! ADMINISTRAR PAISES (En chapin no hay que realizarlo")
    print("0 – Fin del programa")


def seleccionarAccion():
    opcionABM = input("Ingrese la opción deseada: ").upper()
    while opcionABM != "A" and opcionABM != "B" and opcionABM != "C" and opcionABM != "M" and opcionABM != "V":
        opcionABM = input("Ingrese una opción correcta: ").upper()
    return opcionABM


def administrarPaises():
    mostrarMenuPaises()
    abm = seleccionarAccion()
    ejecutarCase_2(abm)


def salir():
    print("Muchas gracias por usar nuestro sistema")


def registrarPuntajes():
    global arLoPuntaje
    global arFiPuntaje
    pun = PuntajePar()
    rta = input("Desea ingresar los resultados de un participante (S / N): ").upper()
    while rta != "S" and rta != "N":
        rta = input("Por favro ingrese (S / N): ").upper()
    while rta == "S":
        pun.nomPartic = input("Nombre del participante: ").ljust(30, " ")
        while len(pun.nomPartic) < 1 or len(pun.nomPartic) > 30:
            pun.nomPartic = input("Por favor no uses mas de 30 caracteres: ")
        listarPaises()
        codPais = input("Ingresa el código del país, entre 0 y 999: ")
        while not validarIngresoEntero(codPais, 0, 999):
            codPais = input("Por favor, un número entero entre 0 y 999: ")
        codPais = int(codPais)
        while buscarPais(codPais) == -1:
            print("Ingresó un código de país que no existe")
            print("Ingreso uno de los códigos listados abajo")
            listarPaises()
            codPais = input("Ingresa el código del país, entre 0 y 999: ")
            while not validarIngresoEntero(codPais, 0, 999):
                codPais = input("Por favor, un número entero entre 0 y 999: ")
            codPais = int(codPais)
        pun.codigo_pais = codPais
        pun.categoria = input("Categoría en la que participa (A/B/C/D): ").upper()
        while pun.categoria != "A" and pun.categoria != "B" and pun.categoria != "C" and pun.categoria != "D":
            pun.categoria = input("Por favro ingrese (A/B/C/D): ").upper()
        for i in range(6):
            puntos = input(f"Ingresa el puntaje del juez {i}, entre 0 y 10: ")
            while not validarIngresoEntero(puntos, 0, 10):
                puntos = input("Por favor, un número entero entre 0 y 10: ")
            puntos = int(puntos)
            pun.puntos[i] = puntos

        mayor = 0
        menor = 10
        for i in range(6):
            if pun.puntos[i] > mayor:
                mayor = pun.puntos[i]
                juezA = i
        for i in range(6):
            if pun.puntos[i] < menor:
                menor = pun.puntos[i]
                juezB = i
        total = 0
        for i in range(6):
            if i != juezA and i != juezB:
                total = total + pun.puntos[i]
        promedio = total / 4
        pun.puntaje_final = promedio
        pickle.dump(pun, arLoPuntaje)
        arLoPuntaje.flush()
        print("Participante dado de alta con éxito")
        mostrarParticipantes(pun)
        rta = input("Desea seguir cargando pariticipantes (S / N): ").upper()
        while rta != "S" and rta != "N":
            rta = input("Por favor ingrese (S / N): ").upper()


def mostrarParticipantes(pun):
    global arLoPuntaje
    global arLoPuntaje
    global arLoPais
    paisPos = buscarPais(pun.codigo_pais)
    arLoPais.seek(paisPos, 0)
    pais = pickle.load(arLoPais)
    print("Nombre Participante:", pun.nomPartic, "  Nombre Pais:", pais.nombre.strip(), "  Categoria:",
          pun.categoria, "Puntaje Total", pun.puntaje_final)


def cargarParticipantes():
    global arFiPuntaje
    global arLoPuntaje
    global arFiPais
    if os.path.getsize(arFiPais) == 0:
        print("Primero debe dar de alta los paises")
        input("Precione una tecla para continuar")
    else:
        os.system("cls")
        print("INGRESO DE PARTICIPANTES \n")
        t = os.path.getsize(arFiPuntaje)
        if t == 0:
            print("Aun no hay participantes registrados")
        else:
            print("Lista de Participantes")
            print("--------------------------")
            arLoPuntaje.seek(0, 0)
            while arLoPuntaje.tell() < t:
                pun = pickle.load(arLoPuntaje)
                print(pun.codigo_pais)
                mostrarParticipantes(pun)
                print("-----------------------------------------------------------------")
        print()
        registrarPuntajes()





def armarPodio():
    global arFiPuntaje
    global arLoPuntaje
    global arLoPais
    ordenarPorPuntaje()
    cats = ["A", "B", "C", "D"]
    t = os.path.getsize(arFiPuntaje)
    for i in cats:
        arLoPuntaje.seek(0, 0)
        pun = pickle.load(arLoPuntaje)
        cont = 0
        while t > arLoPuntaje.tell() and cont < 3:
            if cont == 0 and pun.categoria == i:
                print(f"Medalla de oro en categoría {i}")
                cont = cont + 1
                mostrarParticipantes(pun)
                z = buscarPais(pun.codigo_pais)
                arLoPais.seek(z, 0)
                pais = pickle.load(arLoPais)
                pais.cantMedellas[0] = pais.cantMedellas[0] + 1
                arLoPais.seek(z, 0)
                pickle.dump(pais, arLoPais)
            elif cont == 1 and pun.categoria == i:
                print(f"Medalla de plata en categoría {i}")
                cont = cont + 1
                mostrarParticipantes(pun)
                z = buscarPais(pun.codigo_pais)
                arLoPais.seek(z, 0)
                pais = pickle.load(arLoPais)
                pais.cantMedellas[0] = pais.cantMedellas[0] + 1
                arLoPais.seek(z, 0)
                pickle.dump(pais, arLoPais)
            elif cont == 2 and pun.categoria == i:
                print(f"Medalla de bronce en categoría {i}")
                cont = cont + 1
                mostrarParticipantes(pun)
                z = buscarPais(pun.codigo_pais)
                arLoPais.seek(z, 0)
                pais = pickle.load(arLoPais)
                pais.cantMedellas[0] = pais.cantMedellas[0] + 1
                arLoPais.seek(z, 0)
                pickle.dump(pais, arLoPais)
            pun = pickle.load(arLoPuntaje)
    input("Tocar tecla para continuar...")





def mostrarMedallero():
    global arLoPais
    global arFiPais
    ordenarPorMedalla()
    t = os.path.getsize(arFiPais)
    arLoPais.seek(0, 0)
    while t > arLoPais.tell():
        pais = pickle.load(arLoPais)
        mostrarPaisCompleto(pais)
    input("Tecla para coninuar...")

def ejecutarCase(o):
    if o == 1:
        cargarParticipantes()
    if o == 2:
        armarPodio()
    if o == 3:
        mostrarMedallero()
    if o == 4:
        administrarPaises()
    if o == 0:
        salir()


def menu():
    mostrarOpciones()
    opcion = input("Ingresar opción deseada: ")
    while not validarIngresoEntero(opcion, 0, 9):
        opcion = input("Ingresar opción deseada: ")
    opcion = int(opcion)
    ejecutarCase(opcion)
    while opcion != 0:
        mostrarOpciones()
        opcion = input("Ingresar opción deseada: ")
        while not validarIngresoEntero(opcion, 0, 9):
            opcion = input("Ingresar opción deseada: ")
        opcion = int(opcion)
        ejecutarCase(opcion)

#Acá comienza el programa principal
global arFiPais
global arLoPais
global arFiPuntaje
global arLoPuntaje

validarExistArchivoPais()
validarExistArchivoPuntaje()

menu()

arLoPuntaje.close()
arLoPais.close()

