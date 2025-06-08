# FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E DIGA SE ELA É OU NÃO UM NUMERO PRIMO
import math
n = int(input("Verificar números primos ate: "))
mult = 0

for c in range(2,n): #testa os múltiplos. de N no intervalo entre 2 e N
    if n % c == 0:
        print("Múltiplo de",c)
        mult += 1

if mult == 0:
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)
