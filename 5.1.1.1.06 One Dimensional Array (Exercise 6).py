"""
Practica 3 - One-Dimensional Array- Exercise 06
----------------------------------------------------------------------
English:
The grades for a midterm exam are available for the 30 students in a class.
It is desired to know how many of them obtained a grade higher than the course average.

Spanish: 
Se tienen como datos las notas de un parcial de los 30 alumnos de un curso. Se desea saber cuantos de ellos obtuvieron
una calificacion superior al promedio del curso.
----------------------------------------------------------------------
"""
def load_notes(arr, tam):
    begin = 0
    for i in range(begin, tam):
        arr[i] = int(input("Upload Score: "))
        
def get_average(arr, size):
    total_score = 0
    begin = 0
    for i in range(begin, size):
        total_score += arr[i]
    average = total_score / size
    return average

def get_scores(arr, size, p):
    begin = 0
    c = 0
    for i in range(begin, size):
        if arr[i] > p:
            c += 1
        else:
            print()
    return c

#----------------------------------------------------------------------
# Main Program
T = 3
array = [0] * T

print("Upload notes from exam")
load_notes(array, T)
avg = get_average(array[:], T)
print("The average is ", avg)
print("The number of students above the score is.", get_scores(array, 3, avg))
