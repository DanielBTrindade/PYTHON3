#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO, SE ELE ULTRAPASSAR 80 KM/H
#MOSTRA QUE ELE FOI MULTADO, A MULTA VAI CUSTAR R$7 POR CADA KM ACIMA DO LIMITE
#minha solução
from time import sleep
# Leitura da velocidade do carro
velocidade = int(input('Qual a velocidade do veículo? '))
# Verificação da velocidade
if velocidade > 80:
    # Cálculo do valor da multa
    multa = (velocidade - 80) * 7
    print('PROCESSANDO...')
    sleep(2) # Pausar a execução do programa
    print(f'Você sera multado em {multa} por exceder a velocidade permitida.')
else:
    # Exibição da mensagem caso não haja multa
    print('OBRIGADO POR SEGUIR AS LEIS DE TRANSITO, BOA VIAGEM')
print('Dirija com cuidado.')
#solução do professor
v = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido de 80 KM/H')
    m = (v - 80) * 7
    print(f'Você deve pagar uma multa de R${m:.2f}')
print('Tenha um bom dia! Dirija com segurança!')