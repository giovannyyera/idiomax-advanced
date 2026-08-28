from services.idioma_service import cadastrar_idioma, buscar_idioma, carregar_indice_idiomas, listar_idiomas
from seed.dados_iniciais import carregar_idiomas_iniciais
# import os



raiz_idiomas = carregar_indice_idiomas()

if raiz_idiomas is None:
    raiz_idiomas = carregar_idiomas_iniciais(raiz_idiomas)

# codigo = int(input("Código do idioma: "))
# descricao = input("Descrição do idioma: ")

# raiz_idiomas = cadastrar_idioma(
#     raiz_idiomas,
#     codigo,
#     descricao
# )

# print("Idioma cadastrado com sucesso!")

idiomas = listar_idiomas(raiz_idiomas, [])
print("\nIdiomas disponíveis: ")

for idioma in idiomas:
    print(idioma.codigo, "-", idioma.descricao)

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


# tamanho = os.path.getsize("dados/idiomas.dat")
# print("\nTamanho do arquivo:", tamanho)