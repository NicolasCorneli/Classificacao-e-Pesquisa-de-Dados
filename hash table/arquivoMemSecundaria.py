class Arquivo:
    def __init__(self, nome, caminho, tamanho):
        self.nome = nome
        self.caminho = caminho
        self.tamanho = tamanho

    def __repr__(self):
        return f"Nome: {self.nome}, Caminho: {self.caminho}, Tamanho: {self.tamanho} KB"

class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return sum(ord(c) for c in chave) % self.tamanho

    def adicionar(self, arquivo):
        indice = self._hash(arquivo.nome)
        self.tabela[indice].append(arquivo)

    def buscar(self, nome):
        indice = self._hash(nome)
        for arquivo in self.tabela[indice]:
            if arquivo.nome == nome:
                return arquivo
        return None 

    def remover(self, nome):
        indice = self._hash(nome)
        for i, arquivo in enumerate(self.tabela[indice]):
            if arquivo.nome == nome:
                del self.tabela[indice][i]
                return True
        return False

    def listar(self):
        arquivos = []
        for lista in self.tabela:
            arquivos.extend(lista)
        return arquivos

tabela = TabelaHash(tamanho=10)

arquivo1 = Arquivo("relatorio.pdf", "/documentos/relatorio.pdf", 1024)
arquivo2 = Arquivo("foto.jpg", "/imagens/foto.jpg", 2048)
arquivo3 = Arquivo("dados.csv", "/planilhas/dados.csv", 512)
arquivo4 = Arquivo("backup.zip", "/backup/backup.zip", 4096)

tabela.adicionar(arquivo1)
tabela.adicionar(arquivo2)
tabela.adicionar(arquivo3)
tabela.adicionar(arquivo4)

arquivo_busca = tabela.buscar("dados.csv")
print("Arquivo encontrado:", arquivo_busca)

remover_sucesso = tabela.remover("foto.jpg")
print("Remoção de foto.jpg bem-sucedida:", remover_sucesso)

print("Arquivos restantes na tabela:")
for arquivo in tabela.listar():
    print(arquivo)
