"""
Practica 1 - For Loops - Inconditional - Exercise 02
----------------------------------------------------------------------
English:
Given as input 100 integer numbers,
display each of them indicating:
whether it is POSITIVE or NEGATIVE, as appropriate.

Spanish: 
Dados como datos 100 números enteros, 
mostrar cada uno de ellos indicando:
si es POSITIVO o NEGATIVO, según corresponda.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
begin = 0
end = 5
for i in range(begin,end):
    number = int(input("Ingrese un numero: "))
    if number > 0: 
        print("El numero ingresado en la posicion:",i+1, "es:",number, "y es positivo.")
    elif number < 0:
        print("El numero ingresado en la posicion:",i+1, "es:",number, "y es negativo.")
    else:
        print("Se ingreso el cero")
