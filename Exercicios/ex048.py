# FAÇA UM PROGRAMA QUE CALCULE A NOMA ENTRE TODOS OS NÚMEROS IMPARES QUE SÃO
# MÚLTIPLOS DE 3 E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont+= 1
        s += c
print(f'A soma dos {cont} números que são impares e múltiplos de 3 entre 1 até 500 é {s}')
