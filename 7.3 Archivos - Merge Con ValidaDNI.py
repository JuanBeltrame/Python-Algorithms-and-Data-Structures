# merge sobre archivos examen clínica  y valida los DNI    2023
import os
import pickle
import os.path
import datetime

class Historia:
	def __init__(self):
		self.Nhc = 0
		self.Dni= " "
		self.Fec  = " "
		self.Diagnostico= " "
		self.Medico= 0
		self.Activo= " " # S-N 

def validaRangoEntero(nro, min,max,fin):
    try:              
        nro = int(nro)      
        if (nro >= min and nro <= max) or nro==fin:
            return False 
        else:
            return True  
    except:
        return True 


def BuscaSecFisio(hc):  #hago búsqueda secuencial x q como puedo cargar varios registros en el proceso de carga, van a la cola desordenados 
							# y ordena luego... 
    global ArcFisiFisio, ArcLogFisio 
    t = os.path.getsize(ArcFisiFisio)
    pos=0
    ArcLogFisio.seek(0, 0)  
    if t>0:
        vrFisio = pickle.load(ArcLogFisio)
        while (ArcLogFisio.tell()<t) and (int(hc) != int(vrFisio.Nhc)):
            pos = ArcLogFisio.tell()
            vrFisio = pickle.load(ArcLogFisio)
        if int(vrFisio.Nhc) == int(hc):        
         Doc= vrFisio.Dni
         return Doc   #retorna el dni para que sea asignado directamente y no permitir que lo ingrese el usuario
        else:
         return -1
    else:
        return -1

def BuscaSecTrau(hc):  #hago búsqueda secuencial x q como puedo cargar varios registros en el proceso de carga, van a la cola desordenados y ordena luego... 
    global ArcFisiTrauma, ArcLogTrauma 
    t = os.path.getsize(ArcFisiTrauma)
    pos=0
    ArcLogTrauma.seek(0, 0)  
    if t>0:
        vrTrau = pickle.load(ArcLogTrauma)
        while (ArcLogTrauma.tell()<t) and (int(hc) != int(vrTrau.Nhc)):
            pos = ArcLogTrauma.tell()
            vrTrau = pickle.load(ArcLogTrauma)
        if int(vrTrau.Nhc) == int(hc):        
         Doc= vrTrau.Dni
         return Doc   #retorna el dni para que sea asignado directamente y no permitir que lo ingrese el usuario
        else:
         return -1
    else:
    	return -1


def formatearHistoria(vrHist):
	vrHist.Nhc= str(vrHist.Nhc)
	vrHist.Nhc= vrHist.Nhc.ljust(4, ' ')  
	vrHist.Dni = vrHist.Dni.ljust(10, ' ')
	vrHist.Diagnostico = vrHist.Diagnostico.ljust(30, ' ')
	#vrHist.Fec = str(vrHist.Fec)
	vrHist.Fec =vrHist.Fec.ljust(10, ' ')
	vrHist.Medico= str(vrHist.Medico)
	vrHist.Medico= vrHist.Medico.ljust(4, ' ') 

def Ordenafisio():
	global ArcFisiFisio, ArcLogFisio 
	ArcLogFisio.seek (0,0)
	aux = pickle.load(ArcLogFisio)
	tamReg = ArcLogFisio.tell() 
	tamArch = os.path.getsize(ArcFisiFisio)
	cantReg = int(tamArch / tamReg)  
	for i in range(0, cantReg-1):
		for j in range (i+1, cantReg):
			ArcLogFisio.seek (i*tamReg, 0)
			auxi = pickle.load(ArcLogFisio)
			ArcLogFisio.seek (j*tamReg, 0)
			auxj = pickle.load(ArcLogFisio)
			if (int(auxi.Nhc) > int(auxj.Nhc)):
				ArcLogFisio.seek (i*tamReg, 0)
				pickle.dump(auxj, ArcLogFisio)
				ArcLogFisio.seek (j*tamReg, 0)
				pickle.dump(auxi, ArcLogFisio)
				ArcLogFisio.flush()

