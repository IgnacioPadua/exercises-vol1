# Lea de un mismo registro el nombre, la edad y el sexo de cualquier
# persona e imrima, sólo si la persona es de sexo masculino y mayor
# de edad, el nombre de la persona. NOTA: Suponga que el registro 
# que se  lee tiene grabado, en el campo denominado "sexo" el 
# número 1 en vez de la palabra "masculino" y ó el número 2 en vez
# de la palabra "femenino".

nombre = 'Ignacio'
edad = 17
sexo = 1    # 1 = Masculino   2 = Femenino

if sexo == 1 and edad >= 18:
    print(nombre)