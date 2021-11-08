from random import randrange 
from time import sleep

print('-='*28)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-='*28)
pc = randrange(0,5) 
num = int(input("Em que número eu pensei? "))
print('Processando...')
sleep(1)

if(num == pc):
    print('Acertou mizeravi!')
else:
    print('EROOOOOOU! eu pensei no {}'.format(pc))