def Ordenatrau():
	global ArcFisiTrauma, ArcLogTrauma 
	ArcLogTrauma.seek (0, 0)
	aux = pickle.load(ArcLogTrauma)
	tamReg = ArcLogTrauma.tell() 
	tamArch = os.path.getsize(ArcFisiTrauma)
	cantReg = int(tamArch / tamReg)  
	for i in range(0, cantReg-1):
		for j in range (i+1, cantReg):
			ArcLogTrauma.seek (i*tamReg, 0)
			auxi = pickle.load(ArcLogTrauma)
			ArcLogTrauma.seek (j*tamReg, 0)
			auxj = pickle.load(ArcLogTrauma)
			if (int(auxi.Nhc) > int(auxj.Nhc)):
				ArcLogTrauma.seek (i*tamReg, 0)
				pickle.dump(auxj, ArcLogTrauma)
				ArcLogTrauma.seek (j*tamReg, 0)
				pickle.dump(auxi, ArcLogTrauma)
				ArcLogTrauma.flush()

def Cargafisio():  # se valida con una búsqueda que si el numero de Historia Clinica ya exite en alguno de los dos archivos!!!
					# el Dni debe ser el  mismo. No ingresarlo nuevamente x q podría ingresar otro dni
				
	global ArcFisiFisio, ArcLogFisio
	os.system("cls")
	RegFisio= Historia()
	print("      - Carga de Registros Fisioterapia")
	print("---------------------------------------------\n")
	nhc = input("Ingrese numero de Historia Clinica entre 1000 y 9999 [0- para Volver]: ")
	while validaRangoEntero(nhc, 1000, 9999, 0):
		nhc = input("Incorrecto - Entre 1000 y 9999 [0 para Volver]: ")
	while int(nhc) != 0:
		RegFisio.Nhc = int(nhc)
		DF= BuscaSecFisio(RegFisio.Nhc)
		DT= BuscaSecTrau(RegFisio.Nhc)
		if DF !=-1: #ya existe ese nro de hc debo asignar el dni
			RegFisio.Dni = DF
		elif DT !=-1:
			RegFisio.Dni = DT

		else: # es paciente nuevo, no está en ninguno de los dos archivos
			RegFisio.Dni = input("Dni <hasta 9 caracteres>: ")
			while len(RegFisio.Dni)<1 or len(RegFisio.Dni)>9:
				RegFisio.Dni = input("Incorrecto - dni <hasta 9 caracteres>: ")
		RegFisio.Fec= datetime.datetime.now().strftime("%x")
		RegFisio.Diagnostico = input("Diagnóstico: ")
		while len(RegFisio.Diagnostico)<1 or len(RegFisio.Diagnostico)>30:
			RegFisio.Diagnostico = input("Incorrecto - Diagnostico <hasta 30 caracteres>: ")
		RegFisio.Medico = input("Ingrese matrícula del médico entre 1000 y 9999 : ")
		while validaRangoEntero(RegFisio.Medico, 1000, 9999,0):
			RegFisio.Medico = input("Incorrecto - Entre 1000 y 9999: ")
		RegFisio.Activo='S'
		formatearHistoria(RegFisio)
		ArcLogFisio.seek(0,2)
		pickle.dump(RegFisio, ArcLogFisio)
		print("-----------------------")
		print("   Alta exitosa")
		print("------------------------")
		ArcLogFisio.flush()
		
		nhc = input("Ingrese numero d Historia Clinica entre 1000 y 9999 [0- para Volver]: ")
		while validaRangoEntero(nhc, 1000, 9999, 0):
			nhc = input("Incorrecto - Entre 1000 y 9999 [0 para Volver]: ")
	

