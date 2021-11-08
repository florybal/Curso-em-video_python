from random import shuffle

aluno1 = str(input('Escreva o nome primeiro aluno:'))
aluno2 = str(input('Escreva o nome do segundo aluno:'))
aluno3 = str(input('Escreva o nome do terceiro aluno: '))
aluno4 = str(input('Escreva o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação sera:')
print(lista)
