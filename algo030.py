'''
30. Obtener la suma de los números pares comprendidos entre 1 y 100.
'''

j=0
for i in range(1,101):
    saber_par = i % 2
    if saber_par == 0:
        j+=i
        #print(f'El valor de i es: {i} y de j es: {j}')

print(f'La suma de los números pares entre 1 y 100 es: {j}')