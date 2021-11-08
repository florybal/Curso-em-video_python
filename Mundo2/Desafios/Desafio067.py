"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido 
quando o número solicitado for negativo.
"""
from time import sleep

print("Tabuada")
sleep(1)
n = int(input("Digite um número: "))
cont = 1
while True:
    for c in range(0,11):
        print(f"|{n} x {c:2} = {c*n}|")
    n += 1
    if n < 0:
        break
    if n > 10:
        break