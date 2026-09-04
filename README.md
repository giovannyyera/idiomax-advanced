# MaxLanguage

O **MaxLanguage** é uma aplicação acadêmica para aprendizado de idiomas, desenvolvida com **Python**, **FastAPI** e **Angular**.

O projeto utiliza **arquivos binários `.dat` para persistência dos dados** e uma **Árvore Binária de Busca em memória** para indexação e localização dos registros.

A aplicação permite cadastro de usuários, prática de exercícios por nível, progressão, ranking e emissão de certificados em PDF.

---

## Objetivo do projeto

O objetivo principal do MaxLanguage é aplicar, na prática, conceitos de:

- Arquivos indexados;
- Estruturas de dados;
- Árvore Binária de Busca;
- Persistência em arquivos binários;
- Separação entre área de dados e área de índice;
- Desenvolvimento de API;
- Integração entre frontend e backend;
- Organização de software em camadas.

O projeto foi desenvolvido como trabalho acadêmico da disciplina relacionada a **Estruturas de Dados / Arquivos Indexados**.

---

## Tecnologias utilizadas

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- ReportLab

### Frontend

- Angular
- TypeScript
- HTML
- CSS

### Persistência de dados

- Arquivos binários `.dat`
- Árvore Binária de Busca em memória

---

## Principais funcionalidades

O sistema possui atualmente:

- Cadastro de usuários;
- Código de usuário gerado automaticamente;
- Seleção do idioma de aprendizado;
- Acesso ao sistema utilizando o código do usuário;
- Consulta dos dados do usuário;
- Exercícios separados por idioma e nível;
- Sistema de pontuação;
- Penalização por respostas incorretas;
- Progressão entre níveis;
- Verificação de conclusão do idioma;
- Ranking de usuários;
- Exclusão lógica de usuários;
- Emissão de certificado;
- Geração de certificado em PDF;
- API REST para comunicação com o frontend Angular.

---

## Idiomas disponíveis

Atualmente o sistema possui exercícios para:

- Inglês;
- Espanhol;
- Francês.

Cada idioma possui diferentes níveis de dificuldade.

---

## Sistema de níveis

O usuário inicia no:

```text
Nível 1
```

Cada nível possui uma rodada de exercícios.

A progressão ocorre de acordo com a pontuação acumulada.

Exemplo:

```text
Nível 1 -> 100 pontos
Nível 2 -> 200 pontos
Nível 3 -> 300 pontos
```

Ao atingir a pontuação necessária, o usuário pode avançar para o próximo nível.

Quando conclui o último nível, o idioma é considerado concluído.

---

## Sistema de pontuação

Cada exercício possui uma pontuação definida.

Atualmente:

```text
5 exercícios por nível
20 pontos por resposta correta
```

Portanto:

```text
5 x 20 = 100 pontos por nível
```

Quando o usuário responde corretamente, recebe a pontuação do exercício.

Quando responde incorretamente, perde **10% da pontuação daquele exercício**.

Exemplo:

```text
Exercício vale 20 pontos

Resposta correta:
+20 pontos

Resposta incorreta:
-2 pontos
```

A pontuação nunca pode ficar abaixo de zero.

---

## Ranking

O sistema possui um ranking dos usuários.

A classificação considera principalmente:

1. Pontuação total;
2. Ordem de conclusão;
3. Código do usuário como critério adicional de desempate.

O ranking é gerado dinamicamente a partir dos usuários cadastrados.

---

## Certificado

Quando o usuário conclui o idioma, ele pode emitir um certificado.

O certificado contém informações como:

- Nome do usuário;
- Idioma concluído;
- Nível concluído;
- Pontuação total;
- Código do certificado.

O certificado é gerado automaticamente em formato PDF utilizando a biblioteca **ReportLab**.

Os PDFs gerados são armazenados localmente na pasta:

```text
certificados/
```

Essa pasta não é versionada no Git.

---

## Estrutura do projeto

A estrutura principal do projeto é semelhante a:

