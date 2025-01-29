#DESAFIO 07
#DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UMA ALUNA, CALCULE E MOSTRE SUA MÉDIA.
n1 = (float(input('Nota do primeiro semestre: ')))
n2 = (float(input('Nota do segundo semestre: ')))
print('A média entre {:.1f} e {:.1f} é {:.1f}'.format(n1, n2, (n1 + n2) / 2))
