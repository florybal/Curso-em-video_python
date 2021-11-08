#Tranformação de strings

frase = ('Curso em Video Python')

print(frase[3]) #print 4° letra 3
print(frase[3:13]) # print 4° letra até a 12
print(frase[:16]) #print do inicio até o 12
print(frase[13:]) #print da letra 12 até o final
print(frase[0:15:2]) #print da primeira letra até 14 pulando de duas em duas letras

print("""sock.connect((host, port))
ConnectionRefusedError: [WinError 10061] 
Nenhuma conexão pôde ser feita porque a máquina 
de destino as recusou ativamente""")

print(frase.count('o')) #conta o número de 'o'
print(frase.upper().count('O')) #converte a frase para maiusculo e conta o número de 'O'
print(len(frase)) #conta o ñ de letras (espaços conta)
print(len(frase.strip())) #corta os espaços excedentes(da esquerda, e direita)
print(frase.replace('Python', 'Pau')) #troca o x, pelo y no print

frase = frase.replace('Curso', 'Tema') #Agora sim, altera a frase
print(frase)

print('Tema' in frase)
print(frase.find('Python')) #encontra a frase em uma posição SE estiver na string, caso não a posição é -1

print(frase.split()) #Divide a frase criando uma lista pelos espaços vazios
divido = frase.split()
print(divido[0]) #primeiro componente da lista
print(divido[0][2]) #segunda letra do primeiro componente da lista
