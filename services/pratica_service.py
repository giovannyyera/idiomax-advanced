from services.usuario_service import buscar_usuario, atualizar_usuario
from services.exercicio_service import buscar_exercicio
from services.licao_service import buscar_licao

def pode_praticar_exercicio(raiz_usuarios, raiz_exercicios, codigo_usuario, cod_exercicio):
    usuario = buscar_usuario(raiz_usuarios, codigo_usuario)

    if usuario is None:
        return False

    exercicio = buscar_exercicio(raiz_exercicios, cod_exercicio)

    if exercicio is None:
        return False

    if exercicio.nivel_dificuldade <= usuario.nivel_atual:  
        return True

    return False

def responder_exercicio(raiz_usuarios, raiz_exercicios, raiz_licoes, codigo_usuario, cod_exercicio, resposta_usuario):
    usuario = buscar_usuario(raiz_usuarios, codigo_usuario)
    exercicio = buscar_exercicio(raiz_exercicios, cod_exercicio)

    if usuario is None or exercicio is None:
        return False

    licao = buscar_licao(raiz_licoes, exercicio.cod_licao)

    if licao is None:
        return False

    if not pode_praticar_exercicio(raiz_usuarios, raiz_exercicios, codigo_usuario, cod_exercicio):
        return False

    if resposta_usuario.strip().lower() == exercicio.resposta_correta.strip().lower():
        usuario.pontuacao_total += exercicio.pontuacao
    else:
        penalidade = int(exercicio.pontuacao * 0.10)
        usuario.pontuacao_total -= penalidade

    if usuario.pontuacao_total < 0:
        usuario.pontuacao_total = 0

    verificar_promocao_nivel(usuario, licao)

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