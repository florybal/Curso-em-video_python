from time import sleep
velocidadeC = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidadeC - 80) * 7
print('Processando...')
sleep(1)

if velocidadeC > 80:
    print('Sua velocidade {:.2f}Km/h ultrapassou a velocidade limite de 80Km/h'.format(velocidadeC))
    print('Sua multa será de:')
    sleep(1)
    print('Processando...')
    sleep(1)
    print('R${:.2f}'.format(multa))
    print('Se fudeu otario!!')
else:
    print('Sua velocidade esta abaixo do limite')
    print('Pode seguir, bom cidadão!!')
