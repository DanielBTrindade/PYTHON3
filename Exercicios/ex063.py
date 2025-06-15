#ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E MOSTRE NA TELA OS N
# PRIMEIROS ELEMENTOS DE UMA SEQUENCIA DE FIBONACCI
n = int(input('Quantos números da sequência de Fibonacci quer ver? '))

a, b = 0, 1  # Início da sequência

print(a, end=' -> ')  # Primeiro número
print(b, end=' -> ')  # Segundo número

# Exibir primeiros 'n - 2' termos
for _ in range(n - 2):
    c = a + b
    a, b = b, c
    print(c, end=' -> ')

while True:  # Mantém o programa perguntando até o usuário decidir parar
    mais = int(input('\nMais quantos termos quer ver? (Digite 0 para sair): '))
    if mais == 0:
        break  # Sai do loop se o usuário não quiser mais termos

    for _ in range(mais):  # Gera mais termos conforme o usuário pedir
        c = a + b
        a, b = b, c
        print(c, end=' -> ')

print('FIM')  # Finaliza a execução