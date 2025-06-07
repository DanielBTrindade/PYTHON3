#CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKEMPO COM VOCÊ.
import random

opcoes = ["PEDRA", "PAPEL", "TESOURA"]

while True:
    try:
        jogador = int(input('''
        Escolha sua jogada:
        [1] PEDRA
        [2] PAPEL
        [3] TESOURA
        Digite o número correspondente: '''))

        # Verifica se a entrada é válida
        if jogador not in [1, 2, 3]:
            print("Escolha inválida! Tente novamente.")
            continue  # Reinicia o loop

        escolha_jogador = opcoes[jogador - 1]
        escolha_computador = random.choice(opcoes)

        print(f"\nVocê escolheu: {escolha_jogador}")
        print(f"O computador escolheu: {escolha_computador}")

        # Determina o vencedor
        if escolha_jogador == escolha_computador:
            print("Empate!")
        elif (escolha_jogador == "PEDRA" and escolha_computador == "TESOURA") or \
             (escolha_jogador == "TESOURA" and escolha_computador == "PAPEL") or \
             (escolha_jogador == "PAPEL" and escolha_computador == "PEDRA"):
            print("Você venceu!")
        else:
            print("O computador venceu!")

        # Pergunta se deseja jogar novamente
        jogar_novamente = input("\nQuer jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            break  # Sai do loop se a resposta não for 's'

    except ValueError:
        print("Entrada inválida! Digite apenas números 1, 2 ou 3.")

print("Obrigado por jogar! 🎮")