#CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE,
#SEu PROGRAMA DEVERA LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO.
numero = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' ]

while True:

    num = int(input('Digite um numero de 0 a 20: '))
    if num == 999:
        print('VOLTE SEMPRE!')
        break
    if num < 0 or num > 20:
        print('TENTE NOVAMENTE!', end = ' ')
        continue


    print(f'O numero {num}, por extenso se escreve {numero[num]}.')
