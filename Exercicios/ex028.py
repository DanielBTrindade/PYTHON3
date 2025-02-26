#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUÁRIO
#ADIVINHAR, O PROGRAMA DEVE ESCREVER NA TELA SE O USUÁRIO ACERTOU
#minha solução
from random import randint
x = randint(0, 5)
print('"Estou pensando em um número de 0 a 5"')
n = int(input('Em que número eu estou pensando? '))
if n == x:
    print('Parabéns você acertou!!!')
else:
    print('GANHEI! Tente de novo!')
print(f'O número certo era {x}')
#solução do professor
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! eu pensei no número {}.'.format(computador))