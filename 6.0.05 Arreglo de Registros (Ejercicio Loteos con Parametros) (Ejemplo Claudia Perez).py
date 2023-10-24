import os
#import pickle
import os.path
# se podria ir cerrando y abriendo archivos???
class Lote:
	def __init__(self):
		self.nl=" "
		self.m2=0
		self.pm2=0
		self.pagoc=0
		self.pagoa=0
		self.vend=" "   

class Cliente:
	def __init__(self):
		self.nl=" "
		self.nomc=" "
		self.fpago=0
		self.monto=0
"""class Lotes: 
	pass 
	def crearLotes (nro, metros, precio): 
		rlote.nrol = str.ljust(5, '0') # ajusto para que todos los registros sean de esa dimension
		rlote.m2 = 0                   # los reales son siempre de 8 bytes
		rlote.pm2 = 0 
"""
def buscodico(LOT):
	sup=4
	sup=sup - 1
	inf=0
	band=False
	while (band==False) and (inf < sup):
		med=(inf+sup) // 2
		if LOT[med].nl == nrolot:
			band=True
		else:
			if LOT[med].nl > nrolot:
				sup=med - 1
			else:
				inf=med + 1
	if LOT[med].nl == nrolot:
		resp=med
	else:
		resp=-1
	return resp

def Valor(LOT,r,p):
	V = LOT[r].m2*LOT[r].pm2*p
	return V

def Consulta(LOT):
	#global LOT
	montomax=float(input("Ingrese monto a consultar "))
	for i in range(4):
		if LOT[i].vend == "N" and Valor(LOT,i,1) <= montomax:
			print(LOT[i].nl," ",LOT[i].m2," ",Valor(LOT,i,1))
	
def Ventas(LOT,CLI):
	#global LOT
	#global CLI
	global k,nrolot
	nombre=input("Ingrese nombre cliente ")
	nrolot=input("Ingrese numero de lote ")
	
	forma=str(input("ingrese A nticipo - Contado "))
	while forma != "C" and forma != "A":
		forma=str(input("Error - ingrese A-nticipo - C-ontado "))
	pos=buscodico(LOT)
	if pos != -1:
		LOT[pos].vend="V"
		k=k+1
		CLI[k].nl=nrolot
		CLI[k].nomc=nombre
		CLI[k].fpago=forma
		if forma == "C":
			porc=LOT[pos].pagoc
		else:
			porc=LOT[pos].pagoa
			print("PASO ")
		print(Valor(LOT,pos,porc))
		m = Valor(LOT,pos,porc)
		CLI[k].monto= m
		print("Monto cliente ", CLI[k].monto," ","forma de pago: ",forma," ","porcentaje: ",porc)
		print("Venta exitosa !!")
	else:	
		print("No encontrado el Lote")
	tec=input("Apriete una tecla para continuar..")

def Listados(CLI):
	# global CLI
	sumamonto=0.00
	for t in range(4):
		print(CLI[t].nl," ",CLI[t].nomc," ",CLI[t].fpago," ",CLI[t].monto)
		sumamonto=sumamonto+CLI[t].monto
	print("El monto total recibido es: ", sumamonto)

def CargaLote(LOT):
    i= 0
    nrol=str(input("Ingrese numero de Lote: "))
    while i != 3 and nrol != "0":
    	LOT[i].nl = nrol
    	LOT[i].m2=float(input("Ingrese metros cuadrados "))
    	LOT[i].pm2=float(input("ingrese precio m2 "))
    	LOT[i].pagoc=float(input("Ingrese Pago Contado "))
    	LOT[i].pagoa=float(input("Ingrese Anticipo "))
    	LOT[i].vend=str(input("Vendido S o N "))
    	while LOT[i].vend !="S" and LOT[i].vend != "N":
    		LOT[i].vend=input("Error - Vendido S o N ")
    	i=i+1
    	print()
    	print()
    	nrol=str(input("Ingrese numero de Lote: "))

def Menu():
	os.system("cls")
	print("ABM LOTES \n")
	print("A - Carga de datos")
	print("C - Consultas")
	print("V - Ventas")
	print("L - Listados")
	print("S - Salir \n\n")




# programa principal
LOT=[None]*4
for c in range(4):
	LOT[c]=Lote()

CLI=[" "]*4
for j in range(4):
	CLI[j]=Cliente()


Menu()
global k,r
k=-1
opc=input("Ingrese opción deseada ")
while opc != "C" and opc != "V" and opc !="L" and opc !="S" and opc !="A":
	opc=input("Ingrese opción deseada ")
while opc != "S":
	if opc=="A":
		CargaLote(LOT)
	if opc == "C":
		Consulta(LOT)
	elif opc == "V":
		Ventas(LOT,CLI)
	elif opc == "L":
		Listados(CLI)
	tec=input("ing una tecla para continuar ")
	Menu()
	opc=input("Ingrese opcion deseada ")
	while opc != "C" and opc != "V" and opc !="L" and opc !="S" and opc!="A":
		opc=input("Ingrese opcion deseada ")	
		

