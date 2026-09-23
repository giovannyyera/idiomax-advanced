import struct

from models.exercicio import Exercicio
from services.licao_service import buscar_licao
from services.idioma_service import buscar_idioma
from estrutura.arvore import inserir, buscar

FORMATO_EXERCICIO = "iii100s120s40si" #i = cod_exercicio,cod_licao, nivel_dificuldade, pontuacao, 100s = descricao, 120s = opcoes_resposta, 40s =  resposta_correta
TAMANHO_EXERCICIO = struct.calcsize(FORMATO_EXERCICIO)

def empacotar_exercicio(exercicio):
    opcoes_texto = "|".join(exercicio.opcoes_resposta) # transformar a lista em uma única string

    return struct.pack(
        FORMATO_EXERCICIO,
        exercicio.cod_exercicio,
        exercicio.cod_licao,
        exercicio.nivel_dificuldade,
        exercicio.descricao.encode(),
        opcoes_texto.encode(),
        exercicio.resposta_correta.encode(),
        exercicio.pontuacao
    )

def desempacotar_exercicio(dados_binarios):
    cod_exercicio, cod_licao, nivel_dificuldade, descricao, opcoes_resposta, resposta_correta, pontuacao = struct.unpack(
        FORMATO_EXERCICIO,
        dados_binarios
    )

    return Exercicio(
        cod_exercicio,
        cod_licao,
        nivel_dificuldade,
        descricao.decode().rstrip("\x00"),
        opcoes_resposta.decode().rstrip("\x00").split("|"),
        resposta_correta.decode().rstrip("\x00"),
        pontuacao
    )

def cadastrar_exercicio(raiz_exercicios, raiz_licao, cod_exercicio, cod_licao, nivel_dificuldade, descricao, opcoes_resposta, resposta_correta, pontuacao):
    if buscar(raiz_exercicios, cod_exercicio) is not None:
        return raiz_exercicios
    
    licao = buscar_licao(raiz_licao, cod_licao)

    if licao is None:
        return raiz_exercicios

    exercicio = Exercicio(cod_exercicio, cod_licao, nivel_dificuldade, descricao, opcoes_resposta, resposta_correta, pontuacao)

    with open("dados/exercicios.dat", "ab") as arquivo:
        arquivo.seek(0,2)
        tamanho_arquivo = arquivo.tell()
        posicao = tamanho_arquivo // TAMANHO_EXERCICIO
        arquivo.write(empacotar_exercicio(exercicio))

    raiz_exercicios = inserir(raiz_exercicios, cod_exercicio, posicao)

    return raiz_exercicios

def ler_exercicio(posicao):
    with open("dados/exercicios.dat", "rb") as arquivo:
        arquivo.seek(posicao * TAMANHO_EXERCICIO)

        dados_binario = arquivo.read(TAMANHO_EXERCICIO)

        return desempacotar_exercicio (dados_binario)

def buscar_exercicio(raiz_exercicios, cod_exercicio):
    resultado = buscar(raiz_exercicios, cod_exercicio)

    if resultado is None:
        return None

    exercicio = ler_exercicio(resultado.posicao)
    return exercicio

def carregar_indice_exercicios():
    raiz_exercicio = None

    try:
        with open("dados/exercicios.dat", "rb") as arquivo:
            posicao = 0

            while True:
                dados_binarios = arquivo.read(TAMANHO_EXERCICIO)
                if not dados_binarios:
                    break

                exercicio = desempacotar_exercicio(dados_binarios)
                raiz_exercicio = inserir(raiz_exercicio, exercicio.cod_exercicio, posicao)
                posicao += 1
    except FileNotFoundError:
        return raiz_exercicio

    return raiz_exercicio

def buscar_exercicio_com_idioma(raiz_exercicios, raiz_licoes, raiz_idiomas, cod_exercicio):
    exercicio = buscar_exercicio(raiz_exercicios, cod_exercicio)

    if exercicio is None:
        return None

    licao = buscar_licao(raiz_licoes, exercicio.cod_licao)

    if licao is None:
        return None

    idioma = buscar_idioma(raiz_idiomas, licao.cod_idioma)

    if idioma is None:
        return None

    return exercicio, licao, idioma

def listar_exercicios(raiz_exercicios, lista):
    if raiz_exercicios is not None:
        listar_exercicios(raiz_exercicios.esquerda, lista)
        exercicio = ler_exercicio(raiz_exercicios.posicao)
        lista.append(exercicio)
        listar_exercicios(raiz_exercicios.direita, lista)
    return lista

def obter_proximo_codigo_exercicio(raiz_exercicios, raiz_licoes, cod_licao):
    licao = buscar_licao(raiz_licoes, cod_licao)

    if licao is None:
        return None

    codigo_base = licao.cod_idioma * 1000

    exercicios = listar_exercicios(raiz_exercicios, [])

    maior_codigo = codigo_base

    for exercicio in exercicios:
        if(exercicio.cod_licao == cod_licao and exercicio.cod_exercicio > maior_codigo):
            maior_codigo = exercicio = exercicio.cod_exercicio

    return maior_codigo + 1