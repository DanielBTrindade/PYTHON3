#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO
#ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA
#MINHA SOLUÇÃO
from math import hypot
a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
hip = hypot(a,b)
print(f'A hipotenusa mede {hip:.2f}')