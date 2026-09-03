from services.idioma_service import carregar_indice_idiomas
from services.licao_service import carregar_indice_licoes
from services.exercicio_service import carregar_indice_exercicios
from services.usuario_service import carregar_indice_usuarios

from seed.dados_iniciais import (
    carregar_idiomas_iniciais,
    carregar_licoes_iniciais,
    carregar_exercicios_iniciais,
)

raiz_idiomas = carregar_indice_idiomas()
raiz_licoes = carregar_indice_licoes()
raiz_exercicios = carregar_indice_exercicios()
raiz_usuarios = carregar_indice_usuarios()


if raiz_idiomas is None:
    raiz_idiomas = carregar_idiomas_iniciais(raiz_idiomas)

if raiz_licoes is None:
    raiz_licoes = carregar_licoes_iniciais(raiz_licoes, raiz_idiomas)

if raiz_exercicios is None:
    raiz_exercicios = carregar_exercicios_iniciais(raiz_exercicios, raiz_licoes)
