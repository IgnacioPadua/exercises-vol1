# Lea un número y calcule e imprima su raíz cuadrada. Si
# el número es negativo imprima el número y un mensaje 
# que diga: "tiene raíz imaginaria"
from math import sqrt

numero = -15

# valor_raiz_cuadradada = sqrt(numero)
valor_raiz_cuadradada = numero ** .5

if numero < 0:
    print('El número: ' + str(numero) +' tiene raíz imaginaria')
else:
    print('La raíz cuadrada de ' + str(numero) + ' es: ' + str(valor_raiz_cuadradada))