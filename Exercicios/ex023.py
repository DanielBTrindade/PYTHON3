#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA
# CADA UM DOS DIGITOS SEPARADOS
num = input('Digite um número entre 0 e 9999: ')
if not num.isdigit() or int(num) > 9999:
    print('Erro: Por favor insira um número inteiro entre 0 e 9999.')
else:
    n = num.zfill(4)
    print(f'Milhar: {n[0]}')
    print(f'Centena: {n[1]}')
    print(f'Dezena: {n[2]}')
    print(f'Unidade: {n[3]}')
