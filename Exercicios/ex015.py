#DESAFIO 15
#ESCREVA UM PROGRAMA QUE PERGUNTE  A QUANTIDADE DE  KM PERCORRIDOS POR UM CARRO ALUGADO
#E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA
#R$60 POR DIA  E R$0,15 PO KM
#MINHA SOLUÇÃO
d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foram rodados? '))
diaria = d * 60
distancia = km * 0.15
total = diaria + distancia
print(f'Total das diárias R${diaria:.2f}')
print(f'Total da distância R${distancia:.2f}')
print(f'Total a pagar é de R${total:.2f}')
#SOLUÇÃO DO PROFESSOR
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