def Cargatrau():# se valida con una búsqueda que si el numero de Historia Clinica ya exite
					# el Dni debe ser el  mismo. No ingresarlo nuevamente x q podría ingresar otro dni
	global ArcFisiTrauma, ArcLogTrauma
	os.system("cls")
	RegTrau= Historia()
	print("    - Carga de Registros Traumatología")
	print("---------------------------------------------\n")
	nhc = input("Ingrese numero de Historia Clinica entre 1000 y 9999 [0- para Volver]: ")
	while validaRangoEntero(nhc, 1000, 9999, 0):
		nhc = input("Incorrecto - Entre 1000 y 9999 [0 para Volver]: ")
	while int(nhc) != 0:
		RegTrau.Nhc = int(nhc)
		DF= BuscaSecFisio(RegTrau.Nhc)
		DT= BuscaSecTrau(RegTrau.Nhc)
		if DF !=-1: #ya existe ese nro de hc debo asignar el dni
			RegTrau.Dni = DF
		elif DT !=-1:
			RegTrau.Dni = DT
		else:
			RegTrau.Dni = input("dni <hasta 9 caracteres>: ")
			while len(RegTrau.Dni)<1 or len(RegTrau.Dni)>9:
				RegTrau.Dni = input("Incorrecto - dni <hasta 9 caracteres>: ")
		RegTrau.Fec= datetime.datetime.now().strftime("%x")
		RegTrau.Diagnostico = input("Diagnóstico: ")
		while len(RegTrau.Diagnostico)<1 or len(RegTrau.Diagnostico)>30:
			RegTrau.Diagnostico = input("Incorrecto - Diagnostico <hasta 30 caracteres>: ")
		RegTrau.Medico = input("Ingrese matrícula del médico entre 1000 y 9999 : ")
		while validaRangoEntero(RegTrau.Medico, 1000, 9999,0):
			RegTrau.Medico = input("Incorrecto - Entre 1000 y 9999: ")
		RegTrau.Activo='S'
		formatearHistoria(RegTrau)
		ArcLogTrauma.seek(0,2)
		pickle.dump(RegTrau, ArcLogTrauma)
		print("-----------------------")
		print("   Alta exitosa")
		print("------------------------")
		ArcLogTrauma.flush()
		nhc = input("Ingrese numero de Historia Clinica entre 1000 y 9999 [0- para Volver]: ")
		while validaRangoEntero(nhc, 1000, 9999, 0):
			nhc = input("Incorrecto - Entre 1000 y 9999 [0 para Volver]: ")		
	
def listadoFisio():
	global ArcFisiFisio, ArcLogFisio
	os.system("cls")
	RegFisio= Historia()
	print("OPCION 1 - listado de Registros Fisioterapia")
	print("---------------------------------------------\n")
	ArcLogFisio.seek(0, 0)
	RegFisio = Historia()
	t = os.path.getsize(ArcFisiFisio)
	while ArcLogFisio.tell()<t:
		RegFisio = pickle.load(ArcLogFisio)
		print(RegFisio.Nhc,"  ",RegFisio.Dni, "  ", RegFisio.Fec, " ", RegFisio.Medico, " " ,RegFisio.Activo)
	os.system ("pause")	

def listadoTrau():
	global ArcFisiTrauma, ArcLogTrauma
	os.system("cls")
	RegTrau= Historia()
	print("OPCION 2 - listado de Registros Traumatologia")
	print("---------------------------------------------\n")
	ArcLogTrauma.seek(0, 0)
	t = os.path.getsize(ArcFisiTrauma)
	while ArcLogTrauma.tell()<t:
		RegTrau = pickle.load(ArcLogTrauma)
		print(RegTrau.Nhc,"  ",RegTrau.Dni, "  ", RegTrau.Fec, " ", RegTrau.Medico," " ,RegTrau.Activo)
	os.system ("pause")	

