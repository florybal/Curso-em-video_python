"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e
guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares
"""
a = 0
print("Digite 4 valores: ")
valor1=int(input(""))
valor2=int(input(""))
valor3=int(input(""))
valor4=int(input(""))

valores =(valor1, valor2, valor3, valor4)

print(valores)
print(f"O número de vezes que apareceu o número 9 foi de {valores.count(9)}º vezes")
if 3 in valores:
    print(f"A posição do primeiro número 3 foi na {valores.index(3+1)}°")
else:
    print("O valor 3 não foi digitado em nenhuma opção")
for n in valores: 
    if n %2==0:
        print(n)
print(f"Os números pares na tupla foram: {n}")