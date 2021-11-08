#nome = input("Qual seu nome? ")
#print("prazer em te conhecer {:=^20}".format(nome))
num1 = int(input("Um valor: "))
num2 = int(input("Outro valor: "))
s = num1 + num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2

#para quebrar a linha \n, para não quebrar a linha ',end= ' '   '
print("A soma é {}, \n o produto é {}, e a divisão é {:.3f}".format(s, m, d), end=' >> ')
print("A divisão inteira {} e a potencia {}".format(di, e))
