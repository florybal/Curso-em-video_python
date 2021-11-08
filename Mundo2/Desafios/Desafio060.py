"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
"""
from math import factorial

n = int(input("Digite um número: "))
f = factorial(n)

print('Calculando {}! ='.format(n), end='')
while n >0:
    print(' {}'.format(n), end='')
    print(' x'if n>1 else ' = {}'.format(f), end='')
    n-=1

#print('O fatorial de {}! é de {}'.format(n, f))
