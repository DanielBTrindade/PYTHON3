#CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO.  O PROGRAMA SO VAI PARAR QUANDO O
# USUÁRIO DIGITAR O VALOR 999 QUE É A CONDIÇÃO DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM
# DIGITADOS E A SOMA ENTRE ELES (DESCONSIDERE O FLAG)

try:
    numeros = []
    while True:
        n = int(input('Digite um número (999 pra sair): '))
        if n == 999:
            break
        numeros.append(n)
    cont = len(numeros)
    soma = sum(numeros)

    print(f'Foram digitados {cont} números.')
    print(f'A Soma dos números é: {soma}')
    print(f'Os números digitados foram {numeros}')
    print(f'O maior número é {max(numeros)}, e o menor é {min(numeros)}')

    if cont > 0:
        print(f'A média dos valores é {soma / cont:.2f}')
    else:
        print('Nenhum número válido foi digitado.')


except ValueError:
    print('Valor inválido... Tente novamente.')
