#------------------- IMPORTAR LIBRERIAS ----------------------------------
# Apertura de librerías de Python necesarias para la ejecución
import sys
import pickle
import os.path
import datetime

#----------------------- DEFINICION DE CLASES/REGISTROS ----------------------------------
# Definición de Registros (uno por cada archivo)
class rLotes:
	def __init__(self):
		self.nrol=0
		self.mm=" "
		self.ff=[0]*3
		self.Vp=[[0] * 7 for i in range(7)]       
	
class rModelo:
	def __init__(self):
		self.mod=" "
		self.coef=0.0

class rDescarte:
	def __init__(self):
		self.fd=[0]*3
		self.nl=0
		self.p=[0.00]*3
		self.Vr=0.00

#----------------------------- VALIDACIONES DATOS DE ENTRADA + FORMATEO -----------------------------------------
# funcion para validar el ingreso de una fecha válida (dia/mes/año correctos)
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

# Función que valida que se ingrese un entero positivo
def validaRangoEntero(nro, desde):
	try:              # trata de hacer lo que sigue, si da error se ejecuta el except
		int(nro)      
		if int(nro) >= desde:
			return False #validación correcta, retorna falso para que salga del while que valida
		else:
			return True  #validación incorrecta, retorna verdadero para que siga en el while que valida
	except:
		return True      #validación incorrecta, retorna verdadero para que siga en el while que valida

# Función que valida que se ingrese un numero Real (float)
def validaRangoReal(nro, desde):
	try:              # trata de hacer lo que sigue, si da error se ejecuta el except
		float(nro)    # para enteros cambiar float por int
		if float(nro) >= desde:
			return False #validación correcta, retorna falso para que salga del while que valida
		else:
			return True  #validación incorrecta, retorna verdadero para que siga en el while que valida
	except:
		return True      #validación incorrecta, retorna verdadero para que siga en el while que valida

#----------------------------- BUSQUEDAS Y ORDENAMIENTO -----------------------------------------
# Búsqueda secuencial sobre el archivo Lotes.dat
def buscarLote(nrolot):
	global aflote
	global aflot
	finlote=os.path.getsize(aflote)
	alot.seek(0,0)
	pos=-1
	while(alot.tell() < finlote):
		rl=pickle.load(alot)
		if (rl.nrol == nrolot):
			pos=alot.tell()
	return pos		

# Búsqueda dicotómica sobre Modelos.dat // el archivo está ordenado según enunciado
def dicotomica(model):
	if os.path.getsize(afmod)!= 0:
		amod.seek(0,0)
		m=pickle.load(amod)
		Tamregm=amod.tell()
		cantregm=int(os.path.getsize(afmod) / Tamregm)
		inf=0
		sup=cantregm-1
		medio=(inf+sup)//2
		amod.seek(medio*Tamregm,0)
		m=pickle.load(amod)
		while (inf < sup) and (m.mod != model):
			if model < m.mod:
				sup= medio -1
			else:
				inf=medio + 1
			medio=(inf + sup) // 2
			#f inf < sup:
			amod.seek(medio*Tamregm,0)
			m=pickle.load(amod)
		if m.mod == model:
			pos=m.coef
		else:
			pos=-1
	else:
		pos=-1
	return pos

# Ordenamiento del archivo modelos
# el programa no lo solicita pero debemos ordenarlo para probar la ejecucion
def ordeno():
	amod.seek(0,0)
	t=os.path.getsize(afmod)
	auxi=pickle.load(amod)
	Tamregm=amod.tell()
	cantreg=int(t/Tamregm)
	for i in range(0,cantreg-1):
		for j in range(i+1,cantreg):
			amod.seek(i*Tamregm,0)
			auxi=pickle.load(amod)
			amod.seek(j*Tamregm,0)
			auxj=pickle.load(amod)
			if auxi.mod > auxj.mod:
				amod.seek(i*Tamregm,0)
				pickle.dump(auxj,amod)
				amod.seek(j*Tamregm,0)
				pickle.dump(auxi,amod)
				amod.flush()

#----------------------------- INICIALIZAR -----------------------------------------
# inicializacion en cero, al arreglo Prom (acumulacion y calculo de promedios pedidos)
def inicializo(prome):
	for i in range(3):
		prome[i]=0.00

