#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE 3 RETAS E DIGA AO USUÁRIO
#SE ELAS PODEM OU NÃO SER UM TRIÂNGULO
try:
    #Receber os valores
    a = float(input('Primeira reta: '))
    b = float(input('Segunda reta: '))
    c = float(input('Terceira reta: '))
    # Verificar se as retas podem formar um triângulo
    if a + b > c and a + c > b and b + c > a:
        print(f'Os valores {a, b, c} podem formar um triângulo.')
    else:
        print(f'Os valores {a, b, c} não podem formar um triângulo.')
except ValueError:
    print('Insira um valor válido!')