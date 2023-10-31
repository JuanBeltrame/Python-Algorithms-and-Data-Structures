#------------------- IMPORTAR LIBRERIAS ----------------------------------
#Este programa es para realizar todos los que se piden en el final del hotsale considerando que
#los datos en los archivos de base ya están previamente cargados, empresas y productos.

from io import *  	#modulo que permite trabajar con el sistema de archivos
import pickle 		#librería para as operaciones de lectura y escritura
import os,sys, datetime
from datetime import date

#----------------------- DEFINICION DE CLASES/REGISTROS ----------------------------------
class empresa(): 	#Declarar el registro empresa
	def __init__(self):
		self.code=0
		self.nome=" "
		self.cantidad=0

class producto():
	def __init__(self): 
		self.codp=0
		self.descp=" "
		self.stock = 0
		self.precioReal = 0.00
		self.precioLiq = 0.00
		self. codep = 0

#----------------------------- VALIDACIONES DATOS DE ENTRADA + FORMATEO -----------------------------------------
def validarFecha():
    flag = True
    while flag:
        try:
            fecha = input("Ingresa una fecha en el formato aaaa-mm-dd: ")
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
            print("Fecha valida")
            flag = False 
        except ValueError:
            print("Fecha invalida")
    tec=input()
    return fecha	

def fechavalida(f):
	if f <= str(date.today()):
		return True
	else:
		return False

def validaRangoEntero(nro, desde, hasta):
	try:              # trata de hacer lo que sigue, si da error se ejecuta el except
		int(nro)      
		if int(nro) >= desde and int(nro) <= hasta:
			return False #validación correcta, retorna falso para que salga del while que valida
		else:
			return True  #validación incorrecta, retorna verdadero para que siga en el while que valida
	except:
		return True      #

#----------------------------- BUSQUEDAS Y ORDENAMIENTO ----------------------------------------- 
def busece(CodEmp):
	global aemp
	global afemp
	finemp=os.path.getsize(afemp)
	aemp.seek(0,0)
	pos=-1
	e=aemp.tell()
	re=pickle.load(aemp)
	while(aemp.tell() < finemp) and (re.code!=CodEmp):
		e=aemp.tell()
		re=pickle.load(aemp)
	if (re.code == CodEmp):
		pos=e    #aemp.tell()
	else:
		pos=-1
	return pos	

def busecp(CodProd):
	global aprod
	global afprod
	finprod=os.path.getsize(afprod)
	aprod.seek(0,0)
	pos=-1
	p=aprod.tell()
	rp=pickle.load(aprod)

	while(aprod.tell() < finprod) and (rp.codp != CodProd):
		p=aprod.tell()
		rp=pickle.load(aprod)
	if (rp.codp == CodProd):
		pos=p
	else:
		pos=-1
	return pos		

#----------------------------- INICIALIZAR -----------------------------------------

#----------------------------- CARGAS/ALTAS -----------------------------------------
def muestrop(pr):
	if pr.stock==0:
		print(pr.codp," ",pr.descp," ",pr.precio," ",pr.precioLiq)
		print(" ")

def listadostockcero():
	finprod=os.path.getsize(afprod)
	if finprod==0:
		print("No hay productos a mostrar")
		os.system("pause")
	else:
		print("Listado de productos con stock cero ")
		print("")
		aprod.seek(0,0)
		while aprod.tell() < finprod:
			rp=pickle.load(aprod)
			muestrop(rp)
	os.system("pause")

def mayempresa():
	global aemp
	global afemp
	fine=os.path.getsize(afemp)
	if fine == 0:
		print(" no hay datos")
	else:
		aemp.seek(0,0)
		
		mayemp=" "
		maycant=0
		re=pickle.load(aemp)
		while aemp.tell() < fine:
			#re=pickle.load(aemp)
			if maycant < re.cantidad:
				maycant=re.cantidad
				mayemp=re.nome
			re=pickle.load(aemp)
		print("La empresa con mas productos vendidos es: ",mayemp," con: ",maycant)
	os.system("pause")

def MuestroProd(ce):
	rrp=producto()
	finprod=os.path.getsize(afprod)
	if finprod ==0:
		print("No hay  productos a mostrar ")
	else:
		print(" Lista de Productos de la empresa ", ce)
		aprod.seek(0,0)
		rpp=pickle.load(aprod)
		while aprod.tell() < finprod:
			#rpp=pickle.load(aprod)
			if rpp.codep == ce:
				print(rpp.codp," ",rpp.descp," ",rpp.stock," ",rpp.precio," ",rpp.precioLiq, " ", rpp.codep)
			rpp=pickle.load(aprod)

