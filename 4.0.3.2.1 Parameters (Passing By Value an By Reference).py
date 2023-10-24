"""
Parametros
"""
def doblar_valor(numero):
    return numero * 2

def doblar_valores(numeros):
    for i, numero in enumerate(numeros):
        numeros[i] *=2
    print(numeros)

#----------------------------------------------------------------------
# Main Program
n = 10
print(n)
n = doblar_valor(n) # Los datos simples en Python viajan valor
print(n)

ns = [10,50,100]
print(ns)
doblar_valores(ns[:]) # Los datos estructurados en python viajan por referencia, con este simbolo [:], se pasan por valor
print(ns)

