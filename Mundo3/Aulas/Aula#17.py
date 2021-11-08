#Aula de lista

#tupla = ()
#lista = []

#o comando append('') adiciona o elemento ao final da lista
#para adicionar a um ponto especifico usamos: insert(posição,'valor')

#metodos de apagar algo da lista

#del lanche[3]
#lanche.pop(3)
#lanche.pop() sem declarar valor, apaga o ultimo valor
#lanche.remove('valor')
"""
num=(1,2,5,9,1)
print(num)
n = [2,5,3,9,5,3]
print(n)
n[2] = 53
print(n)
n.append(7)
n.sort(reverse=True)
n.insert(2, 0)
n.pop()
n.pop(2)
n.remove(9)#remove o primeiro algarismo que aparece
print(n)
print(f'Essa lista tem {len(n)} elementos!')
if 4 in n:
    n.remove(4)
else:
    print("Não achei o número 4")
print(n)
"""
"""
valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, valor in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {valor}")
print("Cheguei ao final da lista.")
"""
a = [2,3,4,7]
b = a #esta fazendo uma ligação entre as listas
c = b[:]#copiou os valores de b
b[2] = 8
c[0] = 53
print(f'A lista A ta com {a}')
print(f'A lista B ta com {b}')
print(f'A lista C ta com {c}')
