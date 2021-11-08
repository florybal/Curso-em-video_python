"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar 
em uma lista. Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
"""

#Não ta indo todos os números para a lista de pares e impares

valores = list()
par = list()
impar = list()

while True:
    num = int(input("Digite vários números: "))
    valores.append(num)
    resp = str(input("Quer continuar?[S/N] ")).upper()
    if resp in "nN":
        break
    if num %2 == 0:
        par.append(num)
    elif num %2 == 1 or num %2 != 0:
        impar.append(num)
    
"""
for i, v in enumerate(num):
    if v %2 ==0:
        par.append(v)
    elif v %2 != 0:
        impar.append(v)
"""
print(valores)
print(par)
print(impar)