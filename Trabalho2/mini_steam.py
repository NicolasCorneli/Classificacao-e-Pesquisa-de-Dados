class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos #lista

class NoJogos:
    def __init__(self, jogo, right=None, left=None):
        self.jogo = jogo
        self.right = right
        self.left = left

class ArvoreJogos:
    def __init__(self, arv=None):
        self.arv = arv
    
    def inserir(self, jogo):
        novo_jogo = NoJogos(jogo)
        if self.arv is None:
            self.arv = novo_jogo
        else:
            atual = self.arv
            while True:
                if novo_jogo.jogo.preco < atual.jogo.preco:
                    if atual.left is None:
                        atual.left = novo_jogo
                        break
                    else:
                        atual = atual.left
                else:
                    if atual.right is None:
                        atual.right = novo_jogo
                        break
                    else:
                        atual = atual.right

    def buscar_por_preco(self, preco):
        if self.arv is None:
            print("Sem jogos disponíveis.")
            return None
    
        jogos_encontrados = []
    
        def percorrer_arvore(atual):
            if atual is None:
                return
            
            if atual.jogo.preco == preco:
                jogos_encontrados.append(atual.jogo)

            if preco <= atual.jogo.preco:
                percorrer_arvore(atual.left)
            if preco >= atual.jogo.preco:
                percorrer_arvore(atual.right)
        
        percorrer_arvore(self.arv)
    
        if jogos_encontrados:
            print(f"Jogos encontrados com o preço de R${preco}:")
            for j in jogos_encontrados:
                print(f"Jogo: {j.titulo}, Preço: R${j.preco}")
        else:
            print(f"Nenhum jogo encontrado com o preço de R${preco}.")
    
        return jogos_encontrados if jogos_encontrados else None

    
    def buscar_por_faixa_preco(self, preco_min, preco_max):
        if self.arv is None:
            print("Sem jogos disponíveis.")
            return None
        
        jogos_encontrados = []

        def percorrer_arvore(atual):
            if atual is None:
                return None
            
            if preco_min <= atual.jogo.preco <= preco_max:
                jogos_encontrados.append(atual.jogo)
            
            if atual.jogo.preco > preco_min:
                percorrer_arvore(atual.left)
            if atual.jogo.preco < preco_max:
                percorrer_arvore(atual.right)
        
        percorrer_arvore(self.arv)
        
        if jogos_encontrados:
            print(f"Jogos encontrados na faixa de R${preco_min} a R${preco_max}:")
            for j in jogos_encontrados:
                print(f"Jogo: {j.titulo}, Preço: R${j.preco}")
        else:
            print("Nenhum jogo encontrado nesta faixa de preço.")

class HashGeneros:
    def __init__(self):
        self.genero_jogos = {}

    def adicionar_jogo(self,jogo):
        for g in jogo.generos:
            if g not in self.genero_jogos:
                self.genero_jogos[g] = []
            
            self.genero_jogos[g].append(jogo.titulo)
        
    
    def buscar_jogo_por_genero(self,genero):
        return self.genero_jogos.get(genero, [])
    
class MotorBuscaJogos:
    def __init__(self):
        self.catalogo_jogos = ArvoreJogos()
        self.generos = HashGeneros()
    
    def inserir_jogo(self, jogo):
        self.catalogo_jogos.inserir(jogo)
        self.generos.adicionar_jogo(jogo)

    def buscar_jogo_por_preco(self, preco):
        return self.catalogo_jogos.buscar_por_preco(preco)

    def buscar_jogo_por_faixa_preco(self, preco_min, preco_max):
        return self.catalogo_jogos.buscar_por_faixa_preco(preco_min, preco_max)

    def buscar_jogo_por_genero(self, genero):
        return self.generos.buscar_jogo_por_genero(genero)
    

motor = MotorBuscaJogos()

jogo1 = Jogo(1, "The Witcher 3", "CD Projekt Red", 150, ["RPG", "Aventura"])
jogo2 = Jogo(2, "Minecraft", "Mojang", 80, ["Criatividade", "Mundo Aberto"])
jogo3 = Jogo(3, "Dark Souls III", "FromSoftware", 200, ["RPG", "Ação"])
jogo4 = Jogo(4, "The Last of Us Part II", "Naughty Dog", 250, ["Aventura", "Ação"])
jogo5 = Jogo(5, "Cyberpunk 2077", "CD Projekt Red", 180, ["RPG", "Ação", "Futuro"])
jogo6 = Jogo(6, "FIFA 22", "EA Sports", 150, ["Esporte", "Futebol"])
jogo7 = Jogo(7, "Hades", "Supergiant Games", 120, ["Ação", "Roguelike"])

motor.inserir_jogo(jogo1)
motor.inserir_jogo(jogo2)
motor.inserir_jogo(jogo3)
motor.inserir_jogo(jogo4)
motor.inserir_jogo(jogo5)
motor.inserir_jogo(jogo6)
motor.inserir_jogo(jogo7)

motor.buscar_jogo_por_preco(150)

motor.buscar_jogo_por_faixa_preco(100, 200)

motor.buscar_jogo_por_genero("RPG")
motor.buscar_jogo_por_genero("Mundo Aberto")
