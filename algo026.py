# Leer varios registros cada uno de ellos, conteniendo un nombre.
# El número de estos registros se encuentra grabado en un registro que precede
# a los anteriores. Imprimir cada uno de los nombres leidos.

numero_registros = int(input("Número de registros: "))

for i in range(1,numero_registros+1):
    nombre = input("Introduce un nombre: ")
    print(f"{i}.- {nombre}")