#----------------------------- CARGAS/ALTAS -----------------------------------------
# ingreso de datos(Alta)  al archivo Lotes.dat
# El enunciado lo informa como cargado, pero realizamos la creacion y carga del archivo para poder tener datos de prueba
def cargarLote():
	global alot
	global aflote
	
	l = rLotes()
	nro = input("Ingrese el nro de lote a dar de alta, [ 0 para Volver]: ")
	while ( validaRangoEntero(nro, 0)):
		nro = input ("Incorrecto. Ingrese una nro Lote valido [0 para Volver]: ")
	
	while nro != "0":
		nro = int(nro)
		if buscarLote(nro) == -1:
			l.nrol = nro

			l.mm = input("Ingrese Modelo: ")
			while len(l.mm) !=6:
				l.mm = input("Ingrese Modelo: ")
			while dicotomica(l.mm) == -1:
				l.mm = input("Ingrese Modelo cargado: ")
				while len(l.mm) !=6:
					l.mm = input("Ingrese Modelo: ")	
			print("Ingrese fecha como dd, mm y aa")

			fe=validarFecha()                                     # evalúa que sea una fecha valida
			dia,mes,anio=fe.split("/")                            # la separamos en 3 variables como indica el enunciado
			l.ff[0]=int(dia)
			l.ff[1]=int(mes)
			l.ff[2]=int(anio)
			
			for i in range(7):                                  
				for j in range(7):
					print("Ingrese valor de prueba",i," ",j)
					valor=float(input())
					while (validaRangoReal (valor, 0) ):
						valor= input ("Importe incorrecto. Ingrese importe > a 0")
					l.Vp[i][j] = float(valor)

			alot.seek(0,2)
			pickle.dump(l, alot)                            # Graba al final del archivo
			mostrarLote(l)
			alot.flush()                                    # borra el buffer interno del archivo
			print("Se dio de alta exitosamente el lote")
			#longregistro=sys.getsizeof(l.nrol)+sys.getsizeof(l.m2)+sys.getsizeof(l.pm2)
			#print(longregistro)
			input()
		else:
			print("Ya existe un lote con ese nro ", nro)
		nro = input("Ingrese el nro de lote a dar de alta [0 para Volver]: ")

# Alta en el archivo Lotes.dat
def altalote():
	global aflote                                             # las variables archivos las usamos globales
	global alot
	global l
	os.system("cls")
	print(" ALTA DE LOTES\n")
	t = os.path.getsize(aflote)
	if t==0:
		print ("No hay Lotes registrados")
		#rlote.seek(0,0)
	else:
		print ("Lista de Lotes")
		print ("----------------")
		alot.seek(0, 0)
		while alot.tell()<t:
			l = pickle.load(alot)
			mostrarLote(l)
	print()
	cargarLote()

# ingreso de datos(Alta)  al archivo Modelos.dat
# El enunciado lo informa como cargado, pero realizamos la creación y carga del archivo para poder tener datos de prueba 
def cargarmodelo():
	global amod
	global afmod
	global m
	m = rModelo()
	model = input("Ingrese el modelo de 6 caracteres a dar de alta, [ 0 para Volver]: ")
	
	while model != "0":
		while len(model) != 6:
			model = input("Ingrese el modelo de 6 caracteres a dar de alta, [ 0 para Volver]: ")

		#model=model.ljust(6,")
		c=dicotomica(model)
		if c == -1:
			m.coef = float(input("Ingrese coeficiente de referencia: "))
			amod.seek(0,2)
			m.mod = model
			m.mod=m.mod.ljust(6," ")
			pickle.dump(m, amod)                            # Graba al final del archivo
			mostrarmodelo(m)
			amod.flush()                                    # borra el buffer interno del archivo
			print("Se dio de alta exitosamente al modelo")
			input()
		else:
			print("Ya existe el modelo  ", model)
		model = input("Ingrese el modelo a dar de alta [0 para Volver]: ")
		#model=model.ljust(6,"")
		
# Alta en Modelos.dat
# Debemos cargar con infoemción el archivo para la ejecución de programa y prueba de los otros módulos
def altamodelo():
	global afmod
	global amod
	os.system("cls")
	print(" ALTA DE MODELOS\n")
	t = os.path.getsize(afmod)
	if t==0:
		print ("No hay modelos registrados")
	else:
		print ("Lista de modelos")                      # se muestra la información cargada para control y visualización
		print ("----------------")
		amod.seek(0, 0)
		while amod.tell()<t:
			m = pickle.load(amod)
			mostrarmodelo(m)
	print()
	cargarmodelo()

# armado de registro d en RAM, del archivo Descarte.dat, para su Alta
def armoregd(prome, c):
	global ades
	global d
	d = rDescarte()
	for i in range(3):
		d.fd[i]=l.ff[i]
	d.nl=l.nrol
	for i in range(3):
		d.p[i]=prome[i]
	d.vr=c
	print("Armado con exito")
	tec=input()
# Altas (ingreso de informacion) en archivo Descarte.dat
def altadescarte(c):
	global afdes, ades
	armoregd(prom,c)
	ades.seek(0,2)
	pickle.dump(d,ades)
	ades.flush()
	print("alta exitosa en descarte.dat")
	print(d.nl," ",d.vr)
	tec=input()

