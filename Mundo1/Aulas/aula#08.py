import  random
import emoji
from math import sqrt, floor

print(emoji.emojize("Olá, mundo :earth_americas:", use_aliases=True))
num = random.randint(1, 15)
print(num)

num = int(input("Digite um numero: "))
raiz = sqrt(num)

print("A raiz de {} é igual {}".format(num, floor(raiz)))
