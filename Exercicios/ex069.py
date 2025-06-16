#CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA O PROGRAMA DEVERA PERGUNTAR
# SE O USUÁRIO QUER CONTINUAR, NO FINAL MOSTRA: QUANTAS PESSOAS TEM MAIS DE 18 ANOS, QUANTOS HOMENS FORAM CADASTRADOS
# QUANTAS MULHERES TEM MENOS DE 20 ANOS
mulheres20 = mais18 = homens = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Escolha seu sexo M/F: ').strip().upper()[0])
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]

    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1

    if continuar == 'N':
        break

print(f'Um total de {mais18} pessoas tem mais de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Tem {mulheres20} mulheres com menos de 20 anos')

