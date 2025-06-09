# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA MOSTRE
# A MEDIA DE IDADE DO GRUPO
# NOME DO HOMEM MAIS VELHO
# QUANTAS MULHERES TEM MENOS DE 20 ANOS.
media = 0
velho_nome = ''
velho_idade = 0
mulher_nova = ''
mulher_idade = 100
mulher_menos_20 = 0

for c in range(0, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = int(input('Sexo: [1]Masculino [2]Feminino'))
    media += idade
    if sexo == 1 and idade > velho_idade:
        velho_nome = nome
        velho_idade = idade
    elif sexo == 2 and idade < 20:
        mulher_menos_20 += 1
        if idade <  mulher_idade:
            mulher_nova = nome
            mulher_idade = idade

if mulher_menos_20 > 0:
    print(f'Mulher mais nova {mulher_nova}, tem {mulher_idade} anos')
print(f'media de idade {media/5}')
print(f'O homem mais velho é {velho_nome}, {velho_idade} anos.')
