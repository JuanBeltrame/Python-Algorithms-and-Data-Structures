#------------------- IMPORTAR LIBRERIAS ----------------------------------
import sys
import pickle
import os.path
import datetime

#----------------------- DEFINICION DE CLASES/REGISTROS ----------------------------------
# Definición de Registros 
class RorganizaA:
	def __init__(self):
		self.codSoc=" "
		self.dni=" "
		self.nya=" "
		self.te=" "
		self.cuota="0.00"

#----------------------------- VALIDACIONES DATOS DE ENTRADA + FORMATEO -----------------------------------------

def Asigna():
	global alA
	global afa
	

	afa="c:\\ayed\\organizacionA.dat"
	
	"""if os.path.exists(afa):
		alA=open(afa,"r+b")
	else:"""
	alA=open(afa,"w+b")
	
	rA=RorganizaA()
	alA.seek(0,2)
	rA.codSoc="A100".ljust(8," ")
	rA.nya="Ceciia Gómez".ljust(25," ")
	rA.te="341345678".ljust(10," ")
	rA.cuota=2000.00
	pickle.dump(rA,alA)
	alA.flush()

	rA=RorganizaA()
	rA.codSoc="A101".ljust(8," ")
	rA.nya="Ramiro Saenz".ljust(25," ")
	rA.te="341345678".ljust(10," ")
	rA.cuota=1000.00
	pickle.dump(rA,alA)
	alA.flush()

	rA=RorganizaA()
	rA.codSoc="A102".ljust(8," ")
	rA.nya="Juan Martinez".ljust(25," ")
	rA.te="341345678".ljust(10," ")
	rA.cuota=3000.00
	pickle.dump(rA,alA)
	alA.flush()

	rA=RorganizaA()
	alA.seek(0,2)
	rA.codSoc="A102".ljust(8," ")
	rA.nya="Walter Lopez".ljust(25," ")
	rA.te="341345678".ljust(10," ")
	rA.cuota=1000.00
	pickle.dump(rA,alA)
	alA.flush()

	rA=RorganizaA()
	rA.codSoc="B300".ljust(8," ")
	rA.nya="Clarisa Lopez".ljust(25," ")
	rA.te="341345678".ljust(10," ")
	rA.cuota=2000.00
	pickle.dump(rA,alA)
	alA.flush()

	alA.seek(0,0)
	print("*** DATOS INGRESADOS ***")
	while alA.tell() < os.path.getsize(afa):
		rA=pickle.load(alA)
		print(rA.codSoc," ",rA.cuota)
		input()



def CortedeControl():
	# EL ARCHIVO DEBE ESTAR ORDENADO, Y EL CAMPO DE CONTROL SE REPITE
	global alA
	global afa
	
	# CALCULA EL TAMAÑO DEL REGISTRO DEL ARCHIVO
	
	finA=os.path.getsize(afa)
	if finA!= 0:
		alA.seek(0,0)
		rA=pickle.load(alA)
		tamregA=alA.tell()

        # SOLO PARA INFORMAR
		cantregA=int(finA/tamregA) 
		print("CANTIDAD REGISTRO DE A ",cantregA+1)
		input()
		

		# LECTURA DEL 1ER REGISTRO
		alA.seek(0,0)
		rA=pickle.load(alA)

		# RECORRE EL ARCHIVO HASTA EL FINAL
		while alA.tell() < finA:
			# INICIALIZA EN 0 PARA CADA GRUPO
			cont=0
			# ALMACENAMOS EL CODIGO DE SOCIOS, PARA COMPARAR CON LOS POSTERIORES
			anterior=rA.codSoc
			while (alA.tell() < finA) and (rA.codSoc == anterior):   # CONDICIONES DE FINAL DE CADA SUBGRUPO
				cont=cont+1
				rA=pickle.load(alA)
				#print(rA.codSoc)
				#input()
			
			if rA.codSoc == anterior:      # POR CADA SUBGRUPO
				# CUENTA REGISTROS DEL SUBGRUPO
				cont=cont+1               
				print("cantidad de registros con codigo", anterior," es ", cont)      
			else:
				# NO e incrementa cont, porque lee el registro con campo que cambia el subgrupo
				print("cantidad de registros con codigo", anterior," es ", cont)
				input()
			
		#if b == 1:
		# si finaliza el archivo y en el ultimo se produce el cambio de subgrupo, es 1
		if (alA.tell() == finA) and (rA.codSoc != anterior):
			print("cantidad de registros con codigo", rA.codSoc," es ", 1)
			input()
	else:
		print("ARCHIVO VACIO")
		
def CierreArch():
	alA.close()
	

Asigna()
CortedeControl()
CierreArch()