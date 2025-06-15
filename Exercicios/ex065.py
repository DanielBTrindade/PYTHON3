#CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO, NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE
#TODOS OS VALORES QUAL FOI O MAIOR NUMERO LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO
#CONTINUAR A DIGITAR VALORES?

maior_numero = None
menor_numero = None
lista = []

while True:
    try:
        n = int(input('Digite um número inteiro (0 para sair): '))

        if n == 0:
            break

        lista.append(n)

        if maior_numero is None or n > maior_numero:
            maior_numero = n
        if menor_numero is None or n < menor_numero:
            menor_numero = n

        continuar = input('Quer continuar S/N: ').strip().upper()[0]
        while continuar not in ['S', 'N']:
            continuar = input('Opção inválida. Quer continuar S/N: ').strip().upper()[0]
        if continuar == 'N':
            break

    except ValueError:
        print('Entrada inválida. Digite apenas números inteiros.')

# Após o laço, exibe o resultado
if lista:
    soma = sum(lista)
    media = soma / len(lista)
    print(f'A média entre os números digitados é: {media:.2f}')
    print(f'O maior número digitado foi: {maior_numero}')
    print(f'O menor número digitado foi: {menor_numero}')
else:
    print('Nenhum valor válido digitado.')

print('FIM')
