#MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI PENSAR EM UM NÚMERO ENTRE 0 E 10, SO QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR
#ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSARIOS.
import  random
comp = random.randint(0, 10)
cont = 0
while True:
    try:
        x = int(input('Adivinhe o NÚMERO entre 0 e 10: '))
        while comp != x:
            cont += 1
            x = int(input('Tente novamente:\nAdivinhe o NÚMERO entre 0 e 10: '))
        print(f'Parabéns! ACERTOU!\nO número que eu pensei foi, {comp}.\nVocê precisou de {cont} tentativas.')
        break

    except ValueError:
        print('Entrada inválida! Digite um número inteiro.')