num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))

if num1>num2:
    print('O número {} é maior que o {}'.format(num1, num2))
elif num1<num2:
    print('O número {} é maior que o {}'.format(num2, num2))
else:
    print('Não existe valor maior, os dois são iguais')