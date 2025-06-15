'''cont = 1
while cont <+ 10:
    print(cont, ' -> ', end= '')
    cont += 1
print('FIM')'''
n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma é {s}')
print('FIM')