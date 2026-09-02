from services.idioma_service import cadastrar_idioma
from services.licao_service import cadastrar_licao
from services.exercicio_service import cadastrar_exercicio

IDIOMAS_INICIAIS = [
    (1, "Inglês"),
    (2, "Espanhol"),
    (3, "Francês")
]

def carregar_idiomas_iniciais(raiz):

    for codigo, descricao in IDIOMAS_INICIAIS:
        raiz = cadastrar_idioma(
            raiz,
            codigo,
            descricao
        )

    return raiz

LICOES_INICIAIS = [
    (101, 1, 3),  # Inglês
    (102, 2, 3),  # Espanhol
    (103, 3, 3)   # Francês
]

def carregar_licoes_iniciais(raiz_licoes, raiz_idiomas):

    for cod_licao, cod_idioma, total_niveis in LICOES_INICIAIS:
        raiz_licoes = cadastrar_licao(
            raiz_licoes,
            raiz_idiomas,
            cod_licao,
            cod_idioma,
            total_niveis
        )

    return raiz_licoes

EXERCICIOS_INICIAIS = [
    #! Inglês - Nível 1 (códigos: 1001 até 1005)
    (
        1001,
        101,
        1,
        "Qual é a tradução de 'dog'?",
        ["cachorro", "gato", "casa", "carro"],
        "cachorro",
        20
    ),
    (
        1002,
        101,
        1,
        "Qual é a tradução de 'cat'?",
        ["cachorro", "gato", "livro", "porta"],
        "gato",
        20
    ),
    (
        1003,
        101,
        1,
        "Qual é a tradução de 'house'?",
        ["casa", "carro", "escola", "livro"],
        "casa",
        20
    ),
    (
        1004,
        101,
        1,
        "Qual é a tradução de 'book'?",
        ["mesa", "livro", "janela", "cadeira"],
        "livro",
        20
    ),
    (
        1005,
        101,
        1,
        "Qual é a tradução de 'water'?",
        ["água", "comida", "leite", "café"],
        "água",
        20
    ),
    #! Inglês - Nível 2 (códigos: 1006 até 1010)
    (
        1006,
        101,
        2,
        "Qual é a tradução de 'I am happy'?",
        ["Eu estou feliz", "Eu estou cansado", "Eu tenho fome", "Eu estou triste"],
        "Eu estou feliz",
        20
    ),
    (
        1007,
        101,
        2,
        "Complete: She ___ a student.",
        ["am", "are", "is", "be"],
        "is",
        20
    ),
    (
        1008,
        101,
        2,
        "Qual é o plural de 'book'?",
        ["bookes", "books", "book", "bookies"],
        "books",
        20
    ),
    (
        1009,
        101,
        2,
        "Qual frase significa 'Eu gosto de música'?",
        ["I like music", "I play music", "I see music", "I have music"],
        "I like music",
        20
    ),
    (
        1010,
        101,
        2,
        "Complete: They ___ at home.",
        ["is", "am", "are", "be"],
        "are",
        20
    ),
    #! Inglês - Nível 3 (códigos: 1011 até 1015)
    (
        1011,
        101,
        3,
        "Complete: Yesterday I ___ to school.",
        ["go", "went", "going", "goes"],
        "went",
        20
    ),
    (
        1012,
        101,
        3,
        "Qual frase está no futuro?",
        ["I studied yesterday", "I study every day", "I will study tomorrow", "I am studying now"],
        "I will study tomorrow",
        20
    ),
    (
        1013,
        101,
        3,
        "Complete: If it rains, I ___ at home.",
        ["stay", "stayed", "will stay", "staying"],
        "will stay",
        20
    ),
    (
        1014,
        101,
        3,
        "Qual é a tradução de 'She has been studying for two hours'?",
        ["Ela estudou duas horas", "Ela estuda todo dia", "Ela está estudando há duas horas", "Ela estudará duas horas"],
        "Ela está estudando há duas horas",
        20
    ),
    (
        1015,
        101,
        3,
        "Complete: This book is ___ than that one.",
        ["interesting", "more interesting", "most interesting", "interest"],
        "more interesting",
        20
    ),
    #! Espanhol - Nível 1 (códigos: 2001 até 2005)
    (
        2001,
        102,
        1,
        "Qual é a tradução de 'perro'?",
        ["cachorro", "gato", "mesa", "livro"],
        "cachorro",
        20
    ),
    (
        2002,
        102,
        1,
        "Qual é a tradução de 'gato'?",
        ["cachorro", "gato", "casa", "porta"],
        "gato",
        20
    ),
    (
        2003,
        102,
        1,
        "Qual é a tradução de 'casa'?",
        ["casa", "escola", "rua", "janela"],
        "casa",
        20
    ),
    (
        2004,
        102,
        1,
        "Qual é a tradução de 'libro'?",
        ["cadeira", "mesa", "livro", "caneta"],
        "livro",
        20
    ),
    (
        2005,
        102,
        1,
        "Qual é a tradução de 'agua'?",
        ["água", "leite", "suco", "café"],
        "água",
        20
    ),
    #! Espanhol - Nível 2 (códigos: 2006 até 2010)
    (
        2006,
        102,
        2,
        "Qual é a tradução de 'Estoy feliz'?",
        ["Estou feliz", "Estou triste", "Estou cansado", "Estou com fome"],
        "Estou feliz",
        20
    ),
    (
        2007,
        102,
        2,
        "Complete: Ella ___ estudiante.",
        ["soy", "eres", "es", "somos"],
        "es",
        20
    ),
    (
        2008,
        102,
        2,
        "Qual é o plural de 'libro'?",
        ["libros", "libres", "libroes", "libro"],
        "libros",
        20
    ),
    (
        2009,
        102,
        2,
        "Qual frase significa 'Eu gosto de música'?",
        ["Me gusta la música", "Tengo música", "Escucho la casa", "Soy música"],
        "Me gusta la música",
        20
    ),
    (
        2010,
        102,
        2,
        "Complete: Nosotros ___ amigos.",
        ["soy", "eres", "somos", "es"],
        "somos",
        20
    ),
    #! Espanhol - Nível 3 (códigos: 2011 até 2015)
    (
        2011,
        102,
        3,
        "Complete: Ayer yo ___ al mercado.",
        ["voy", "fui", "iré", "vamos"],
        "fui",
        20
    ),
    (
        2012,
        102,
        3,
        "Qual frase está no futuro?",
        ["Estudié ayer", "Estudio ahora", "Estudiaré mañana", "Estudio todos los días"],
        "Estudiaré mañana",
        20
    ),
    (
        2013,
        102,
        3,
        "Complete: Si tengo tiempo, ___ contigo.",
        ["iré", "fui", "iba", "voy ayer"],
        "iré",
        20
    ),
    (
        2014,
        102,
        3,
        "Qual é a tradução de 'He estudiado durante dos horas'?",
        ["Estudei durante duas horas", "Estudarei duas horas", "Estudo amanhã", "Não estudei"],
        "Estudei durante duas horas",
        20
    ),
    (
        2015,
        102,
        3,
        "Complete: Este libro es ___ que aquel.",
        ["más interesante", "muy interés", "interesado", "más interesar"],
        "más interesante",
        20
    ),
    #! Francês - Nível 1 (códigos: 3001 até 3005)
    (
        3001,
        103,
        1,
        "Qual é a tradução de 'chien'?",
        ["cachorro", "gato", "livro", "carro"],
        "cachorro",
        20
    ),
    (
        3002,
        103,
        1,
        "Qual é a tradução de 'chat'?",
        ["cachorro", "gato", "casa", "mesa"],
        "gato",
        20
    ),
    (
        3003,
        103,
        1,
        "Qual é a tradução de 'maison'?",
        ["casa", "escola", "rua", "porta"],
        "casa",
        20
    ),
    (
        3004,
        103,
        1,
        "Qual é a tradução de 'livre'?",
        ["mesa", "livro", "cadeira", "janela"],
        "livro",
        20
    ),
    (
        3005,
        103,
        1,
        "Qual é a tradução de 'eau'?",
        ["água", "leite", "café", "comida"],
        "água",
        20
    ),
    #! Francês - Nível 2 (códigos: 3006 até 3010)
    (
        3006,
        103,
        2,
        "Qual é a tradução de 'Je suis heureux'?",
        ["Estou feliz", "Estou cansado", "Estou triste", "Estou com fome"],
        "Estou feliz",
        20
    ),
    (
        3007,
        103,
        2,
        "Complete: Elle ___ étudiante.",
        ["suis", "es", "est", "sommes"],
        "est",
        20
    ),
    (
        3008,
        103,
        2,
        "Qual é o plural de 'livre'?",
        ["livres", "livrez", "livre", "livreses"],
        "livres",
        20
    ),
    (
        3009,
        103,
        2,
        "Qual frase significa 'Eu gosto de música'?",
        ["J'aime la musique", "Je suis musique", "J'ai la maison", "Je vois musique"],
        "J'aime la musique",
        20
    ),
    (
        3010,
        103,
        2,
        "Complete: Nous ___ amis.",
        ["sommes", "êtes", "suis", "est"],
        "sommes",
        20
    ),
    #! Francês - Nível 3 (códigos: 3011 até 3015)
    (
        3011,
        103,
        3,
        "Complete: Hier, je ___ au marché.",
        ["vais", "suis allé", "irai", "aller"],
        "suis allé",
        20
    ),
    (
        3012,
        103,
        3,
        "Qual frase está no futuro?",
        ["J'ai étudié hier", "J'étudie maintenant", "J'étudierai demain", "J'étudie chaque jour"],
        "J'étudierai demain",
        20
    ),
    (
        3013,
        103,
        3,
        "Complete: Si j'ai le temps, je ___ avec toi.",
        ["irai", "suis allé", "allais hier", "aller"],
        "irai",
        20
    ),
    (
        3014,
        103,
        3,
        "Qual é a tradução de 'J'ai étudié pendant deux heures'?",
        ["Estudei durante duas horas", "Estudarei amanhã", "Estou indo estudar", "Não estudei"],
        "Estudei durante duas horas",
        20
    ),
    (
        3015,
        103,
        3,
        "Complete: Ce livre est ___ que celui-là.",
        ["plus intéressant", "très intéresser", "intéressé plus", "plus intéresse"],
        "plus intéressant",
        20
    ) 
]

def carregar_exercicios_iniciais(raiz_exercicios, raiz_licoes): 
    for cod_exercicio, cod_licao, nivel_dificuldade, descricao, opcoes_resposta, resposta_correta, pontuacao in EXERCICIOS_INICIAIS:
        raiz_exercicios = cadastrar_exercicio(
            raiz_exercicios, 
            raiz_licoes, 
            cod_exercicio, 
            cod_licao, 
            nivel_dificuldade, 
            descricao, 
            opcoes_resposta, 
            resposta_correta, 
            pontuacao
        )

    return raiz_exercicios