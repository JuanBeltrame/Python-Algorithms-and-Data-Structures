# merge sobre archivos examen SUCURSALES
import os
import pickle
import os.path

class Sucursal:
	def __init__(self):
		self.codArt = 0
		self.cantidad= 0
		
class Existencia:
	def __init__(self):
		self.codArt = 0
		self.cantS1= 0
		self.cantS2= 0
		

def validaRangoEntero(nro, min,max,fin):
    try:              
        nro = int(nro)      
        if (nro >= min and nro <= max) or nro==fin:
            return False 
        else:
            return True  
    except:
        return True 


def formatearSucursal(vrSuc):
	vrSuc.codArt= str(vrSuc.codArt)
	vrSuc.codArt= vrSuc.codArt.ljust(4, ' ')  
	vrSuc.cantidad= str(vrSuc.cantidad)
	vrSuc.cantidad = vrSuc.cantidad.ljust(10, ' ')
	
def formatearExistencia(vrExi):
	vrExi.codArt= str(vrExi.codArt)
	vrExi.codArt= vrExi.codArt.ljust(4, ' ')  
	vrExi.cantS1= str(vrExi.cantS1)
	vrExi.cantS1 = vrExi.cantS1.ljust(10, ' ')
	vrExi.cantS2= str(vrExi.cantS2)
	vrExi.cantS2 = vrExi.cantS2.ljust(10, ' ')

#----------------------------- BUSQUEDAS Y ORDENAMIENTO -----------------------------------------
def BuscaS1(A):
    global ArcFisiSucu1, ArcLogSuc1
    RegSuc1= Sucursal()
    t = os.path.getsize(ArcFisiSucu1)
    pos=0
    ArcLogSuc1.seek(0, 0)  
    if t>0:
        RegSuc1 = pickle.load(ArcLogSuc1)
        while (ArcLogSuc1.tell()<t) and (int(A) != int(RegSuc1.codArt)):
            pos = ArcLogSuc1.tell()
            RegSuc1 = pickle.load(ArcLogSuc1)
        if int(RegSuc1.codArt) == int(A):        
         return pos
        else:
         return -1
    else:
        print('-----------------')
        print("Archivo sin datos")
        print('-----------------')
        return -1

def BuscaS2(A):
    global ArcFisiSucu2, ArcLogSuc2
    RegSuc2= Sucursal()
    t = os.path.getsize(ArcFisiSucu2)
    pos=0
    ArcLogSuc2.seek(0, 0)  
    if t>0:
        RegSuc2 = pickle.load(ArcLogSuc2)
        while (ArcLogSuc2.tell()<t) and (int(A) != int(RegSuc2.codArt)):
            pos = ArcLogSuc2.tell()
            RegSuc2 = pickle.load(ArcLogSuc2)
        if int(RegSuc2.codArt) == int(A):        
         return pos
        else:
         return -1
    else:
        print('-----------------')
        print("Archivo sin datos")
        print('-----------------')
        return -1

def OrdenaSuc1():
	global ArcFisiSucu1, ArcLogSuc1 
	ArcLogSuc1.seek (0,0)
	aux = pickle.load(ArcLogSuc1)
	tamReg = ArcLogSuc1.tell() 
	tamArch = os.path.getsize(ArcFisiSucu1)
	cantReg = int(tamArch / tamReg)  
	for i in range(0, cantReg-1):
		for j in range (i+1, cantReg):
			ArcLogSuc1.seek (i*tamReg, 0)
			auxi = pickle.load(ArcLogSuc1)
			ArcLogSuc1.seek (j*tamReg, 0)
			auxj = pickle.load(ArcLogSuc1)
			if (int(auxi.codArt) > int(auxj.codArt)):
				ArcLogSuc1.seek (i*tamReg, 0)
				pickle.dump(auxj, ArcLogSuc1)
				ArcLogSuc1.seek (j*tamReg, 0)
				pickle.dump(auxi, ArcLogSuc1)
				ArcLogSuc1.flush()

def OrdenaSuc2():
	global ArcFisiSucu2, ArcLogSuc2 
	ArcLogSuc2.seek (0,0)
	aux = pickle.load(ArcLogSuc2)
	tamReg = ArcLogSuc2.tell() 
	tamArch = os.path.getsize(ArcFisiSucu2)
	cantReg = int(tamArch / tamReg)  
	for i in range(0, cantReg-1):
		for j in range (i+1, cantReg):
			ArcLogSuc2.seek (i*tamReg, 0)
			auxi = pickle.load(ArcLogSuc2)
			ArcLogSuc2.seek (j*tamReg, 0)
			auxj = pickle.load(ArcLogSuc2)
			if (int(auxi.codArt) > int(auxj.codArt)):
				ArcLogSuc2.seek (i*tamReg, 0)
				pickle.dump(auxj, ArcLogSuc2)
				ArcLogSuc2.seek (j*tamReg, 0)
				pickle.dump(auxi, ArcLogSuc2)
				ArcLogSuc2.flush()

