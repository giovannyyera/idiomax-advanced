from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import core.estado as estado

from services.exercicio_service import listar_exercicios, buscar_exercicio
from services.licao_service import buscar_licao
from services.idioma_service import listar_idiomas, buscar_idioma
from services.usuario_service import listar_usuarios, buscar_usuario_com_idioma, cadastrar_usuario, buscar_usuario, excluir_usuario, gerar_ranking
from services.pratica_service import responder_exercicio, finalizar_rodada, emitir_certificado
from api.schemas import UsuarioCreate, RespostaExercicio


app = FastAPI(
    title="MaxLanguage API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def inicio():
    return {
        "mensagem": "MaxLanguage API funcionando!"
    }


@app.get("/idiomas")
def listar_idiomas_api():
    idiomas = listar_idiomas(
        estado.raiz_idiomas,
        []
    )

    resultado = []

    for idioma in idiomas:
        resultado.append({
            "codigo": idioma.codigo,
            "descricao": idioma.descricao
        })

    return resultado

@app.get("/usuarios")
def listar_usuarios_api():
    usuarios = listar_usuarios(
        estado.raiz_usuarios,
        []
    )

    resultado = []

    for usuario in usuarios:
        idioma = buscar_idioma(
            estado.raiz_idiomas,
            usuario.codigo_idioma_aprendizado
        )

        resultado.append({
            "codigo": usuario.codigo,
            "nome": usuario.nome,
            "idioma": idioma.descricao,
            "nivel_atual": usuario.nivel_atual,
            "pontuacao_total": usuario.pontuacao_total
        })

    return resultado

@app.get("/usuarios/{codigo}")
def buscar_usuario_api(codigo: int):
    resultado = buscar_usuario_com_idioma(
        estado.raiz_usuarios,
        estado.raiz_idiomas,
        codigo
    )

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    usuario, idioma = resultado

    return {
        "codigo": usuario.codigo,
        "nome": usuario.nome,
        "idioma": idioma.descricao,
        "nivel_atual": usuario.nivel_atual,
        "pontuacao_total": usuario.pontuacao_total
    }

@app.post("/usuarios")
def cadastrar_usuario_api(dados: UsuarioCreate):
    usuario_existente = buscar_usuario(
        estado.raiz_usuarios,
        dados.codigo
    )

    if usuario_existente is not None:
        raise HTTPException(
            status_code=409,
            detail="Já existe um usuário com esse código"
        )

    idioma = buscar_idioma(
        estado.raiz_idiomas,
        dados.codigo_idioma_aprendizado
    )

    if idioma is None:
        raise HTTPException(
            status_code=404,
            detail="Idioma não encontrado"
        )

    estado.raiz_usuarios = cadastrar_usuario(
        estado.raiz_usuarios,
        estado.raiz_idiomas,
        dados.codigo,
        dados.nome,
        dados.codigo_idioma_aprendizado
    )

    usuario = buscar_usuario(
        estado.raiz_usuarios,
        dados.codigo
    )

    return {
        "mensagem": "Usuário cadastrado com sucesso",
        "usuario": {
            "codigo": usuario.codigo,
            "nome": usuario.nome,
            "idioma": idioma.descricao,
            "nivel_atual": usuario.nivel_atual,
            "pontuacao_total": usuario.pontuacao_total
        }
    }

@app.delete("/usuarios/{codigo}")
def excluir_usuario_api(codigo: int):
    usuario = buscar_usuario(
        estado.raiz_usuarios,
        codigo
    )

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    estado.raiz_usuarios = excluir_usuario(
        estado.raiz_usuarios,
        codigo
    )

    return {
        "mensagem": "Usuário excluído com sucesso"
    }

@app.get("/ranking")
def ranking_api():
    ranking = gerar_ranking(
        estado.raiz_usuarios
    )

    resultado = []

    for posicao, usuario in enumerate(
        ranking,
        start=1
    ):
        idioma = buscar_idioma(
            estado.raiz_idiomas,
            usuario.codigo_idioma_aprendizado
        )

        resultado.append({
            "posicao": posicao,
            "codigo": usuario.codigo,
            "nome": usuario.nome,
            "idioma": idioma.descricao,
            "nivel_atual": usuario.nivel_atual,
            "pontuacao_total": usuario.pontuacao_total,
            "ordem_conclusao": usuario.ordem_conclusao
        })

    return resultado

@app.get("/usuarios/{codigo}/exercicios")
def listar_exercicios_usuario_api(codigo: int):
    usuario = buscar_usuario(
        estado.raiz_usuarios,
        codigo
    )

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    if usuario.ordem_conclusao != 0:
        raise HTTPException(
            status_code=400,
            detail="Usuário já concluiu o idioma"
        )

    idioma = buscar_idioma(
        estado.raiz_idiomas,
        usuario.codigo_idioma_aprendizado
    )

    todos_exercicios = listar_exercicios(
        estado.raiz_exercicios,
        []
    )

    exercicios_disponiveis = []

    for exercicio in todos_exercicios:
        licao = buscar_licao(
            estado.raiz_licoes,
            exercicio.cod_licao
        )

        if (
            licao is not None
            and licao.cod_idioma == usuario.codigo_idioma_aprendizado
            and exercicio.nivel_dificuldade == usuario.nivel_atual
        ):
            exercicios_disponiveis.append({
                "codigo": exercicio.cod_exercicio,
                "descricao": exercicio.descricao,
                "opcoes": exercicio.opcoes_resposta
            })

    return {
        "usuario": usuario.nome,
        "idioma": idioma.descricao,
        "nivel_atual": usuario.nivel_atual,
        "pontuacao_total": usuario.pontuacao_total,
        "exercicios": exercicios_disponiveis
    }

@app.post("/usuarios/{codigo}/responder")
def responder_exercicio_api(
    codigo: int,
    dados: RespostaExercicio
):
    usuario = buscar_usuario(
        estado.raiz_usuarios,
        codigo
    )

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    exercicio = buscar_exercicio(
        estado.raiz_exercicios,
        dados.codigo_exercicio
    )

    if exercicio is None:
        raise HTTPException(
            status_code=404,
            detail="Exercício não encontrado"
        )

    acertou = (
        dados.resposta.strip().lower()
        == exercicio.resposta_correta.strip().lower()
    )

    resultado = responder_exercicio(
        estado.raiz_usuarios,
        estado.raiz_exercicios,
        estado.raiz_licoes,
        codigo,
        dados.codigo_exercicio,
        dados.resposta
    )

    if not resultado:
        raise HTTPException(
            status_code=400,
            detail="Não foi possível responder esse exercício"
        )

    usuario_atualizado = buscar_usuario(
        estado.raiz_usuarios,
        codigo
    )

    resposta = {
        "acertou": acertou,
        "pontuacao_total": usuario_atualizado.pontuacao_total
    }

    if not acertou:
        resposta["resposta_correta"] = exercicio.resposta_correta

    return resposta

@app.post("/usuarios/{codigo}/finalizar-rodada")
def finalizar_rodada_api(codigo: int):
    usuario = buscar_usuario(
        estado.raiz_usuarios,
        codigo
    )

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    todos_exercicios = listar_exercicios(
        estado.raiz_exercicios,
        []
    )

    cod_licao = None

    for exercicio in todos_exercicios:
        licao = buscar_licao(
            estado.raiz_licoes,
            exercicio.cod_licao
        )

        if (
            licao is not None
            and licao.cod_idioma == usuario.codigo_idioma_aprendizado
            and exercicio.nivel_dificuldade == usuario.nivel_atual
        ):
            cod_licao = exercicio.cod_licao
            break

    if cod_licao is None:
        raise HTTPException(
            status_code=404,
            detail="Lição não encontrada para o usuário"
        )

    resultado = finalizar_rodada(
        estado.raiz_usuarios,
        estado.raiz_licoes,
        codigo,
        cod_licao
    )

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="Não foi possível finalizar a rodada"
        )

    promoveu, concluiu = resultado

    usuario_atualizado = buscar_usuario(
        estado.raiz_usuarios,
        codigo
    )

    return {
        "promoveu": promoveu,
        "concluiu": concluiu,
        "nivel_atual": usuario_atualizado.nivel_atual,
        "pontuacao_total": usuario_atualizado.pontuacao_total,
        "ordem_conclusao": usuario_atualizado.ordem_conclusao
    }

@app.get("/usuarios/{codigo}/certificado")
def certificado_api(codigo: int):
    certificado = emitir_certificado(
        estado.raiz_usuarios,
        estado.raiz_idiomas,
        codigo
    )

    if certificado is None:
        raise HTTPException(
            status_code=400,
            detail="Usuário ainda não concluiu o idioma"
        )

    return certificado