# FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS NO FINAL MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDO

maior = 0
menor = float('inf')  # Inicializa 'menor' com um valor alto para garantir a comparação correta
nome_maior = ''
nome_menor = ''

for p in range(5):  # Não é necessário usar 'range(0, 5)', apenas 'range(5)' já funciona
    nome = input('Digite seu nome: ').title()
    peso = float(input('Digite seu peso: KG ').replace(',', '.'))

    if peso > maior:
        maior = peso
        nome_maior = nome

    if peso < menor:  # Agora compara corretamente para encontrar o menor peso
        menor = peso
        nome_menor = nome

print(f'O {nome_maior} tem o maior peso: {maior} KG.')
print(f'O {nome_menor} tem o menor peso: {menor} KG.')  # Corrigida a mensagem
