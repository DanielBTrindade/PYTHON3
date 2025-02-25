#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE
#-QUANTAS VEZES APARECE A LETRA 'A'
#-EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ-EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ
#MINHA SOLUÇÃO
frase = str(input('Digite uma frase qualquer: ')).strip().lower()
q_a = frase.count('a')
primeiro_a = frase.find('a')+1
ultimo_a = frase.rfind('a')+1
if 'a' in frase:
    print(f'A frase possui {q_a} A.')
    print(f'A primeira vez ele aparece na posição {primeiro_a}')
    print(f'A última vez que ele aparece e na posição {ultimo_a}')
else:
    print('Não possui "A" na frase.')
