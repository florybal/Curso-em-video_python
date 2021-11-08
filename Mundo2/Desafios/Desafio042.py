print('=-'*12)
print('Analisador de trinagulos')
print('-='*12)

print('Digite três lados para um tringulo: ')

lado1 = float(input(''))
lado2 = float(input(''))
lado3 = float(input(''))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
            if lado1 == lado2 == lado3:
                print('Este Triângulo é equilátero, todos lados iguais')
            elif lado1 != lado2 == lado3 or lado1 == lado2 != lado3 or lado3 != lado1 == lado2:
                print('Este Triângulo é um Isóceles, dois lados iguais, um diferente')
            else:
                print('Este Triângulo é um Escaleno, todos lados diferentes')
else:
    print('Os segmentos acima não podem formar um trinagulo')