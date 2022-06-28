""" 
Leer un conjunto de registros cada uno de ellos conteniendo el código y el nombre
 de cada uno de los estudiantes de la universidad. El último registro del conjunto
 (registro centinela) contiene el código 99999999 y es utilizado sólo para chequear
 el final de los registros. Imprima cadauno de los códigos leídos. Lógicamente la 
 información del registro centinela no se imprime porque no pertenece a ningún estudiante.
      <.   . > 
"""

id_estudiante = 99999997
int(id_estudiante)

while id_estudiante < 99999999 :
    codigo_estudiante = int(input("Código estudiante: "))
    nombre_estudiante = input("Nombre estudiante: ")
    print("-"*40)
    print(f"Código estudiante: {codigo_estudiante} \nNombre estudiante: {nombre_estudiante}")
    print("-"*40)
    id_estudiante += 1
    print(id_estudiante)