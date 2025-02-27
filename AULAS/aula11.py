print('\33[1;31;43mOlá mundo\033[m')
print('\33[4;30;45mOlá mundo\033[m')
print('\33[1;36;47mOlá mundo\033[m')
print('\33[30;41mOlá mundo\033[m')
nome = 'DANIEL'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print(f'Olá! Muito prazer em te conhecer,{cores["pretoebranco"]} {nome} {cores["limpa"]}')

