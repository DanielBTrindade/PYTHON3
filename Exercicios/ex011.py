#DESAFIO 11
#FAÇA UM PROGRAMA QUE LEIA A ALTURA DE UMA PAREDE EM METROS CALCULE SUA ÁREA E A QUANTIDADE DE TINTA NECESSARIA PARA PINTÁ-LA,
#SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M²
#MINHA SOLUÇÃO
a = float(input('Quantos metros de altura?'))
l = float(input('Quantos metros de largura?'))
area: float = a * l
lt = area / 2
print('Sua parede tem {}M². Voce vai precisar de {} litros de tinta.'.format(area, lt))
#SOLUÇÃO DO PROFESSOR
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede você vai precisar de {}l de tinta.'.format(tinta))
