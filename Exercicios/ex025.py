#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSO E DIGA SE ELA TEM SILVA NO NOME
#A MINHA SOLUÇÃO
nome = str(input('Qual o seu nome? ')).strip().lower()
if 'trindade' in nome:
    print('Você é um TRINDADE 🫡.')
else:
    print('Você não é um TRINDADE 🫡.')
#solução do professor
n = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem silva? {}'.format('silva' in n.lower()))
