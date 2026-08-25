import struct 

from models.idioma import Idioma
from estrutura.arvore import inserir 

FORMATO_IDIOMA = "i30s"  # Formato para serialização: inteiro (código) e string de 30 bytes (descrição)
TAMANHO_IDIOMA = struct.calcsize(FORMATO_IDIOMA)  # Tamanho total do registro de idioma em bytes

def empacotar_idioma(idioma):
    return struct.pack(
        FORMATO_IDIOMA,
        idioma.codigo,
        idioma.descricao.encode() 
    )

def cadastrar_idioma(raiz, codigo, descricao):
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