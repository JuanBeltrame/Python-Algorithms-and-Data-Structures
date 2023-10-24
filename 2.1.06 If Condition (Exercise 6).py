"""
Practica 1 - If Conditional - Exercise 06
----------------------------------------------------------------------
English:
Enter three uppercase letters and display them sorted alphabetically

Spanish: 
Ingresar tres letras mayúsculas y mostrarlas ordenadas alfabéticamente. 
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
letra1 = str(input("Ingresar la primera letra: "))
letra2 = str(input("Ingresar la segunda letra: "))
letra3 = str(input("Ingresar la tercera letra: "))

if letra1 == letra2 or letra1 == letra3 or letra2 == letra3: 
    print("Algunas de las letras ingresadas son iguales")
elif letra1 < letra2 and letra1 < letra3:
    if letra2 < letra3:
        print(letra1,letra2,letra3)
    else:
        print(letra1,letra3,letra2)

elif letra2 < letra1 and letra2 < letra3:
    if letra1 < letra3:
        print(letra2,letra1,letra3)
    else:
        print(letra2,letra3,letra1)

elif letra3 < letra1 and letra3 < letra2:
    if letra1 < letra2:
        print(letra3,letra1,letra2)
    else:
        print(letra3,letra2,letra1)
