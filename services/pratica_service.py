from services.usuario_service import buscar_usuario, atualizar_usuario, obter_proxima_ordem_conclusao
from services.exercicio_service import buscar_exercicio
from services.licao_service import buscar_licao
from services.idioma_service import buscar_idioma

def pode_praticar_exercicio(raiz_usuarios, raiz_exercicios, raiz_licoes, codigo_usuario, cod_exercicio):
    usuario = buscar_usuario(raiz_usuarios, codigo_usuario)

    if usuario is None:
        return False

    exercicio = buscar_exercicio(raiz_exercicios, cod_exercicio)

    if exercicio is None:
        return False

    licao = buscar_licao(raiz_licoes, exercicio.cod_licao)

    if licao is None:
        return False

    if licao.cod_idioma != usuario.codigo_idioma_aprendizado:
        return False

    if exercicio.nivel_dificuldade > usuario.nivel_atual:  
        return False

    return True

def responder_exercicio(raiz_usuarios, raiz_exercicios, raiz_licoes, codigo_usuario, cod_exercicio, resposta_usuario):
    usuario = buscar_usuario(raiz_usuarios, codigo_usuario)
    exercicio = buscar_exercicio(raiz_exercicios, cod_exercicio)

    if usuario is None or exercicio is None:
        return False

    licao = buscar_licao(raiz_licoes, exercicio.cod_licao)

    if licao is None:
        return False

    if not pode_praticar_exercicio(raiz_usuarios, raiz_exercicios, raiz_licoes, codigo_usuario, cod_exercicio):
        return False

    if resposta_usuario.strip().lower() == exercicio.resposta_correta.strip().lower():
        usuario.pontuacao_total += exercicio.pontuacao
    else:
        penalidade = int(exercicio.pontuacao * 0.10)
        usuario.pontuacao_total -= penalidade

    if usuario.pontuacao_total < 0:
        usuario.pontuacao_total = 0

    pontuacao_maxima_nivel = usuario.nivel_atual * 100

    if usuario.pontuacao_total > pontuacao_maxima_nivel:
        usuario.pontuacao_total = pontuacao_maxima_nivel

    atualizar_usuario(raiz_usuarios, usuario)

    return True

def verificar_promocao_nivel(usuario, licao):
    pontuacao_necessaria = usuario.nivel_atual * 100

    if licao.cod_idioma != usuario.codigo_idioma_aprendizado:
        return False

    if usuario.pontuacao_total >= pontuacao_necessaria:
        if usuario.nivel_atual < licao.total_niveis:
            usuario.nivel_atual += 1
            return True
    
    return False

def verificar_conclusao_idioma(usuario, licao):
    return(
        usuario.nivel_atual == licao.total_niveis 
        and usuario.pontuacao_total >= usuario.nivel_atual * 100
    )

def emitir_certificado(usuario, idioma, licao):
    if not verificar_conclusao_idioma(usuario, licao):
        return None

    return {"nome": usuario.nome, "idioma": idioma.descricao, "nivel_concluido": licao.total_niveis}

def finalizar_rodada(raiz_usuarios, raiz_licoes, codigo_usuario, cod_licao):
    usuario = buscar_usuario(raiz_usuarios, codigo_usuario)
    licao = buscar_licao(raiz_licoes, cod_licao)

    if usuario is None or licao is None:
        return False

    promoveu = verificar_promocao_nivel(usuario, licao)
    concluiu = verificar_conclusao_idioma(usuario, licao)

    if concluiu and usuario.ordem_conclusao == 0:
        usuario.ordem_conclusao = obter_proxima_ordem_conclusao(raiz_usuarios)

    atualizar_usuario(raiz_usuarios, usuario)

    return promoveu, concluiu

def emitir_certificado(raiz_usuarios, raiz_idiomas, codigo_usuario):
    usuario = buscar_usuario(raiz_usuarios, codigo_usuario)

    if usuario is None:
        return None

    if usuario.ordem_conclusao == 0:
        return None

    idioma = buscar_idioma(raiz_idiomas, usuario.codigo_idioma_aprendizado)

    if idioma is None:
        return None

    certificado = {
        "nome": usuario.nome,
        "idioma": idioma.descricao,
        "nivel_concluido": usuario.nivel_atual,
        "pontuacao_total": usuario.pontuacao_total,
        "ordem_conclusao": usuario.ordem_conclusao
    }

    return certificado