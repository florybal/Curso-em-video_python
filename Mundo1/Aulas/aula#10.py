nome = str(input('Qual seu nome? '))
if nome == 'Lucas':
    print('Que nome lindo você tem!')
else:
    print('Que nome normal!')
print('bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print('A sua média foi de {:.1f}'.format(m))
if m>= 6.0:
    print('Sua média foi boa! Parabens')
else:
    print('Sua média foi ruim! Estude mais!!!')
# ou print('Parabens' if m>=6 else 'Estude mais')
