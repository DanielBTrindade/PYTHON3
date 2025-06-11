#CREI UM PROGRAMA QUE LEIA 2 VALORES E MOSTRE UM MENU NA TELA SOMAR, MULTIPLICAR, MAIOR, NOVOS NÚMEROS, SAIR DO PROGRAMA
#SEU PROGRAMA DEVERA REALIZAR A OPERAÇÃO SOLICITADA A CADA CASO.
def obter_numero(mensagem): # garante que o usuario digite um valor valido
    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print('Valor Inválido! Digite um número válido.')

def obter_opcao():#garente que o usuario escolha uma opção valida no menu
    while True:
        try:
            opcao = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair\nEscolha um opção: '))
            if 1 <= opcao <= 5:
                return opcao
            else:
                print('Opção inválida! Escolha um número entre 1 e 5.')
        except ValueError:
            print('Entrada Inválida! Digite um número inteiro.')

n1 = obter_numero('Digite o 1º valor: ')
n2 = obter_numero('Digite o 2º valor: ')

while True:
    menu = obter_opcao()
    if menu == 1:
        print(f'A soma dos valores é: {n1 + n2}')
    elif menu == 2:
        print(f'A multiplicação dos valores é: {n1 * n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'O primeiro valor {n1}, é o maior.')
        elif n1 < n2:
            print(f'O segundo valor {n2}, é o maior.')
        else:
            print(f'Os valores são iguais.')
    elif menu == 4:
        n1 = obter_numero('Digite o 1º valor: ')
        n2 = obter_numero('Digite o 2º valor: ')
    elif menu == 5:
        print('Programa encerrado!')
        break