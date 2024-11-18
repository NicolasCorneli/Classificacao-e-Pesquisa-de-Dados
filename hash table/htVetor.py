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

htable = HashTableVetor(5)
htable.insert(1, 22)
htable.insert(2, 4)
htable.insert(3, 77)
print(htable.search(2)) 
htable.delete(2)
print(htable.search(2))  
