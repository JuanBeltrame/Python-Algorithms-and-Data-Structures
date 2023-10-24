# Busqueda Secuencial | Linear Search

# Type
# vec = array[0..9] de enteros
# Variables v:vec


def cargar(x): # cargar arreglo con procedimiento
    begin = 0
    end = 10
    for i in range(begin, end): # son 10 vueltas del for
        x[i] = int(input("Nro: "))


def muestra(x): # muestra con procedimiento
    begin = 0
    end = 10
    for i in range(begin, end):# son 10 vueltas del for
        print("Elemento de la posicion: ", i, "es: ", x[i])

def buscar(x,e): # procedimiento
    i = 0
    while (x[i] != e and i <= 8): # cuando i sea 8 si entra al mientras le suma 1 y cae en la ultima posicion del arreglo
        i = i + 1
    if x[i]==e:
        print("El numero: ", e, "se encontro en la posicion: ", i)
    else:
        print("el numero: ", e, "no se encontro")

def funcion_buscar_bool(x,e): # funcion que retorna true/false depende si lo encontro o no. 
    global i, bandera
    i = 0
    while (x[i] != e and i <=8):
        i = i + 1
    if x[i] == e:
        bandera = True
    else:
        bandera = False

    return bandera

def fun_buscar(x,e): # Funcion que retorna la posicion del arreglo donde esta el elemento o -1 si no lo encontro. 
    i = 0
    while (x[i] != e and i <=8):
        i = i + 1
    if x[i] == e:
        return i
    else:
        return -1

#----------------------------------------------------------------------
# Programa principal
V = [0] * 10 # aca limpio y declaro el arreglo de numeros enteros

cargar(V) # invoco al procedimiento cargar
muestra(V)
N = int(input("Ingresar el elemento a buscar"))

print("\n Resultado del procedimiento buscar")
buscar(V,N) #invoco al procedimiento buscar. Notar que i es variable local de buscar



print("\n Resultado de la funcion buscar retornando la posicion que es un entero")
posicion = fun_buscar(V,N) # invoco a la funcion en una sentencia de asignacion
if posicion != -1:
    print("El numero: ",N, " se encontro en la posicion: ", posicion)
else:
    print("El elemento: ",N," no se encontro")



print("\n Resultado de la funcion buscar retornando un booleano true o false")
band = funcion_buscar_bool(V,N) #invoco la funcion en una sentencia de asignacion
if band: 
    print("El numero: ",N, " se encontro en la posicion: ", i)
else:
    print("El elemento: ",N," no se encontro")
