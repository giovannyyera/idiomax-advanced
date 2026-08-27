from services.idioma_service import cadastrar_idioma, buscar_idioma, carregar_indice_idiomas


raiz_idiomas = carregar_indice_idiomas()


codigo = int(input("Código do idioma: "))
descricao = input("Descrição do idioma: ")


raiz_idiomas = cadastrar_idioma(
    raiz_idiomas,
    codigo,
    descricao
)


print("Idioma cadastrado com sucesso!")


codigo_busca = int(
    input("\nDigite o código para buscar: ")
)


idioma = buscar_idioma(
    raiz_idiomas,
    codigo_busca
)

if idioma is not None:
    print("\nIdioma encontrado:")
    print("Código:", idioma.codigo)
    print("Descrição:", idioma.descricao)

else:
    print("\nIdioma não encontrado!")