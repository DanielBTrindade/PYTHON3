#DESAFIO 10
#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR
#CONSIDERANDO UU$ 1 = R$ 3,27
#MINHA SOLUÇÃO
n = float(input('Quantos reais você tem?'))
print('Com R$ {:.2f} você pode comprar UU$ {:.2f} '.format(n, (n / 3.27)))
#SOLUÇÃO DO PROFESSOR
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27
print('Com R$ {:.2f} você pode comprar UU$ {:.2f}'.format(real, dolar))