"""
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e 
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.
"""
valores = list()
for c in range(0, 5):
    num = int(input(""))
    print(f'Digite {5-c} números: ')
    if c == 0 or c > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, c)
                break
            pos += 1
print(valores)

