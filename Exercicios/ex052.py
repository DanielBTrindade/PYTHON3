# FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E DIGA SE ELA É OU NÃO UM NUMERO PRIMO
n = int(input("Verificar números primos ate: "))
multiplos = 0

for count in range(2,n):
    if (n % count == 0):
            print("Múltiplo de",count)
        multiplos += 1

if(multiplos==0):
    print("É primo")
else:
    print("Tem",multiplos," múltiplos acima de 2 e abaixo de",n)
