class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableLinkedLists:
    def __init__(self, size):
        self.size = size
        self.table = {i: None for i in range(size)}

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        node = self.table[index]
        if not node:
            self.table[index] = Node(key, value)
        else:
            while node.next:
                if node.key == key:
                    node.value = value 
                    return
                node = node.next
            if node.key == key:
                node.value = value  
            else:
                node.next = Node(key, value)

    def search(self, key):
        index = self._hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        index = self._hash(key)
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                return
            prev = node
            node = node.next

htable = HashTableLinkedLists(5)
htable.insert(1, 6)
htable.insert(2, 33)
htable.insert(3, 55)
print(htable.search(2))  
htable.delete(2)
print(htable.search(2)) 
