from services.idioma_service import carregar_indice_idiomas, buscar_idioma, listar_idiomas
from services.licao_service import carregar_indice_licoes, buscar_licao
from services.exercicio_service import carregar_indice_exercicios, listar_exercicios
from services.usuario_service import carregar_indice_usuarios, cadastrar_usuario, buscar_usuario, buscar_usuario_com_idioma, listar_usuarios, gerar_ranking, excluir_usuario
from services.pratica_service import responder_exercicio, finalizar_rodada

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

while True:
    print("\n- IDIOMAX -")
    print("1 - Cadastrar usuário")
    print("2 - Buscar usuário")
    print("3 - Listar usuários")
    print("4 - Praticar exercícios")
    print("5 - Ver ranking")
    print("6 - Excluir usuário")
    print("7 - Sair")

    opcao = input("\nEscolha uma opção: ")
    if opcao not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("\nOpção inválida. Digite uma opção de 1 a 7.")
        continue

    if opcao == "1":
        print("\n CADASTRAR USUÁRIO ")

        while True:
            try:
                codigo_usuario = int(input("Digite o código do usuário: "))
            except ValueError:
                print("\nDigite apenas números.\n")
                continue

            usuario_existente = buscar_usuario(raiz_usuarios, codigo_usuario)

            if usuario_existente is not None:
                print("\nEsse código de usuário já existe. Digite outro código.\n")
            else:
                break

        while True:
            nome_usuario = input("Digite o nome do usuário: ").strip()

            if nome_usuario: 
                break

            print("\nO nome não pode ficar vazio.")

        idiomas = listar_idiomas(raiz_idiomas, [])
        print("\nIdiomas disponíveis: ")

        for idioma in idiomas:
            print(idioma.codigo, "-", idioma.descricao)

        while True:
            try:
                codigo_idioma = int(input("\nEscolha o idioma: "))
            except ValueError:
                print("\nDigite apenas o número do idioma.")
                continue

            idioma = buscar_idioma(raiz_idiomas, codigo_idioma)

            if idioma is None:
                print("\nOpção de idioma inválida. Escolha novamente.")
            else:
                break

        raiz_usuarios = cadastrar_usuario(raiz_usuarios, raiz_idiomas, codigo_usuario, nome_usuario, codigo_idioma)

        print("\nUsuário cadastrado com sucesso!")

    elif opcao == "2":
        print("\n BUSCAR USUÁRIO ")

        while True:
            try:
                codigo_usuario = int(input("Digite o código do usuário: "))
                break
            except ValueError:
                print("\nDigite apenas números.")

        resultado = buscar_usuario_com_idioma(raiz_usuarios, raiz_idiomas, codigo_usuario)

        if resultado is None:
            print("\nUsuário não encontrado.")

        else:
            usuario, idioma = resultado

            print("\nUsuário encontrado:")
            print("Código:", usuario.codigo)
            print("Nome:", usuario.nome)
            print("Idioma de aprendizado:", idioma.descricao)
            print("Nível atual:", usuario.nivel_atual)
            print("Pontuação total:", usuario.pontuacao_total)

    elif opcao == "3":
        print("\n LISTAR USUÁRIOS ")

        usuarios = listar_usuarios(raiz_usuarios, [])

        if len(usuarios) == 0:
            print("\nNenhum usuário cadastrado.")

        else:
            print()

            for usuario in usuarios:
                idioma = buscar_idioma(
                    raiz_idiomas,
                    usuario.codigo_idioma_aprendizado
                )

                print(
                    "Código:", usuario.codigo,
                    "| Nome:", usuario.nome,
                    "| Idioma:", idioma.descricao,
                    "| Nível:", usuario.nivel_atual,
                    "| Pontuação:", usuario.pontuacao_total
                )

    elif opcao == "4":
        print("\n PRATICAR EXERCÍCIOS")

        while True:
            try:
                codigo_usuario = int(input("Digite o código do usuário: "))
                break
            except ValueError:
                print("\nDigite apenas números.")

        usuario = buscar_usuario(raiz_usuarios, codigo_usuario)

        if usuario is None:
            print("\nUsuário não encontrado.")
            continue

        if usuario.ordem_conclusao != 0:
            print("\nVocê já concluiu este idioma!")
            continue

        idioma = buscar_idioma(raiz_idiomas, usuario.codigo_idioma_aprendizado)

        todos_exercicios = listar_exercicios(raiz_exercicios,[])

        exercicios_nivel = []

        for exercicio in todos_exercicios:
            licao = buscar_licao(raiz_licoes, exercicio.cod_licao)

            if (
                licao is not None
                and licao.cod_idioma == usuario.codigo_idioma_aprendizado
                and exercicio.nivel_dificuldade == usuario.nivel_atual
            ):
                exercicios_nivel.append(exercicio)

        if len(exercicios_nivel) == 0:
            print("\nNenhum exercício disponível para este nível.")
            continue

        print("\nUsuário:", usuario.nome)
        print("Idioma:", idioma.descricao)
        print("Nível atual:", usuario.nivel_atual)
        print("Pontuação atual:", usuario.pontuacao_total)

        for numero, exercicio in enumerate(
            exercicios_nivel,
            start=1
        ):
            print(
                f"\n--- EXERCÍCIO {numero} DE {len(exercicios_nivel)} ---"
            )

            print(exercicio.descricao)

            for numero_opcao, opcao_resposta in enumerate(
                exercicio.opcoes_resposta,
                start=1
            ):
                print(
                    numero_opcao,
                    "-",
                    opcao_resposta
                )

            while True:
                try:
                    escolha = int(input("\nEscolha uma alternativa: "))

                    if 1 <= escolha <= len(exercicio.opcoes_resposta):
                        break

                    print("\nAlternativa inválida. Tente novamente.")
                except ValueError:
                    print("\nDigite apenas o número da alternativa.")

            resposta_usuario = exercicio.opcoes_resposta[
                escolha - 1
            ]

            acertou = (
                resposta_usuario.strip().lower()
                == exercicio.resposta_correta.strip().lower()
            )

            resultado_resposta = responder_exercicio(
                raiz_usuarios,
                raiz_exercicios,
                raiz_licoes,
                codigo_usuario,
                exercicio.cod_exercicio,
                resposta_usuario
            )

            if not resultado_resposta:
                print("\nNão foi possível processar o exercício.")
                continue

            usuario = buscar_usuario(
                raiz_usuarios,
                codigo_usuario
            )

            if acertou:
                print("\nResposta correta!")
            else:
                print("\nResposta incorreta!")
                print(
                    "Resposta correta:",
                    exercicio.resposta_correta
                )

            print(
                "Pontuação atual:",
                usuario.pontuacao_total
            )

        cod_licao = exercicios_nivel[0].cod_licao

        resultado_final = finalizar_rodada(
            raiz_usuarios,
            raiz_licoes,
            codigo_usuario,
            cod_licao
        )

        if resultado_final is False:
            print("\nNão foi possível finalizar a rodada.")
            continue

        promoveu, concluiu = resultado_final

        usuario = buscar_usuario(
            raiz_usuarios,
            codigo_usuario
        )

        print("\n RESULTADO DA RODADA")
        print(
            "Pontuação atual:",
            usuario.pontuacao_total
        )

        if concluiu:
            print("\nParabéns!")
            print("Você concluiu o idioma!")

        elif promoveu:
            print("\nParabéns!")
            print(
                "Você avançou para o nível",
                usuario.nivel_atual
            )

        else:
            pontuacao_necessaria = (
                usuario.nivel_atual * 100
            )

            faltam = (
                pontuacao_necessaria
                - usuario.pontuacao_total
            )

            print("\nVocê permanece no nível atual.")
            print(
                "Faltam",
                faltam,
                "pontos para avançar."
            )

    elif opcao == "5":
        print("\n RANKING")

        ranking = gerar_ranking(
            raiz_usuarios
        )

        if len(ranking) == 0:
            print("\nNenhum usuário cadastrado.")
            continue

        for posicao, usuario in enumerate(
            ranking,
            start=1
        ):
            idioma = buscar_idioma(
                raiz_idiomas,
                usuario.codigo_idioma_aprendizado
            )

            print(
                f"{posicao}º -",
                usuario.nome,
                "| Pontuação:",
                usuario.pontuacao_total,
                "| Nível:",
                usuario.nivel_atual,
                "| Idioma:",
                idioma.descricao
            )

    elif opcao == "6":
        print("\n EXCLUIR USUÁRIO")

        while True:
            try:
                codigo_usuario = int(input("Digite o código do usuário que deseja excluir: "))
                break
            except ValueError:
                print("\nDigite apenas números.")

        usuario = buscar_usuario(
            raiz_usuarios,
            codigo_usuario
        )

        if usuario is None:
            print("\nUsuário não encontrado.")
            continue

        print("\nUsuário encontrado:")
        print("Código:", usuario.codigo)
        print("Nome:", usuario.nome)
        print("Pontuação:", usuario.pontuacao_total)

        while True:
            confirmacao = input("\nTem certeza que deseja excluir este usuário? (S/N): ").strip().lower()

            if confirmacao in ["s", "n"]:
                break

            print("\nDigite apenas S ou N.")

        if confirmacao  == "s":
            raiz_usuarios = excluir_usuario(
                raiz_usuarios,
                codigo_usuario
            )

            print("\nUsuário excluído com sucesso!")

        else:
            print("\nExclusão cancelada.")

    elif opcao == "7":
        print("\nEncerrando o IdioMax...")
        break