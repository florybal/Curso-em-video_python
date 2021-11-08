"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
valores = []
maior = 0
menor = 0
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
    if cont == 0:
        maior = menor = valores
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f"O menors valor foi de {menor} e está na posição {valores[cont]}")
print(f"O maior valor foi de {maior}")

#print(f"O maior valor digitado foi {max(valores)}")
#print(f"O menor valor digitado foi {min(valores)}")
