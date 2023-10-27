#examen final del 26/02/2014 - Multas de tránsito
import os
import pickle
import os.path
import datetime
from datetime import date  
class Multa:
    def __init__(self):  # constructor dentro de la clase multa
        self.codigo = 0
        self.patente = " "  # 6
        self.dni = " "  # 9
        self.tipo = 0
        self.lugar = " "  # 30
        self.fecVto = " "  # 8
        self.grua = " "  # S/N
        self.fecPago = " "  # 8
        self.pagado = False

class Tipo:
    def __init__(self):  # constructor dentro de la clase Tipos de infracción
        self.tipo = 0
        self.descripción = " "  # no lo pide el enunciado pero es conveniente saber que infracción es.
        self.valor = 0.00



def validargrua():
    letra = input("Ingrese si fue acarreado con Grua -S si   N-no : ").upper()
    while (letra !='S') and (letra !='N') :
        letra = input("Incorrecto. Ingrese si fue acarreado con Grua -S si   N-no : ").upper()
    return letra
 
def validaRangoEntero(nro, min,max):
    try:              
        nro = int(nro)      
        if nro >= min and nro <= max:
            return False 
        else:
            return True  
    except:
        return True  
def validaRangoReales(nro, desde, hasta):
	try:              
		float(nro)      
		if float(nro) >= desde and float(nro) <= hasta:
			return False 
		else:
			return True  
	except:
		return True 

def validarFechaVto():
    flag = True
    while flag:
        try:
            fecha = input("Ingresa una fecha de Vencimiento con formato dd/mm/aa: ")
            datetime.datetime.strptime(fecha, '%d/%m/%y')
            print("fecha válida")
            flag = False
        except ValueError:
            print("fecha inválida")
    return fecha


def formatearMulta(vrMul):
	vrMul.codigo= str(vrMul.codigo)
	vrMul.codigo= vrMul.codigo.ljust(4, ' ')  
	vrMul.patente= vrMul.patente.ljust(6, ' ')     
	vrMul.dni = vrMul.dni.ljust(8, ' ')
	vrMul.tipo = str(vrMul.tipo)
	vrMul.tipo = vrMul.tipo.ljust(3,' ')
	vrMul.lugar = vrMul.lugar.ljust(30, ' ')
	vrMul.fecVto = str(vrMul.fecVto)
	vrMul.fecVto =vrMul.fecVto.ljust(10, ' ')
	#vrMul.grua = vrMul.grua.ljust(1) 
	vrMul.fecPago = vrMul.fecPago.ljust(10, ' ')
    #formatear un booleano

def FormatearTipos(vrTip): 
    vrTip.tipo= str(vrTip.tipo)
    vrTip.tipo= vrTip.tipo.ljust(3, ' ') 
    vrTip.descripción= vrTip.descripción.ljust(30, ' ')  
    vrTip.valor= str(vrTip.valor)
    vrTip.valor= vrTip.valor.ljust(10, ' ') 



def ordenaMultasxCodigo():  #ordena por campo codigo 
    global ArcFisiMul, ArcLogMul 
    ArcLogMul.seek (0, 0)
    aux = pickle.load(ArcLogMul)
    tamReg = ArcLogMul.tell() 
    tamArch = os.path.getsize(ArcFisiMul)
    cantReg = int(tamArch / tamReg)  
    for i in range(0, cantReg-1):
        for j in range (i+1, cantReg):
            ArcLogMul.seek (i*tamReg, 0)
            auxi = pickle.load(ArcLogMul)
            ArcLogMul.seek (j*tamReg, 0)
            auxj = pickle.load(ArcLogMul)
            if (int(auxi.codigo) > int(auxj.codigo)):
                ArcLogMul.seek (i*tamReg, 0)
                pickle.dump(auxj, ArcLogMul)
                ArcLogMul.seek (j*tamReg, 0)
                pickle.dump(auxi, ArcLogMul)
                ArcLogMul.flush()

