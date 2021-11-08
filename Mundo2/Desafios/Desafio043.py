print('-='*8)
print('Peso ideial')
print('-='*8)

print('Digite seu peso e sua altura: ')

peso = float(input(''))
altura = float(input(''))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso ')
elif imc > 18.5 < 25:
    print('Peso ideal')
elif imc > 25 < 30:
    print('Sobrepeso')
elif imc > 30 < 40:
    print('Obesidade')
else:
    print('Obesidade Móbida')