#----------------------------- BAJA LOGICA -----------------------------------------

#----------------------------- MODIFICAR/ACTUALIZAR un campo -----------------------------------------


#----------------------------- CALCULOS -----------------------------------------	
# Procedimiento que calcula los promedios pedidos en enunciado con los valores de prueba	
def calculoprom(prome,pos,fil,col):
	#for i in range(7):
	prome[pos]=prome[pos] + l.Vp[fil][col]
	
# función que determina si un lote es descartado, según condición dada en enunciado
def descarto(p,cf):
	return ((p[0] > cf) and (p[1] > cf)) or ((p[0] > cf) and (p[2] > cf)) or ((p[1] > cf) and (p[2] > cf)) 

# Realiza los calculos que se solicitan en enunciado para descartar los lotes, y armar el archivo descarte
def calculos():
	global prom
	finAlot=os.path.getsize(aflote)
	alot.seek(0,0)
	while alot.tell() < finAlot:
		l=pickle.load(alot)
		inicializo(prom)
		for k in range(7):
			calculoprom(prom,0,k,k)              # llamado al mismo procedimiento con parámetros para el cálculo de los promedios
			calculoprom(prom,1,2,k)
			calculoprom(prom,2,k,5)
		for j in range(3):
			prom[j]=prom[j]/7
		coeficiente=dicotomica(l.mm)
		if coeficiente != -1:
			if descarto(prom,coeficiente)==True:
				altadescarte(coeficiente)

#----------------------------- CONSULTA DE UN REGISTRO / LISTAR / MOSTRAR -----------------------------------------
def mostrarLote(lot): 
	print("Nro lote: ",lot.nrol,"  fecha:", lot.ff[0],"/",lot.ff[1],"/",lot.ff[2]," ","Modelo: ",lot.mm)

def mostrarmodelo(m): 
	print("Modelo: ", m.mod,"  Coeficiente: ", m.coef,)
	
# Litado solicitado, recorriendo el archivo de descarte.dat
def listado():
	os.system("cls")
	print(" LISTADO\n")
	print("\n\nFecha   Nro Lote   Prom1  Prom2   Prom3     Valor Referencia\n\n")
	
	find=os.path.getsize(afdes)
	ades.seek(0,0)
	while ades.tell() < find:
		d=pickle.load(ades)
		for i in range(3):
			print(d.fd[i], end="")
		print("  ",d.nl," ","{0:.2f}".format(d.p[0])," ","{0:.2f}".format(d.p[1]),"{0:.2f}".format(d.p[2])," ","{0:.2f}".format(d.vr))
	os.system("pause")

#----------------------------- PROGRAMA PRINCIPAL -----------------------------------------
global aflote, afmod, afdes                   # archivos
global alot, amod, ades   
global l, m, d, prom                               
l=rLotes()
m=rModelo()
d=rDescarte()                  # registros

#----------------------------- APERTURA DE ARCHIVOS -----------------------------------------
aflote = "c:\\ayed\\lotes.dat"  #nombre y ubicación física del archivo
if not os.path.exists(aflote):
	#print ("El archivo " + afAlumno + " NO existe")
	alot = open (aflote, "w+b")   #variable o nombre lógico de tipo archivo para escribir
else:
	#print ("El archivo " + afAlumno + " YA existe")
	alot = open (aflote, "r+b")   #variable o nombre lógico de tipo archivo para leer

afmod = "c:\\ayed\\modelos.dat"  #nombre y ubicación física del archivo
if not os.path.exists(afmod):
	#print ("El archivo " + afAlumno + " NO existe")
	amod = open (afmod, "w+b")   #variable o nombre lógico de tipo archivo para escribir
else:
	#print ("El archivo " + afAlumno + " YA existe")
	amod = open (afmod, "r+b")   #variable o nombre lógico de tipo archivo para leer

afdes = "c:\\ayed\\descarte.dat"  #nombre y ubicación física del archivo
if not os.path.exists(afdes):
	#print ("El archivo " + afAlumno + " NO existe")
	ades = open (afdes, "w+b")   #variable o nombre lógico de tipo archivo para escribir
else:
	#print ("El archivo " + afAlumno + " YA existe")
	ades=open(afdes,"r+b")

# declaracion del arreglo de promedios
prom=[0]*3

# Programa Principal: En este ejercicio, no se solicita Menu, los procesos se realizan en el orden Lógico pedido, en forma secuencial		
altamodelo()
ordeno()
altalote()

# Los anteriores procesos son necesarios para contar con datos de prueba para el resto de los procesos.
calculos()
listado()
print("\n\nGracias por visitarnos ...\n\n")

# Cierre al finalizar, de los 3 archivos utilizados
alot.close()
amod.close()
ades.close()



		
		
