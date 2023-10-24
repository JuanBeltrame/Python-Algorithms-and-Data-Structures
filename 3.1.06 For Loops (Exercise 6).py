"""
Practica 1 - For Loops - Inconditional - Exercise 06
----------------------------------------------------------------------
English:
Knowing that a university degree consists of X number of courses,
enter the grades with which a student passed each of the courses during their university career
and finally display the average grade of that student.

Spanish: 
Sabiendo que una carrera universitaria cuenta con X cantidad de materias, 
ingresar las notas con que un alumno aprobó cada una de las materias durante su carrera universitaria 
y finalmente mostrar la nota promedio de dicho alumno.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
cant_materias = int(input("Ingresar la cantidad de materias: "))
begin = 0
end = cant_materias
acum_notas = 0
for i in range(begin,end):
    nota = float(input("Ingresar nota del alumno: "))
    acum_notas = acum_notas + nota
    print("para la materia numero:",i+1, "la nota es:",nota)
average = acum_notas/cant_materias
print("El Promedio del alumno es de:",average)
