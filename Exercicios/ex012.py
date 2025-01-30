#DESAFIO 12
#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO
#MINHA SOLUÇÃO
valor = float(input('Valor do produto?'))
print(f'Esse produto custa {valor}R$')
print('Você ganhou um desconto de 5%!!\nAplicando desconto!!!!')
desconto = valor * (5/100)
print(f'Valor do desconto: {desconto}R$')
preço = valor - desconto
print(f'Você vai pagar só {preço}R%')
