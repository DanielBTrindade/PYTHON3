# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA
# COMEÇA OU NÃO COM O NOME "SANTO"
#A MINHA SOLUÇÃO
cidade = str(input('Digite o nome de uma cidade: ')).strip()
inicio = cidade.split()
if inicio[0].lower() == 'santo':
    print(f'A cidade começa com {inicio[0].upper()}')
else:
    print(f'A cidade não começa com o nome "SANTO" E sim com o nome {inicio[0].upper()}')
#SOLUÇÃO DO PROFESSOR
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')