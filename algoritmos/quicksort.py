def quicksort(lista, inicio, final):
    if inicio < final:
        pivo_index = particionar(lista, inicio, final)
        quicksort(lista, inicio, pivo_index - 1)
        quicksort(lista, pivo_index + 1, final)

def particionar(lista, inicio, final):
    pivo = lista[inicio]
    esq = inicio + 1
    dir = final

    while True:
        while esq <= dir and lista[esq] <= pivo:
            esq = esq + 1
        while dir >= esq and lista[dir] > pivo:
            dir = dir - 1
        if esq < dir:
            lista[esq], lista[dir] = lista[dir], lista[esq]
        else:
            break

    lista[inicio], lista[dir] = lista[dir], lista[inicio]
    return dir

lista = [8,5,4,3,2,6,7,9,10,1]
quicksort(lista, 0, len(lista) - 1)
print(lista)
