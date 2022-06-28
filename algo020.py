# Para un salario bruto hasta de $1500 no hay retención. Para un salario bruto 
# de $1500 a $3000 el porcentaje  de retención  es de 5%. Para un salario bruto 
# mayor de $3000 el porcentaje de retención  es de 8%. Obtener el nombre del empleado,
# el salario bruto, el valor de la retención y el salario neto. Se debe leer el 
# nombre y el salario.


nombre_empleado = input("Nombre del empleado: ")
salario_bruto = int(input("¿Cuál es el salario bruto? "))

if salario_bruto > 1500 and salario_bruto <= 3000:
    valor_retencion = (salario_bruto * 5)/100
    salario_neto = salario_bruto - valor_retencion
    print("Empleado: " + nombre_empleado + " \nValor de retención: " + 
        str(valor_retencion) + " \nSalario neto: " + str(salario_neto))
elif salario_bruto > 3000:
    valor_retencion = (salario_bruto * 8)/100
    salario_neto = salario_bruto - valor_retencion
    print("Empleado: " + nombre_empleado + " \nValor de retención: " + 
        str(valor_retencion) + " \nSalario neto: " + str(salario_neto))
else:
    salario_neto = salario_bruto
    print("Empleado: " + nombre_empleado + " \nNo hay retención. " + 
        " \nSalario neto: " + str(salario_neto))

