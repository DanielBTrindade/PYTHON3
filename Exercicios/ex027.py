#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE EM SEGUIDA
#O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'Seu primeiro nome é: {n[0]}')
print(f'Seu último nome é: {n[-1]}')
