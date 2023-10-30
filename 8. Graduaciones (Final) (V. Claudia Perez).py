#------------------- IMPORTAR LIBRERIAS ----------------------------------
# Apertura de librerías de Python necesarias para la ejecución
import sys
import pickle
import os.path
import datetime


#----------------------- DEFINICION DE CLASES/REGISTROS ----------------------------------
# Definición de Registros (uno por cada archivo)
class Rgraduacion:
	def __init__(self):
		self.noms=" "
		self.valor=[0]*3
		
class Rasistente:
	def __init__(self):
		self.dni=" "  # string[8]
		self.nya=" "   # string[30]
		self.cs=0
		self.cat=0
		self.pago=" "
		self.emitido=" "

#----------------------------- VALIDACIONES DATOS DE ENTRADA + FORMATEO -----------------------------------------
def validaRangoEntero(nro, desde,hasta):
	try:              # trata de hacer lo que sigue, si da error se ejecuta el except
		int(nro)      
		if (int(nro) >= desde) and (int(nro) <= hasta):
			return False #validación correcta, retorna falso para que salga del while que valida
		else:
			return True  #validación incorrecta, retorna verdadero para que siga en el while que valida
	except:
		return True      #validación incorrecta, retorna verdadero para que siga en el while que valida

def validonumeros(nro,desde,hasta):
	int(nro)
	while int(nro) < desde and int(nro) < hasta:
		op=input()

#----------------------------- BUSQUEDAS Y ORDENAMIENTO ----------------------------------------- 
# Función de Búsqueda secuencial de dni en Asistentes.dat
def buscasis(d):
	global ala
	global afa
	global ra
	TamarA=os.path.getsize(afa)
	ala.seek(0,0)
	posr=ala.tell()
	ra=pickle.load(ala)
	while (ala.tell() < TamarA) and (ra.dni != d):
		posr=ala.tell()
		ra=pickle.load(ala)
	if ra.dni== d:
		b=posr
	else:
		b=-1
	return b

# función de busueda secuencial, por dos campos dni y código de salón
def existe(d,c):
	global ala
	global afa

	Tamala=os.path.getsize(afa)
	ex=-1
	if Tamala == 0:
		print("Archivo vacio ")
	else:
		ala.seek(0,0)
		posa=ala.tell()
		ra=pickle.load(ala)
		while (ala.tell() < Tamala) and ((ra.dni!=d) and (ra.cs!= c)):
			posa=ala.tell()
			ra=pickle.load(ala)
		if (ra.dni==d) and (ra.cs== c):
			ex=posa
		else:
			ex=-1
	return ex

#----------------------------- INICIALIZAR -----------------------------------------

#----------------------------- CARGAS/ALTAS -----------------------------------------
# Procedimiento de carga en Graduaciones.dat, por enunciado se encuentra con datos cargados.
def Cargasalones():
	global alg
	global afg
	print("*********Ingresar DATOS DE SALONES  **********")
	rg=Rgraduacion()
	continuar = "s"
	if os.path.getsize(afg)==0:
		print("Archivo vacio ")
		cods=0
	else:
		alg.seek(0,0)
		rg=pickle.load(alg)
		Tamregm=alg.tell()
		cantregm=int(os.path.getsize(afg) / Tamregm)
		alg.seek(0,2)
		
		cods=int(cantregm)
	
	while (continuar == "s") and (cods < 30):
		
		rg.noms=input("ingrese nombre del salón / máximo 30 caracteres: ")
		rg.noms=rg.noms.ljust(30," ")
		print("Ingrese los montos de las tarjetas ")
		rg.valor[0]=float(input("Ingrese valor Tarjeta Graduado: "))
		rg.valor[1]=float(input("Ingrese valor Tarjeta Asistente a Cena: "))
		rg.valor[2]=float(input("Ingrese valor Tarjeta Asistente a Brindis: "))
		pickle.dump(rg,alg)
		alg.flush()
		cods=int(cods+1)
		continuar = input("Desea continuar (s): ")    	#Para ver si sigo llenando
	print("**GRACIAS POR INGRESAR LOS DATOS DE SALONES Y VALOR DE ENTRADA**")
	os.system("cls")


# CREACIÓN Y APERTURA DE ARCHIVOS

def Asignar():
	global ala
	global afa
	global alg
	global afg
	afa="c:\\ayed\\asistentes.dat"
	afg="c:\\ayed\\graduaciones.dat"
	if os.path.exists(afa):
		ala=open(afa,"r+b")
	else:
		ala=open(afa,"w+b")
	if os.path.exists(afg):
		alg=open(afg,"r+b")
	else:
		alg=open(afg,"w+b")





