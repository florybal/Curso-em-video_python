"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
"""
from random import randint

print("Jogo")
print("Par ou impar")

cont = 0
computador = randint(0, 1)
vit = False

while vit == False:
    jogador = int(input("0 [par] 1 [impar] "))
    if jogador != computador:
        print("Perdeu")
        break
    else:
        print("Ganhou!!")
        cont += 1