#----------------------------- INICIALIZAR -----------------------------------------
def CargaSuc1(): 
	global ArcFisiSucu1, ArcLogSuc1
	os.system("cls")
	RegSuc1= Sucursal()
	print("      - Carga de Artículos a la Sucursal 1")
	print("-------------------------------------------------\n")
	na = input("Ingrese numero de Artículo entre 1 y 100000 [0- para Volver]: ")
	while validaRangoEntero(na, 1, 100000, 0):
		na = input("Incorrecto - Entre 1 y 100000 [0 para Volver]: ")
	while int(na) != 0:
		if BuscaS1(int(na)) == -1:
			RegSuc1.cantidad = input("Ingrese cantidad entre 1 y 999999 : ")
			while validaRangoEntero(RegSuc1.cantidad, 1, 999999,0):
				RegSuc1.cantidad = input("Incorrecto - Entre 1 y 999999: ")
			RegSuc1.codArt=na
			formatearSucursal(RegSuc1)
			ArcLogSuc1.seek(0,2)
			pickle.dump(RegSuc1, ArcLogSuc1)
			#print("-----------------------")
			#print("   Alta exitosa")
			#print("------------------------")
			ArcLogSuc1.flush()
		else:
			print("Ya existe Artículo con ese codigo, ingrese nuevamente..")
			os.system("pause")
		na = input("Ingrese numero de Artículo entre 1 y 100000 [0- para Volver]: ")
		while validaRangoEntero(na, 1, 100000, 0):
			na = input("Incorrecto - Entre 1 y 100000 [0 para Volver]: ")
			

def CargaSuc2(): 
	global ArcFisiSucu2, ArcLogSuc2
	os.system("cls")
	RegSuc2= Sucursal()
	print("      - Carga de Artículos a la Sucursal 2")
	print("-------------------------------------------------\n")
	na = input("Ingrese numero de Artículo entre 1 y 100000 [0- para Volver]: ")
	while validaRangoEntero(na, 1, 100000, 0):
		na = input("Incorrecto - Entre 1 y 100000 [0 para Volver]: ")
	while int(na) != 0:
		if BuscaS2(int(na)) == -1:
			RegSuc2.cantidad = input("Ingrese cantidad entre 1 y 999999 : ")
			while validaRangoEntero(RegSuc2.cantidad, 1, 999999,0):
				RegSuc2.cantidad = input("Incorrecto - Entre 1 y 999999: ")
			RegSuc2.codArt=na
			formatearSucursal(RegSuc2)
			ArcLogSuc2.seek(0,2)
			pickle.dump(RegSuc2, ArcLogSuc2)
			#print("-----------------------")
			#print("   Alta exitosa")
			#print("------------------------")
			ArcLogSuc2.flush()
		else:
			print("Ya existe Artículo con ese codigo, ingrese nuevamente..")
			os.system("pause")
		na = input("Ingrese numero de Artículo entre 1 y 100000 [0- para Volver]: ")
		while validaRangoEntero(na, 1, 100000, 0):
			na = input("Incorrecto - Entre 1 y 100000 [0 para Volver]: ")	
	
def listadoSuc1():
	global ArcFisiSucu1, ArcLogSuc1
	os.system("cls")
	RegSuc1= Sucursal()
	print("OPCION 1 - listado de Artículos Sucursal 1")
	print("---------------------------------------------")
	print("   Codigo Art.         Cantidad Stock")
	print("---------------------------------------------")
	ArcLogSuc1.seek(0, 0)
	RegSuc1 = Sucursal()
	t = os.path.getsize(ArcFisiSucu1)
	while ArcLogSuc1.tell()<t:
		RegSuc1 = pickle.load(ArcLogSuc1)
		print("      ",RegSuc1.codArt,"             ",RegSuc1.cantidad)
	os.system ("pause")	


