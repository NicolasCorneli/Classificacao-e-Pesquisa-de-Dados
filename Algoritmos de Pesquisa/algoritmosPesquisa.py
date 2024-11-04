import timeit
import math
import random

# Função para busca binária iterativa
def busca_binaria_iterativa(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Função para busca binária recursiva
def busca_binaria_recursiva(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return busca_binaria_recursiva(arr, x, mid + 1, high)
    else:
        return busca_binaria_recursiva(arr, x, low, mid - 1)

# Função para pesquisa por salto
def busca_por_salto(arr, x):
    length = len(arr)
    step = int(math.sqrt(length))
    prev, curr = 0, 0

    while curr < length and arr[curr] < x:
        prev = curr
        curr += step
        if curr > length - 1:
            curr = length

    for i in range(prev, min(curr, length)):
        if arr[i] == x:
            return i
    return -1

# Função para pesquisa Fibonacci
def busca_fibonacci(arr, x):
    n = len(arr)
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2

    while fibM < n:
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2

    offset = -1

    while fibM > 1:
        i = min(offset + fibM_minus_2, n - 1)
        if arr[i] < x:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            offset = i
        elif arr[i] > x:
            fibM = fibM_minus_2
            fibM_minus_1 -= fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i
    if fibM_minus_1 and offset < (n - 1) and arr[offset + 1] == x:
        return offset + 1
    return -1

# Função para medir o desempenho dos algoritmos
def teste_de_desempenho():
    arr = sorted(random.sample(range(1000000), 100000))
    x = arr[random.randint(0, 99999)] 
  
    tempo_binaria_iterativa = timeit.timeit(lambda: busca_binaria_iterativa(arr, x), number=100)
    print("Busca Binária Iterativa:", tempo_binaria_iterativa / 100)

    tempo_binaria_recursiva = timeit.timeit(lambda: busca_binaria_recursiva(arr, x, 0, len(arr) - 1), number=100)
    print("Busca Binária Recursiva:", tempo_binaria_recursiva / 100)

    tempo_por_salto = timeit.timeit(lambda: busca_por_salto(arr, x), number=100)
    print("Busca por Salto:", tempo_por_salto / 100)

    tempo_fibonacci = timeit.timeit(lambda: busca_fibonacci(arr, x), number=100)
    print("Busca Fibonacci:", tempo_fibonacci / 100)

teste_de_desempenho()

'''
a. Qual método teve o menor número de comparações em média?
A busca binária (iterativa e recursiva) possui o menor número de comparações em listas ordenadas devido à sua divisão do problema em duas partes a cada passo.

b. Em quais situações você acha que cada método seria mais apropriado?
Busca Binária: Ideal para listas grandes e ordenadas, onde o objetivo é encontrar um item específico com eficiência.
Pesquisa por Salto: Pode ser apropriada em listas muito grandes ordenadas e onde o acesso sequencial a blocos de memória é mais rápido (como em alguns sistemas de armazenamento).
Pesquisa Fibonacci: Ideal para busca em listas grandes, pois utiliza propriedades matemáticas que combinam bem com o acesso a dados estruturados em camadas.

c. Como a ordenação da lista afeta a eficiência de cada método?
Busca Binária e Pesquisa Fibonacci: A eficiência desses métodos depende diretamente da ordenação. Sem ordenação, eles não podem dividir a lista em subpartes de maneira significativa e, portanto, não funcionam corretamente.
Pesquisa por Salto: Também depende da lista estar ordenada para ser eficiente. Em listas não ordenadas, o método de saltos seguidos de verificação sequencial se torna ineficaz.

'''
