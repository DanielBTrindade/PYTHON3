#O mesmo professor quer sortear a ordem de apresentação de trabalho dos alunos
#faça um programa que leia os nomes e mostre a ordem sorteada
import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
lista = [a1, a2, a3, a4]
# Sorteaar um aluno da lista
random.shuffle(lista)
print(f'A ordem sorteada dos alunos é: {lista}')

