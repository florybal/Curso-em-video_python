"""
Exercício Python 076: Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados 
em forma tabular.
"""

produtos = ("Cadedira", 200, "mesa", 400, "Tv", 1000, "Rádio",
600, "Sofá", 500, "lampáda", 15)

#print(f"Nome dos produtos: \n{produtos[0::2]}")
#print(f"Preço dos produtos: \n{produtos[1::2]}")

for pos in range(0, len(produtos)):
    if pos %2==0:
        print(f"Nome do produto: {produtos[pos]:30}")
    else:
        print(f"Preço do produto: R${produtos[pos]}")
