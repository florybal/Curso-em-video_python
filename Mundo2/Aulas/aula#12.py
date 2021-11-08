#estruturas de controle
#condições aninhadas

nome = str(input('Qual o seu nome? '))
if nome == 'Lucas':
    print('Que nome boito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil.') 
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal')
print('tenha um bom dia, {}!'.format(nome))
