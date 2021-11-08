from time import sleep
distanciaPNC = float(input('Por favor informe distancia percorrida, filha da puta: '))

if distanciaPNC <= 200:
    print('O valor da sua passagem é: ')
    print('Processando...')
    sleep(1)
    print('R${}'.format(0.5*distanciaPNC))
else:
    print('O valor da sua passagem é:')
    print('Processando...')
    sleep(1)
    print('R${}'.format(distanciaPNC*0.45))