def BuscaDico(Cod):
    global ArcFisiMul, ArcLogMul
    RegMul = Multa()
    t = os.path.getsize(ArcFisiMul)
    if t > 0:
        ArcLogMul.seek(0, 0)
        RegMul = pickle.load(ArcLogMul)
        tamReg = ArcLogMul.tell()
        cantReg = int(os.path.getsize(ArcFisiMul) / tamReg)
        inferior = 0
        superior = cantReg - 1
        medio = inferior + superior // 2
        ArcLogMul.seek(medio * tamReg, 0)
        RegMul = pickle.load(ArcLogMul)
        while int(RegMul.codigo) != Cod and (inferior < superior):
            if int(Cod) < int(RegMul.codigo):
                superior = medio - 1
            else:
                inferior = medio + 1
            medio = (inferior + superior) // 2
            ArcLogMul.seek(medio * tamReg, 0)
            RegMul = pickle.load(ArcLogMul)
        if int(RegMul.codigo) == Cod:
            return medio * tamReg
        else:
            return -1
    else:
        print('-----------------')
        print("Archivo sin datos")
        print('-----------------')
        input()
        return -1

        
def ingresa(cod,vrMul):
		vrMul.codigo = int(cod)
		vrMul.patente = input("Patente: ")
		while len(vrMul.patente)<1 or len(vrMul.patente)>7:
			vrMul.patente = input("Incorrecto - Patente <hasta 7 caracteres>: ")
		vrMul.dni = input("dni <hasta 9 caracteres>: ")
		while len(vrMul.dni)<1 or len(vrMul.dni)>9:
			vrMul.dni = input("Incorrecto - dni <hasta 9 caracteres>: ")
		ArcLogTip.seek(0,0)
		aux=pickle.load(ArcLogTip)
		tamReg= ArcLogTip.tell()
		tamArch= os.path.getsize(ArcFisiTip)
		cantReg= tamArch// tamReg
		vrMul.tipo=input("Ingrese Número de tipo de Infracción: ")
		while validaRangoEntero(vrMul.tipo, 1, cantReg):
			print(" incorrecto...el numero debe ser menos o igual a ", cantReg)
			vrMul.tipo= input()#"incorrecto...ingrese nuevamente:  ")
		vrMul.lugar = input("Lugar de la Infracción: ")
		while len(vrMul.lugar)<1 or len(vrMul.lugar)>30:
			vrMul.lugar = input("Incorrecto - lugar <hasta 30 caracteres>: ")
		fv= validarFechaVto()
		vrMul.fecVto= fv
		vrMul.grua = validargrua()
		vrMul.pagado= False

def CargaMulta():
	global ArcFisiMul, ArcLogMul
	os.system("cls")
	RegMul= Multa()
	print("OPCION 2 - Carga de Multas")
	print("----------------------------\n")
	cod = input("Ingrese el codigo de la multa entre 1 y 9999 [0- para Volver]: ")
	while validaRangoEntero(cod, 0, 9999):
		cod = input("Incorrecto - Entre 1 y 9999 [0 para Volver]: ")
	while int(cod) != 0:
		if BuscaDico(int(cod)) == -1:
			ingresa(cod,RegMul)
			formatearMulta(RegMul)
			ArcLogMul.seek(0,2)
			pickle.dump(RegMul, ArcLogMul)
			print("-----------------------")
			print("Alta de Multa exitosa")
			print("------------------------")
			ArcLogMul.flush()
			ordenaMultasxCodigo()
			print("--------ORDENADO-----------------------")
			ArcLogMul.seek(0, 0)
			RegMul = Multa()
			t = os.path.getsize(ArcFisiMul)
			while ArcLogMul.tell()<t:
				RegMul = pickle.load(ArcLogMul)
				print(RegMul.codigo,"  ",RegMul.dni, "  ", RegMul.patente, " ", RegMul.tipo," ",RegMul.fecVto)
			os.system ("pause")	

		else:
			print("Ya existe Multa con ese codigo, ingrese nuevamente..")
			os.system("pause")

		cod = input("Ingrese el codigo de multa a dar de alta, entre 1 y 9999 [0 para Volver]: ")
		while validaRangoEntero(cod, 0, 9999):
			cod = input("Incorrecto - Entre 0 y 9999 [0 para Volver]: ")

