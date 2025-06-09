#DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS
#DAQUELES QUE FOREM PARES. SE O VALOR FOR IMPAR DESCONSIDERE-O.
s = 0
pares = [] # Inicializa uma lista vazia

for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        pares.append(n)# Adiciona o número à lista
        s += n

print(f'Números Pares: {pares}')
print(f'A soma dos números pares é: {s}')
