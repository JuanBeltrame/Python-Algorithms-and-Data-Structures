"""
Procedures and Functions
"""
def saludo_bievenida():
    print("Bienvenido, aprendamos a programar")

def consultar_nombre():
    mi_nombre = input("Cual es tu nombre? ")
    return mi_nombre

#----------------------------------------------------------------------
# Main Program
print("Hola")
saludo_bievenida() # invocacion / llamada
nombre = consultar_nombre()
print("Hola", nombre)
