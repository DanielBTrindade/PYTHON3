#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO, SE ELE ULTRAPASSAR 80 KM/H
#MOSTRA QUE ELE FOI MULTADO,  A MULTA  VAI CUSTAR R$7 POR CADA KM ACIMA DO LIMITE
from time import sleep
# Leitura da velocidade do carro
velocidade = int(input('Qual a velocidade do veículo? '))
# Verificação da velocidade
if velocidade > 80:
    # Cálculo do valor da multa
    multa = (velocidade - 80) * 7
    print('PROCESSANDO...')
    sleep(2) # Pausar a execução do programa
    print(f'Você sera multado em {multa} por exceder a velocidade permitida')
else:
    # Exibição da mensagem caso não haja multa
    print('OBRIGADO POR SEGUIR AS LEIS DE TRANSITO, BOA VIAGEM')