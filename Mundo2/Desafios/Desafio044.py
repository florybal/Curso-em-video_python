from time import sleep
print('¨¨¨¨'*12)
print(' Supermercado Vila Verde ')
print('¨¨¨¨'*12)

valor = float(input('Insira o valor do produto: '))
sleep(1)
print("""E qual a forma de pagamento você deseja:
[1] à vista dinheiro/cheque: 10% de desconto

[2] à vista no cartão: 5% de desconto

[3] em até 2X no cartão: preço formal

[4] 3X ou mais no cartão: 20% de juros
""")

pagamento = int(input('> '))

print("Foma de pagamento escolhida...")
sleep(1)
print("Processando...")
sleep(1)
if pagamento == 1:
    print("à vista dinheiro/cheque: 10% de desconto")
    print("O produto custava {:.2f}, com 10% de desconto ficou {:.2f}\n".format(valor, (valor - (valor*10/100))))
elif pagamento == 2:
    print("à vista no cartão: 5% de desconto")
    print("O produto custava {:.2f}, com 5% de descontou ficou {:.2f}\n".format(valor, (valor -(valor*5/100))))
elif pagamento == 3:
    print("em até 2X no cartão: preço formal")
    print("O produto custava {:.2f}, e em 2x ficou {:.2f}".format(valor, (valor/2)))
elif pagamento == 4:
    print("3X ou mais no cartão: 20% de juros")
    print("O produto custava {:.2f}, e em 3x ou mais ficou {}".format(valor, ()))
else:
    print("Por favor escolha uma forma de pagamento disponível.")