def listadoClinica():
	global ArcFisiClinica, ArcLogClini
	os.system("cls")
	RegCli= Historia()
	print("OPCION 3 - listado de Registros Clinica (Traumatologia+Fisioterapia)")
	print("--------------------------------------------------------------------\n")
	ArcLogClini.seek(0, 0)
	t = os.path.getsize(ArcFisiClinica)
	while ArcLogClini.tell()<t:
		RegCli = pickle.load(ArcLogClini)
		print(RegCli.Nhc,"  ",RegCli.Dni, "  ", RegCli.Fec, " ", RegCli.Medico," " ,RegCli.Activo)
	os.system ("pause")	

def Intercalo():
	global ArcFisiFisio, ArcLogFisio
	global ArcFisiTrauma, ArcLogTrauma
	global ArcFisiClinica, ArcLogClini
	ArcLogClini = open(ArcFisiClinica, "w+b") # lo creo desde cero
	ArcLogFisio.seek(0,0)
	ArcLogTrauma.seek(0,0)     
	RegFisio= pickle.load(ArcLogFisio) 
	RegTrau= pickle.load(ArcLogTrauma)
	tamReg=ArcLogFisio.tell()
	print(" tamaño del registro:", tamReg)
	i= 1
	tf =os.path.getsize(ArcFisiFisio)
	j = 1 
	tt=os.path.getsize(ArcFisiTrauma)
	cantRegFisio= tf//tamReg
	print("cantidad de registros de Fisioterapia: ", cantRegFisio)
	cantRegTrau= tt//tamReg
	print("cantidad de registros de Traumatologia: ", cantRegTrau)
	while (i <= cantRegFisio)  and  (j <= cantRegTrau) :
		if RegFisio.Nhc < RegTrau.Nhc:
			pickle.dump(RegFisio,ArcLogClini)
			if i!= cantRegFisio :
				RegFisio=pickle.load(ArcLogFisio)
			i= i + 1
		else:
			pickle.dump (RegTrau,ArcLogClini)
			if j != cantRegTrau:
				RegTrau=pickle.load(ArcLogTrauma)
			j= j + 1
	if i> cantRegFisio :
		for k  in range( j,cantRegTrau+1): #son las vueltas del for
			pickle.dump(RegTrau,ArcLogClini) 
			if k != cantRegTrau:
				RegTrau=pickle.load(ArcLogTrauma)
	else:
		for k in range( i,cantRegFisio+1):
			pickle.dump(RegFisio,ArcLogClini)
			if k != cantRegFisio:
				RegFisio=pickle.load(ArcLogFisio)
	ArcLogClini.flush()
	tc=os.path.getsize(ArcFisiClinica)
	cantRegCli=tc//tamReg
	print("cantidad de registros de clinica: ",cantRegCli)
	print("    --MERGE REALIZADO CON EXITO!--")