def listadoSuc2():
	global ArcFisiSucu2, ArcLogSuc2
	os.system("cls")
	RegSuc1= Sucursal()
	print("OPCION 2 - listado de Artículos Sucursal 2")
	print("---------------------------------------------")
	print("   Codigo Art.         Cantidad Stock")
	print("---------------------------------------------")
	ArcLogSuc2.seek(0, 0)
	RegSuc2 = Sucursal()
	t = os.path.getsize(ArcFisiSucu2)
	while ArcLogSuc2.tell()<t:
		RegSuc2 = pickle.load(ArcLogSuc2)
		print("      ",RegSuc2.codArt,"             ",RegSuc2.cantidad)
	os.system ("pause")	

def listadoExistencias():
	global ArcFisiExistencias, ArcLogExistencias
	os.system("cls")
	RegExis= Existencia()
	print("OPCION 3 - listado de Artículos en Existencias")
	print("--------------------------------------------------------------")
	print("   Codigo Art.       Cantidad Suc1          Cantidad Suc2")
	print("--------------------------------------------------------------")
	ArcLogExistencias.seek(0, 0)
	te = os.path.getsize(ArcFisiExistencias)
	while ArcLogExistencias.tell()<te:
		RegExis = pickle.load(ArcLogExistencias)
		print("      ",RegExis.codArt,"         ",RegExis.cantS1,"             ",RegExis.cantS2)
	os.system ("pause")	

def ArtParaOfertar():
	global ArcFisiOfertas, ArcLogOfertas
	os.system("cls")
	RegExis= Existencia()
	print("OPCION 4 - listado de Artículos para Ofertar")
	print("----------------------------------------------------------------------------")
	print("   Codigo Art.       Cantidad Suc1          Cantidad Suc2          Total")
	print("----------------------------------------------------------------------------")
	to = os.path.getsize(ArcFisiOfertas)
	ArcLogOfertas.seek(0, 0)
	while ArcLogOfertas.tell()<to:
		RegExis = pickle.load(ArcLogOfertas)
		total= int(RegExis.cantS1)+int(RegExis.cantS2)
		print("      ",RegExis.codArt,"         ",RegExis.cantS1,"             ",RegExis.cantS2, "        ",total)
	os.system ("pause")	


def GeneraOfertas():
	global ArcFisiExistencias, ArcLogExistencias
	#ArcLogOfertas = open(ArcFisiOfertas, "w+b") # lo creo desde cero. puntero en 0
	ArcLogExistencias.seek(0, 0)
	RegExis = Existencia()
	te = os.path.getsize(ArcFisiExistencias)
	while ArcLogExistencias.tell()<te:
		RegExis = pickle.load(ArcLogExistencias)
		if (int(RegExis.cantS1) + int(RegExis.cantS2))>= 200:
			#formatearExistencia(RegExis)
			pickle.dump(RegExis,ArcLogOfertas)
	ArcLogOfertas.flush()    	


