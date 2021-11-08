import random

print('Digite o nome dos alunos: ')
aluno1 = (input(''))
aluno2 = (input(''))
aluno3 = (input(''))
aluno4 = (input(''))
lista = [aluno1, aluno2, aluno3, aluno4]

sorteio = random.choice(lista)

print('O escolhido foi {}'.format(sorteio))