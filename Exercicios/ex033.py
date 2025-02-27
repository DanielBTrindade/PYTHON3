#CRIE UM PROGRAMA QUE LEIA 3 NÚMEROS E MOSTRE QUAL É O MAIOR, QUAL É O MENOR
# Receber os números
#MINHA SOLUÇÃO
from time import sleep
#lidar com entradas inválidas
try:
    #receber os valores
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    n3 = int(input('Digite um número: '))
    print('PROCESSANDO...')
    sleep(2)
    #verificar o maior
    maior = max(n1, n2, n3)
    print(f'O maior número é: {maior}')
    #verificar o menor
    menor = min(n1, n2, n3)
    print(f'O menor número é: {menor}')
#em caso de entradas inválidas
except ValueError:
    print('Erro: por favor, digite um número válido.')