def venta(p,cant,pp):
	global afprod
	global aprod
	print("*********VENTA REALIZADA")
	aprod.seek(pp,0)
	p.stock=p.stock - cant
	p.stock=int(p.stock)
	pickle.dump(p,aprod)
	aprod.flush()

"""def verificostock(e,p,cant,pe,pp):
	global aemp
	global afemp
	global afprod
	global aprod
	print(p.stock)
	tec=input()
	if p.stock >= cant:
		e.cantidad=e.cantidad - cant
		aemp.seek(pe,0)
		pickle.dump(e,aemp)
		aemp.flush()
		venta(p,cant,pp)
	else:
		print("stock insuficiente ")
		tec=input()"""

def pantalla():
	global afemp
	global aemp
	global afprod
	global aprod
	
	finemp=os.path.getsize(afemp)
	if finemp==0:
		print("No hay empresas a mostrar")
		os.system("pause")
	else:
		print("\n\nCodigo         Nombre\n\n")
		aemp.seek(0,0)
		print(aemp.tell())
		tec=input()
		while aemp.tell() < finemp:
			re=pickle.load(aemp)
			print(re.code,"   ",re.nome)
		codEmp = int(input("Indique empresa a consultar: "))
		pose=busece(codEmp)
		if pose != -1:
			MuestroProd(codEmp)
			resp=input("Desea comprar ? S/N")
			while (resp!="S") and (resp!="N"):
				resp=input("Invalido - Desea comprar ? S/N")
			if resp=="S":
				codProd=int(input("Ingrese codigo de producto a comprar: "))
				posp=busecp(codProd)
				if posp!=-1:

					cantcompra=int(input("Ingrese cantidad a comprar: "))
					aprod.seek(posp,0)
					rp=pickle.load(aprod)
					print(rp.codp," ",rp.stock)
					tec=input()
					if rp.stock >= cantcompra:
						aemp.seek(pose,0)
						re=pickle.load(aemp)
						re.cantidad=re.cantidad + cantcompra
						re.cantidad=int(re.cantidad)
						aemp.seek(pose,0)
						pickle.dump(re,aemp)
						aemp.flush()
						venta(rp,cantcompra,posp)
						print(aemp.tell())
						#aemp.seek(0,0)
						#aprod.seek(0,0)
						print("venta exitosa")

						tec=input()
						#verificostock(re,rp,cantcompra,pose,posp)
					else:
						print("stock insuficiente ")
						tec=input()
					
				else:
					print("Codigo de Producto no encontrado")
			else:
				print("No desea realizar la compra")
		else:
			print("Codigo de Empresa no encontrado")

def menu():
	global afemp
	global aemp
	global afprod, aprod
	global re,rp
	os.system("cls")

	print("*********Menú de Opciones*********")
	print("1. Consulta y Venta de productos")
	print("2. Empresa que mas productos vendió")
	print("3. Listado de productos que agotaron su stock")
	print("0. Fin de operaciones")
	opcion = input("Seleccionar opcion: ")
	while (validaRangoEntero(opcion, 0, 3)):
			opcion = input("Invaida - Seleccionar opcion: ")
	while opcion != "0":
		if opcion == "1":
			if fechavalida(fechav)==True:
				pantalla()
			else:
				print("Liquidación finalizada")
				os.system("pause")
		elif opcion == "2":
			mayempresa()
			print(" ")
			print(" ")
		elif opcion == "3":
			listadostockcero()
			print(" ")
			print(" ")
		elif opcion == "0":
			print("Gracias por usar el hot sale")
		os.system("cls")

		print("*********Menú de Opciones*********")
		print("1. Consulta y Venta de productos")
		print("2. Empresa que mas productos vendió")
		print("3. Listado de productos que agotaron su stock")
		print("0. Fin de operaciones")
		opcion = input("Seleccionar opcion: ")
		while (validaRangoEntero(opcion, 0, 3)):
			opcion = input("Invalida - Seleccionar opcion: ")

# programa principal
global aemp, aprod
global afemp, afprod
re=empresa()
rp=producto()

afemp="c:\\ayed\\empresa.dat"
if os.path.exists(afemp)==True:
	aemp=open(afemp,"r+b")
else:
	aemp=open(afemp,"w+b")

afprod="c:\\ayed\\productos.dat"
if os.path.exists(afprod)==True:
	aprod=open(afprod,"r+b")
else:
	aprod=open(afprod,"w+b")


global fechav
fechav=validarFecha()
os.system("cls")		
menu()
aemp.close()
aprod.close()
fin=input("Precione ENTER para salir")



