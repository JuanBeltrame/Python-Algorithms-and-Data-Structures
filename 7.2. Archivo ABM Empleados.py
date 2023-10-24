import os
import pickle
import os.path

class Empleado:
    def __init__(self):
        self.legajo = 0
        self.nomyape = ""
        self.sueldo = 0.00
        self.estado = "A"  # "A" activo o "B" baja

def busquedaDico(L):  # método de búsqueda dicotómica con una sola lectura en el mientras
    # antes de llamar a la búsqueda dicotomica se debe validar que el archivo tenga registros
    # sino hay que hacerlo al comienzo de la DICO para que no de error el primer load para medir
    # el tamaño del registro
    global afEmpleados, alEmpleados
    aux = Empleado()
    alEmpleados.seek(0, 0)
    aux = pickle.load(alEmpleados)
    tamReg = alEmpleados.tell()
    cantReg = os.path.getsize(afEmpleados) // tamReg
    desde = 0
    hasta = cantReg - 1
    encontrado = False
    while not encontrado and desde <= hasta:
        medio = (desde + hasta) // 2
        alEmpleados.seek(medio * tamReg, 0)
        vrEmp = pickle.load(alEmpleados)
        if int(vrEmp.legajo) == L:
            encontrado = True
        else:
            if L < int(vrEmp.legajo):
                hasta = medio - 1
            else:
                desde = medio + 1

    if int(vrEmp.legajo) == L:
        return medio * tamReg
    else:
        return -1

"""
def busquedaDico(L):
    # Método de búsqueda dicotómica
    global afEmpleados, alEmpleados 
    alEmpleados.seek(0, 0)
    aux = pickle.load(alEmpleados)
    tamReg = alEmpleados.tell()
    cantReg = int(os.path.getsize(afEmpleados) / tamReg)
    desde = 0
    hasta = cantReg - 1
    medio = (desde + hasta) // 2
    alEmpleados.seek(medio * tamReg, 0)
    vrEmp = pickle.load(alEmpleados)
    
    while int(vrEmp.legajo) != L and desde < hasta:
        if L < int(vrEmp.legajo):
            hasta = medio - 1
        else:
            desde = medio + 1
        medio = (desde + hasta) // 2
        alEmpleados.seek(medio * tamReg, 0)
        vrEmp = pickle.load(alEmpleados)
    
    if int(vrEmp.legajo) == L:
        return medio * tamReg
    else:
        return -1
"""

def ordenaEmpleados():  # método ordenamiento falso burbuja
    global afEmpleados, alEmpleados
    alEmpleados.seek(0, 0)
    aux = pickle.load(alEmpleados)
    tamReg = alEmpleados.tell()
    tamArch = os.path.getsize(afEmpleados)
    cantReg = int(tamArch / tamReg)
    for i in range(0, cantReg - 1):
        for j in range(i + 1, cantReg):
            alEmpleados.seek(i * tamReg, 0)
            auxi = pickle.load(alEmpleados)
            alEmpleados.seek(j * tamReg, 0)
            auxj = pickle.load(alEmpleados)
            if (auxi.legajo > auxj.legajo):
                alEmpleados.seek(i * tamReg, 0)
                pickle.dump(auxj, alEmpleados)
                alEmpleados.seek(j * tamReg, 0)
                pickle.dump(auxi, alEmpleados)
                alEmpleados.flush()

def listarEmpleadosActivos():
    global alEmpleados, afEmpleados
    os.system("cls")
    print("OPCION 4 - Lista de Empleados Activos")
    print("-------------------------------------\n")
    t = os.path.getsize(afEmpleados)
    if t == 0:
        print("No hay Empleados registrados")
    else:
        ordenaEmpleados()
        encabezado = ''
        encabezado = encabezado + '{:<15}'.format("Legajo")
        encabezado = encabezado + '{:<40}'.format("Nombre y Apellido")
        encabezado = encabezado + '{:<20}'.format("Sueldo")
        encabezado = encabezado + '{:<10}'.format("Estado")
        print(encabezado)
        print("---------------------------------------------------------------------------------")
        emp = Empleado()
        alEmpleados.seek(0, 0)
        while alEmpleados.tell() < t:
            emp = pickle.load(alEmpleados)
            if emp.estado == "A":
                mostrarEmpleado(emp)
        print()
        leg = input("Ingrese el legajo a buscar, entre 1 y 99999 [0 para Volver]: ")
        while validaRangoEnteros(leg, 0, 99999):
            leg = input("Incorrecto - Entre 1 y 99999 [0 para Volver]: ")
        leg = int(leg)
        if leg != 0:
            if busquedaDico(leg) == -1:
                print("Legajo no Encontrado")
            else:
                print("Legajo Encontrado")
    os.system("pause")

