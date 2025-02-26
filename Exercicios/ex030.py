#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPAR
# Recebimento do número
n = int(input('Digite um número: '))
#Verificar o tipo de numero, um numero é par se o resto da divisão por 2 for 0
par = n % 2
# se for par
if par == 0:
    print(f'O número {n} é par!')
# se for impar
else:
    print(f'O número {n} é impar!')
