class Node:
    def __init__(self,valor,right=None,left=None):
        self.valor = valor
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.valor)

def em_ordem(arv):
    if arv:
        em_ordem(arv.left)
        print(arv.valor)
        em_ordem(arv.right)

def insere(arv,v):
    if arv is None:
        return Node(v)
    
    if v < arv.valor:
        arv.left = insere(arv.left,v)
    else:
        arv.right = insere(arv.right,v)
    return arv

def remove(arv, v):
    if arv is None:
        return None
    
    if v < arv.valor:
        arv.left = remove(arv.left, v)
    elif v > arv.valor:
        arv.right = remove(arv.right, v)
    else:
        if arv.left is None and arv.right is None:
            return None
    
        elif arv.left and arv.right is None:
            return arv.left
        
        elif arv.left is None and arv.right:
            return arv.right
        
        else:
            f = arv.left
            while f.right is not None:
                f = f.right
            arv.valor = f.valor
            arv.left = remove(arv.left, f.valor)
    
    return arv


def busca(arv,v):
    if arv is None:
        return 
    if v < arv.valor:
        return busca(arv.left,v)
    elif v > arv.valor:
        return busca(arv.right,v)
    return arv

arvore = None
arvore = insere(arvore,30)
arvore = insere(arvore,20)
arvore = insere(arvore,40)
em_ordem(arvore)


print(" ")

arvore1 = busca(arvore,20)
print(arvore1)