def bajaEmpleado():
    global afEmpleados, alEmpleados
    os.system("cls")
    print("OPCION 3 - Baja de un Empleado")
    print("------------------------------\n")
    t = os.path.getsize(afEmpleados)
    if t == 0:
        print("No hay Empleados registrados\n")
        os.system("pause")
    else:
        leg = input("Ingrese el legajo del empleado a dar de baja, entre 1 y 99999 [0 para Volver]: ")
        while validaRangoEnteros(leg, 0, 99999):
            leg = input("Incorrecto - Entre 1 y 99999 [0 para Volver]: ")
        leg = int(leg)
        if leg != 0:
            emp = Empleado()
            pos = buscarEmpleado(leg, emp)
            if pos == -1:
                print("El legajo del empleado no existe")
            else:
                if emp.estado == "B":
                    print("El empleado ya está dado de baja")
                else:
                    print("Datos del empleado a dar de baja:")
                    mostrarEmpleado(emp)
                    rpta = input("Confirma la baja? (Si o No): ")
                    while rpta.lower() != "si" and rpta.lower() != "no":
                        rpta = input("Incorrecto - Confirma? (Si o No): ")
                    if rpta.lower() == "si":
                        emp.estado = "B"
                        alEmpleados.seek(pos, 0)
                        pickle.dump(emp, alEmpleados)
                        alEmpleados.flush()
                        print("Baja lógica exitosa")
                        print("Los datos actualizados del empleado son:")
                        mostrarEmpleado(emp)
    os.system("pause")

def mostrarEmpleado(vrEmp):
    salida = ''
    salida = salida + '{:<15}'.format(vrEmp.legajo.strip())
    salida = salida + '{:<40}'.format(vrEmp.nomyape.strip())
    salida = salida + '{:<20}'.format(vrEmp.sueldo.strip())
    salida = salida + '{:<10}'.format(vrEmp.estado.strip())
    print(salida)

def formatearEmpleado(vrEmp):
    vrEmp.legajo = str(vrEmp.legajo)
    vrEmp.legajo = vrEmp.legajo.ljust(10, ' ')
    vrEmp.nomyape = vrEmp.nomyape.ljust(40, ' ')
    vrEmp.sueldo = str(vrEmp.sueldo)
    vrEmp.sueldo = vrEmp.sueldo.ljust(10, ' ')
    # el estado no lo formateo porque es un char y se asignan valores fijos por programa y 
    # de la misma longitud: "A" o "B"

def modificarEmpleado():
    global afEmpleados, alEmpleados
    os.system("cls")
    print("OPCION 2 - Modificación de un Empleado")
    print("--------------------------------------\n")
    t = os.path.getsize(afEmpleados)
    if t == 0:
        print("No hay Empleados registrados\n")
        os.system("pause")
    else:
        leg = input("Ingrese el legajo del empleado a modificar, entre 1 y 99999 [0 para Volver]: ")
        while validaRangoEnteros(leg, 0, 99999):
            leg = input("Incorrecto - Entre 1 y 99999 [0 para Volver]: ")
        leg = int(leg)
        if leg != 0:
            emp = Empleado()
            pos = buscarEmpleado(leg, emp)
            if pos == -1:
                print("El legajo del empleado no existe")
            else:
                if emp.estado == "B":
                    print("El empleado está dado de baja (no es posible modificar sus datos)")
                else:
                    print("Empleado a modificar:")
                    mostrarEmpleado(emp)
                    print("\n Solo se podrán modificar el nombre y apellido y su sueldo \n")
                    
                    emp.nomyape = input("Nuevo nombre y apellido <hasta 40 caracteres>: ")
                    while len(emp.nomyape) < 1 or len(emp.nomyape) > 40:
                        emp.nomyape = input("Incorrecto - Nombre y apellido <hasta 40 caracteres>: ")
                    
                    emp.sueldo = input("Nuevo sueldo <entre 100000 y 300000>: ")
                    while validaRangoReales(emp.sueldo, 100000, 300000):
                        emp.sueldo = input("Incorrecto - sueldo válido entre 100000 y 300000: ")
                    emp.sueldo = float(emp.sueldo)
                    
                    rpta = input("Confirma? (Si o No): ") 
                    while rpta.lower() != "si" and rpta.lower() != "no":
                        rpta = input("Incorrecto - Confirma? (Si o No): ")
                    if rpta.lower() == "si":
                        alEmpleados.seek(pos, 0)
                        formatearEmpleado(emp)
                        pickle.dump(emp, alEmpleados)
                        alEmpleados.flush()
                        print("Modificación exitosa")
                        print("Los datos actualizados del empleado son:")
                        mostrarEmpleado(emp)
            os.system("pause")

