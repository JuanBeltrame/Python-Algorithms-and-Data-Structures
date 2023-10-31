#------------------- IMPORTAR LIBRERIAS ----------------------------------
import os				#importa la librería de comandos del sistema operativo
import pickle			#importa módulo pickle para serialización de archivos
import os.path			#importa la librería para importar el sistema de carpetas del sistema operativo
import datetime			#para poder trabajar con fechas

#----------------------- DEFINICION DE CLASES/REGISTROS ----------------------------------
# declaración de una clase con un constructor...
# Lo usamos para indicar como va a ser el registro, como si fuera el tipo
class Disfraz:
    def __init__(self):  # constructor dentro de la clase Dizfraz
        self.numero = 0
        self.descripcion = ""  # String(30)
        self.precio = [[0.00] * 2 for i in range(2)]  # Matriz 2*2 enteros
        self.disponibilidad = True
        self.baja = False
			
class Alquiler:
	def __init__(self):
		self.nroDisfraz = 0 			#int
		self.nomyape = ""				#(strign(30)
		self.fechaAlquiler = ""			#mas adelante lo vamos a usar como fecha, por ahora string
		self.devuelto = True				# (char: S/N)

#----------------------------- VALIDACIONES DATOS DE ENTRADA + FORMATEO ----------------------------------------- 
def validarArchivoDisfraz():
	global arFiDisfraz
	global arLoDisfraz
	arFiDisfraz = "disfraces10.dat"  			#nombre y ubicación física del archivo
	if not os.path.exists(arFiDisfraz):    	#Condición para saber si el archivo existe físicamente
		print ("El archivo " + arFiDisfraz + " NO existe")
		arLoDisfraz = open (arFiDisfraz, "w+b")   #variable o nombre lógico de tipo archivo. W+ crea o reemplaza físicamente el archivo, b es para indicar archivo binario
	else:
		arLoDisfraz = open (arFiDisfraz, "r+b")   #variable o nombre lógico de tipo archivo. r+ lectura/escritura, b es para indicar archivo binario

def validarArchivoAlquiler():
	global arFiAlquiler
	global arLoAlquiler
	arFiAlquiler = "Alquiler10.dat"  		#nombre y ubicación física del archivo
	if not os.path.exists(arFiAlquiler):    #Condición para saber si el archivo existe físicamente
		print ("El archivo " + arFiAlquiler + " NO existe")
		arLoAlquiler = open (arFiAlquiler, "w+b")   #variable o nombre lógico de tipo archivo. W+ crea o reemplaza físicamente el archivo, b es para indicar archivo binario
	else:
		#print ("El archivo " + arFiAlquiler + " YA existe")
		arLoAlquiler = open (arFiAlquiler, "r+b")   #variable o nombre lógico de tipo archivo. r+ lectura/escritura, b es para indicar archivo binario

def validarIngresoEntero(x,y,z):
	try:
		valor = int(x)
		if valor >= y and valor <= z:
			return True
		else:
			print(f"Por favor, ingrese un valor entre {y} y {z}")
			return False
	except ValueError:
		print(f"Por favor, ingrese un valor entero")
		return False

def validarIngresoReal(x,y,z):
	try:
		valor = float(x)
		if valor >= y and valor <= z:
			return True
		else:
			print(f"Por favor, ingrese un valor entre {y} y {z}")
			return False
	except ValueError:
		print(f"Por favor, ingrese un número")
		return False

#----------------------------- BUSQUEDAS Y ORDENAMIENTO -----------------------------------------  
def buscarDisfraz(numero):
	global arFiDisfraz
	global arLoDisfraz
	d = Disfraz()
	t = os.path.getsize(arFiDisfraz)
	pos = 0
	arLoDisfraz.seek(pos,0) 
	if t>0:
		d = pickle.load(arLoDisfraz)

	while (arLoDisfraz.tell()<t) and (int(numero) != int(d.numero)):
		pos = arLoDisfraz.tell()
		d = pickle.load(arLoDisfraz)
	if int(d.numero) == int(numero):		
		return pos
	else:
		return -1

def buscarAlquiler(numero):
	global arFiAlquiler
	global arLoAlquiler
	t = os.path.getsize(arFiAlquiler)
	if t > 0:
		pos = 0
		arLoAlquiler.seek(pos, 0) 
		a = pickle.load(arLoAlquiler)

		while (arLoAlquiler.tell()<t) and (numero != a.nroDisfraz):
			print(a.nroDisfraz)
			pos = arLoAlquiler.tell()
			a = pickle.load(arLoAlquiler)
		if a.nroDisfraz == numero:		
			return pos
		else:
			return -1
	else:
		return -1

