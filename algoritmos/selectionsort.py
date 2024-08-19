lista = [3, 2, 1, 4, 5]

for x in range(len(lista)):
    menor = lista[x]
    menor_id = x  
    for j in range(x + 1, len(lista)):
        if lista[j] < menor:
            menor = lista[j]
            menor_id = j
    lista[x], lista[menor_id] = lista[menor_id], lista[x]

print(lista)
