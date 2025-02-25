#CRIE UM PROGRAMA QUE LEIA UM NOME COMPLETO DE UMA PESSOA E MOSTRE
#O NOME EM MAIÚSCULA
#O NOME EM MINÚSCULA
#QUANTAS LETRAS AO TODO SEM CONSIDERAR OS ESPAÇOS
#QUANTAS LETRAS TEM O PRIMEIRO NOME
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome completo é {nome.title()}.')
print(f'Nome em MAIÚSCULO: {nome.upper()}.')
print(f'Nome em minúsculo: {nome.lower()}.')
print(f'Seu nome tem {len(nome)-nome.count(' ')} letras ao todo.')
primeiro_nome = nome.split()
print(f'Seu primeiro nome é {primeiro_nome[0]} e ele tem {len(primeiro_nome[0])} letras.')

