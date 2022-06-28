# Lea dos números de un mismo registro. Calcule la suma de los números 
# imprima los números leídos y solo si su suma es negativa. Imprimala
# también.

numero1 = 10
numero2 = 6
resultado_suma = numero1 + numero2

if resultado_suma < 0:
    print('La suma de ' + str(numero1) + ' + ' + str(numero2) + ' es: ' + str(resultado_suma))
else:
    print(numero1, numero2)