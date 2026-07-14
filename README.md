# 📺 Catálogo de Séries API

Uma API REST desenvolvida com **FastAPI** para gerenciamento de um catálogo de séries de TV.

O projeto foi desenvolvido como parte dos estudos em desenvolvimento Backend com Python e evoluído além dos requisitos do curso, aplicando boas práticas de arquitetura, organização em camadas e utilização de ORM com SQLAlchemy.

---

# 🚀 Objetivos do Projeto

Este projeto tem como objetivo demonstrar conhecimentos em:

* Desenvolvimento de APIs REST com FastAPI
* Arquitetura em camadas (Router → Service → Repository)
* Modelagem de dados com Pydantic
* Persistência de dados com SQLite
* ORM utilizando SQLAlchemy
* Organização de projetos Python
* Boas práticas de desenvolvimento Backend
* Versionamento utilizando Git e GitHub

---

# 🛠 Tecnologias Utilizadas

* Python 3.13
* FastAPI
* Uvicorn
* SQLAlchemy
* SQLite
* Pydantic
* Git
* GitHub

---

# 📁 Estrutura do Projeto

```
catalogo-series-api/
│
├── app/
│   ├── database.py
│   ├── main.py
│
│   ├── routers/
│   │   └── series.py
│   │
│   ├── services/
│   │   └── series_service.py
│   │
│   ├── repositories/
│   │   └── series_repository.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── serie_model.py
│   │
│   └── schemas/
│       ├── __init__.py
│       └── serie.py
│
├── data/
│   └── series.db
│
├── requirements.txt
└── README.md
```

---

# 🏛 Arquitetura

O projeto segue uma arquitetura em camadas para separar responsabilidades e facilitar manutenção e evolução.

```
Cliente
   │
   ▼
FastAPI Router
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
SQLite Database
```

### Router

Responsável por:

* Receber requisições HTTP
* Validar parâmetros
* Retornar respostas HTTP
* Tratar exceções

---

### Service

Responsável por:

* Regras de negócio
* Comunicação entre Router e Repository

---

### Repository

Responsável por:

* Acesso ao banco de dados
* Consultas utilizando SQLAlchemy
* Operações CRUD

---

### Models

Representam as tabelas do banco de dados utilizando SQLAlchemy.

---

### Schemas

Representam os modelos utilizados pela API através do Pydantic para validação de entrada e saída de dados.

---

# 📚 Funcionalidades

Atualmente a API permite:

* Cadastro de séries
* Listagem de todas as séries
* Busca de série por ID
* Atualização de informações
* Exclusão de registros

Todas as operações utilizam persistência em banco SQLite através do SQLAlchemy.

---

# 🔗 Endpoints

## Criar série

```
POST /series
```

---

## Listar séries

```
GET /series
```

---

## Buscar série por ID

```
GET /series/{id}
```

---

## Atualizar série

```
PUT /series/{id}
```

---

## Excluir série

```
DELETE /series/{id}
```

---

# 📄 Exemplo de Requisição

```json
{
    "titulo": "Breaking Bad",
    "genero": "Drama",
    "ano_lancamento": 2008,
    "temporadas": 5,
    "sinopse": "Professor de química inicia uma carreira no tráfico de drogas."
}
```

---

# 📤 Exemplo de Resposta

```json
{
    "id": 1,
    "titulo": "Breaking Bad",
    "genero": "Drama",
    "ano_lancamento": 2008,
    "temporadas": 5,
    "sinopse": "Professor de química inicia uma carreira no tráfico de drogas."
}
```

---

# ▶ Como executar o projeto

## Clone o repositório

```bash
git clone https://github.com/danielbramos4/catalogo-series-api.git
```

---

## Entre na pasta

```bash
cd catalogo-series-api
```

---

## Crie um ambiente virtual

Windows

```bash
python -m venv .venv
```

Linux

```bash
python3 -m venv .venv
```

---

## Ative o ambiente

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

---

## Instale as dependências

```bash
pip install -r requirements.txt
```

---

## Execute a API

```bash
uvicorn app.main:app --reload
```

---

# 📖 Documentação automática

Após iniciar a aplicação:

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 💡 Conceitos aplicados

Durante o desenvolvimento foram aplicados conceitos como:

* Programação Orientada a Objetos
* Arquitetura em Camadas
* API REST
* CRUD
* ORM
* SQLAlchemy
* SQLite
* Pydantic
* Injeção de Dependência
* Organização de Projeto
* Versionamento com Git

---



# 📈 Aprendizados

Este projeto foi desenvolvido para consolidar conhecimentos em desenvolvimento Backend utilizando Python e FastAPI.

Durante sua evolução foi possível aplicar conceitos importantes utilizados no mercado, como separação de responsabilidades, organização em camadas, persistência de dados com ORM e boas práticas de desenvolvimento.

O projeto continuará sendo evoluído com novas funcionalidades e melhorias arquiteturais, servindo como parte do meu portfólio de desenvolvimento Backend.

---

# 👨‍💻 Autor

**Daniel Barbosa Ramos**

* GitHub: https://github.com/danielbramos4
* LinkedIn: https://www.linkedin.com/in/daniel-barbosa-ramos-5a428b287

---

⭐ Caso este projeto tenha sido útil ou interessante para você, deixe uma estrela no repositório.
