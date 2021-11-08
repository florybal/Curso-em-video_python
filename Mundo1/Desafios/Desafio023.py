"""
Faça um programa que leia um progra que leia um numero de 0 a 9999 e mostre
na tela cada um dos digitos separados.
EX. Digite um numero: 1834
unidade: 4
dezena: 3
centena:8
milhar:1
"""
'revisar'
num = int(input('Dgite um núemero de 0 a 9999:'))
u = num //1 % 10
d = num //10 % 10
c = num //100 % 10
m = num// 1000 % 10

print('Unidade:{}\nDezena:{}\nCentena:{}\nMilhar:{}'.format(u, d, c, m))
