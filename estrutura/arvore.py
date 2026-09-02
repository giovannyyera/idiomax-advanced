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

def menor_no(raiz):
    atual = raiz

    while atual.esquerda is not None:
        atual = atual.esquerda

    return atual

def excluir(raiz, codigo):
    if raiz is None:
        return None

    if codigo < raiz.codigo:
        raiz.esquerda = excluir(raiz.esquerda, codigo)

    elif codigo > raiz.codigo:
        raiz.direita = excluir(raiz.direita, codigo)

    else:
        if raiz.esquerda is None and raiz.direita is None:
            return None

        elif raiz.esquerda is None:
            return raiz.direita

        elif raiz.direita is None:
            return raiz.esquerda

        else:
            sucessor = menor_no(raiz.direita)

            raiz.codigo = sucessor.codigo 
            raiz.posicao = sucessor.posicao

            raiz.direita = excluir(raiz.direita, sucessor.codigo)

    return raiz
    