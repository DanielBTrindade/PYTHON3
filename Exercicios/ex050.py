#DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS
#DAQUELES QUE FOREM PARES. SE O VALOR FOR IMPAR DESCONSIDERE-O.
s = 0
pares = []
for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        pares.append(n)
        s += n
print(f'Números Pares: {pares}')
print(f'A soma dos números pares é: {s}')