#------------------- IMPORTAR LIBRERIAS ----------------------------------
from io import *  	#modulo que permite trabahar con el sistema de archivos
import pickle 		#librería para seliarzar

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

def validorangoentero(nro, desde, hasta):
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
	while(aemp.tell() < finemp):
		re=pickle.load(aemp)
		if (re.code == CodEmp):
			pos=aemp.tell()
	return pos	

def busecp(CodProd):
	global aprod
	global afprod
	finprod=os.path.getsize(afprod)
	aprod.seek(0,0)
	pos=-1
	while(aprod.tell() < finprod):
		rp=pickle.load(aprod)
		if (rp.codp == CodProd):
			pos=aprod.tell()
	return pos		

#----------------------------- INICIALIZAR -----------------------------------------

#----------------------------- CARGAS/ALTAS -----------------------------------------




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

print("*********Ingresar las Empresas del HOT SALE**********")
continuar = "s"
while continuar == "s":
	e = input("Código de la empresa: ")
	while validorangoentero(e,10000,15000):
		e=input("Código de la empresa: ") 
	e=int(e)
	if busece(e)!= -1:
		print("Ya existe")	
	else:
		re.code=e
		re.nome= input("Nombre de la empresa: ")
		#aemp.seek(0,2)
		re.nome=re.nome.ljust(30," ")
		pickle.dump(re,aemp)
		aemp.flush()	
		print(re.code," ",re.nome)
		tec=input()
	continuar = input("Desea continuar (s): ")    	#Para ver si sigo llenando
  	#S
print("**GRACIAS POR INGRESAR EMPRESAS**")
os.system("cls")

	#declar un lista que va a contener los objetos que guardo
print("**************Ingresar los productos del HOT SALE************")
continuar = "s"
while continuar == "s":
	cP = input("Código de producto: ")
	while validorangoentero(cP,0,99999999):
		cP = input("Código de producto: ")
	cP=int(cP)
	if busecp(cP) != -1:
		print("ya existe el producto")
		finprod=os.path.getsize(afprod)
		if finprod != 0:
			aprod.seek(0,0)
			while aprod.tell() < finprod:
				rp=pickle.load(aprod)
				print(rp.codp," ",rp.stock," ",rp.codep," ",rp.precio)
			tec=input()
		else:
			print("archivo vacio")
			tec=input()

		os.system("pause")
	else:
		rp.desp = input("Descripcion del Producto: ")
		rp.desp=rp.desp.ljust(30," ")
		rp.stock = int(input("Stock: "))
		rp.precio = float(input("Precio Real: "))
		rp.precioLiq = float(input("Precio Liquidación: "))
		rp.codep = int(input("Código Empresa: "))
		if busece(rp.codep) != -1:
			rp.codp=cP
			#aprod.seek(0,2)
			pickle.dump(rp, aprod)
			aprod.flush()
			print(rp.codp," ",rp.stock," ",rp.precio," ",rp.codep)
			tec=input()
		else:
			print(" no existe la Empresa")
			os.system("pause")
		continuar = input("Desea continuar: ")  
	
aprod.close() #se cierra el archivo
aemp.close()
terminar=input("Toque ENTER para terminar")

