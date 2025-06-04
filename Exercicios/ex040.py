#CRIE UM PROGRAMA QUE CALCULE DUAS NOTAS DE UM ALUNO
#E CALCULE SUA MEDIA MOSTRANDO UMA MENSAGEM DO FINAL,
#DE ACORDO COM A MEDIA ATINGIDA.
#- MÉDIA ABAIXO DE 5 : REPROVADO
#- MÉDIA ENTRE 5 E 6,9 : RECUPERAÇÃO
#- MÉDIA 7 OU SUPERIOR : APROVADO
try:
    nota1 = float(input("Digite a primeira nota: ").replace(",", "."))
    nota2 = float(input("Digite a segunda nota: ").replace(",", "."))

    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
        raise ValueError('As notas devem estar entre o e 10')

    media = (nota1 + nota2) / 2
    print(f'Sua média final é: {media:.2f}')

    if media >= 7:
        print('Parabéns você foi aprovado.')
    elif media <= 5:
        print('Você foi reprovado.')
    else:
        print('Você está em recuperação')

except ValueError:
    print("Erro! Certifique-se de digitar números válidos entre 0 e 10.")