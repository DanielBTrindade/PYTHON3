#CRIE UM PROGRAMA QUE LEIA UM NOME COMPLETO DE UMA PESSOA E MOSTRE
#O NOME EM MAIÚSCULA
#O NOME EM MINÚSCULA
#QUANTAS LETRAS AO TODO SEM CONSIDERAR OS ESPAÇOS
#QUANTAS LETRAS TEM O PRIMEIRO NOME
nome = str(input('Digite seu nome completo: '))
print(f'Seu nome completo é {nome.title()}.')
print(f'Nome em MAIÚSCULO: {nome.upper()}.')
print(f'Nome em minúsculo: {nome.lower()}.')
nome_sem_espacos = nome.replace(" ", "")
print(f'Seu nome tem {len(nome_sem_espacos)} letras ao todo.')
primeiro_nome = nome.split()[0]
print(f'Seu primteiro nome tem {len(primeiro_nome)} letras.')

