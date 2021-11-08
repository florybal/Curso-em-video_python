nome = str(input('Digite seu nome completo:'))
nomes = nome.split()

print('Nome: {}'.format(nomes[0]))
print('Sobrenome: {}'.format(nomes[len(nomes)-1]))
