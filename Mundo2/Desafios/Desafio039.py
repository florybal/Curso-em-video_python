from time import sleep
from datetime import date

print('-'*31)
print('Informe sua data de nascimento: ')
print('-'*31)

dia = int(input(''))
mes = str(input(''))
ano = int(input(''))
Atual = date.today().year
conta = Atual - ano

if conta == 18:
    fez = str(input('Já fez seu alistamento Militar? '))
    if fez == 'não':
        print('Ta na hora de se alistar mermao')
        print('DIA 11 DE JULHO VAGABUNDO')
    else:
        print('Apresente-se na esquida do teu cu')
elif conta > 18:
    saldo = conta - 18
    print('Você já deveria ter se alistado há {}'.format(saldo))
else:
    saldo = 18 - conta
    print('Ainda faltam {} anos para o alistamento, teras até dia 11 de julho para se alistar!'.format(saldo))
