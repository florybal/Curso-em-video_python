print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

lado1 = float(input('Digite o primeiro segmento: '))
lado2 = float(input('Digite o segundo segmento: '))
lado3 = float(input('Digite o terceiro segmento: '))

if (lado2-lado3)< lado1 < (lado2+lado3):
    if (lado1-lado3) < lado2 <(lado1+lado3):
        if (lado1-lado2)< lado3 <(lado1+lado2):
            print('Os segmentos acima podem formar um triângulo!')
        else:    
            print('Os segmentos acima não podem formar um trinagulo')

"""
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

lado1 = float(input('Digite o primeiro segmento: '))
lado2 = float(input('Digite o segundo segmento: '))
lado3 = float(input('Digite o terceiro segmento: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um trinagulo')
"""