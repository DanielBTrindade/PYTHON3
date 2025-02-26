#DESAFIO 07
#CRIE UM ALGORITMO QUE LEIA UM NUMERO E MOSTRE O DOBRO O TRIPLO E A RAIZ QUADRADA
n1 = int(input('Digite um numero: '))
print('O Dobro de {} é: {}'.format(n1, n1*2))
print('O Triplo de {} é: {}'.format(n1, n1*3))
#CALCULAR RAIZ QUADRADA
print('A Raiz quadrada de {} é: {:.3f}'.format(n1, (n1**(1/2))))
print('A Raiz quadrada de {} é: {:.2f}'.format(n1, pow(n1, (1/2))))