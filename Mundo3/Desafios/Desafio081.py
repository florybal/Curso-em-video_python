"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:                                                                                                                                                
A) Quantos números foram digitados.                                                                                                                   
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = list()

while True:
    num = int(input("Digite um número: ")) 
    lista.append(num)
    resp = str(input("Quer continuar?[S/N] ")).upper()
    if resp in "nN":
        break

print(len(lista))
lista.sort(reverse=True)
print(sorted(lista)) #tentar fazer pelo outro metodo
if '5' in lista:
    print("O número 5 está na lista")
else:
    print("O número 5 não está na lista")

