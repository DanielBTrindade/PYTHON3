#ESCREVA UM PROGRAMA PARA APROVAR UM EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA
#O PROGRAMA VAI PERGUNTAR O VALOR DA CASA O SALÁRIO DO COMPRADOR E QUANTOS ANOS ELE VAI PAGAR
#CALCULE O VALOR DA PRESTAÇÃO MENSAL SABENDO QUE ELA NÃO PODE EXCEDER 30 % DO SALÁRIO
#OU ENTÃO O EMPRÉSTIMO É NEGADO
import time
imovel = float(input('Valor do imóvel R$ ? '))
salario = float(input('Qual é o seu salário R$ ? '))
anos = int(input('Em quantas anos vai pagar? '))
parcela = imovel / (anos * 12)
maximo = salario * 30 / 100
print(f'As parcelas do empréstimo de R${imovel:.2f} não pode passar de 30% do seu salário que é de R${salario:.2f}.')
print('CALCULANDO...')
time.sleep(3)
print(f'O valor da parcela do empréstimo é de R$ {parcela:.2f}, e 30% do se salário é R$ {maximo}')
time.sleep(2)
if parcela >= maximo:
    print('Infelizmente seu empréstimo negado')
else:
    print('Parábens seu empréstimo foi aprovado.')

