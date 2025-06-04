#ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE OS MOSTRANDO NA TELA UMA MENSAGEM
#- PRIMEIRO VALOR É MAIOR
#- SEGUNDO VALOR É MAIOR
#- NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
if n1 > n2:
    print(f'O número {n1} é o maior.')
elif n2 > n1:
    print(f'O número {n2} é o maior.')
else:
    print(f'Os números são iguais.')