def Consultas():
	global alg
	global afg
	Tamarch=os.path.getsize(afg)
	if Tamarch==0:
		print("Archivo vacio")
	else:
		alg.seek(0,0)
		rg=pickle.load(alg)
		tamregG=alg.tell()
		print("**** CONSULTAS ****")
		print("")
		print("Codigo   Nombre de salon Valor graduado valor cena valor brindis")
		while alg.tell() < Tamarch:
			rg=pickle.load(alg)
			print(int(alg.tell()-tamregG)," ",rg.noms," ",rg.valor[0]," ",rg.valor[1]," ",rg.valor[2])
			print("")
			input()

# Genera y formatea el registro de asistentes para luego inscribirlo (grabar en archivo)

def armorega(r, d, c):
	r.dni=d.ljust(8," ")
	r.cs=c
	r.nya=input("Ingrese nombre y apellido ").ljust(30," ")
	r.cat=int(input("Ingrese categoría 1-2-3 "))
	while r.cat < 1 or r.cat > 3:
		r.cat=int(input("Inválida - Ingrese categoría 1-2-3 "))
	r.pago="N"
	r.emitido="N"


			
# Realiza las Inscripciones a las graduaciones de los asistentes
def Inscripción():
	global ala
	global afa
	print("**** INSCRIPCIONES A LAS GRADUACIONES ****")
	print("")
	ra=Rasistente()
	dni=input("Ingrese dni / 0 para salir ")
	ala.seek(0,2)
	while dni != "0":
 		cs=int(input("Ingrese código de salón: "))
 		while (cs < 1) and (cs > 30):
 			cs=int(input("Inválida - Ingrese código de salón: "))
 		pos_asist=existe(dni,cs)
 		if pos_asist == -1:
 			armorega(ra,dni,cs)
 			print(ra.dni," ",ra.cs," ",ra.nya," ",ra.cat," ",ra.pago," ",ra.emitido)
 			input()
 			pickle.dump(ra,ala)
 			ala.flush()
 			print("*** Inscripción exitosa ***")
 			input()
 		else:
 			print("ya está inscripto el dni en esa categoría")
 			print(" ")
 		dni=input("Ingrese dni / 0 para sair ")

# Reacudación por salón y categoría
# Se utiliza una 2 arreglos bidimensionales de 30 filas (salones), 3 columnas(categorias), como acumuladores para los totales recuadados y adeudados
def Recaudación():
	global cod, cate
	global afa
	global ala
	global afg
	global ala
	i=int()
	j=int()
	k=int()
	for i in range(30):
		for j in range(3):
			totrec[i][j]=float(0)
			totdeu[i][j]=float(0)
	print("**** RECAUDACIÓN POR SALÓN Y CATEGORÍA ****")
	print("")
	cod=int()
	cate=int()
	
	# Calcula el tamaño de registro de graduaciones, para calculo de posición relativa
	alg.seek(0,0)
	rg=pickle.load(alg)
	TamreG=alg.tell()
	# Calculo del tamaño del archivo de asistentes para su barrido secuencial
	TamaA=os.path.getsize(afa)
	if TamaA==0:
		print("Archivo vacío")
	else:
		# Barrido secuencial
		ala.seek(0,0)
		while ala.tell() < TamaA:
			ra=pickle.load(ala)
			# calculo posicion relativa del registro y lectura, para obtener el valor según la categoria de graduaciones
			posreG=int(TamreG*(ra.cs-1))
			alg.seek(posreG,0)
			rg=pickle.load(alg)
			
			cod=int(ra.cs -1)
			cate=int(ra.cat-1)
			rg.valor[cate]=float(rg.valor[cate])
			# Decide si esta pago o no la tarjeta para los calculos de recaudado y adeudado
			if ra.pago=="S":
				totrec[cod][cate]=totrec[cod][cate]+rg.valor[cate]
			else:
				totdeu[cod][cate]=totdeu[cod][cate]+rg.valor[cate]
		for s in range(30):
			print("")
			print(" SALÓN ", s+1)
			for c in range(3):
				print("Categoria ", c+1)
				print("Recaudado: ",totrec[s][c])
				print("Adeudado:  ",totdeu[s][c])
				print("")
			input()
		# en 2 arreglos unidimensionales (por salones), donde  se acumula lo recuadado y adeudado para mostrar que salon adeuda mas de lo recaudado.
		for s in range(30):
			r[s]=float(0)
			a[s]=float(0)
			for c in range(3):
				r[s]=r[s]+totrec[s][c]
				a[s]=a[s]+totdeu[s][c]
			#print("** El salon ", s+1," Recaudó: ",r[s]," Adeudado: ", a[s])
			#input()
			if  a[s] > r[s]:
				print("*** ATENCIÓN  - EL SALÓN ", s+1," SU DEUDA ", a[s], " SUPERA LO RECAUDADO *** ",r[s])
				input()
		os.system("pause")	

