#REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER
#SO QUE AGORA UTILIZANDO UM LAÇO FOR
n = int(input('DIGITE o número que deseja saber a tabuada: '))
print(f'A tabuada do {n} é: ')
print('='*12)
for c in range(0, 11):
    print(f'{n} * {c} = {n * c}')
print('='*12)