"""
Escreva um programa para aprovar o empréstimo bancário para a compra 
de uma casa. Pergunte o valor da casa, o salário do comprador e em 
quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do 
salário ou então o empréstimo será negado.
"""
#revisar esse exercicio

from time import sleep

print('-='*12)
print('Sistema de Emprestimo')
print('-='*12)
sleep(2)

casa = float(input('Qual o valor da sua residência? '))
salario = float(input('Por favor, informe a sua renda: '))
ano = int(input('E em quantos anos você pretende pagar? '))
minimo = (salario *30 /100)
ValorAPagar = casa / (ano *12)

sleep(1)
print('-='*12)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, ano))
print('-='*12)
sleep(1)
print('A prestação será de R${:.2f}'.format(ValorAPagar))

if ValorAPagar <= minimo:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo NEGADO!')