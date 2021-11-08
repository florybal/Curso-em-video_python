from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura """)
jogador = int(input("Qual é sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("Po!!!")

print("-="*12)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print("-="*12)

if computador == 0:
    if jogador == 0:
        print("empate")
    elif jogador == 1:
        print("Jogador ganhou")
    elif jogador == 2:
        print("Computador Ganhou")
    else:
        print("Jogada inválida")
elif computador == 1:
    if jogador == 0:
        print("Computador Ganhou")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("Jogador ganhou")
    else:
        print("Jogada Inválida")
else:
    if jogador == 0:
        print("Jogador ganhou")
    elif jogador == 1:
        print("Computador ganhou")
    elif jogador == 2:
        print("Empate")
    else:
        print("Jogada inválida!")
"""
import pygame 
from pygame.locals import*

pygame.init()
size = Width, Height = 360, 520
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

def main():
    while 1:
        for event_var in pygame.event.get():
            if event_var.type == QUIT:
                pygame.quit()
                return
            elif event_var.type == MOUSEWHEEL:
                print(event_var)
        clock.tick(60)
        pygame.display.flip()
pygame.__package__
main()

"""