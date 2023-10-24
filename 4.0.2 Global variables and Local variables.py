"""
Global variables and Local variables
"""
def localVariable():
    #global i
    i = 2
    print("Valor de la variable LOCAL dentro del procedimiento ", i)
def globalVariable():
    global i
    i = 3
    print("Valor de la variable GLOBAL dentro del procedimiento", i)

#----------------------------------------------------------------------
# Main Program
i = 1

print("Valor de la variable i: antes de llamar a los procedimientos: ",i )

localVariable()
globalVariable()

print("Valor de la variable en el progama principal al final es: ", i)