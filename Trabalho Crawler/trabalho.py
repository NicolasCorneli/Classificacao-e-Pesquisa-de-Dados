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
