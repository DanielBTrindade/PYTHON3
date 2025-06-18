#TUPLAS
#TUPLAS SÃO IMUTÁVEIS
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(len(lanche))
for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} na posição {cont}')
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida}, na posição {pos}')
print(sorted(lanche))#em ordem alfabetica
a = (2,5,4)
b = (5,8,1,2)
c = a+b
print(a)
print(b)
print(c)
#print(sorted(c))
print(len(c))
print(c.count(5))#quantas vezes aparece o 5 dentro de C
print(c.index(8))#em que posiçao está o 8
del(c)
