#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE
#-QUANTAS VEZES APARECE A LETRA 'A'
#-EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ-EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ
#MINHA SOLUÇÃO
frase = str(input('Digite uma frase qualquer: ')).strip().lower()
if 'a' in frase:
    print(f'A frase possui {frase.count('a')} A.')
    print(f'A primeira vez ele aparece na posição {frase.find('a')+1}')
    print(f'A última vez que ele aparece e na posição {frase.rfind('a')+1}')
else:
    print('Não possui "A" na frase.')
