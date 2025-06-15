# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE SEU FATORIAL!
import math

n = int(input('Digite um número para saber seu fatorial: '))
while n != 0:
    n = int(input('Digite um número para saber seu fatorial: '))
    resultado = math.factorial(n)
    print(f'O fatorial de {n} é: {resultado}')
print('FIM')