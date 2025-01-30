#DESAFIO 13
#FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE SE NOVO SALARIO COM 15% DE AUMENTO
#MINHA SOLUÇÃO
salario = float(input("Digite o salário do funcionário: R$ "))
print(f'Aplicando aumento de 15% Ao salário R${salario:.2f}')
aumento = salario + (salario * 15 / 100)
print(f'Salário aumentou para R${aumento:.2f}')
#SOLUÇÃO DO PROFESSOR
salário = float(input('Qual é o salário do funcionario? R$ '))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganha R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