def CargaTipos():
	global ArcFisiTip, ArcLogTip
	os.system("cls")
	print("OPCION 1 - Carga de Tipos de infracción ")
	print("-----------------------------------------\n")
	RegTip=Tipo()
	rta= input("desea ingresar una nueva infracción a ser juzgada por la municipalidad? S-si   N-no: ").upper()
	while rta != "S" and rta != "N":
		rta = input("Por favor, solo S para Si o N para No:").upper()
	while rta=='S':
		#hay que ir a buscar el último codigo y suamrle 1!!! pero ademas verificar que no exista!!
		ArcLogTip.seek (0, 0)
		t= os.path.getsize(ArcFisiTip)
		print("tamaño del archivo:", t)
		if t==0:  # si el archivo esta vacío iniciar con el primer tipo de infracción en 1
			RegTip.tipo=1
		else:
			ArcLogTip.seek(0,0)
			RegTip = pickle.load(ArcLogTip)
			tamReg = ArcLogTip.tell()
			cantReg= t//tamReg
			print("Cantidad de registros:", cantReg)
			ArcLogTip.seek ((cantReg-1)*tamReg,0)
			puntero=ArcLogTip.tell()
			print("puntero tell:",puntero) 
			aux = pickle.load(ArcLogTip)
			ultimo= int(aux.tipo)
			RegTip.tipo= ultimo +1
		RegTip.descripción= str(input("ingrese descripción de la Infracción hasta 30 caracteres: "))
		RegTip.valor=input("valor de la infracción <entre 1000 y 300000> $: ")
		while validaRangoReales(RegTip.valor, 1000, 300000):
			RegTip.valor = input("Incorrecto - valor válido entre 1000 y 300000  $: ")
		RegTip.valor = float(RegTip.valor)
		print (" ....registro a Cargar......")
		print("Tipo: ", RegTip.tipo)
		print("Descripción: ", RegTip.descripción)
		print("Valor: ", RegTip.valor)
		print ("------------------------------")
		graba= input("confirma el Ata? S-Si   N-no: ").upper()
		while graba != "S" and graba != "N":
			graba = input("Por favor, solo S para Si o N para No:").upper()
		if graba=='S':
			FormatearTipos(RegTip)
			ArcLogTip.seek(0,2)
			pickle.dump(RegTip, ArcLogTip)
			print("----------------------------------")
			print("Alta de tipo de Infracción exitosa")
			print("-----------------------------------")
			ArcLogTip.flush()
		
		rta= input("desea ingresar una nueva infracción a ser juzgada por la municipalidad? S-si   N-no: ").upper()
		while rta != "S" and rta != "N":
			rta = input("Por favor, solo S para Si o N para No:").upper()


def Calculo(ti,gr):
	global ArcFisiTip, ArcLogTip
	aux=Tipo()
	ArcLogTip.seek(0,0)
	aux=pickle.load(ArcLogTip)
	tamReg= ArcLogTip.tell()
	posic= int(ti)-1
	ArcLogTip.seek(posic*tamReg,0)
	aux=pickle.load(ArcLogTip)
	if gr=="S":
		return float(aux.valor)*1.1
	else:
		return float(aux.valor)

