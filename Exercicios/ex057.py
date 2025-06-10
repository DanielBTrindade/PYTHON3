#FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SO ACEITA OS VALORES 'M' OU 'F'. CASO ESTEJA ERRADO, PEÇA A
#DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.

'''while True:
    sexo = str(input('Qual seu sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        print(f'{sexo}')
        print('Obrigado!')
        break
    else:
        print('Opção Inválida. Tente Novamente!')
print('FIM!!')'''

sexo = str(input('Qual seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Informe seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo {sexo}, registrado com sucesso.')

