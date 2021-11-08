"""
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
"""
from time import sleep

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input("Peso da {}° pessoa? ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {} KG".format(maior))
sleep(1)
print("Seu obeso")

sleep(1)
print("O menor peso lido foi {} KG".format(menor))
sleep(1)
print("Ta na hora de comer né")