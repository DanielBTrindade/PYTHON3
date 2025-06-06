#DESENVOLVA UMA LÓGICA QUE LEIA O PESO A ALTURA DE UMA PESSOA CALCULE SEU IMC E MOSTRE SEU STATUS DE ACORDO
#COM A TABELA ABAIXO
#- ABAIXO DE 18,5: ABAIXO DO PESO
#- ENTRE 18,5 E 25: PESO IDEAL
#- DE 25 ATÉ 30: SOBREPESO
#- DE 30 ATÉ 40: OBESIDADE
#- ACIMA DE 40: OBESIDADE MORBIDA
peso = float(input('Digite seu peso em Kg: ').replace(',', '.'))
altura = float(input('Digite sua altura em metros: ').replace(',', '.'))
imc = peso / (altura * altura)
print(f'Seu  índice de massa corporal (IMC) é: {imc:.2f}')
if imc < 18.5:
    print(f'ABAIXO DO PESO.')
elif imc < 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO.')
elif imc < 40:
    print('OBESIDADE.')
else:
    print('OBESIDADE MORBIDA')

