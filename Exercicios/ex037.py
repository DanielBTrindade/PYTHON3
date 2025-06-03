#ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTERIRO QUALQUER E PEÇA PARA QUE O USUARIO ESCOLHA QUAL SERÁ
#A BASE DE CONVERSÃO 1 PARA BINARIO, 2 PARA OCTAL E 3 PARA HEXADECIMAL
n = int(input('Digite um número para conversão: '))
trans = int(input('Escolha uma opção:\n'
                  '1 para transformar em binário\n'
                  '2 para transformar em octal\n'
                  '3 para transformar em hexadecimal\n'
                  'Digite sua escolha: '))
opcoes = {1: bin, 2: oct, 3: hex}
if trans in opcoes:
    resultado = opcoes[trans](n)[2:]
    print(f'Numero convertido: {resultado}')
else:
    print('Digite uma opção válida.')
