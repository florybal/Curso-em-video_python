print('Digite suas notas: ')

num1 = float(input(''))
num2 = float(input(''))
num3 = float(input(''))
num4 = float(input(''))

media = (num1+num2+num3+num4)/4

if media >= 7:
    print('Sua nota foi de {}'.format(media))
    print('APROVADO')
elif media<7 and media >5:
    print('Sua nota foi de {}'.format(media))
    print('EM RECUPERAÇÃO')
else:
    print('Sua nota foi de {}'.format(media))
    print('REPROVADO')