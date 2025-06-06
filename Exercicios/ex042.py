#REFORÇA O DESAFIO 35 DOS 3 TRIANGULOS ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIANGULO SERA FORMADO
#- EQUILATERO: TODOS OS LADOS IGUAIS
#- ISOCELES: DOIS LADOS IGUAIS
#- ESCALENO: TODOS OS LADOS DIFERENTES
try:
    #Receber os valores
    a = float(input('Primeira reta: '))
    b = float(input('Segunda reta: '))
    c = float(input('Terceira reta: '))
    # Verificar se as retas podem formar um triângulo
    if a + b > c and a + c > b and b + c > a:
        print(f'Os valores {a}, {b}, {c} podem formar um triângulo.')

        if a == b == c:
            print('Esse triângulo é EQUILATERO.')
        elif a == b or a == c or b == c:
            print('Esse triângulo é ISÓSCELES.')
        else:
            print('Esse triângulo é ESCALENO.')

    else:
        print(f'Os valores {a}, {b}, {c} não podem formar um triângulo.')

except ValueError:
    print('Insira um valor válido!')