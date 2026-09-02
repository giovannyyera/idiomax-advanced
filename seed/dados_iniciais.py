from services.idioma_service import cadastrar_idioma
from services.licao_service import cadastrar_licao
from services.exercicio_service import cadastrar_exercicio

IDIOMAS_INICIAIS = [
    (1, "Inglês"),
    (2, "Espanhol"),
    (3, "Francês")
]

def carregar_idiomas_iniciais(raiz):

    for codigo, descricao in IDIOMAS_INICIAIS:
        raiz = cadastrar_idioma(
            raiz,
            codigo,
            descricao
        )

    return raiz

LICOES_INICIAIS = [
    (101, 1, 3),  # Inglês
    (102, 2, 3),  # Espanhol
    (103, 3, 3)   # Francês
]

def carregar_licoes_iniciais(raiz_licoes, raiz_idiomas):

    for cod_licao, cod_idioma, total_niveis in LICOES_INICIAIS:
        raiz_licoes = cadastrar_licao(
            raiz_licoes,
            raiz_idiomas,
            cod_licao,
            cod_idioma,
            total_niveis
        )

    return raiz_licoes

EXERCICIOS_INICIAIS = [
    (
        1001,
        101,
        1,
        "Qual é a tradução de 'dog'?",
        ["cachorro", "gato", "casa", "carro"],
        "cachorro",
        20
    ),
    (
        1002,
        101,
        1,
        "Qual é a tradução de 'cat'?",
        ["cachorro", "gato", "livro", "porta"],
        "gato",
        20
    ),

    (
        2001,
        102,
        1,
        "Qual é a tradução de 'perro'?",
        ["cachorro", "gato", "mesa", "livro"],
        "cachorro",
        20
    ),
    (
        2002,
        102,
        1,
        "Qual é a tradução de 'gato'?",
        ["cachorro", "gato", "casa", "porta"],
        "gato",
        20
    ),

    (
        3001,
        103,
        1,
        "Qual é a tradução de 'chien'?",
        ["cachorro", "gato", "livro", "carro"],
        "cachorro",
        20
    ),
    (
        1003,
        101,
        2,
        "Qual é a tradução de 'house'?",
        ["casa", "carro", "gato", "livro"],
        "casa",
        20
    ),
    (
        3002,
        103,
        1,
        "Qual é a tradução de 'chat'?",
        ["cachorro", "gato", "casa", "mesa"],
        "gato",
        20
    )
]

def carregar_exercicios_iniciais(raiz_exercicios, raiz_licoes): 
    for cod_exercicio, cod_licao, nivel_dificuldade, descricao, opcoes_resposta, resposta_correta, pontuacao in EXERCICIOS_INICIAIS:
        raiz_exercicios = cadastrar_exercicio(
            raiz_exercicios, 
            raiz_licoes, 
            cod_exercicio, 
            cod_licao, 
            nivel_dificuldade, 
            descricao, 
            opcoes_resposta, 
            resposta_correta, 
            pontuacao
        )

    return raiz_exercicios