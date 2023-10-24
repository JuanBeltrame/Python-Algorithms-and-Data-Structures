# Usando subprograma
"""
Tipo de dato 
SECC= Array [1..30] de Reales

Variables 
A,B,C de tipo SECC
"""

def Cargar(X,Tam): # Tam parametro formal por valor 
    for i in range(0,Tam):
        X[i]=float(input("Ingrese Nro: "))

def Mostrar (X,Tam):
    print("Lo recorro y lo muestro")
    for j in range(0,Tam):
        print(X[j])

def Suma(X,Tam):
    global Ac
    Ac=0
    for i in range(0,Tam):
        Ac = Ac + X[i]
        return Ac

# Programa Principal 
TA = 2 # Dimensiono los arreglos de distintos tamaños # Este seria el tamano de A
TB = 4 # Este seria el tamano de B
TC = 5 # Este seria el tamano de C

A = TA*[0.0] # Se crean e inicializan los arreglos en cero, 0.0 si ingreso flotantes. 
B = TB*[0.0]
C = TC*[0.0] 

print("Carga del Arreglo A")
Cargar(A,TA)
print(("La suma del arreglo A es: "), Suma(A,TA))# Aca invoco a la funcion  en el mostrar
print()

print("Carga del Arreglo B")
Cargar(B,TB)
SumaB= Suma(B,TB) # Aca invoco a la funcion suma en una sentencia de asigancion
print(("La suma del arreglo B es: "), SumaB)
print()

print("Carga del Arreglo C")
Cargar(C,TC)
SumaC= Suma(C,TC) # Aca invoco a la funcion suma en una sentencia de asigancion
print(("La suma del arreglo C es: "), SumaC)  