# Emite la tarjeta al asistente
def emisión(d,nomap, salon,desc):
	print("DNI    NOMBRE Y APELLIDO    NRO Y NOMBRE DEL SALON")
	print(d,"  ",nomap," ",salon," ",desc)
	print()
	input()
# formatea el registro y actualiza el archivo de asistentes registrando el pago y la emisión de la entrada
def actualizar(r, p):
	global ala
	global afa
	r.pago="S"
	r.emitido="S"
	r.nya=r.nya.ljust(30," ")
	r.dni=r.dni.ljust(8," ")
	ala.seek(p,0)
	pickle.dump(r,ala)
	ala.flush()
	print(" Actualizado con exito ")
	input()

# Proceso de pago y emision con busqueda directa (por posición relativa a registro) en Graduaciones
def Pagoyemisión():
	global ala
	global afa
	global alg
	global afg
	# Calculo del Tamaño de registro de Graduaciones
	alg.seek(0,0)
	rg=pickle.load(alg)
	TamregG=alg.tell()
	print("**** EMISIÓN DE TARJETAS ****")
	print("")
	dni=input("Ingrese dni / 0 para salir ")
	while dni != "0":
		if os.path.getsize(afg)==0 or os.path.getsize(afa)==0:
			print("Archivos vacios")
			input(" ")
		else:
			posrega=buscasis(dni)
			if posrega != -1:
				# Calcula la posición en el registro graduaciones
				posrelativaG=int(TamregG*(ra.cs-1))
				alg.seek(posrelativaG,0)
				rg=pickle.load(alg)
				if  (ra.emitido=="N"):
						if ra.cat==1:
							descrip="Graduados"
						elif ra.cat==2:
							descrip="Asistencia a cena"
						else:
							descrip="Asistencia a brindis"
						"""ra.emite="S"
						ra.pago="S"""
						emisión(dni,ra.nya,rg.noms,descrip)
						actualizar(ra,posrega)
				else:
					print("Ya esta emitida")
					input()
			else:
				print("Asistente no encontrado")
				input()
		dni=input("Ingrese dni / 0 para salir ")

def Menu():
	global ala
	global afa
	global alg
	global afg
	os.system("cls")

	print("*********Menú de Opciones*********")
	print("0. Carga de datos Archivo Graduaciones (única vez)")
	print("1. Incripción a graduaciones")
	print("2. Recaudación ")
	print("3. Emisión de Tarjetas")
	print("4. Cobro de Tarjetas")
	print("5. Sair")
	print(" ")
	opcion = input("Seleccionar opcion: ")
	"""while (validonumeros(opcion, 0, 3)):
			opcion = input("Invalida - Seleccionar opcion: ")"""
	while validaRangoEntero(opcion,0,5):
		opcion = input(" Invalida  / Seleccionar opcion: ")
	while opcion != "5":
		if opcion=="0":
			Cargasalones()
			Consultas()
		if opcion == "1":
			Inscripción()
			os.system("pause")
		elif opcion == "2":
			Recaudación()
			print(" ")
			print(" ")
		elif opcion == "3":
			Pagoyemisión()
			print(" ")
			print(" ")
		elif opcion == "4":
			#Cobro()
			print("*** Opción inhabilitada ***")
			input()
		elif opcion == "5":
			print("Gracias por usar programa de Graduaciones")
		os.system("cls")
		print("*********Menú de Opciones*********")
		print("0. Carga de datos Archivo Graduaciones (única vez)")
		print("1. Incripción a graduaciones")
		print("2. Recaudación ")
		print("3. Emisión de Tarjetas")
		print("4. Cobro de Tarjetas")
		print("5. Salir")
		print(" ")
		
		opcion = input("Seleccionar opcion: ")
		"""while (validonumeros(opcion, 0, 3)):
			opcion = input("Invalida - Seleccionar opcion: ")"""
		while validaRangoEntero(opcion,0,5):
			opcion = input(" Invalida  / Seleccionar opcion: ")

# Programa principal
Asignar()
# declaracion de arreglos
totrec=[0.00]*30
for k in range(30):
	totrec[k]=[0.00]*3

totdeu=[0.00]*30 
for k in range(30):
	totdeu[k]=[0.00]*3

r=[0.00]*30
a=[0.00]*30

Menu()
#Cierre de archivos
ala.close()
alg.close()
