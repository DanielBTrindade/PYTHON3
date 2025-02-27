#desenvolva um programa que pergunte a distançia de uma viagem em km e calcule o preço da passagem
#cobrando R$0,50 por km para viagens até 200 km e R$0,45 para viagens mais longas
#MINHA SOLUÇÃO
#Receber a distância da viagem
from time import sleep
distancia = float(input('Qual a distância em KM da sua viagem? '))
#calcular o valor da passagem da viagem até 200 km
print('CALCULANDO...')
sleep(2)
if distancia <= 200:
    preco = distancia * 0.50
# calcular o valor da passagem da viagem mais longa
else:
    preco = distancia * 0.45
# mostrar o valor da passagem
print(f'Sua passagem vai custar {preco:.2f}')
