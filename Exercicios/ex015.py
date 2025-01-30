#DESAFIO 15
#ESCREVA UM PROGRAMA QUE PERGUNTE  A QUANTIDADE DE  KM PERCORRIDOS POR UM CARRO ALUGADO
#E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA
#R$60 POR DIA  E R$0,15 PO KM
#MINHA SOLUÇÃO
d = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foram rodados? '))
diaria = d * 60
distancia = km * 0.15
total = diaria + distancia
print(f'Total das diárias R${diaria}')
print(f'Total da distância R${distancia}')
print(f'Total a pagar é de {total}')
