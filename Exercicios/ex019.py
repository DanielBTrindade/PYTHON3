#UM PROFESSOR QUER SORTEAR UM DE SEUS QUATRO ALUNOS PARA APAGAR O QUADRO
#FAÇA UM PROGRAMA QUE AJUDE ELE LENDO O NOME DELES E ESCRENDO O NOME ESCOLHIDO
import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
lista = [a1, a2, a3, a4]
# Sorteaar um aluno da lista
print('O sorteado foi: ' + random.choice(lista))