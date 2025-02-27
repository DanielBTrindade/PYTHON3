print('\33[1;31;43mOlá mundo\033[m')
print('\33[4;30;45mOlá mundo\033[m')
print('\33[1;36;47mOlá mundo\033[m')
print('\33[30;41mOlá mundo\033[m')
nome = 'DANIEL'
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',
    'pretoebranco': '\033[7;30m',
    'negrito': '\033[1m',
    'sublinhado': '\033[4m'
}
# Exemplo de uso
print(f'Olá! Muito prazer em te conhecer, {cores["verde"]}{nome}{cores["limpa"]}')