def Proceso(dp):
	global ArcFisiTip, ArcLogTip
	global ArcFisiMul, ArcLogMul
	RegMul= Multa()
	rt= Tipo()
	total=0.0
	ArcLogMul.seek (0, 0)
	t=os.path.getsize(ArcFisiMul)
	while ArcLogMul.tell() < t:
		RegMul= pickle.load(ArcLogMul)
		if (RegMul.dni == str(dp) or RegMul.patente== str(dp) )and RegMul.pagado== False:
			apagar = Calculo(RegMul.tipo, RegMul.grua)
			total= total+ apagar
			print(RegMul.tipo,"... ",RegMul.dni,"... ", RegMul.patente," ...",RegMul.fecVto,"...  ",RegMul.grua)
			
	print("Ud. debe abonar un total de $ ",total)
	input()

def Consulta():
	global ArcFisiMul, ArcLogMul
	global ArcFisiTip, ArcLogTip
	os.system("cls")
	print("OPCION 3 - CONSULTA ")
	print("----------------------------\n")
	
	rta= input("desea Consulta por DNI ó por PATENTE? ingrese D ó P: ").upper()
	while rta != "D" and rta != "P":
		rta = input("Por favor, ingrese D-Dni ó P-Patente:").upper()
	if rta=='D':
		doc= input("Ingrese numero de Dni hasta 8 caracteres: ")
		while len(doc)<1 or len(doc)>8:
			doc = input("Incorrecto - dni <hasta 8 caracteres>: ")
		Proceso(doc)
	else:
		pat= input("Ingrese numero de Patente hasta 6 caracteres: ")
		while len(pat)<1 or len(pat)>6:
			pat = input("Incorrecto - patente  <hasta 6 caracteres>: ")
		Proceso(pat)

def Pagos():
	global ArcFisiMul, ArcLogMul
	global ArcFisiTip, ArcLogTip
	RegMul=Multa()
	os.system("cls")
	print("OPCION 4 - PAGOS")
	print("----------------------------\n")
	cod = input("Ingrese el codigo de MULTA entre 1 y 9999 : ")
	while validaRangoEntero(cod, 1, 9999):
		cod = input("Incorrecto - Entre 1 y 9999 : ")
	Pos=BuscaDico(int(cod))
	if Pos == -1:
		print("-------------------------------------------")
		print(" el código de MULTA ingresado NO EXISTE")
		print("-------------------------------------------")
	else:
		ArcLogMul.seek(Pos,0)
		RegMul=pickle.load(ArcLogMul) 
		if RegMul.pagado== False:
			print ("regmultipo:", RegMul.tipo)
			print(" regmulgrua:", RegMul.grua)
			apagar=Calculo(RegMul.tipo, RegMul.grua)
			print( RegMul.tipo," ",RegMul.dni,"///  ", RegMul.patente,"  ",RegMul.fecVto,"  ",RegMul.grua)
			print("Monto a abonar: $",apagar)
			#input()
			rtapaga= input("Confirma el pago de la multa? S-si N-no: ").upper()
			while rtapaga != "S" and rtapaga != "N":
				rtapaga = input("Por favor, ingrese S-si ó N-no: ").upper()
			if rtapaga=='S':
				RegMul.fecPago= datetime.datetime.now().strftime("%x")
				#RegMul.fecPago= str(date.today())
				RegMul.pagado= True
				formatearMulta(RegMul)
				ArcLogMul.seek(Pos,0)
				pickle.dump(RegMul,ArcLogMul)
				ArcLogMul.flush()
				print(" Pago exitoso!")
		else:
			print(" la multa ya está paga!!")

