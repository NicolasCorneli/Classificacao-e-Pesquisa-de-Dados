# 🎮 mini-Steam: Algoritmo Localizador de Jogos

Este projeto é um mecanismo de busca para uma loja digital de jogos chamado **mini-Steam**. Ele permite localizar jogos com base no preço e no gênero de forma eficiente, utilizando estruturas de dados como **Árvore Binária de Busca (BST)** e **Hash Table**.

## 📚 Tecnologias e Estruturas Utilizadas

  - Linguagem: Python
  - Árvore Binária de Busca (BST)
  - Hash Table

## 🛠️ Funcionalidades

1. **Gerenciamento de Jogos por Preço**:
   - Adicionar jogos com base no preço usando uma BST.
   - Buscar jogos por um preço específico.
   - Buscar jogos dentro de uma faixa de preços definida.

2. **Gerenciamento de Jogos por Gênero**:
   - Adicionar jogos a uma hash table indexada por gênero.
   - Buscar jogos pertencentes a um gênero específico.

3. **Integração Eficaz**:
   - Combinação eficiente das estruturas de dados para busca rápida.

## 📂 Estrutura do Projeto

### Classes e Responsabilidades

- **`Jogo`**:
  Representa um jogo com ID, título, desenvolvedor, preço e gêneros.

- **`NoJogos`**:
  Representa um nó da Árvore Binária de Busca (BST), armazenando um jogo e referências para os filhos esquerda e direita.

- **`ArvoreJogos`**:
  Gerencia jogos por preço, permitindo:
  - Inserir jogos na árvore.
  - Buscar jogos por preço exato.
  - Buscar jogos por faixa de preço.

- **`HashGeneros`**:
  Gerencia jogos por gênero, permitindo:
  - Adicionar jogos à tabela hash.
  - Buscar jogos por gênero.

- **`MotorBuscaJogos`**:
  Integra a BST e a Hash Table, oferecendo uma interface unificada para inserir e buscar jogos.

### Exemplos de Uso

Abaixo estão exemplos práticos para testar o funcionamento do mecanismo de busca:

```python
# Criando jogos
jogo1 = Jogo(1, "The Witcher 3", "CD Projekt Red", 150, ["RPG", "Aventura"])
jogo2 = Jogo(2, "Minecraft", "Mojang", 80, ["Criatividade", "Mundo Aberto"])
jogo3 = Jogo(3, "Dark Souls III", "FromSoftware", 200, ["RPG", "Ação"])

# Criando o motor de busca
motor = MotorBuscaJogos()

# Adicionando jogos
motor.inserir_jogo(jogo1)
motor.inserir_jogo(jogo2)
motor.inserir_jogo(jogo3)

# Buscando por preço
motor.buscar_jogo_por_preco(150)

# Buscando por faixa de preço
motor.buscar_jogo_por_faixa_preco(100, 200)

# Buscando por gênero
motor.buscar_jogo_por_genero("RPG")
```

## ✨Dupla --> Nicolas Marin e Bruno Carneiro
