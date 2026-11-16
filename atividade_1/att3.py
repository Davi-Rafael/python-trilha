num1, num2, num3 = input().split(' ')
lista = []
num1 = lista.append(int(num1))
num2 = lista.append(int(num2))
num3 = lista.append(int(num3))
crescente = sorted(lista)
decrescente = sorted(lista, reverse=True)

print(crescente)
print(decrescente)