def Listado():
	global ArcFisiMul, ArcLogMul
	global ArcFisiTip, ArcLogTip
	total=0
	aux=Tipo()
	os.system("cls")
	ArcLogTip.seek(0,0)
	aux=pickle.load(ArcLogTip)
	tamReg= ArcLogTip.tell()
	tamArch= os.path.getsize(ArcFisiTip)
	cantReg= tamArch// tamReg
	ti=input("Ingrese Número de tipo de Infracción: ")
	while validaRangoEntero(ti, 1, cantReg):
		print(" incorrecto...el numero debe ser menos o igual a ", cantReg)
		ti= input()#"incorrecto...ingrese nuevamente:  ")
	print("-------------Listado por tipo de Infracción---------------")
	print(" Codigo  Dni   Patente   Acarreo   fecha de vencimiento ")
	print("----------------------------------------------------------")
	ArcLogMul.seek(0, 0)
	RegMul = Multa()
	t = os.path.getsize(ArcFisiMul)
	while ArcLogMul.tell()<t:
		RegMul = pickle.load(ArcLogMul)
		if int(RegMul.tipo)== int(ti)and RegMul.pagado==False:
			total=total + Calculo(ti, RegMul.grua)
			print (RegMul.codigo," ", RegMul.dni,"  ", RegMul.patente,"  ",RegMul.fecVto,"  ",RegMul.grua)
	print("Se deberá recaudar por tipo",ti," de multas impagas Un total de $", total)
	os.system ("pause")

def ListadoTipos():
	global ArcFisiTip, ArcLogTip
	os.system("cls")
	print("OPCION 6 - Listado de Tipos de Infracción")
	print("------------------------------------------\n")
	print("tipo infracción    descripción    valor ")
	print("------------------------------------------\n")
	ArcLogTip.seek(0, 0)
	RegTip = Tipo()
	t = os.path.getsize(ArcFisiTip)
	while ArcLogTip.tell()<t:
		RegTip = pickle.load(ArcLogTip)
		print(RegTip.tipo,"  ",RegTip.descripción," ",RegTip.valor )

def ListadoMultas():
	global ArcFisiMul, ArcLogMul
	os.system("cls")
	print("OPCION 7 - Listado de Multas")
	print("---------------------------------------------------------------\n")
	print("codigo   Tipo     Dni    patente   vencimiento  acarreo  fecha pago ")
	print("---------------------------------------------------------------\n")
	ArcLogMul.seek(0, 0)
	RegMul = Multa()
	t = os.path.getsize(ArcFisiMul)
	while ArcLogMul.tell()<t:
		RegMul = pickle.load(ArcLogMul)
		print(RegMul.codigo,"  ",RegMul.tipo,"  ",RegMul.dni," ",RegMul.patente," ",RegMul.fecVto," ",RegMul.grua," ",RegMul.fecPago )
	input()

def pantalla():
    print('Menu de opciones');
    print('-----------------');
    print()
    print('1-Carga Tipos de Infracción')
    print('2-Carga Multas')
    print('3-Consulta X Dni ó X Patente')
    print('4-Pagos')
    print('5-Listado')
    print('6-Listado de tipos de Infracción')
    print('7-Listado de todas las multas cargadas')
    print('8-Salir')
    print()


### Programa Principal ###
ArcFisiMul = "D:\\AEDD\\multas.dat"  
ArcFisiTip = "D:\\AEDD\\tipos.dat"
if not os.path.exists(ArcFisiMul):   
    ArcLogMul = open(ArcFisiMul, "w+b")   
else:
    ArcLogMul = open(ArcFisiMul, "r+b")   

if not os.path.exists(ArcFisiTip):   
    ArcLogTip = open(ArcFisiTip, "w+b")   
else:
    ArcLogTip = open(ArcFisiTip, "r+b")  
opc = -1

while (opc != 8):
    os.system("cls")
    pantalla()
    opc = input("Ingrese opcion <1 a 8>: ")
    while (validaRangoEntero(opc, 1, 8)):
        opc = input("Incorrecto. Ingrese opcion <1 a 7>: ")
    opc = int(opc)
    if (opc == 1):
        CargaTipos()
    elif (opc == 2):
        CargaMulta()
    elif (opc == 3):
        Consulta()
    elif (opc == 4):
        Pagos()
    elif (opc == 5):
        Listado()   
    elif (opc == 6):
        ListadoTipos()
    elif (opc == 7):
        ListadoMultas()    
    elif (opc == 8):
        ArcLogMul.close()
        ArcLogTip.close()    
        print("\n\n archivos cerrados ..Fin del programa!!")
print("\n\n CHAU!!!!")
input()
