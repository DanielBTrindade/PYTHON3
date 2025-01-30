#DESAFIO 09
#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA
#MINHA RESOLUÇÃO
n = int(input('Qual número você quer saber a tabuada?'))
print('A tabuada do {} é:\n{} x 0 = {}\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}'.format(n, n, n*0, n, n*1, n, n*2, n, n*3, n, n*4, n, n*5, n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))
#RESOLUÇÃO DO PROFESSOR
n = int(input('Digite um número para ver sua tabuada:'))
print('-' * 12)
print('{} x {:2} = {}'.format(n, 0, n*0))
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {} = {}'.format(n, 10, n*10))
print('-' * 12)