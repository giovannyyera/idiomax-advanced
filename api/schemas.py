from pydantic import BaseModel, Field, field_validator


class UsuarioCreate(BaseModel):
    nome: str = Field(min_length=1)
    codigo_idioma_aprendizado: int = Field(gt=0)

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor):
        valor = valor.strip()

        if not valor:
            raise ValueError("O nome não pode ficar vazio")

        return valor


class RespostaExercicio(BaseModel):
    codigo_exercicio: int = Field(gt=0)
    resposta: str = Field(min_length=1)

    @field_validator("resposta")
    @classmethod
    def validar_resposta(cls, valor):
        valor = valor.strip()

        if not valor:
            raise ValueError("A resposta não pode ficar vazia")

        return valor


# codigo <= 0
# → rejeitado

# nome vazio
# → rejeitado

# idioma <= 0
# → rejeitado

# resposta vazia
# → rejeitada


class IdiomaCreate(BaseModel):
    descricao: str = Field(min_length=1)

    @field_validator("descricao")
    @classmethod
    def validar_descricao(cls, valor):
        valor = valor.strip()

        if not valor:
            raise ValueError(
                "A descrição do idioma é obrigatória."
            )

        return valor


class ExercicioCreate(BaseModel):
    codigo_licao: int = Field(gt=0)
    nivel_dificuldade: int = Field(ge=1, le=3)
    descricao: str = Field(min_length=1)
    opcoes_resposta: list[str]
    resposta_correta: str = Field(min_length=1)
    pontuacao: int = Field(gt=0)
    # validar que existem exatamente 4 alternativas, já que é o padrão atual
    @field_validator("opcoes_resposta")
    @classmethod
    def validar_opcoes(cls, opcoes):
        if len(opcoes) != 4:
            raise ValueError(
                "O exercício deve possuir 4 alternativas."
            )

        return opcoes

class LicaoCreate(BaseModel):
    codigo_idioma: int = Field(gt=0)