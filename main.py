from models.idioma import Idioma
from estrutura.arvore import inserir
from services.idioma_service import cadastrar_idioma

raiz_idiomas = None

codigo = int(input('Código do idioma:  '))
descricao = input('Descrição do idioma: ')

raiz_idiomas = cadastrar_idioma(
    raiz_idiomas, 
    codigo,
    descricao
)

print('Idioma cadastrado com sucesso!')

def cadastrar_idioma(raiz, dados_idiomas): 
    codigo = int(input('Código do idioma: '))
    descricao = input('Descrição do idioma: ')

    idioma = Idioma(codigo, descricao)

    posicao = len(dados_idiomas)
    dados_idiomas.append(idioma)

    raiz = inserir(raiz, codigo, posicao)

    return raiz

raiz = None
dados_idiomas = []

raiz = cadastrar_idioma(raiz, dados_idiomas)