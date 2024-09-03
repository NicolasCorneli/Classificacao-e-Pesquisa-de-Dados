#1. Implementar os algoritmos Quick Sort e o ShellSort
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


def shell(lista):
    sub_lista = len(lista) // 2
    while sub_lista > 0:
        for posicao_inicial in range(sub_lista):
            insertion(lista,posicao_inicial,sub_lista)
        print("Depois dos incrementos de tamanho",sub_lista,"A lista é",lista)
        sub_lista = sub_lista // 2

def insertion(lista,inicio,pulo):
    for i in range(inicio+pulo,len(lista),pulo):
        valor_atual = lista[i]
        posicao = i
        while posicao >= pulo and lista[posicao - pulo] > valor_atual:
            lista[posicao] = lista[posicao - pulo]
            posicao = posicao - pulo
        lista[posicao] = valor_atual

lista = [8,5,4,3,2,6,7,9,10,1]
shell(lista)
