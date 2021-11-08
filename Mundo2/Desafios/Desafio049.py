num = int(input("Qual tabuada você quer?"))

for n in range(1, 11):
    print("|{} x {:2} = {} |".format(num, n, num*n))