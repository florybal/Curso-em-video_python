'''
Crie um programa que leia um numero real qualquer pelo teclado e mostra sua porção
inteira.
EX. Digite um numero:6.127
o numero 6.127 tem a parte inteira 6
'''
from math import trunc

num1 = float(input('Digite um número: '))
print('o número {} tem a parte inteira {}'.format(num1, trunc(num1)))
#ou print('o numero {} tem a parte inteira {}'.format(num1, int(num))
