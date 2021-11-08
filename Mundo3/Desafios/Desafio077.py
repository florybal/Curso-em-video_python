"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('sargento', 'coronel', 'tunel', 'pastel', 'abobado', 'aliviado', 'maltratado')

for p in palavras:
    print(f'Na palavra {p} temos ')
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=' ')