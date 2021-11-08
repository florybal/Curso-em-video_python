""" 
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros 
colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem 
de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
"""


times = ('Grêmio', 'Internacional', 'São Paulo', 'Juventos', 'Barcelona',
'Santos', 'Vasco', 'Cruzeiro', 'Botafogo', 'Atlético', 'Coritiba', 'Arsenal',
'Brasil de pelotas', 'Água Negra', 'Chapecoense', 'Flamengo', 'Caxias',
'Pelotas', 'Fluminense', 'Brusque')

print(times[:5])
#for t in times:   
#   print(t)
print(times[-4:])
print(sorted(times))
print(f'O chapecoense está na posição {times.index("Chapecoense")}')
