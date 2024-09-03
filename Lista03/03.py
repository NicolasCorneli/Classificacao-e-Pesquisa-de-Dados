#3. Pesquisar e implementar o algoritmo Heapsort
def heapsort(lista):
    k = (len(lista) // 2) - 1 
    while k >= 0:
        maxheapfy(lista, k, len(lista))
        k = k - 1
    
    n = len(lista) - 1
    while n >= 1:
        lista[0], lista[n] = lista[n], lista[0]
        maxheapfy(lista, 0, n)
        n = n - 1
    
def maxheapfy(lista, i, n):
    maior = i
    l = 2 * i + 1 
    r = 2 * i + 2 
    if l < n and lista[l] > lista[maior]:
        maior = l
    if r < n and lista[r] > lista[maior]:
        maior = r
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        maxheapfy(lista, maior, n)

lista = [8, 5, 4, 3, 2, 6, 7, 9, 10, 1]
heapsort(lista)
print(lista)
