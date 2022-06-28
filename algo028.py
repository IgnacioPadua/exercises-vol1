'''
28. Imprimir cuatro columnas. En la primera columna, los enteros del 1 al 50. 
En las otras columnas, la segunda, la tercera y la cuarta potencia 
de los enteros de la primera columna.
'''

for i in range(1, 51):
    print(f'{i}   {pow(i, 2)}   {pow(i, 3)}   {pow(i, 4)} ')

