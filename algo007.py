'''
Lea de un registro el nombre, la edad, el sexo y el estado civil de cualquier persona e imprima
, solo si la persona es hombre o mujer menor de edad o es hombre casado de cualquier edad, 
el nombre de la persona y un mensaje que diga "usted no se manda". En los demás casos imprima
el nombre de la persona solamente.
'''

nombre_persona = input("Nombre: ")
edad_persona = int(input("Edad: "))
sexo_persona = input("Sexo: ")
estado_civil_persona = input("Estado civil: ")

if edad_persona < 18 or (estado_civil_persona == 'casado' and sexo_persona == 'hombre'):
    print(f'{nombre_persona} usted no se manda')
else:
    print(f'{nombre_persona}')
