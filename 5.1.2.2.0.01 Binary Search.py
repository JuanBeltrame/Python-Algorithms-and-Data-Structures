# Busqueda Binaria/Dicotomica
# type vec = array [0..9] de enteros
# variables V:vec

def cargar(W):
    for i in range(10):
        W[i] = int(input("Ingresar un numero: "))


def ordenar(W):
    for i in range(9):
        for j in range(i+1, 10):
            if W[i] > W[j]:
                aux = W[i]
                W[i] = W[j]
                W[j] = aux


def mostrar(X):
    for i in range(0, 10):
        print("Elemento de la posicion: ", i, "es: ", X[i])


def busca_dico(W, e):  # procedimiento
    inf = 0
    sup = 9
    med = (inf+sup) // 2
    while ((W[med] != e) and (inf < sup)):
        if e > W[med]:
            inf = med + 1
        else:
            sup = med - 1
        med = (inf + sup) // 2
        if W[med] == e:
            print("El elemento buscado esta en la posicion: ", med)
        else:
            print("No se encontro el elemento")

def busca_dico_int(W,e): #funcion que devuelva la posicion o -1 si no lo encuentra
    inf = 0
    sup = 9 # vean aca ahora en python el superior sera uno menos 
    med = (inf + sup) // 2
    #while (W[med] != e) and (inf < sup):
        
        