#----------------------------- INICIALIZAR ----------------------------------------- 

#----------------------------- CARGAS/ALTAS -----------------------------------------


def mostrarDisfraz(d): 
	print("Número:", d.numero,"  Descripción:", d.descripcion.strip()) 
	print("Precio Temporada baja día hábil: ", d.precio[0][0], "Precio Temporada baja día no hábil: ", d.precio[0][1])
	print("Precio Temporada alta día hábil: ", d.precio[1][0], "Precio Temporada alta día no hábil: ", d.precio[1][1])
	if d.baja == False:
		print("Para alquilar")
	elif d.baja == True:
		print("Discontinuado", end='\n')
	if d.disponibilidad == True:
		print("Disponible")
	elif d.disponibilidad == False:
		print("Alquilado")

def cargarDisfraz():
	global arLoDisfraz
	d = Disfraz()	#Se asigna a la variable de que sea del tipo Disfraz

	num = input("Ingresa el código del nuevo disfraz, entre 1 y 99999 [0 para Volver]: ")
	while not validarIngresoEntero(num,0,99999):
		num = input("Ingresar código nuevamente: ")
	num = int(num)

	while num != 0:
		pos = buscarDisfraz(num)
		if pos == -1:
			d.numero = str(num).ljust(5, " ")
			d.descripcion = input("Descripción del disfraz: ").ljust(30, " ")
			d.disponibilidad = True
			d.baja = False
			while len(d.descripcion)<1 or len(d.descripcion)>30:
				d.descripcion = input("Por favor no uses mas de 30 caracteres: ")
			for i in range(2):
				for j in range(2):
					precio = input(f"Precio {i} {j}:")
					while not validarIngresoReal(precio,0,99999):
						precio = input("Ingresar el precio nuevamente (menor a $ 100.000): ")
					d.precio[i][j] = float(precio)

			pickle.dump(d, arLoDisfraz)   #Guarda el objeto 'd' en el archivo
			arLoDisfraz.flush()           #Borra el contenido del archivo lógico sin necesidad de cerrarlo, no el del disco
			print("Se dio de alta exitosamente el Disfraz:")
			mostrarDisfraz(d)
		else:
			arLoDisfraz.seek(pos,0)
			d = pickle.load(arLoDisfraz)
			if d.baja == True:
				print(f"El disfraz con el numero fue dadado de baja")
			else:
				print("Ya existe un disfraz con ese número")
		num = input("Ingresa el código del nuevo disfraz, entre 1 y 99999 [0 para Volver]: ")
		while not validarIngresoEntero(num,0,99999):
			num = input("Ingresar código nuevamente: ")
		num = int(num)

def crearDisfraz():
	global arFiDisfraz
	global arLoDisfraz
	os.system("cls")  #limpia la pantalla
	print("ALTA DE DISFRACES\n")
	t = os.path.getsize(arFiDisfraz)    #Almacena en la variable t el tamaño del archivo de Disfraz
	if t==0:
		print ("No hay Disfraces registrados")
	else:
		print ("Lista de Disfraces")
		print ("------------------")
		arLoDisfraz.seek(0, 0)     	#Ubica el puntero en al principio del archivo.
									#El primer parámetro indica lugares a avanzar desde un punto
									#Seugndo parámetro indica punto de partida. 
									#0. Caracter de inicio del archivo. 1. Punto actual del puntero. 2.Final del archivo
		while arLoDisfraz.tell()<t:    #El método tell devuelve la posición del puntero, si es menor a t significa que no llegó al final del archivo.
			#print(arLoDisfraz.tell())
			regDisfraz = pickle.load(arLoDisfraz)   #En la variable regDisfraz asigna el contenido del archivo
			if regDisfraz.baja == False:
				mostrarDisfraz(regDisfraz) #llama a la procedimiento mostrarDisfraz
				print("-----------------------------------------------------------------")
	print()
	cargarDisfraz()

