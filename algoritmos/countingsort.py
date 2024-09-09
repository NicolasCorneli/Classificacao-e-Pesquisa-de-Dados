def counting_sort(arr):
    # Encontra o maior valor no array
    max_val = max(arr)
    
    # Cria um array de contagem de tamanho max_val + 1
    count = [0] * (max_val + 1)
    
    # Conta as ocorrências de cada valor no array original
    for num in arr:
        count[num] += 1

    # Altera count[i] para que count[i] contenha a posição final de cada elemento
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Cria um array de saída para armazenar os valores ordenados
    output = [0] * len(arr)
    
    # Coloca os elementos em suas posições corretas no array de saída
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    # Copia os valores ordenados de volta para o array original
    for i in range(len(arr)):
        arr[i] = output[i]

# Exemplo de uso
arr = [4, 2, 2, 8, 3, 3, 1]
print("Array original:", arr)
counting_sort(arr)
print("Array ordenado:", arr)
