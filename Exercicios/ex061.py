# REFORÇE O DESAFIO 51 LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS
#DA PA USANDO A ESTRUTURA WHITE
'''num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = [num]
print(num, end='->')

while len(pa) < 10:
    num += razao
    pa.append(num)
    print(num, end='->')

print('FIM')'''
print('GERADOR DE PA')
print('-=' *10)
primeiro = int(input('primeiro termo: '))
razao = int(input('razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, end='->')
    termo += razao
    cont += 1
print('FIM')

