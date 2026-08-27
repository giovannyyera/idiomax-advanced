class No:
    def __init__(self, codigo, posicao):
        self.codigo = codigo
        self.posicao = posicao
        self.esquerda = None
        self.direita = None

def buscar(raiz, codigo):
    atual = raiz    

    while atual is not None: 
        if codigo == atual.codigo: 
            return atual 

        if codigo < atual.codigo:
            atual = atual.esquerda
        else:
            atual = atual.direita

    return None

def inserir(raiz, codigo, posicao):
    novo = No(codigo, posicao)

    if raiz is None:
        return novo

    atual = raiz
    pai = None

    while atual is not None:
        pai = atual

        if codigo < atual.codigo:
            atual = atual.esquerda
        else: 
            atual = atual.direita

    if codigo < pai.codigo:
        pai.esquerda = novo
    else:
        pai.direita = novo

    return raiz

