from services.idioma_service import cadastrar_idioma

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