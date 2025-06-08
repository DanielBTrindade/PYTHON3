# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL MOSTRE QUANTAS PESSOAS AINDA
# NÃO ATINGIRAM A MAIOR IDADE E QUANTAS JÁ SÃO MAIORES.
import datetime

ano_atual = datetime.datetime.now().year
for c in range(0, 7):
    nome = input('Nome: ')
    ano_nascimento = int(input("Ano de nascimento: "))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        print(f'{nome.title()}, você tem {idade}. É maior de idade.')
    elif idade < 21:
        print(f'{nome.title()}, Você tem {idade}. É menor de idade.')
print('OBRIGADO!')