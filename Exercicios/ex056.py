# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA MOSTRE
# A MEDIA DE IDADE DO GRUPO
# NOME DO HOMEM MAIS VELHO
# QUANTAS MULHERES TEM MENOS DE 20 ANOS.
# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA MOSTRE
# A MEDIA DE IDADE DO GRUPO
# NOME DO HOMEM MAIS VELHO
# QUANTAS MULHERES TEM MENOS DE 20 ANOS.

media = 0
velho_nome = ''
velho_idade = 0
mulher_nova = ''
mulher_idade = None  # Inicializa corretamente
mulher_menos_20 = 0
nomemulheres20 = []

for c in range(4):
    nome = input('Digite seu nome: ').title()
    idade = int(input('Digite sua idade: '))
    sexo = int(input('Sexo: [1]Masculino [2]Feminino'))

    media += idade

    if sexo == 1 and idade > velho_idade:
        velho_nome = nome
        velho_idade = idade

    elif sexo == 2 and idade < 20:
        mulher_menos_20 += 1
        nomemulheres20.append(nome)

        if mulher_idade is None or idade < mulher_idade:
            mulher_nova = nome
            mulher_idade = idade

print(f'A média de idade do grupo é {media/4:.2f} anos')
print(f'O homem mais velho é {velho_nome.title()}, com {velho_idade} anos.')

if mulher_menos_20 > 0:
    print(f'A mulher mais nova é {mulher_nova.title()}, com {mulher_idade} anos.')
    print(f'Tem {mulher_menos_20} mulheres com menos de 20 anos no grupo. São elas: {", ".join(nomemulheres20)}')
else:
    print('Não há mulheres com menos de 20 anos no grupo.')

print('OBRIGADO!')
