# Lea dos numeros de un mismo registro e imprima ambos
# números sólo si son de diferente signo y distintos de cero.

numero_uno = -10
numero_dos = 1

if numero_uno != 0 and numero_dos != 0:
    if numero_uno > 0 and numero_dos < 0:
        print(numero_uno, numero_dos)
    elif numero_dos > 0 and numero_uno < 0:
        print(numero_uno, numero_dos)
        