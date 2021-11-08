frase = str(input('Digite uma frase mermao:')).lower()

print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A letra A apareceu pela primeira vez na posição:{} '.format(frase.find('a')+1))
print('A letra A apareceu pela ultima vez na posição:'.format(frase.rfind('a')+1))
