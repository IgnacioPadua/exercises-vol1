#Lea los 20 primeros registros de un archivo, cada uno de los cuales contienen un nombre.
#Imprimir los nombres

for i in range(1, 21):
    names = input("Introduce un nombre: ")
    print(f"{i}.- {names}")