#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM POLINDROMO DESCONSIDERANDO OS ESPAÇOS.
print('Quer saber se a frase é um palíndromo?')
frase = input('Digite a frase para testar: ').replace(' ', '').lower()  # Remove espaços e coloca tudo em minúsculas
frase_reversa = frase[::-1]
if frase == frase[::-1]:  # Compara a frase normal com sua versão invertida
    print('É um palíndromo!')
    print(f'Frase para testar {frase}')
    print(f'Frase reversa: {frase_reversa}')  # Exibe a frase invertida

else:
    print('Não é um palíndromo.')