def deshabilitarDisfraz():
	global arLoDisfraz
	d = Disfraz()
	os.system("cls")
	print("BAJA LÓGICA DE UN DISFRAZ\n")
	num = input("Ingresa el código del nuevo disfraz, entre 1 y 99999 [0 para Volver]: ")
	while not validarIngresoEntero(num,0,99999):
		num = input("Ingresar código nuevamente: ")
	num = int(num)
	if num != 0:
		
		pos = buscarDisfraz(num)   	#invoca la función buscarDisfraz para obtener la posición
									#donde comienza el registro
		if pos == -1:				#si no se encontró el Disfraz
			print("El disfraz no existe")
		else:
			arLoDisfraz.seek(pos, 0)		#Ubico el punto en la posición donde comienza el registro
			d = pickle.load(arLoDisfraz)	#Carlo el registro en memoria
			print("Disfraz a dar de baja:")
			mostrarDisfraz(d)
			d.baja = True	
			rpta = input("Confirma? (S o N): ")
			while rpta.upper() != "S" and rpta.upper() != "N":
				rpta = input("Incorrecto - Confirma? (S o N): ")
			if rpta.upper() == "S":
				arLoDisfraz.seek(pos, 0)
				pickle.dump(d, arLoDisfraz)
				arLoDisfraz.flush()
				print("Eliminación exitosa")
				print("El disfraz eliminado es: ")
				mostrarDisfraz(d)
		os.system("pause")

def actualizarPrecios():
	global arLoDisfraz
	d = Disfraz()
	os.system("cls")
	print("ACTUALIZACIÓN DEL PRECIO DE UN DISFRAZ\n")
	num = input("Ingresa el código del nuevo disfraz, entre 1 y 99999 [0 para Volver]: ")
	while not validarIngresoEntero(num,0,99999):
		num = input("Ingresar código nuevamente: ")
	num = int(num)
	if num != 0:
		pos = buscarDisfraz(num)   	
		if pos == -1:				
			print("El disfraz no existe o fue dado de baja")
		else:
			arLoDisfraz.seek(pos, 0)		#Ubico el punto en la posición donde comienza el registro
			d = pickle.load(arLoDisfraz)	
			print("Disfraz a actualizar el precio:")
			mostrarDisfraz(d)
			s = input("Deseas Modificar el precio (S/N)").upper()
			while s != "S" and s != "N":
				s = input("Por favor, solo contesta con S para Si o N para No").upper()
			if s == "S":
				temp = input("Ingrese temporada a actualizar el precio (1 Baja / 2 Alta): ")
				while not validarIngresoEntero(temp,1,2):
					temp = input("Ingresar código nuevamente: ")
				temp = int(temp)

				dia = input("Ingrese día a actualizar el precio (1 día hábil, 2 día no hábil: ")
				while not validarIngresoEntero(dia,1,2):
					dia = input("Ingresar día nuevamente: ")
				dia = int(dia)

				nuevoPrecio = input(f"Precio {temp} {dia}:")
				while not validarIngresoReal(nuevoPrecio,0,99999):
					nuevoPrecio = input("Ingresar el precio nuevamente (menor a $ 100.000): ")
				d.precio[temp-1][dia-1] = float(nuevoPrecio)

			
			rpta = input("¿Confirma actualización? (S o N): ")
			while rpta.upper() != "S" and rpta.upper() != "N":
				rpta = input("Incorrecto - Confirma? (S o N): ")
			if rpta.upper() == "S":
				arLoDisfraz.seek(pos, 0)
				pickle.dump(d, arLoDisfraz)
				arLoDisfraz.flush()
				print("Modificación exitosa")
				print("Los datos actualizados del disfraz son:")
				mostrarDisfraz(d)
		os.system("pause")

def listar():
	global arLoDisfraz
	global arFiDisfraz
	t = os.path.getsize(arFiDisfraz)
	arLoDisfraz.seek(0, 0)
	while arLoDisfraz.tell()<t:
		d = pickle.load(arLoDisfraz)
		if d.baja == False:
			mostrarDisfraz(d)

	print("---------------------------------------------------")
	input("Toque una tecla para continuar...")

def alquilar():
	global arLoDisfraz
	global arFiAlquiler
	global arFiAlquiler
	
	numero = input("Ingresa el código del nuevo disfraz, entre 1 y 99999 [0 para Volver]: ")
	while not validarIngresoEntero(numero,0,99999):
		numero = input("Ingresar código nuevamente: ")
	numero = int(numero)
	
	pos = buscarDisfraz(numero)
	
	a = Alquiler()
	d = Disfraz()
	
	if pos != -1:
		arLoDisfraz.seek(pos, 0)
		d = pickle.load(arLoDisfraz)
		#print(d.baja)
		if d.baja == False and d.disponibilidad == True:
			mostrarDisfraz(d)
			a.nroDisfraz = numero
			a.nomyape = input("Nombre y Apellido: ").ljust(30, " ")
			a.fechaAlquiler = datetime.date.today()
			a.devuelto = False
			arLoAlquiler.seek(0,2)
			pickle.dump(a,arLoAlquiler)
			arLoDisfraz.seek(pos,0)
			d.disponibilidad = False
			pickle.dump(d,arLoDisfraz)

		else:
			print("El disfraz NO está disponible")
	else:
		print("No existe un disfraz con es número")
	input("Precione una tecla para continuar...")

