#DESAFIO 12
#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO
#MINHA SOLUÇÃO
valor = float(input('Valor do produto? R$ '))
print(f'Esse produto custa R${valor:.2f}')
print('Você ganhou um desconto de 5%!!\nAplicando desconto!!!!')
desconto = valor * 5/100
print(f'Valor do desconto: R${desconto:.2f}')
preço = valor - desconto
print(f'Você vai pagar só R${preço:.2f}')
#RESOLUÇÃO DO PROFESSOR
preço = float(input('Qual preço é do produto? R$ '))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))