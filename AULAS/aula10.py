#tempo = int(input('Quantos anos tem seu carro? '))
#if tempo <= 3:
#    print("Carro novo")
#else:
#    print('Carro velho')
#print('--FIM--')
#print('Carro novo' if tempo <= 3 else 'Carro velho')
#nome = str(input('Qual é o seu nome? ')).title()
#if nome == 'Daniel':
#    print('Que nome lindo!!!')
#else:
#   print(f'Bom dia {nome}')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média é {m:.1f}')
if m >= 6:
    print('Você foi aprovado!')
else:
    print('Você Foi reprovado!!')