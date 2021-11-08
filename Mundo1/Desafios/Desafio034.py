from time import sleep

salario = float(input('Digite o seu salário: '))

if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print('O aumento do seu salário de R${:.2f} é de 10%'.format(salario))
    sleep(1)
    print('Processando...')
    sleep(1)
    print('Seu novo salário é de R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 15 /100)
    print('O aumento do seu salário de R${:.2f} é de 15%'.format(salario))
    sleep(1)
    print('Processando...')
    sleep(1)
    print('Seu novo salário é de R${:.2f}'.format(aumento))
