#Leer de un registro un número entero positivo y obtener los múltiplos de 3 
# comprendidos entre 1 y el número leído.

numero = int(input("Número: "))

if numero > 0:
    for i in range(1, numero+1):
        multiplo = 3 * i
        print(f" 3 x {i} = {multiplo}")
else:
    print("Dato incorrecto")
