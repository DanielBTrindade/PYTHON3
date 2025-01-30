#DESAFIO 10
#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR
#Cotação do dia 30/01/2025
#MINHA SOLUÇÃO
n = float(input('Quantos reais você tem?'))
print('Com R$ {:.2f} você pode comprar UU$ {:.2f} '.format(n, (n / 5.89)))
print('Com R$ {:.2f} você pode comprar EUR {:.2f} '.format(n, (n / 6.13)))
print('Com R$ {:.2f} você pode comprar JPY {:.2f} '.format(n, (n / 0.03802)))
print('Com R$ {:.2f} você pode comprar ARS {:.2f} '.format(n, (n / 0.0056)))
#SOLUÇÃO DO PROFESSOR
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27
print('Com R$ {:.2f} você pode comprar UU$ {:.2f}'.format(real, dolar))