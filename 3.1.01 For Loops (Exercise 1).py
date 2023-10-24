"""
Practica 1 - For Loops - Inconditional - Exercise 01
----------------------------------------------------------------------
English:
Calculate the salary for each of the 50 factory workers
given as data the hourly wage (which is the same for all workers)
and the number of hours each worker worked in the month.

Spanish: 
Calcular el sueldo de cada uno de los 50 operarios de una fábrica 
dados como datos la remuneración por hora (es la misma para todos los operarios) 
y la cantidad de horas que trabajó en el mes cada operario.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
precioXhora = float(input("Ingrese la remuneracion por hora: ")) # Esto se ingresa una sola vez, ya que es la misma para todas. 
begin = 0 
end = 2
for i in range(begin,end):
    print("Numero de operario: ",i+1)
    cantHoras = int(input("Ingrese la cantidad de horas trabajadas: "))
    sueldo = precioXhora * cantHoras
    print("El operario:",i+1, "trabajo:",cantHoras,"horas y su sueldo es de:",sueldo)
