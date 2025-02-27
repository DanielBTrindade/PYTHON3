#desenvolva um programa que pergunte a distançia de uma viagem em km e calcule o preço da passagem
#cobrando R$0,50 por km para viagens até 200 km e R$0,45 para viagens mais longas
#MINHA SOLUÇÃO
#Receber a distância da viagem
distancia = float(input('Qual a distância em KM da sua viagem? '))
#calcular o valor da passagem da viagem até 200 km
if distancia <= 200:
    d1 = distancia * 0.50
    # mostrar o valor da passagem da viagem até 200 km
    print(f'Sua passagem vai custar {d1:.2f}')
# calcular o valor da passagem da viagem mais longa
else:
    d2 = distancia * 0.45
    # mostrar o valor da passagem da viagem mais longa
    print(f'Sua passagem vai custar {d2:.2f}')