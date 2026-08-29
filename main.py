from services.idioma_service import cadastrar_idioma, buscar_idioma, carregar_indice_idiomas, listar_idiomas
from seed.dados_iniciais import carregar_idiomas_iniciais, carregar_licoes_iniciais, carregar_exercicios_iniciais
from services.licao_service import buscar_licao_com_idioma, carregar_indice_licoes
from services.exercicio_service import carregar_indice_exercicios, buscar_exercicio_com_idioma, listar_exercicios
# import os

raiz_idiomas = carregar_indice_idiomas()
raiz_licoes = carregar_indice_licoes()
raiz_exercicios = carregar_indice_exercicios()

if raiz_idiomas is None:
    raiz_idiomas = carregar_idiomas_iniciais(raiz_idiomas)

if raiz_licoes is None:
    raiz_licoes = carregar_licoes_iniciais(raiz_licoes, raiz_idiomas)

if raiz_exercicios is None:
    raiz_exercicios = carregar_exercicios_iniciais(raiz_exercicios, raiz_licoes)

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

codigo_licao = int(input("\nDigite o código da lição para buscar: "))

resultado = buscar_licao_com_idioma(raiz_licoes, raiz_idiomas, codigo_licao)

if resultado is not None:
    licao, idioma = resultado

    print("\nLição encontrada: ")
    print("Código da lição: ", licao.cod_licao)
    print("Idioma: ", idioma.descricao)
    print("Total de níveis: ", licao.total_niveis)
else:
    print("\nLição não encontrada")

exercicios = listar_exercicios(raiz_exercicios, [])
print("\nExercícios disponíveis: ")

for exercicio in exercicios:
    print(exercicio.cod_exercicio, "-", exercicio.descricao)

codigo_exercicio = int(input("\nDigite o código do exercício para buscar: "))

resultado = buscar_exercicio_com_idioma(raiz_exercicios, raiz_licoes, raiz_idiomas, codigo_exercicio)

if resultado is not None:
    exercicio, licao, idioma = resultado

    print("\nExercício encontrado: ")
    print("Código do exercício: ", exercicio.cod_exercicio)
    print("Código da lição: ", exercicio.cod_licao)
    print("Idioma: ", idioma.descricao)
    print("Nível de dificuldade: ", exercicio.nivel_dificuldade)
    print("Descrição: ", exercicio.descricao)
    print("Opções: ", exercicio.opcoes_resposta)
    print("Resposta correta: ", exercicio.resposta_correta)
    print("Pontuação: ", exercicio.pontuacao)
else:
    print("\nExercício não encontrado!")
