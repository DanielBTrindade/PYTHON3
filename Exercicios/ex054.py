# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL MOSTRE QUANTAS PESSOAS AINDA
# NÃO ATINGIRAM A MAIOR IDADE E QUANTAS JÁ SÃO MAIORES.
import datetime

ano_atual = datetime.datetime.now().year
cont_maior = 0
cont_menor = 0
nome_maior = []
nome_menor = []
idade_maior = []
idade_menor = []

for c in range(7):  # Apenas "range(7)" já funciona
    nome = input('Nome: ')
    ano_nascimento = int(input("Ano de nascimento: "))
    idade = ano_atual - ano_nascimento

    if idade >= 21:
        cont_maior += 1
        nome_maior.append(nome)
        idade_maior.append(idade)
    else:
        cont_menor += 1
        nome_menor.append(nome)
        idade_menor.append(idade)

print(f'Maiores de idade: {cont_maior}')
print(f'Menores de idade: {cont_menor}')

if nome_maior:  # Só imprime se houver maiores de idade
    print(f'Pessoas maiores de idade: {", ".join(nome_maior).title()}. Idades: {", ".join(map(str, idade_maior))}')
else:
    print('Nenhuma pessoa maior de idade foi cadastrada.')

if nome_menor:  # Só imprime se houver menores de idade
    print(f'Pessoas menores de idade: {", ".join(nome_menor).title()}. Idades: {", ".join(map(str, idade_menor))}')
else:
    print('Nenhuma pessoa menor de idade foi cadastrada.')

print('OBRIGADO!')