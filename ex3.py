notas = list()
media = 0
soma = 0 
for i in range(0,3):
    nota_dig = float(input("Digite uma nota:"))
    notas.append(nota_dig)
    soma = soma + notas[i]
media = soma/3
notas.sort(reverse=False)
menor = min(notas)
maior = max(notas)
print("A menor nota é",menor)
print("A maior nota é",maior)
print("A media das notas é:",media)
print(notas)