"""def Intercalo():  #otra opción usando el tamaño del registro
	global ArcFisiFisio, ArcLogFisio
	global ArcFisiTrauma, ArcLogTrauma
	global ArcFisiClinica, ArcLogClini
	ArcLogClini = open(ArcFisiClinica, "w+b") # lo creo desde cero
	ArcLogFisio.seek(0,0)
	ArcLogTrauma.seek(0,0)     
	RegFisio= pickle.load(ArcLogFisio) 
	RegTrau= pickle.load(ArcLogTrauma)
	tamReg=ArcLogFisio.tell()
	print(" tamaño del registro:", tamReg)
	i= 1
	tf =os.path.getsize(ArcFisiFisio)
	j = 1 
	tt=os.path.getsize(ArcFisiTrauma)
	cantRegFisio= tf//tamReg
	print("cantidad de registros de Fisioterapia: ", cantRegFisio)
	cantRegTrau= tt//tamReg
	print("cantidad de registros de Traumatologia: ", cantRegTrau)
	while (i*tamReg <= tf)  and  (j*tamReg <= tt) :  ##notar que tambien puedo trabajarlo con el tamaño en bytes
		if RegFisio.Nhc < RegTrau.Nhc:
			pickle.dump(RegFisio,ArcLogClini)
			if (i*tamReg)!= tf :
				RegFisio=pickle.load(ArcLogFisio)
			i= i + 1
		else:
			pickle.dump (RegTrau,ArcLogClini)
			if (j*tamReg) != tt :
				RegTrau=pickle.load(ArcLogTrauma)
			j= j + 1
	if (i*tamReg) > tf :
		for k  in range( j,cantRegTrau+1):
			pickle.dump(RegTrau,ArcLogClini) 
			if (k*tamReg)!= tt:
				RegTrau=pickle.load(ArcLogTrauma)
	else:
		for k in range( i,cantRegFisio+1):
			pickle.dump(RegFisio,ArcLogClini)
			if (k*tamReg) != tf:
				RegFisio=pickle.load(ArcLogFisio)
	ArcLogClini.flush()
	tc=os.path.getsize(ArcFisiClinica)
	cantRegCli=tc//tamReg
	print("cantidad de registros de clinica: ",cantRegCli)"""

def ListadoXpac(): #corte de control
	global ArcFisiClinica, ArcLogClini
	print ('      LISTADO de visitas totales por Pacientes   ')
	print('--------------------------------------------------------')
	print ('      CORTE DE CONTROL SOBRE EL ARCHIVO CLINICA   ')
	print('--------------------------------------------------------')
	print ("   Nro Historia Clinica       Cant. Visitas")
	print('--------------------------------------------------------')
	RegCli = Historia()
	ArcLogClini.seek(0,0)
	tc = os.path.getsize(ArcFisiClinica)
	while ArcLogClini.tell()< tc:
		cont = 0
		RegCli = pickle.load(ArcLogClini)
		anterior = RegCli.Nhc
		while anterior ==RegCli.Nhc and ArcLogClini.tell()< tc:
			cont = cont +1
			pos = ArcLogClini.tell()
			RegCli = pickle.load(ArcLogClini)
		if anterior != RegCli.Nhc  : # cambio el grupo y no es fin de archivo
			print  ("       ",anterior,"                   ", cont)
			ArcLogClini.seek(pos)   # retrocedo para no perderlo porque cambió del anterior   	 
		else:
			print  ('       ',anterior,'                   ', cont+1)
        

