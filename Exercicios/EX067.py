# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUÁRIO.
# O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO.
while True:
    n = int(input('Digite um número para ver a tabuada (Zero para sair): '))
    if n <= 0:
        break
    print('-=' * 10)
    for c in range(1, 11):
        tabuada = n * c

        print(f'{n} x {c} = {tabuada}')
    print('-=' * 10)
print('FIM')