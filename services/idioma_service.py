import struct 

from models.idioma import Idioma
from estrutura.arvore import inserir, buscar, excluir

FORMATO_IDIOMA = "i30s"  # Formato para serialização: inteiro (código) e string de 30 bytes (descrição)
TAMANHO_IDIOMA = struct.calcsize(FORMATO_IDIOMA)  # Tamanho total do registro de idioma em bytes

def empacotar_idioma(idioma):
    return struct.pack(
        FORMATO_IDIOMA,
        idioma.codigo,
        idioma.descricao.encode()
    )

def cadastrar_idioma(raiz, codigo, descricao):
    if buscar(raiz, codigo) is not None:
        return raiz
    
    idioma = Idioma(codigo, descricao)

    with open ("dados/idiomas.dat", "ab") as arquivo: #a = append, b = binário
        arquivo.seek(0,2) #vai para o final do arquivo
        tamanho_arquivo = arquivo.tell() #retorna a posição atual do ponteiro no arquivo em bytes
        posicao = tamanho_arquivo // TAMANHO_IDIOMA
        arquivo.write(empacotar_idioma(idioma))

    raiz = inserir(raiz, codigo, posicao)

    return raiz

def desempacotar_idioma(dados_binarios):
    codigo, descricao = struct.unpack( #pega todos os dados binários e separa em variáveis codigo e descricao
        FORMATO_IDIOMA,
        dados_binarios
    )

    return Idioma(
        codigo,
        # .decode() pega os bytes e os transforma em uma string comum do Python
        # .rstrip("\x00") serve para apagar todos os zeros invisíveis que sobram no final da palavra após a decodificação, garantindo que fique apenas o texto limpo
        descricao.decode().rstrip("\x00")
    )

def ler_idioma(posicao):
    with open("dados/idiomas.dat", "rb") as arquivo:
        arquivo.seek(posicao * TAMANHO_IDIOMA)

        dados_binarios = arquivo.read(TAMANHO_IDIOMA)

        return desempacotar_idioma(dados_binarios)

def buscar_idioma(raiz, codigo):
    resultado = buscar(raiz, codigo)

    if resultado is None:
        return None

    idioma = ler_idioma(resultado.posicao)
    return idioma

def carregar_indice_idiomas():
    raiz = None

    try:
        with open("dados/idiomas.dat", "rb") as arquivo:
            posicao = 0

            while True: 
                dados_binarios = arquivo.read(TAMANHO_IDIOMA)
                if not dados_binarios:
                    break

                idioma = desempacotar_idioma(dados_binarios)
                if idioma.codigo != 0:
                    raiz = inserir(raiz, idioma.codigo, posicao)
                posicao += 1

    except FileNotFoundError:
        return raiz

    return raiz

def listar_idiomas(raiz, lista): 
    if raiz is not None:
        listar_idiomas(raiz.esquerda, lista)
        idioma = ler_idioma(raiz.posicao)
        lista.append(idioma)
        listar_idiomas(raiz.direita, lista)
    return lista

def obter_proximo_codigo_idioma(raiz_idiomas):
    idiomas = listar_idiomas(raiz_idiomas, [])

    maior_codigo = 0

    for idioma in idiomas:
        if idioma.codigo > maior_codigo:
            maior_codigo = idioma.codigo

    return maior_codigo + 1

def excluir_idioma(raiz_idiomas, codigo):
    resultado = buscar(raiz_idiomas, codigo)

    if resultado is None:
        return raiz_idiomas

    posicao = resultado.posicao

    idioma = ler_idioma(posicao)
    idioma.codigo = 0

    with open("dados/idiomas.dat", "r+b") as arquivo:
        arquivo.seek(posicao * TAMANHO_IDIOMA)
        arquivo.write(empacotar_idioma(idioma))

    raiz_idiomas = excluir(raiz_idiomas, codigo)

    return raiz_idiomas