def BajaLogica():
	global ArcFisiFisio, ArcLogFisio
	global ArcFisiTrauma, ArcLogTrauma
	global ArcFisiClinica, ArcLogClini
	RegCli = Historia()
	RegFisio= Historia()
	RegTrau= Historia()
	os.system("cls")
	print("                     Baja lógica x Médico")
	print("----------------------------------------------------------------------")
	print("   RECUERDE! que esta acción colocará el campo Activo en N")
	print (" Luego de Confirmar NO PODRÁ volver a Activar los registros marcados")
	print("------------------------------------------------------------------------")
	mat = input("Ingrese la matricula del médico cuyos pacientes se darán de baja -entre 1000 y 9999: ")
	while validaRangoEntero(mat, 1000, 9999,0):
		mat = input("Incorrecto - Entre 1000 y 9999 : ")
	print()
	rta = input("seguro Deseas dar de baja los pacientes de ésta matrícula? (S/N): ").upper()
	while rta != "S" and rta != "N":
		rta = input("Por favor, solo contesta con S para Si o N para No: ").upper()
	if rta == "S":
		tc = os.path.getsize(ArcFisiClinica)
		ArcLogClini.seek(0,0)
		RegCli=pickle.load(ArcLogClini)
		tamReg= ArcLogClini.tell()   # notar que todos los registros de los 3 archivos tienen el mismo tamaño
		ArcLogClini.seek(0,0)
		while ArcLogClini.tell() < tc:
			RegCli= pickle.load(ArcLogClini)
			if RegCli.Medico == mat:
				RegCli.Activo='N'
				pos=ArcLogClini.tell()
				atras= pos-tamReg
				ArcLogClini.seek(atras,0) 
				pickle.dump(RegCli,ArcLogClini)
		ArcLogClini.flush()  
				
		ArcLogFisio.seek(0,0)
		tf = os.path.getsize(ArcFisiFisio)
		while ArcLogFisio.tell() < tf:
			RegFisio= pickle.load(ArcLogFisio)
			if RegFisio.Medico == mat:
				RegFisio.Activo='N'
				pos=ArcLogFisio.tell()
				atras= pos-tamReg
				ArcLogFisio.seek(atras,0)
				pickle.dump(RegFisio,ArcLogFisio) 
		ArcLogFisio.flush() 
		        
		ArcLogTrauma.seek(0,0)
		tt = os.path.getsize(ArcFisiTrauma)
		while ArcLogTrauma.tell() < tt:
			RegTrau= pickle.load(ArcLogTrauma)
			if RegTrau.Medico == mat:
				RegTrau.Activo='N'
				pos=ArcLogTrauma.tell()
				atras= pos-tamReg
				ArcLogTrauma.seek(atras,0) 
				pickle.dump(RegTrau,ArcLogTrauma) 
				
		ArcLogTrauma.flush()
		
		print ("---------------------------------")
		print(" Baja lógica Registrada con Éxito ")
		print ("---------------------------------")
	else: 
		print('tranquilo...los datos no fueron borrados')
		os.system("pause")

def pantalla():
	print()
	print('           Menu de opciones');
	print('-------------------------------------------');
	print('1-listado de pacientes Fisioterapia')
	print('2-listado de pacientes Traumatologia')
	print('3-listado de pacientes clinica (Fisioterapia+Traumatologia)')
	print('4-listado x paciente')  # corte de control
	print('5-Baja logica sobre Archivo Clinica')
	print('0- Fin')

### Programa Principal ###
#DefinoArchivos()
ArcFisiFisio = "D:\\AEDD\\Fisioterapia.dat"  
ArcFisiTrauma = "D:\\AEDD\\Traumatologia.dat"
ArcFisiClinica = "D:\\AEDD\\Clinica.dat"
if not os.path.exists(ArcFisiFisio):   
    ArcLogFisio = open(ArcFisiFisio, "w+b")   
else:
    ArcLogFisio = open(ArcFisiFisio, "w+b")   

if not os.path.exists(ArcFisiTrauma):   
    ArcLogTrauma = open(ArcFisiTrauma, "w+b")   
else:
    ArcLogTrauma = open(ArcFisiTrauma, "w+b") 

Cargafisio()
Ordenafisio()
listadoFisio()# Muestro acá para ver si está bien cargado y ordenado pero no sería necesario!
Cargatrau()
Ordenatrau()
listadoTrau()
print ('PROCESO DE INTERCALACION DE ARCHIVOS...');
Intercalo()
listadoClinica()  #muestro acá el listado para ver si se intercaló correctamente

opc = -1

while (opc != 0):
    os.system("cls")
    pantalla()
    opc = input("Ingrese opcion <0 a 5>: ")
    while (validaRangoEntero(opc, 0, 5, 0)):
        opc = input("Incorrecto. Ingrese opcion <0 a 5>: ")
    opc = int(opc)
    if (opc == 1):
        listadoFisio()
    elif (opc == 2):
        listadoTrau()
    elif (opc == 3):
        listadoClinica()
    elif (opc == 4):
        ListadoXpac()
        input()
    elif (opc == 5):
        BajaLogica()   
    elif (opc == 0):
        ArcLogFisio.close()
        ArcLogTrauma.close() 
        ArcLogClini.close()    
        print("\n\n archivos cerrados ..Fin del programa!!")

print("\n\n CHAU!!!!")
input()


