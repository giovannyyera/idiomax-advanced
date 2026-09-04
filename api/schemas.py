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