'''
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calucule
o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

print('carro alugado qualquer')
distancia = float(input('Informe a distancia percorrida: '))
dia = float(input('e os dias de uso:'))

print('O preço a pagar pelos dias e distancia percorrida pelo automovel são: R${}'.format(60*dia+0.15*distancia))
