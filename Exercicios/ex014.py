#DESAFIO 14
#ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM ºC PARA ºF
#MINHA SOLUÇÃO
c = float(input('Qual a temperatura em Cº '))
f = c * 1.8 + 32
print(f'A temperatura de {c}ºC equivale a {f}ºF!')
#DE ºF PARA ºC
f = float(input('Qual a temperatura em ºF '))
c = (f - 32) * (5/9)
print(f'A temperatura de {f}ºF equivale a {c}ºC')

#SOLUÇÃO DO PROFESSOR
c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))
