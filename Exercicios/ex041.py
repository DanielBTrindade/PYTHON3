#A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA
#E MOSTRE SUA CATEGORIA CONFORME A IDADE.
#- ATÉ 9 ANOS: MIRIM
#- ATÉ 14 ANOS: INFANTIL
#- ATÉ 19 ANOS: JUNIOR
#- ATÉ 20 ANOS: SENIOR
#- ACIMA MASTER
from datetime import datetime

try:
    nome = input('Digite o nome do atleta: ').title()
    ano_atual = datetime.now().year
    nasc = input('Digite o ano de nascimento do atleta: ')
    
    if not nasc.isdigit() or not (1900 <= int(nasc) <= ano_atual):
        raise ValueError('Ano de nascimento inválido. Digite um ano entre 1900 e o ano atual.')

    nasc = int(nasc)
    idade = ano_atual - nasc
    print(f'{nome} tem {idade} anos.')

    if idade <= 9:
        categoria = 'MIRIM'
    elif idade <= 14:
        categoria = 'INFANTIL'
    elif idade <= 19:
        categoria = 'JÚNIOR'
    elif idade <= 20:
        categoria = 'SÊNIOR'
    else:
        categoria = 'MASTER'

    print(f'A categoria do atleta {nome} é {categoria}.')

except ValueError as e:
    print(f'Erro! {e} Tente Novamente!')