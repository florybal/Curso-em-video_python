"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
import random

list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_adv = random.choice(list_of_numbers)
 
print(num_adv)
vit = False

while vit == False:
    print("jogo da advinhação")
    num = int(input("Digite um numero entre 0 e 10: "))
    if num > num_adv:
        print("Passou longe")
    elif num < num_adv:
        print("Não chegou perto")
    else:
        print("VOCÊ ACERTOU! PARABENS")
        vit = True

"""
ou:
computador = randint(1, 10)
contador = 0
acertou = False

while not acertou:
    jogador = int(input("Digite um numero entre 1 e 10: "))
    contador += 1
    if jogador == computador:
        print("Voce ganhou!")
        acertou = True
    else:
        if jogador<computador:
            print("Mais...tente mais uma vez")
        elif jogador > computador:
            print("Menos... tente mais uma vez")
print("Acertou com {} palpites".format(palpites))
"""