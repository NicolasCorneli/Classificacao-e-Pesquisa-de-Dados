def heapsort(lista):
    k = (len(lista) // 2) - 1 
    while k >= 0:
        minheapfy(lista, k, len(lista))
        k = k - 1
    
    n = len(lista) - 1
    while n >= 1:
        lista[0], lista[n] = lista[n], lista[0]
        minheapfy(lista, 0, n)
        n = n - 1
    
def minheapfy(lista, i, n):
    menor = i
    l = 2 * i + 1 
    r = 2 * i + 2 
    if l < n and lista[l] < lista[menor]:
        menor = l
    if r < n and lista[r] < lista[menor]:
        menor = r
    if menor != i:
        lista[i], lista[menor] = lista[menor], lista[i]
        minheapfy(lista, menor, n)

lista = [8, 5, 4, 3, 2, 6, 7, 9, 10, 1]
heapsort(lista)
print(lista)
