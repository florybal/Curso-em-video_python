"""
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só
aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente 
até ter um valor correto.
"""

sexo = str(input("Digite seu sexo: ")).strip().upper()[0]

while sexo not in "MmFf":
    sexo = str(input("dados invalidos, digite novamente seu sexo: ")).strip().upper()[0]
print("seu sexo é {}".format(sexo))

