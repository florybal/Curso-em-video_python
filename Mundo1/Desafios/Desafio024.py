"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou 
não com nome 'santo' 
"""

cidade = str(input('Digite o nome da cidade:')).strip()

print(cidade[:5].upper() == 'Santo')
