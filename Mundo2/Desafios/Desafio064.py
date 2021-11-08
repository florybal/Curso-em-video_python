"""
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados 
e qual foi a soma entre eles (desconsiderando o flag).
"""

num = int(input("Digite uns numeros: "))
cont = 1
soma = 0
while num != 999:
    num = int(input("Digite o numero certo: "))
    cont += 1
    soma = soma + num
print(cont, soma)
