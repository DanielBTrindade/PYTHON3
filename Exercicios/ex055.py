# FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS NO FINAL MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDO
maior = 0
nome_maior = ''
for p in range(0, 5):
    nome = input('Digite seu nome: ').title()
    peso = float(input('Digite seu peso: KG').replace(',', '.'))
    if peso > maior:
        maior = peso  # Atualiza 'maior' somente se 'peso' for maior
        nome_maior = nome
print(f'O {nome_maior}, tem o peso de KG {maior}.')
