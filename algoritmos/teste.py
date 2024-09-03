import time

def selection(lista):
    start_time = time.time()
    for x in range(len(lista)):
        menor = lista[x]
        menor_id = x  
        for j in range(x + 1, len(lista)):
            if lista[j] < menor:
                menor = lista[j]
                menor_id = j
        lista[x], lista[menor_id] = lista[menor_id], lista[x]
    end_time = time.time()  
    print("Selection Sort:", lista)
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")

def insertion(lista):
    start_time = time.time()
    for x in range(1, len(lista)):
        i = x - 1
        tmp = lista[x]
        while i >= 0 and tmp < lista[i]:
            lista[i+1] = lista[i]
            i = i - 1
        lista[i+1] = tmp
    end_time = time.time()
    print("Insertion Sort:", lista)
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")

def bubble(lista):
    start_time = time.time()  
    for x in range(len(lista) - 1):
        for i in range(len(lista) - 1 - x):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    end_time = time.time()  
    print("Bubble Sort:", lista)
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")

def merge(v, ini, meio, fim):
    temp = []
    p1 = ini
    p2 = meio + 1
    tam = fim - ini + 1

    while p1 <= meio and p2 <= fim:
        if v[p1] < v[p2]:
            temp.append(v[p1])
            p1 += 1
        else:
            temp.append(v[p2])
            p2 += 1

    while p1 <= meio:
        temp.append(v[p1])
        p1 += 1

    while p2 <= fim:
        temp.append(v[p2])
        p2 += 1

    for i in range(tam):
        v[ini + i] = temp[i]

def merge_sort(v, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)
        merge_sort(v, meio + 1, fim)
        merge(v, ini, meio, fim)


def copia_lista(lista):
    print("\nLista inicial:", lista)
    insertion(lista.copy())
    selection(lista.copy())
    bubble(lista.copy())
    
    lista_copy = lista.copy()
    start_time = time.time()
    merge_sort(lista_copy, 0, len(lista_copy) - 1)
    end_time = time.time()
    print("Merge Sort:", lista_copy)
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")

# Aleatória
lista = [7, 13, 2, 25, 8, 19, 3, 21, 11, 5]
copia_lista(lista)

# Ordenada
lista = [1, 4, 7, 10, 12, 15, 18, 21, 25, 30]
copia_lista(lista)

# Inversa
lista = [50, 42, 33, 27, 19, 11, 6, 4, 2, 1]
copia_lista(lista)

# Com valores repetidos
lista = [8, 3, 7, 8, 5, 7, 2, 3, 6, 8]
copia_lista(lista)
