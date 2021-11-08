"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a 
digitar valores.
"""


cont = 1
soma = 0
dnv = 0

while dnv == 0:
    nums = int(input("Digite um número: "))
    cont += 1
    soma+=nums
    if cont == 5:
        nundnv = bool(input("Quer continuar? [1]não [0]sim "))
