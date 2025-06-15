#MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI PENSAR EM UM NÚMERO ENTRE 0 E 10, SO QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR
#ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSARIOS.
from random import randint

while True:  # Reinicia o jogo completamente caso o usuário erre
    comp = randint(0, 10)  # Número aleatório entre 0 e 10
    cont = 1

    while True:
        try:
            x = int(input('Adivinhe o NÚMERO entre 0 e 10: '))

            # Se o número digitado for maior que 10, reinicia o jogo
            if x > 10:
                print('Número Inválido! O jogo será reiniciado...\n')
                break  # Sai do loop interno e reinicia o jogo

            while comp != x:
                cont += 1

                if comp < x:
                    x = int(input('Menos... Tente novamente: '))
                elif comp > x:
                    x = int(input('Mais... Tente novamente: '))

            print(f'Parabéns! ACERTOU!\nVocê precisou de {cont} tentativas.')
            exit()  # Termina o jogo ao acertar

        except ValueError:
            print('Entrada inválida! Digite um número inteiro.')