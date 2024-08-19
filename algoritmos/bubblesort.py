
# BubbleSort

lista = [2,7,3,8,9,3,6,11]

for x in range(1, len(lista)):
    for i in range(x+1,len(lista)):
        if lista[x] > lista[i]:
            lista[x], lista[i] = lista[i], lista[x]

print(lista)
        
