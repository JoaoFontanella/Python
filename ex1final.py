num = list()
soma = 0
for i in range(0,10):
    num_dig = float(input("Digite uma numero:"))
    num.append(num_dig)
num.sort(reverse=True)
print(num)