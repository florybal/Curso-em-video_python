cont = 1
while True:
    print(cont, '', end='')
    cont += 1
print('Acabou')

#trabalhando com flags
#flag = ponto de parada
n = 0
while n !=99: #99 é p flag
    n = int(input("digite um numero: "))
    cont += 1

#trabalhando com contador
n = cont = 0
while cont <5:
    n = int(input("Dgite um numero: "))
    cont += 1

#somando
n = s = 0
while n !=99: #99 é p flag
    n = int(input("digite um numero: "))
    cont += 1
    s = s + n #somando s mais um numero
s -= 999 # gambiarra
print("A soma vale {}".format(s))


n = s = 0
while True: #99 é p flag
    n = int(input("digite um numero: "))
    cont += 1
    if n == 999: #metodo certo
        break
    s = s + n  #ou s += n
print("A soma vale {}".format(s))


#fstrings
print(f"A soma vale {s}")

nome ='jose'
idade = 33
salario = 9978.3
print(f'o {nomme:-^20} tem {idade} anos e ganha R${salario:.2f}')
