#DESAFIO 08
#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS
#MINHA SOLUÇÃO
n1 = float(input('Quantos metros você quer converter?'))
print('{} Quilêmetro'.format(n1 / 1000))
print('{} Hectômetro'.format(n1 / 100))
print('{} Decâmetro'.format(n1/10))
print('{} Metros'.format(n1))
print('{:.0f} Decímetro'.format(n1*10))
print('{:.0f} Centímetro'.format(n1*100))
print('{:.0f} Milímetro'.format(n1*1000))
#SOLUÇÃO DO PROFESSOR
