#Crie um programa que leia o nome completo de uma pessoa e mostre:
"""
-O nome completo com todas letras maiúsculas
-O nome com todas minusculas
-Quantas letras ao todo(sem considerar espaços)
-Quntas letras tem o primeiro nome
"""

nome = str(input('Digite seu nome completo:'))

print(nome.upper())
print(nome.lower())
print(len(nome.strip()))
nome1 = nome.split()
print(nome1[0]) 