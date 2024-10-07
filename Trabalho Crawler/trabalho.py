import requests
from bs4 import BeautifulSoup

def parsing(url):
    response = requests.get(url)

    site = BeautifulSoup(response.content, 'html.parser')

    produtos_html = site.find_all('li', attrs={'class': 'item first'}) + site.find_all('li', attrs={'class': 'item'}) + site.find_all('li', attrs={'class': 'item last'})

    produtos = []
    check = []

    for produto in produtos_html:
        nome = produto.find('h2', attrs={'class': 'product-name'})
        valor = produto.find('p', attrs={'class': 'valprincipal'})
        
        if nome and valor:
            nome_produto = nome.get_text(strip=True)
            valor_produto = valor.get_text(strip=True)

            valor_produto = valor_produto.replace('R$', '').replace('Por', '').replace('.', '').replace(',', '.').strip()
            valor_produto = float(valor_produto)  
            
            if nome_produto not in check:
                check.append(nome_produto)
                produtos.append((nome_produto, valor_produto))
    
    return produtos

def quicksort(produtos, inicio, final):
    if inicio < final:
        pivo_index = particionar(produtos, inicio, final)
        quicksort(produtos, inicio, pivo_index - 1)
        quicksort(produtos, pivo_index + 1, final)

def particionar(produtos, inicio, final):
    pivo = produtos[inicio][1] 
    esq = inicio + 1
    dir = final

    while True:
        while esq <= dir and produtos[esq][1] <= pivo:
            esq += 1
        while dir >= esq and produtos[dir][1] > pivo:
            dir -= 1
        if esq < dir:
            produtos[esq], produtos[dir] = produtos[dir], produtos[esq]
        else:
            break

    produtos[inicio], produtos[dir] = produtos[dir], produtos[inicio]
    return dir

url = 'https://shoxstore.com.br/chuteiras/chuteira-de-campo'

produtos = parsing(url)

quicksort(produtos, 0, len(produtos) - 1)

for produto in produtos:
    print(f'Produto: {produto[0]} - Valor: R$ {produto[1]:.2f}')