def Intercalo():
	global ArcFisiSucu1, ArcLogSuc1
	global ArcFisiSucu1, ArcLogSuc2
	global ArcFisiExistencias, ArcLogExistencias
	ArcLogExistencias = open(ArcFisiExistencias, "w+b") # lo creo desde cero
	RegExis= Existencia()
	ArcLogSuc1.seek(0,0)
	ArcLogSuc2.seek(0,0)     
	RegSuc1= pickle.load(ArcLogSuc1) 
	RegSuc2= pickle.load(ArcLogSuc2)
	tamReg=ArcLogSuc1.tell()
	print(" tamaño del registro:", tamReg)
	i= 1
	tS1 =os.path.getsize(ArcFisiSucu1)
	j = 1 
	tS2=os.path.getsize(ArcFisiSucu2)
	cantRegS1= tS1//tamReg
	print("cantidad de Artículos en Sucursal 1: ", cantRegS1)
	cantRegS2= tS2//tamReg
	print("cantidad de Artículos en Sucursal 2: ", cantRegS2)
	while (i <= cantRegS1)  and  (j <= cantRegS2) :
		if int(RegSuc1.codArt) < int(RegSuc2.codArt):
			RegExis.codArt= RegSuc1.codArt
			RegExis.cantS1= RegSuc1.cantidad
			RegExis.cantS2= 0
			formatearExistencia(RegExis)
			pickle.dump(RegExis,ArcLogExistencias)
			if i!= cantRegS1 :
				RegSuc1=pickle.load(ArcLogSuc1)
			i= i + 1
		elif int(RegSuc2.codArt) < int(RegSuc1.codArt):
			RegExis.codArt= RegSuc2.codArt
			RegExis.cantS2= RegSuc2.cantidad
			RegExis.cantS1= 0
			formatearExistencia(RegExis)
			pickle.dump(RegExis,ArcLogExistencias)
			if j!= cantRegS2:
				RegSuc2=pickle.load(ArcLogSuc2)
			j= j + 1
		else: # el art esta en las dos sucursales
			RegExis.codArt= RegSuc1.codArt  # son iguales asigno cualquier CodArt
			RegExis.cantS1= RegSuc1.cantidad
			RegExis.cantS2= RegSuc2.cantidad
			formatearExistencia(RegExis)
			pickle.dump(RegExis,ArcLogExistencias)
			if i!= cantRegS1 :
				RegSuc1=pickle.load(ArcLogSuc1)
			i= i + 1
			if j != cantRegS2:
				RegSuc2=pickle.load(ArcLogSuc2)
			j= j + 1
	if i>= cantRegS1 :  #copio los registros que quedaron de Suc2
		for k  in range( j,cantRegS2+1): #son las vueltas del for
			RegExis.codArt= RegSuc2.codArt
			RegExis.cantS2= RegSuc2.cantidad
			RegExis.cantS1= 0
			formatearExistencia(RegExis)
			pickle.dump(RegExis,ArcLogExistencias)
			if k != cantRegS2:
				RegSuc2=pickle.load(ArcLogSuc2)
	else:
		for k in range( i,cantRegS1+1):
			RegExis.codArt= RegSuc1.codArt
			RegExis.cantS1= RegSuc1.cantidad
			RegExis.cantS2= 0
			formatearExistencia(RegExis)
			pickle.dump(RegExis,ArcLogExistencias)
			if k != cantRegS1:
				RegSuc1=pickle.load(ArcLogSuc1)
	ArcLogExistencias.flush()
	ArcLogExistencias.seek(0,0)
	RegExis= pickle.load(ArcLogExistencias)
	tamRegE = ArcLogExistencias.tell()
	te=os.path.getsize(ArcFisiExistencias)
	cantRegExist=te//tamRegE
	print("cantidad de registros en Existencias: ",cantRegExist)# notar que son la suma de ambos registros. 
	print()
	print("    --MERGE REALIZADO CON EXITO!--")



def pantalla():
	print()
	print('           Menu de opciones');
	print('-------------------------------------------');
	print('1-listado de Artículos Sucursal 1')
	print('2-listado de Artículos Sucursal 2')
	print('3-listado de Existencias totales (Suc1+Suc2)')
	print('4-listado de Artículos para Ofertar') 
	print('0- Fin')

### Programa Principal ###
#DefinoArchivos()
ArcFisiSucu1 = "D:\\AEDD\\SucursalUno.dat"  
ArcFisiSucu2= "D:\\AEDD\\SucursalDos.dat"
ArcFisiExistencias = "D:\\AEDD\\Existencia.dat"
ArcFisiOfertas = "D:\\AEDD\\Ofertas.dat"
if not os.path.exists(ArcFisiSucu1):   
    ArcLogSuc1 = open(ArcFisiSucu1, "w+b")   
else:
    ArcLogSuc1 = open(ArcFisiSucu1, "r+b")   

if not os.path.exists(ArcFisiSucu2):   
    ArcLogSuc2 = open(ArcFisiSucu2, "w+b")   
else:
    ArcLogSuc2 = open(ArcFisiSucu2, "r+b") 
ArcLogOfertas = open(ArcFisiOfertas, "w+b")
CargaSuc1()
OrdenaSuc1()
listadoSuc1()# Muestro aca para ver si está bien cargado y ordenado
CargaSuc2()
OrdenaSuc2()
listadoSuc2()
print ('PROCESO DE INTERCALACION DE ARCHIVOS...');
Intercalo()
listadoExistencias()  #muestro acá el listado para ver si se intercaló correctamente
GeneraOfertas()
ArtParaOfertar()  # cantidad mayor a 200 unidades
opc = -1

while (opc != 0):
	os.system("cls")
	pantalla()
	opc = input("Ingrese opcion <0 a 4>: ")
	while (validaRangoEntero(opc, 0, 4,0)):
	    opc = input("Incorrecto. Ingrese opcion <0 a 4>: ")
	opc = int(opc)
	if (opc == 1):
		listadoSuc1()
	elif (opc == 2):
		listadoSuc2()
	elif (opc == 3):
		listadoExistencias()
	elif (opc == 4):
		ArtParaOfertar()
	elif (opc == 0):
		ArcLogSuc1.close()
		ArcLogSuc2.close() 
		ArcLogExistencias.close()
		ArcLogOfertas.close()    
		print("\n\n archivos cerrados ..Fin del programa!!")
print("\n\n Gracias por usar nuestro sistema!!!!")


