# FAÇA UM PROGRAMA QUE CALCULE A NOMA ENTRE TODOS OS NÚMEROS IMPARES QUE SÃO
# MÚLTIPLOS DE 3 E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500
s = 0
for c in range(3, 501, 3):
    s += c
print(f'A soma de todos os múltiplos de 3 entre 1 até 500 é {s}')
