#CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO. NO INICIO PERGUNTE AO USUÁRIO QUAL O VALOR
#A SER SACADO NUMERO INTEIRO E O PROGRAMA VAI INFORMAR QUANTS CEDULAS DE CADA VALOR SERÃO ENTREGUES
#OBS: CONSIDERE QUE O CAIXA POSSUI CEDULAS DE 50, 20, 10 E 1 REAL.
valor = int(input('Digite o valor que quer sacar: R$ '))
cedula = [50, 20, 10, 1]

for i in range(len(cedula)):
    qtd = valor // cedula[i]
    valor -= qtd * cedula[i]
    if qtd > 0:
        print(f'{qtd} cédula(s) de R$ {cedula[i]}')


