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