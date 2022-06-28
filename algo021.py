# Leer de un registro  el número de un empleado, el salario básico
# por hora y el número de horas trabajadas durante una semana. 
# Caluclar el salario neto, teniendo en cuenta que si el número de
# horas trabajadas durante la semana es mayor de 48, esas horas de 
# más se consideran horas extras y tienen un 35% de recargo.
# Imprima el nombre del empleado y el salario neto. 

111
salario_basico = 70
id_empleado = int(input("ID Empleado: "))
nombre_empleado = input("Nombre del empleado: ")
horas_trabajadas = int(input("Horas trabajadas: "))

if horas_trabajadas < 48 :
    salario_neto = salario_basico * horas_trabajadas
    print("Empleado: " + nombre_empleado + "\nSalario neto: " + str(salario_neto))
else:
    horas_extras = horas_trabajadas - 48
    recargo = (horas_extras * 35)/100
    salario_neto = (salario_basico * horas_trabajadas)
    salario_neto_recargo = (salario_basico * horas_trabajadas) +  recargo
    print("Empleado: " + nombre_empleado + "\nHoras extras: " + str(horas_extras) + 
          "\nSalario neto: " + str(salario_neto) + "\nSalario neto con recargo: " + str(salario_neto_recargo))