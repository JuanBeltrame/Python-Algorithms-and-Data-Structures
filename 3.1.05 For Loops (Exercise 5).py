"""
Practica 1 - For Loops - Inconditional - Exercise 05
----------------------------------------------------------------------
English:
For 1,000 residential electricity users, pairs of values are available that indicate, 
for each meter, the Kilowatt-hour consumption at the end of the previous month and the Kilowatt-hour consumption at the end of the current month. 
Additionally, the price per Kilowatt-hour is known. 
Display, for each user, 
the Kilowatt-hour price, the monthly consumption, and the amount to be paid.

Spanish: 
Para 1000 usuarios residenciales de energía eléctrica se cuenta con pares de valores que indican, 
para cada medidor, el consumo de Kilowatios al final del mes anterior y el consumo de Kilowatios al final del mes actual. 
Además, se tiene el precio por Kilowatio.
Exhibir, para cada usuario, 
el precio del Kilowatio, el consumo del mes y el importe a abonar.
----------------------------------------------------------------------
"""
#----------------------------------------------------------------------
# Main Program
begin = 0
end = 5
precio_x_kw = float(input("Ingresar el precio del kw: "))
for i in range(begin,end):
    print("Usuario Numero: ",i+1)
    kw_mes_anterior = float(input("Ingrese los Kw del mes anterior: "))
    kw_mes_acutal = float(input("Ingrese los kw del mes actual: "))
    consumo = kw_mes_acutal - kw_mes_anterior
    consumo_a_pagar = consumo * precio_x_kw
    print("Consumo de KW en el mes - Precio del Kw - Importe a Pagar")
    print("----------------------------------------------------------")
    print(f"{consumo}                      {precio_x_kw}             {consumo_a_pagar} ")
    print()
