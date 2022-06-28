# Lea de un mismo registro el nombre, la edad, el sexo(1 ó 2) y 
# el estado civil de cualquier persona e imprima sólo si la persona
# es un hombre soltero mayor de edad, el nombre de la persona.
# NOTA:  En el campo de "estado civil" aparece grabado el número 1
# en vez de "soltero", el número 2 en vez de "casado" ó el número 3
# en vez de "otro"

nombre = 'nacho'
edad = 18
sexo = 1     # hombre = 1  mujer = 2
estado_civil = 1  # soltero = 1  casado = 2 otro = 3

if sexo == 1 and edad >= 18 and estado_civil == 1:
    print(nombre)