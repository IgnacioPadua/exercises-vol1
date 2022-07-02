'''
29. Calcule la suma de los 100 primeros numeros naturales.
'''
j=0
for i in range(1, 101):
    j=i+j
    #print(f'{j}')
print(f'La suma de los primeros 100 números naturales es: {j}')
