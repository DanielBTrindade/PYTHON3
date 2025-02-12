#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO
# E MOSTRE NA TELA SUA PARTE INTEIRA
from math import trunc
num = float(input('Digite um número real qualquer: '))
print(f'A porção inteira de {num} é igual a {trunc(num)}')
print(f'A porção inteira de {num} é igual a {int(num)}')