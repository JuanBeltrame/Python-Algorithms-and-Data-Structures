"""
Practica 1 - If Conditional - Exercise 07
----------------------------------------------------------------------
English:
Quality Control of Two Types of Parts in a Factory is Desired
A and B will be used to denote the two types of parts.
a. The type of part and its measurement in millimeters are given as data.
b. It must be indicated whether it meets the specifications, knowing that
c. Type A pieces must measure 165 mm and a tolerance of +/-2 mm is allowed.
d. Type B pieces must measure 180 mm and a tolerance of +/-3 mm is allowed.

Spanish: 
Se desea controlar en una fábrica la calidad de dos tipos de piezas 
que denominaremos A y B.
a. Se dan como datos el tipo de pieza y su medida en milímetros.
b. Se debe indicar si cumple con las especificaciones sabiendo que
c. Las piezas de tipo A deben medir 165 mm y se admite un error de +/-2 mm.
d. Las piezas de tipo B deben medir 180 mm y se admite un error de +/-3 mm.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
tipo_pieza = str(input("Ingresar tipo de pieza A-B: "))
if tipo_pieza == "A":
    print("Se ingreso la pieza:",tipo_pieza)
    medida = int(input("Ingresar la medida de la pieza: ")) 
    if 163 <= medida <= 167:
        print("La pieza:",tipo_pieza, "que mide: ", medida,"mm", "cumple con las medidas correctas")
    else:
        print("La pieza:",tipo_pieza, "que mide: ", medida,"mm"+ "NO cumple con las medidas correctas")
elif tipo_pieza == "B":
    medida = int(input("Ingresar la medida de la pieza: ")) 
    if 177 <= medida <= 183:
        print("Se ingreso la pieza:",tipo_pieza)
        print("La pieza:",tipo_pieza, "que mide: ", medida, "cumple con las medidas correctas")
else:
    print("Lo siento, la pieza ingresada es Incorrecta")
