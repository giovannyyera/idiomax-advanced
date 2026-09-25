import struct 

from models.licao import Licao
from estrutura.arvore import inserir, buscar, excluir
from services.idioma_service import buscar_idioma

FORMATO_LICAO = "iii" # 3 inteiros em licao.py
TAMANHO_LICAO = struct.calcsize(FORMATO_LICAO)

def empacotar_licao(licao):
    return struct.pack(
        FORMATO_LICAO,
        licao.cod_licao,
        licao.cod_idioma,
        licao.total_niveis
    )

def desempacotar_licao(dados_binarios):
    cod_licao, cod_idioma, total_niveis = struct.unpack(
        FORMATO_LICAO,
        dados_binarios
    )

    return Licao(
        cod_licao,
        cod_idioma,
        total_niveis
    )

def cadastrar_licao(raiz_licoes, raiz_idiomas, cod_licao, cod_idioma, total_niveis):
    if buscar(raiz_licoes, cod_licao) is not None:
        return raiz_licoes
    
    idioma = buscar_idioma(raiz_idiomas, cod_idioma)

    if idioma is None:
        return raiz_licoes

    licao = Licao(cod_licao, cod_idioma, total_niveis)

    with open ("dados/licoes.dat", "ab") as arquivo:
        arquivo.seek(0,2)
        tamanho_arquivo = arquivo.tell()
        posicao = tamanho_arquivo // TAMANHO_LICAO
        arquivo.write(empacotar_licao(licao))

    raiz_licoes = inserir(raiz_licoes, cod_licao, posicao)

    return raiz_licoes

def ler_licao(posicao):
    with open("dados/licoes.dat", "rb") as arquivo:
        arquivo.seek(posicao * TAMANHO_LICAO)

        dados_binarios = arquivo.read(TAMANHO_LICAO)

        return desempacotar_licao(dados_binarios)

def buscar_licao(raiz_licoes, cod_licao):
    resultado = buscar(raiz_licoes, cod_licao)

    if resultado is None:
        return None

    licao = ler_licao(resultado.posicao)
    return licao

def carregar_indice_licoes():
    raiz_licao = None

    try:
        with open("dados/licoes.dat", "rb") as arquivo:
            posicao = 0

            while True:
                dados_binarios = arquivo.read(TAMANHO_LICAO)
                if not dados_binarios:
                    break

                licao = desempacotar_licao(dados_binarios)
                if licao.cod_licao != 0:
                    raiz_licao = inserir(raiz_licao, licao.cod_licao, posicao)
                posicao += 1
    except FileNotFoundError:
        return raiz_licao

    return raiz_licao

def buscar_licao_com_idioma(raiz_licoes, raiz_idiomas, cod_licao):
    licao = buscar_licao(raiz_licoes, cod_licao)

    if licao is None:
        return None

    idioma = buscar_idioma(raiz_idiomas, licao.cod_idioma)

    if idioma is None: 
        return None

    return licao, idioma

def listar_licoes(raiz_licao, lista):
    if raiz_licao is not None:
        listar_licoes(raiz_licao.esquerda, lista)
        licao = ler_licao(raiz_licao.posicao)
        lista.append(licao)
        listar_licoes(raiz_licao.direita, lista)
    return lista

def obter_proximo_codigo_licao(raiz_licoes):
    licoes = listar_licoes(raiz_licoes, [])

    maior_codigo = 100

    for licao in licoes:
        if licao.cod_licao > maior_codigo:
            maior_codigo = licao.cod_licao

    return maior_codigo + 1

def excluir_licao(raiz_licoes, codigo):
    resultado = buscar(raiz_licoes, codigo)

    if resultado is None:
        return raiz_licoes

    posicao = resultado.posicao

    licao = ler_licao(posicao)
    licao.cod_licao = 0

    with open("dados/licoes.dat", "r+b") as arquivo:
        arquivo.seek(posicao * TAMANHO_LICAO)
        arquivo.write(empacotar_licao(licao))

    raiz_licoes = excluir(raiz_licoes, codigo)

    return raiz_licoes