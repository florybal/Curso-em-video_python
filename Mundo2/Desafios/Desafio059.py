"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
soma = num1 + num2
multi = num1*num2
troca = False

while troca == False:
    print("Qual a operação você deseja: ")
    print("""
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
    """)
    escolha = int(input(" "))
    if escolha == 1:
        print("A opção escolhida foi: '[1] Somar'")
        print("Processando...")
        sleep(1)
        print("A soma entre os numeros {} e {} é {}".format(num1, num2, soma))
        troca = True
    elif escolha == 2:
        print("A opção escolhida foi: '[2] Multiplicar'")
        print("Processando...")
        sleep(1)
        print("A multiplicação entre os numeros {} e {} é {}".format(num1, num2, multi))
        troca = True
    elif escolha == 3:
        print("Processando...")
        sleep(1)
        print("A opção escolhida foi: '[3] Maior' ")
        print("Processando...")
        sleep(1)
        if num1>num2:
            print("O maior numero entre {} e {} é {}".format(num1, num2, num1))
            troca = True
        else:
            print("O maior numero entre {} e {} é {}".format(num1, num2, num2))
            troca = True
    elif escolha == 4:
        print("Processando....")
        sleep(1)
        print("A opção escolhida foi: '[4] Novos valores'")
        num1 = int(input("Digite o primeiro novo valor: "))
        num2 = int(input("Digite o segundo novo valor: "))
        print("O novos valores são: ")
        print("{}, {}".format(num1, num2))
        troca = True
    elif escolha == 5:
        print("Saindo do programa...")
        sleep(1)
        troca = True