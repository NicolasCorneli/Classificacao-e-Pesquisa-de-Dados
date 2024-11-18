class HashTableVetor:
    def __init__(self, size):
        self.size = size
        self.table = {i: [] for i in range(size)}

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

# Exemplo de uso
htable = HashTableVetor(5)
htable.insert("chave1", "valor1")
htable.insert("chave2", "valor2")
htable.insert("chave3", "valor3")
print(htable.search("chave2"))  # Saída: valor2
htable.delete("chave2")
print(htable.search("chave2"))  # Saída: None
