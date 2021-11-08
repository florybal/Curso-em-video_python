num1 = int(input('Digite um numero: '))
num2 = int(input('Digite mais um numero cara: '))
num3 = int(input('Eu sei que ta chato, mas esse é o ultimo: '))

if num1>num2:
    if num1>num3:
        print('O primeiro {}, número é maior'.format(num1))
if num2>num1:
    if num2>num3:
        print('O segundo {}, número é maior'.format(num2))
if num3>num1:
    if num3>num2:
        print('O terceiro {}, número é maior'.format(num3))
        