"""
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário
se ele quer mostrar mais alguns termos. O programa encerrará quando
ele disser que quer mostrar 0 termos.
"""

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
dnv = 0
mais = 10

while mais !=0:
    dnv = dnv + mais
    while cont <= dnv:
        print("{} ->".format(termo), end=' ')
        termo += razao
        cont += 1
    print("pausa")
    mais = int(input("Quantos termos você mostrar a mais? "))
print("progressão terminada com {} termos mostrados".format(dnv))
