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
