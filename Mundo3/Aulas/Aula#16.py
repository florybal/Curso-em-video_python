#tuplas
#tuplas são imutáveis

#tuplas = ()
#lista = []
#dicionario = {}
"""
lanche = ("Hamburguer", "suco", "Pizza", "Pudim")
# ou : lanche = "Hamburguesr", "suco", "Pizza", "Pudim"
print(f"quantidade de itens na tupla: {len(lanche)}")

#fatiamento
print(lanche[1])
#lanche[1] = ("refrigerante")
#tuplas são imutáveis

print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])#até o final
print(lanche[:2])
print(lanche[-2:])

# 3 maneiras de fazer a mesma coisa :
print("1º maneira: ")
for comida in lanche:
    print(f"Vou comer {comida}")
print("2º maneiraa: ")
for cont in range(0, len(lanche)):
    print(f"vou comer {lanche[cont]} na posição {cont}")#print na posição do contador
print("3º maneira: ")
for pos, comida in enumerate(lanche):
    print(f"Vou comer {comida} na posição{pos}")

print("comi pra caramba!")

print(sorted(lanche))#não mudou a ordem, mandou mostrar em ordem
print(lanche)
"""
"""
a = (2,5,4)
b = (5,8,1,2)
c = a+b #adiciona a tupla b em a
print(c)
print(sorted(c))
print(len(c))
print(c.count(5))#quantas vezes aparece 5 em c
print(c.index(2))#em que posição está o número em questão
"""

pessoa = (13, "gustavo", 99.5, "M")#Possivel ter dados diferentes nas tuplas
print(pessoa)
#para mudar a tupla podemos:
del(pessoa)
#não da de apagar apenas um item na tupla, apenas a tupla inteira
pessoa = (13, "lucas", 62.3, "M")
print(pessoa)


