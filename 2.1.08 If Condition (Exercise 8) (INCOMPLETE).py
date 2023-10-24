"""
Practica 1 - If Conditional - Exercise 08
----------------------------------------------------------------------
English:
Three positive numbers are read. 
Determine whether they are the lengths of the sides of a triangle. 
Remember that in any triangle, each side is less than or equal to the sum of the other two sides and less than their difference (it is sufficient to show this for one side). 
If so, report whether the triangle is:

Equilateral (3 equal sides),
Isosceles (2 equal sides), or
Scalene (3 different sides)

Spanish: 
Se leen tres números positivos. 
Determinar si son las longitudes de los lados de un triángulo: 
Recordar que en todo triangulo cada lado es menor o igual que la suma de los
otros dos y menor que su diferencia (basta mostrarlo para un lado). 
En caso afirmativo, informar si el mismo es:
equilátero (3 lados iguales), 
isósceles (2 lados iguales) o
escaleno (3 lados distintos).
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
lado1 = int(input("Ingrese el primer lado"))
lado2 = int(input("Ingrese el segundo lado"))
lado3 = int(input("Ingrese el tercer lado"))
if lado1 + lado2 + lado3 != 180:
    print("No se ingresaron las medidas correctas para un triangulo")
elif lado1 == lado2 == lado3: 
    print("las medidas ingresadas representan un triangulo EQUILATERO")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("las medidas ingresadas representan un triangulo ESCALENO")
else:
    print("Las medidas ingresadas representan un triangulo ISOSCELES")