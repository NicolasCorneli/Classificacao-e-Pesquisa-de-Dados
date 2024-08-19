lista = [3,2,1,4,5]

for x in range(1,len(lista)):
    i = x - 1
    tmp = lista[x]
    while i >= 0 and tmp < lista[i]:
        lista[i+1] = lista[i]
        i = i - 1
    
    lista[i+1] = tmp

print(lista)
