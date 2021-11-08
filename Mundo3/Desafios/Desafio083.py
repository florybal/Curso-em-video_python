"""
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar se a expressão passada está
com os parênteses abertos e fechados na ordem correta
"""
char = str(input(" Digite uma expressão: "))
list = []

for simb in char:
    if simb == '(':      #para cada parenteses que ele encontrar ele vai adicionar 
        list.append('(') #na lista 
    elif simb == ')':    # e verificar se tem um parenteses a mais
        if len(list) > 0 :
            list.pop()   #tira o parenteses da lista
        else:
            list.append(')')
            break
if len(list) == 0:
    print("Sua expressão é válida")
else:
    print("Sua expressão está errada")