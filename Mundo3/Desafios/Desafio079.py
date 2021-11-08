"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""

valores = list()
while True:
    num = int(input("Digite um número: "))
    if num not in valores:
        valores.append(num)
        print("Valor adicionado!")
    else:
        print("Valor duplicado, não adicionado!")
    
    r = str(input("Quer continuar?[s/n]"))
    if r in "Nn":
        break    
print(sorted(valores))
