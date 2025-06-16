#FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR. O JOGO SERA INTERROMPIDO QUANDO O JOGADOR PERDER.
#MOSTRANDO O TOTAL DE VITORIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO.
import random

print('Vamos jogar PAR ou IMPAR')
print('-=' *10)
cont = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = random.randint(1, 10)
    escolha = str(input('Escolha PAR / IMPAR:')).upper().strip()
    total = jogador + computador
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f'O resultado foi: {resultado}')
    if escolha == resultado:
        print('Parabéns você ganhou.')
        cont += 1
    else:
        print('O computador ganhou tente novamente.')
        print(f'Você ganhou {cont} vezes.')
        break