```text
idiomax-advanced/
│
├── api/
│   ├── __init__.py
│   ├── app.py
│   └── schemas.py
│
├── assets/
│   └── certificado_modelo.png
│
├── certificados/
│
├── core/
│   ├── __init__.py
│   └── estado.py
│
├── dados/
│   ├── idiomas.dat
│   ├── licoes.dat
│   ├── exercicios.dat
│   └── usuarios.dat
│
├── estrutura/
│   └── arvore.py
│
├── models/
│   ├── idioma.py
│   ├── licao.py
│   ├── exercicio.py
│   └── usuario.py
│
├── seed/
│   └── dados_iniciais.py
│
├── services/
│   ├── certificado_service.py
│   ├── exercicio_service.py
│   ├── idioma_service.py
│   ├── licao_service.py
│   ├── pratica_service.py
│   └── usuario_service.py
│
├── frontend/
│   └── aplicação Angular
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Organização do backend

O backend foi separado em diferentes responsabilidades.

### `models/`

Contém as classes utilizadas para representar as entidades do sistema.

Exemplos:

- Idioma;
- Lição;
- Exercício;
- Usuário.

### `services/`

Contém as regras de negócio e operações relacionadas às entidades.

Exemplos:

- Cadastro;
- Busca;
- Leitura;
- Atualização;
- Exclusão;
- Ranking;
- Prática;
- Certificado.

### `estrutura/`

Contém a implementação da Árvore Binária de Busca utilizada como índice.

### `dados/`

Contém os arquivos binários utilizados para persistência.

### `seed/`

Contém os dados iniciais utilizados para popular idiomas, lições e exercícios.

### `api/`

Contém a API FastAPI responsável pela comunicação entre o backend Python e o frontend Angular.

### `core/`

Mantém o estado compartilhado das árvores de índice utilizadas pela aplicação.

---

## Arquivos indexados

O projeto utiliza dois conceitos principais:

```text
Área de dados
+
Área de índice
```

### Área de dados

Os registros são armazenados em arquivos binários:

```text
dados/*.dat
```

### Área de índice

Os índices são mantidos em memória utilizando uma:

```text
Árvore Binária de Busca
```

Cada nó da árvore armazena informações como:

```text
código
posição do registro no arquivo
filho esquerdo
filho direito
```

Isso permite localizar a posição de um registro no arquivo sem precisar percorrer todos os registros.

---

## Exclusão de usuários

A exclusão do usuário é realizada utilizando exclusão lógica no arquivo.

O registro permanece fisicamente no arquivo `.dat`, porém seu código é alterado para:

```text
0
```

Dessa forma ele passa a ser considerado excluído.

Ao reconstruir o índice, registros com código `0` são ignorados.

O nó correspondente também é removido da árvore em memória.

---

# Como executar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/giovannyyera/idiomax-advanced.git
```

Acesse a pasta:

```bash
cd idiomax-advanced
```

---

## 2. Criar o ambiente virtual Python

No Windows:

```bash
python -m venv venv
```

Ative o ambiente:

```bash
venv\Scripts\activate
```

Quando estiver ativo, o terminal deverá apresentar algo semelhante a:

```text
(venv) C:\idiomax-advanced>
```

---

## 3. Instalar as dependências do backend

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

---

## 4. Executar a API

Na raiz do projeto:

```bash
uvicorn api.app:app --reload
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

---

## Documentação da API

O FastAPI disponibiliza automaticamente a documentação Swagger.

Acesse:

```text
http://127.0.0.1:8000/docs
```

Por essa página é possível consultar e testar os endpoints disponíveis.

---

## 5. Executar o frontend Angular

Abra outro terminal.

Entre na pasta:

```bash
cd frontend
```

Instale as dependências:

```bash
npm install
```

Depois execute:

```bash
npm start
```

O frontend ficará disponível em:

```text
http://localhost:4200
```

---

## Execução completa

Para utilizar a aplicação completa, devem existir dois terminais abertos.

### Terminal 1 - Backend

```bash
uvicorn api.app:app --reload
```

### Terminal 2 - Frontend

```bash
cd frontend
npm start
```

Depois acesse:

```text
http://localhost:4200
```

---

## Principais rotas da API

Algumas das principais rotas disponíveis são:

```text
GET    /idiomas
GET    /usuarios
GET    /usuarios/{codigo}
POST   /usuarios
DELETE /usuarios/{codigo}

GET    /usuarios/{codigo}/exercicios
POST   /usuarios/{codigo}/responder
POST   /usuarios/{codigo}/finalizar-rodada

GET    /ranking

GET    /usuarios/{codigo}/certificado
GET    /usuarios/{codigo}/certificado/pdf
```

A lista completa pode ser consultada pelo Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Fluxo principal da aplicação

O fluxo básico do usuário é:

```text
Cadastro
   ↓
Recebe código de usuário
   ↓
Acessa utilizando o código
   ↓
Home
   ↓
Prática de exercícios
   ↓
Pontuação
   ↓
Progressão de nível
   ↓
Conclusão do idioma
   ↓
Certificado
```

O usuário também pode acessar o ranking ou excluir sua conta.

---

## Arquivos que não são enviados ao GitHub

O projeto utiliza `.gitignore` para evitar o versionamento de arquivos locais ou gerados automaticamente.

Entre eles:

```text
venv/
.env
dados/*.dat
certificados/
__pycache__/
frontend/node_modules/
frontend/dist/
frontend/.angular/cache/
```

Por isso, arquivos de dados e certificados gerados localmente não fazem parte do repositório.

---

## Frontend

O frontend foi desenvolvido utilizando Angular e se comunica com a API FastAPI por requisições HTTP.

As principais páginas são:

```text
Acesso
Cadastro
Home
Prática
Ranking
Certificado
```

A organização principal está em:

```text
frontend/src/app/pages/
```

E a comunicação com a API está centralizada em:

```text
frontend/src/app/services/api.service.ts
```

---

## Estado atual do projeto

Atualmente o projeto possui o fluxo principal funcional entre frontend e backend.

As próximas etapas envolvem principalmente:

- Refinamento visual;
- Melhorias de experiência do usuário;
- Testes adicionais;
- Correção de possíveis falhas encontradas durante os testes;
- Ajustes finais para entrega acadêmica.

---

## Observação

Este projeto foi desenvolvido com finalidade acadêmica.

A arquitetura com arquivos binários e Árvore Binária de Busca foi escolhida principalmente para aplicação prática dos conceitos estudados na disciplina, e não como uma arquitetura destinada a aplicações comerciais de grande escala.

---

## Repositório

GitHub:

```text
https://github.com/giovannyyera/idiomax-advanced
```

---

## MaxLanguage

Aprenda. Pratique. Evolua.