def buscarEmpleado(leg, vr):
    global afEmpleados, alEmpleados
    t = os.path.getsize(afEmpleados)
    alEmpleados.seek(0, 0)
    vrTemp = Empleado()
    encontrado = False
    while alEmpleados.tell() < t and not encontrado:
        pos = alEmpleados.tell()
        vrTemp = pickle.load(alEmpleados)
        if int(vrTemp.legajo) == leg:
            encontrado = True
    if encontrado:
        vr.legajo = vrTemp.legajo
        vr.nomyape = vrTemp.nomyape
        vr.sueldo = vrTemp.sueldo
        vr.estado = vrTemp.estado
        return pos
    else:
        return -1

def altaEmpleado():
    global afEmpleados, alEmpleados
    emp = Empleado()
    os.system("cls")
    print("OPCION 1 - Alta de Empleados")
    print("----------------------------\n")
    t = os.path.getsize(afEmpleados)
    if t == 0:
        print("No hay Empleados registrados")
    else:
        print("Lista de Empleados")
        print("------------------")
        alEmpleados.seek(0)
        while alEmpleados.tell() < t:
            emp = pickle.load(alEmpleados)
            mostrarEmpleado(emp)
            print()
    leg = input("Ingrese el legajo del empleado a dar de alta, entre 1 y 99999 [0 para Volver]: ")
    while validaRangoEnteros(leg, 0, 99999):
        leg = input("Incorrecto - Entre 1 y 99999 [0 para Volver]: ")
    leg = int(leg)
    while leg != 0:
        if buscarEmpleado(leg, emp) == -1:
            emp.legajo = leg
            emp.nomyape = input("Nombre y Apellido <hasta 40 caracteres>: ")
            while len(emp.nomyape) < 1 or len(emp.nomyape) > 40:
                emp.nomyape = input("Incorrecto - Nombre y Apellido <hasta 40 caracteres>: ")
            emp.sueldo = input("Sueldo <entre 100000 y 300000>: ")
            while validaRangoReales(emp.sueldo, 100000, 300000):
                emp.sueldo = input("Incorrecto - sueldo válido entre 100000 y 300000: ")
            emp.sueldo = float(emp.sueldo)
            formatearEmpleado(emp)
            pickle.dump(emp, alEmpleados)
            alEmpleados.flush()
            print("Alta de empleado exitosa\n")
        else:
            print("El empleado ya existe. Sus datos son:")
            mostrarEmpleado(emp)
        os.system("pause")
        leg = input("Ingrese el legajo del empleado a dar de alta, entre 1 y 99999 [0 para Volver]: ")
        while validaRangoEnteros(leg, 0, 99999):
            leg = input("Incorrecto - Entre 1 y 99999 [0 para Volver]: ")
        leg = int(leg)

def validaRangoReales(nro, desde, hasta):
    try:
        float(nro)
        if float(nro) >= desde and float(nro) <= hasta:
            return False
        else:
            return True
    except:
        return True

def validaRangoEnteros(nro, desde, hasta):
    try:
        int(nro)
        if int(nro) >= desde and int(nro) <= hasta:
            return False
        else:
            return True
    except:
        return True

def mostrarMenu():
    os.system("cls")
    print("ABM de EMPLEADOS")
    print("----------------\n")
    print("1 - Alta de Empleados")
    print("2 - Modificación de un Empleado")
    print("3 - Baja de un Empleado")
    print("4 - Listado de Empleados Activos")
    print("0 - Salir \n\n")

### Programa principal ###
afEmpleados = "./Python/Archivos/Empleados.dat"
if not os.path.exists(afEmpleados):
    alEmpleados = open(afEmpleados, "w+b")
else:
    alEmpleados = open(afEmpleados, "r+b")
opc = -1
while opc != 0:
    mostrarMenu()
    opc = input("Ingrese opción [0-4]: ")
    while validaRangoEnteros(opc, 0, 4):
        opc = input("Incorrecto - Ingrese opción [0-4]: ")
    opc = int(opc)
    if opc == 1:
        altaEmpleado()
    elif opc == 2:
        modificarEmpleado()
    elif opc == 3:
        bajaEmpleado()
    elif opc == 4:
        listarEmpleadosActivos()
    else:
        print("\n\nGracias por visitarnos ...\n\n")
        alEmpleados.close()



