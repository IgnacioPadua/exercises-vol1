# Leer de un registro el nombre de un empleado, su salario básico
# por hora, el número de horas trabajadas en el periodo y el porcentaje
# de retención en la fuente. Calcular el salario bruto, el valor de la retención
# y el salario neto

nombre_empleado = 'Nacho'
salario_por_hora = 100
horas_trabajadas = 8
porcentaje_retencion = 10

salario_bruto = (salario_por_hora * horas_trabajadas) 
valor_retención = salario_bruto * .10
salario_neto = salario_bruto - valor_retención

print("El salario bruto de " + nombre_empleado + " es: " + str(salario_bruto) + 
    " el valor de retención es: " + str(valor_retención) + " y su salario neto es: " + str(salario_neto) + " . ")