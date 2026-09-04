import struct

from models.usuario import Usuario
from services.idioma_service import buscar_idioma
from estrutura.arvore import inserir, buscar, excluir

FORMATO_USUARIO = "i100siiii"
TAMANHO_USUARIO = struct.calcsize(FORMATO_USUARIO)

def empacotar_usuario(usuario):
    return struct.pack(
        FORMATO_USUARIO,
        usuario.codigo,
        usuario.nome.encode(),
        usuario.codigo_idioma_aprendizado,
        usuario.nivel_atual,
        usuario.pontuacao_total,
        usuario.ordem_conclusao
    )

def desempacotar_usuario(dados_binarios):
    codigo, nome, codigo_idioma_aprendizado, nivel_atual, pontuacao_total, ordem_conclusao = struct.unpack(
        FORMATO_USUARIO,
        dados_binarios
    )

    return Usuario(
        codigo, 
        nome.decode().rstrip("\x00"), 
        codigo_idioma_aprendizado, 
        nivel_atual, 
        pontuacao_total,
        ordem_conclusao
    )

def cadastrar_usuario(raiz_usuarios, raiz_idiomas, codigo, nome, codigo_idioma_aprendizado):
    usuario_existente = buscar(raiz_usuarios, codigo)
    
    if usuario_existente is not None:
        return raiz_usuarios
    
    idioma = buscar_idioma(raiz_idiomas, codigo_idioma_aprendizado)

    if idioma is None:
        return raiz_usuarios

    nivel_atual = 1
    pontuacao_total = 0
    ordem_conclusao = 0

    usuario = Usuario(codigo, nome, codigo_idioma_aprendizado, nivel_atual, pontuacao_total, ordem_conclusao)

    with open ("dados/usuarios.dat", "ab") as arquivo:
        arquivo.seek(0,2)
        tamanho_arquivo = arquivo.tell()
        posicao = tamanho_arquivo // TAMANHO_USUARIO
        arquivo.write(empacotar_usuario(usuario))

    raiz_usuarios = inserir(raiz_usuarios, codigo, posicao)

    return raiz_usuarios

def ler_usuario(posicao):
    with open("dados/usuarios.dat", "rb") as arquivo: 
        arquivo.seek(posicao * TAMANHO_USUARIO)

        dados_binarios = arquivo.read(TAMANHO_USUARIO)

        return desempacotar_usuario(dados_binarios)

def buscar_usuario(raiz_usuarios, codigo_usuario):
    resultado = buscar(raiz_usuarios, codigo_usuario)

    if resultado is None: 
        return None

    usuario = ler_usuario(resultado.posicao)
    return usuario

def carregar_indice_usuarios():
    raiz_usuarios = None

    try:
        with open("dados/usuarios.dat", "rb") as arquivo:
            posicao = 0

            while True:
                dados_binarios = arquivo.read(TAMANHO_USUARIO)
                if not dados_binarios:
                    break

                usuario = desempacotar_usuario(dados_binarios)
                if usuario.codigo != 0:
                    raiz_usuarios = inserir(raiz_usuarios, usuario.codigo, posicao)
                posicao += 1
    except FileNotFoundError:
        return raiz_usuarios

    return raiz_usuarios

def buscar_usuario_com_idioma(raiz_usuarios, raiz_idiomas, codigo_usuario):
    usuario = buscar_usuario(raiz_usuarios, codigo_usuario)

    if usuario is None:
        return None

    idioma = buscar_idioma(raiz_idiomas, usuario.codigo_idioma_aprendizado)

    if idioma is None:
        return None

    return usuario, idioma

def listar_usuarios(raiz_usuarios, lista):
    if raiz_usuarios is not None:
        listar_usuarios(raiz_usuarios.esquerda, lista)
        usuario = ler_usuario(raiz_usuarios.posicao)
        lista.append(usuario)
        listar_usuarios(raiz_usuarios.direita, lista)
    return lista

def atualizar_usuario(raiz_usuarios, usuario):
    resultado = buscar(raiz_usuarios, usuario.codigo)

    if resultado is None:
        return False

    posicao = resultado.posicao

    with open("dados/usuarios.dat", "r+b") as arquivo: 
            arquivo.seek(posicao * TAMANHO_USUARIO)
            arquivo.write(empacotar_usuario(usuario))
    

    return True

def gerar_ranking(raiz_usuarios):
    usuarios = listar_usuarios(raiz_usuarios, [])

    ranking = sorted(usuarios, key=lambda usuario: (-usuario.pontuacao_total, usuario.ordem_conclusao if usuario.ordem_conclusao != 0 else float("inf"),
                                                    usuario.codigo))

    return ranking

def obter_proximo_codigo_usuario(raiz_usuarios):
    usuarios = listar_usuarios(raiz_usuarios, [])

    maior_codigo = 0

    for usuario in usuarios:
        if usuario.codigo > maior_codigo:
            maior_codigo = usuario.codigo

    return maior_codigo + 1

def excluir_usuario(raiz_usuarios, codigo_usuario):
    resultado = buscar(raiz_usuarios, codigo_usuario)

    if resultado is None:
        return raiz_usuarios

    posicao = resultado.posicao

    usuario = ler_usuario(posicao)
    usuario.codigo = 0

    with open("dados/usuarios.dat", "r+b") as arquivo: #r = ler, + = também escrever, b = binário
                arquivo.seek(posicao * TAMANHO_USUARIO)
                arquivo.write(empacotar_usuario(usuario))

    raiz_usuarios = excluir(raiz_usuarios, codigo_usuario)

    return raiz_usuarios

def obter_proxima_ordem_conclusao(raiz_usuarios):
    usuarios = listar_usuarios(raiz_usuarios, [])

    maior_ordem = 0

    for usuario in usuarios:
        if usuario.ordem_conclusao > maior_ordem:
            maior_ordem  = usuario.ordem_conclusao

    return maior_ordem + 1