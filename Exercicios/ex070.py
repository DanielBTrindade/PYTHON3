#CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. O PROGRAMA DEVERA PERGUNTAR SE O USUáRIO VAI
# CONTINUAR NO FINAL MOSTRA: #QUAL É  O TOTAL GASTO NA COMPRA, QUANTOS PRODUTOS CUSTAM MAIS DE R$ 1000,
# QUAL É O NOME DO PRODUTO MAIS BARATO.
maisde1000 = 0
soma = 0
barato = None
maisbarato = []
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$ '))
    soma += valor

    if valor >= 1000:
        maisde1000 += 1
    if barato is None or valor < barato:
        barato = valor
        maisbarato = produto


    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Você comprou {maisde1000} produtos que valem mais de 1000 reais')
print(f'Você gastou um total de R$ {soma}')
print(f'O produto mais barato é {maisbarato}, custa R$ {barato}')