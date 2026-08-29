from services.idioma_service import cadastrar_idioma
from services.licao_service import cadastrar_licao

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