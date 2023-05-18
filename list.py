x = list()
for i in range(0,5):
    valor = int(input("Digite um valor inteiro:"))
    x.append(valor)
print(x)
x.sort(reverse=False)
print(x)
x.sort(reverse=True)
print(x)