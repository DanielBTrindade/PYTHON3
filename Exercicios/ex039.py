#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME DE ACORDO COM SUA IDADE
#-SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR
#- SE É A HORA DE SE ALISTAR
#- SE JA PASSOU A HORA DE SE ALISTAR
#O PROGRAMA TAMBÉM DEVE MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.
from datetime import datetime
ano = int(input('DIGITE sua data de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - ano
ano_alistamento = ano + 18
falta = 18 - idade
if idade < 18:
    print(f'Ainda não chegou o ano do seu alistamento. \nVocê deve se alistar em {ano_alistamento}.\nFalta {falta} anos para seu alistamento.')
elif idade == 18:
    print('PARABÉNS, ESSE É O ANO DO SEU ALISTAMENTO.')
elif idade > 18:
    print(f'Já passou o ano do seu alistamento.\nDeveria ter se alistado em {ano_alistamento}.\nJa passaram {falta} anos do seu alistamento.')
else:
    print('INFORMAÇÃO INVÁLIDA.\nTENTE NOVAMENTE.')



