#MELHORE O DESAFIO 061 PERGUNTANDO PARA O USUARIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS DA PROGRESSÃO
#O PROGRAMA ENCERRA QUANDO ELE FIZER QUE QUER MOSTRAR ZERO TERMOS
num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print(num, end=' -> ')

mais = 9
cont = 1

while mais != 0:
    cont += mais
    for _ in range(mais):  # Adicionando múltiplos termos de uma vez
        num += razao
        print(num, end=' -> ')
    print('PAUSA')

    mais = int(input('\nQuer ver mais quantos termos? '))
    print(f'Foram mostrados {cont} termos')

print('\nFIM')