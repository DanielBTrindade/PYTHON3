#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM POLINDROMO DESCONSIDERANDO OS ESPAÇOS.
print('Quer saber se a frase é um palíndromo?')
frase = str(input('Digite a frase para testar: ').replace(' ', '').lower())  # Remove espaços e coloca tudo em minúsculas
frase_reversa = frase[::-1]
if frase == frase_reversa:  # Compara a frase normal com sua versão invertida
    print('É um palíndromo!')
    print(f'Frase para testar {frase}')
    print(f'Frase reversa: {frase_reversa}')  # Exibe a frase invertida

else:
    print(f'Não é um palíndromo. {frase_reversa}')