def devolver():
	global arLoDisfraz
	global arFiAlquiler
	global arFiAlquiler
	d = Disfraz()
	a = Alquiler()
	
	num = input("Ingresa el código del nuevo disfraz, entre 1 y 99999 [0 para Volver]: ")
	while not validarIngresoEntero(num,0,99999):
		num = input("Ingresar código nuevamente: ")
	num = int(num)

	posAlq = buscarAlquiler(num)

	if posAlq == -1:
		print("El disfraz no está pendiente de devolución")
	else:
		arLoAlquiler.seek(posAlq, 0)
		a = pickle.load(arLoAlquiler)
		
		if a.devuelto == True:
			print("El disfraz no está pendiente de devolución")
		else:
			posDis = buscarDisfraz(num)
			arLoDisfraz.seek(posDis,0)
			d = pickle.load(arLoDisfraz)
			d.disponibilidad = True
			pickle.dump(d, arLoDisfraz)
			arLoDisfraz.seek(posAlq,0)
			a.devuelto = True
			pickle.dump(a, arLoAlquiler)
			print("Gracias por devolver el disfraz")

	input("Presione una tecla para continuar")

def crearReclamos():
	global arFiAlquiler
	global arFiAlquiler
	a = Alquiler()
	arLoAlquiler.seek(0,0)
	t = os.path.getsize(arFiAlquiler)
	cont = 0
	while arLoAlquiler.tell()<t:
		a = pickle.load(arLoAlquiler)
		dd = (datetime.date.today() - a.fechaAlquiler)
		if dd.days > 3 and a.devuelto == False:
			print(f"Número disfraz: {a.nroDisfraz}     Nombre y Apellido: {a.nomyape}")
			cont =+ 1
	if cont == 0:
		print("No hay disfraces para reclamar")
	input("Presion una tecla para continuar")

"""
	while opcion < 0 or opcion > 7:
		while True:
			try:
				opcion = int(input("Por favor ingreser una opción entre 0 y 7: "))
			except ValueError:
				print("Por favor ingresa un valor numérico entero")
				continue
			break
"""

#Menú de opciones iterativo
def menu():
	os.system("cls")  #limpia la pantalla
	print("1- Alta de un disfraz")
	print("2- Baja lógicca de un disfraz")
	print("3- Actulizar precios")
	print("4. Listado de disfraces disponibles")
	print("5- Alquilar Disfraz")
	print("6- Devolver Disfraz")
	print("7- Reclamar")
	print("0- Salir")

	opcion = input("Ingresar opción deseada: ")
	while not validarIngresoEntero(opcion,0,7):
		opcion = input("Ingresar opción deseada: ")

	opcion = int(opcion)


	if opcion == 1:
		crearDisfraz()
	elif opcion == 2:
		deshabilitarDisfraz()
	elif opcion == 3:
		actualizarPrecios()
	elif opcion == 4:
		listar()
	elif opcion == 5:
		alquilar()
	elif opcion == 6:
		devolver()
	elif opcion == 7:
		crearReclamos()
	elif opcion == 0:
		print("Gracias por utilizar nuestra tienda de Disfraces")
		input()
	while opcion != 0:
		os.system("cls")  #limpia la pantalla
		print("........")
		print("1- Alta de un disfraz")
		print("2- Baja lógicca de un disfraz")
		print("3- Actulizar precios")
		print("4. Listado de disfraces disponibles")
		print("5- Alquilar Disfraz")
		print("6- Devolver Disfraz")
		print("7- Reclamar")
		print("0- Salir")
		
		opcion = input("Ingresar opción deseada: ")
		while not validarIngresoEntero(opcion,0,7):
			opcion = input("Ingresar opción deseada: ")

		opcion = int(opcion)

		
		if opcion == 1:
			crearDisfraz()
		elif opcion == 2:
			deshabilitarDisfraz()
		elif opcion == 3:
			actualizarPrecios()
		elif opcion == 4:
			listar()
		elif opcion == 5:
			alquilar()
		elif opcion == 6:
			devolver()
		elif opcion == 7:
			crearReclamos()
		elif opcion == 0:
			print("Gracias por utilizar nuestra tienda de Disfraces")
			input()

global arFiDisfraz 
global arLoDisfraz 
global arFiAlquiler
global arLoAlquiler

validarArchivoDisfraz()
validarArchivoAlquiler()

menu()
arLoDisfraz.close()
arLoAlquiler.close()
