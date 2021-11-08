from time import sleep

num =  int(input('Digite um número qualquer: '))

print('PROCESSANDO...')
sleep(1)
print("""Escolha uma das bases para conversão:
    [1] Converter para Binário
    [2] Converter para Octal
    [3] Converter para Hexadecimal
""")
pergunta = int(input('Sua opção: '))
print('PROCESSANDO...')
sleep(1)

if pergunta == 1:
    print('O número escolhido é {} e a base conversão é Binário'.format(num))
    print(bin(num))
elif pergunta == 2:
    print('O número escolhido é {} e a base conversão é Octal'.format(num))
    print(oct(num))
elif pergunta == 3:
    print('O número escolhido é {} e a base conversão é Hexadecimal'.format(num))
    print(hex(num))
else:
    print('Opção invalido') 