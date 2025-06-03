#ESCREVA UM PROGRAMA PARA APROVAR UM EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA
#O PROGRAMA VAI PERGUNTAR O VALOR DA CASA O SALÁRIO DO COMPRADOR E QUANTOS ANOS ELE VAI PAGAR
#CALCULE O VALOR DA PRESTAÇÃO MENSAL SABENDO QUE ELA NÃO PODE EXCEDER 30 % DO SALÁRIO
#OU ENTÃO O EMPRÉSTIMO É NEGADO
import time

imovel = float(input('Valor do imóvel? '))
salario = float(input('Qual é o seu salário? '))
parcela = int(input('Em quantas vezes quer vai parcelar? '))
print(f'As {parcela} parcelas do seu empréstimo de {imovel:.2f} não pode passar de 30% do seu salário, '
      f'que é de {salario:.2f}.')
time.sleep(3)
print('CALCULANDO...')
time.sleep(3)
parte_salario = salario * 30 / 100
print(f'30 % do  seu salário é {parte_salario}')
time.sleep(2)
valor_parcela = imovel / parcela
print(f'O valor da parcela  do seu imprestimo é de {valor_parcela:.2f}')
time.sleep(2)
if valor_parcela > parte_salario:
    print('Infelizmente seu empréstimo negado')
else:
    print('Parábens seu empréstimo foi aprovado.')

