numero = int(input('Digite um número: '))
sepa = numero % 2

if sepa == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é impar '.format(numero))
