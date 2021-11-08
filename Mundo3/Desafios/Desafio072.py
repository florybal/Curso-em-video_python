"""
Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado 
(entre 0 e 20) e mostrá-lo por extenso.
"""
n = 0
#sim = 0
cont = ('zero', 'um', 'dois','tres','quatro','cinco', 'seis','sete',
 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
 'dezesseis', 'dezesete','dezoito','deznove','vinte')

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num >= 0 and num <= 20:
        for c in range(0, num):
            n+= 1
        print("-=" * 15)
        print(f'Você digitou o Número {cont[n]}')
        print("-="*15)
    print("tente novamente.", end=' ')
"""
        print("Você quer continuar? ")
        
        perguntao = str(input(" ")).strip().upper()[0]

        if perguntao == "Ss":
            sim == 0
        if perguntao == "Nn":
            sim == 1
"""