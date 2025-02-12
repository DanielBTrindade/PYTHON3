#FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE O VALOR DO
# SENO CONESSENO E TANGENTE DESSE âNGULO
#MINHA SOLUÇÃO
import math
x = float(input('Insira um ângulo qualquer em graus: '))
#Converte o ângulo x de graus para radianos.
r = math.radians(x)
#Retorna o cosseno X
c = math.cos(r)
#Retorna o seno de X
s = math.sin(r)
#Retorna o tangente de X
t = math.tan(r)
print(f'O valor do cosseno é {c:.4f}')
print(f'O valor de seno é {s:.4f}')
print(f'O valor da tangente é {t:.4f}')
