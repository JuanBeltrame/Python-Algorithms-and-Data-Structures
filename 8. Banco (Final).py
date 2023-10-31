#------------------- IMPORTAR LIBRERIAS ----------------------------------
import os
import pickle
import os.path

#----------------------- DEFINICION DE CLASES/REGISTROS ----------------------------------
class Cliente:
    def __init__(self):
        self.dni: 0
        self.ayn:"0"
        self.cbu:"0"

class Saldo:
    def __init__(self):
        self.cbu: 0
        self.clave: "0"
        self.saldo: "0"

#----------------------------------------------------------------------
def cerrarArchivo():
    aLc.close()
    aLs.close()
#----------------------------------------------------------------------
# Metodos del Menu
def mostrarUI():
    os.system("cls")
    print("----------------\n")
    print("1 - Identificate")
    print("2 - Consultas")
    print("3 - Movimientos")
    print("4 - Despedir al cliente")
    print("5 - Salir \n\n")

def validaRangoEntero(numero, desde, hasta):
    try:
        int(numero)
        if int(numero) >= desde and int(numero) <= hasta:
            return False
        else:
            return True
    except:
        return True

def menu():
    opc = -1
    while (opc != 5):
        os.system("cls")
        mostrarUI()
        opc = input("Ingrese una opcion entre 1 y 5")
        while validaRangoEntero(opc,1,5):
            opc = input("Incorrecto - Ingrese una opcion entre 1 y 5")
        opc = int(opc)
    if (opc == 1):
        indentificate()
    elif (opc == 2):
        consultas()
    elif (opc == 3):
        movimientos()
    elif (opc == 4):
        sale()
    elif (opc == 5):
        sale()        
#----------------------------------------------------------------------
# Metodos del Modulo Identificate
def BuscarDni(doc, v_rlc):
    bandera = False
    v_rlc = Cliente()
    limiteCli = os.path.getsize(aFc)
    aLc.seek(0, 0)
    
    while aLc.tell < limiteCli and bandera == False:
        punteroCli = aLc.tell
        v_rlc = pickle.load(aLC)
        
        if v_rlc.dni == doc:
            bandera = True
        else: 
            bandera = True

   
#def BuscarCBU():
  
    

def iden():
    dni = input("Ingresar DNI: ")
    if BuscarDni(dni,rLc):
        if BuscarCBU(cbu):
            MostrarCBU()
        else:
            Print("Error")
    else: 
        Print("El DNI no existe")




#----------------------------- PROGRAMA PRINCIPAL -----------------------------------------

aFc = "./Python/Archivos/Banco_Clientes.dat"
aFs = "./Python/Archivos/Banco_Saldo.dat"
if not os.path.exists(aFc):
    aLc = open(aFc, "w+b")
else:
    aLc = open(aFc, "r+b")
if not os.path.exists(aFs):
    aLs = open(aFs, "w+b")
else:
    aLs = open(aFs, "r+b")
rLc = Cliente()
rLS = Saldo()

menu()
cerrarArchivo()

