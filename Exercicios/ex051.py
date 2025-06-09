# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA NO FINAL
# MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
pa = [n]
for c in range(9):
    n += r
    pa.append(n)
print(f'{pa}')
