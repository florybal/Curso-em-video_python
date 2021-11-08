soma = 0 #acumalddor
cont = 0 #contador
for n in range(1, 501, 2):
    if n %3 == 0:
        cont += 1
        soma += n
print(cont, soma)

