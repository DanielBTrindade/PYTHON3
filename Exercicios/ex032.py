#FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO
#MINHA SOLUÇÃO
from datetime import date
from calendar import isleap
#lidar com entradas inválidas
try:
    # Receber o ano
    ano = int(input('Que ano você quer analisar? Digite 0 para analisar o ano atual. '))
    # Se o ano for 0, usar o ano atual
    if ano == 0:
        ano = date.today().year
    # Verificar se o ano é bissexto
    bis = isleap(ano)
    # Exibir o resultado
    if bis:
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano de {ano} não é bissexto')
#mensagem de erro por não inserir um número valido
except ValueError:
    print('Erro: por favor, digite um número válido.')

