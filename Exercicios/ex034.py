#ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO
#PARA SALÁRIOS SUPERIORES A R$1250 CALCULE UM AUMENTO DE 10%
#PARA INFERIORES OU IGUAIS  CALCULE UM AUMENTO DE 15%
try:
    salario = float(input('Qual é o valor do seu salário? R$ '))
    if salario > 1250:
        aumento = salario * 10 / 100 + salario
        print(f'{aumento}')
        print(f'Voce recebeu um aumento de 10%. Salário atualizado {aumento:.2f}')
    else:
        aumento = salario * 15 / 100 + salario
        print(f'Voce recebeu um aumento de 15%. Salário atualizado {aumento:.2f}')
except ValueError:
    print('Insira um valor válido!')