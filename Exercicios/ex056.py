# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA MOSTRE
# A MEDIA DE IDADE DO GRUPO
# NOME DO HOMEM MAIS VELHO
# QUANTAS MULHERES TEM MENOS DE 20 ANOS.
media = 0
velho = 0
for c in range(0, 2):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = int(input('Sexo: [1]Masculino [2]Feminino'))
    media += idade / 2
    velho = nome

print(f'O homem mais velho é {velho}, {idade} anos.')
print(f'media de idade {media}')

