"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""
qtd = pmil = gasto = maior = menor = 0
barato = ''

print("Compraas")

while True:
    produto = str(input("Qual o nome do produto: "))
    preco = float(input("Informe o preço do produto: R$"))
    qtd += 1
    gasto += preco
    if preco >= 1000:
        pmil+=1
    if qtd == 1 or preco < menor:
        menor = preco
        barato = produto
    pergunta = ' '
    while pergunta not in "SN":
        pergunta = str(input("Quer continuar? [sim] [não]\n")).strip().upper()[0]
    if pergunta == "N":
        break
print("{:-^40}".format(" FIM DO PROGRAMA "))
print(f"O gasto total na compra de {qtd} produtos foi de {gasto:.2f} ")
print(f"{pmil} produtos custaram mais de R$:1000")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")
