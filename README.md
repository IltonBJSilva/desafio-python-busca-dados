# 📄 Desafio Técnico de Python – Microsserviço de Busca de Documentos

## 1️⃣ Descrição do Projeto

##### Este microsserviço permite a criação, armazenamento e busca de documentos textuais. Foi desenvolvido em **Python 3** e utiliza um banco de dados relacional (como SQLite podendo migrar para o PostgreSQL facilmente) para persistência de dados. A aplicação oferece as seguintes funcionalidades:

* Criação de documentos através de requisições `POST`.
* Busca de documentos por palavra-chave ou frases completas via `GET`.
* Ordenação de resultados por proximidade geográfica, utilizando latitude e longitude.
* Persistência de dados garantida, não utilizando armazenamento em memória.

## 2️⃣ Decisões de Projeto e Arquitetura

##### Para atender aos critérios de avaliação, a arquitetura e as tecnologias foram escolhidas com foco em  **performance, manutenibilidade, escalabilidade e boas práticas de programação** .

* **Arquitetura Leve (MVC-like):** A estrutura do projeto foi organizada de forma a separar as responsabilidades, facilitando a manutenção e a legibilidade do código:
  * `routes`: Camada responsável por receber as requisições HTTP e direcioná-las.
  * `services`: Onde a lógica de negócio, como a busca e a ordenação, é implementada.
  * `models`: Define a estrutura dos dados que serão persistidos no banco.
  * `schemas`: Garante a validação e serialização dos dados, evitando a entrada de informações inválidas.
* **Framework Flask:** Escolhido por ser um microframework leve, flexível e ideal para a construção de microsserviços. Ele permite iniciar rapidamente e adicionar extensões conforme a necessidade, sem sobrecarregar o projeto.
* **SQLAlchemy como ORM:** Para a interação com o banco de dados, o SQLAlchemy foi a escolha principal. Ele abstrai as consultas SQL, o que previne vulnerabilidades como **SQL Injection** (um dos testes de segurança implementados) e facilita a troca do banco de dados (de SQLite para PostgreSQL, por exemplo) sem alterações na lógica de negócio.
* **Marshmallow para Validação:** O uso do Marshmallow para definir schemas de validação garante que todos os dados recebidos pela API estejam no formato correto antes de serem processados, tornando a aplicação mais robusta e evitando erros em tempo de execução

## 3️⃣ Funcionalidades Implementadas

##### A solução implementa todas as funcionalidades solicitadas no desafio:

* **Criação de Documentos:** Endpoint `POST /documentos` para persistir novos documentos em um banco de dados relacional.
* **Busca por Palavra-Chave:** O endpoint `GET /documentos` permite a busca por uma palavra-chave no título, conteúdo ou autor do documento.
* **[Bônus] Ordenação por Localização:** A busca pode ser refinada com os parâmetros `latitude` e `longitude`, que ordenam os resultados do mais próximo ao mais distante, utilizando a fórmula de Haversine para precisão.
* **[Bônus] Busca por Expressões:** A lógica de busca foi aprimorada para aceitar frases completas (e não apenas uma palavra), dividindo a busca em múltiplos termos e garantindo que todos estejam presentes nos documentos retornados.

## 4️⃣ Estrutura do Projeto

##### O projeto segue uma estrutura organizada, separando as responsabilidades em diferentes módulos:

**Bash**

```
desafio-python-busca-dados/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # Ponto de entrada da aplicação Flask
│   ├── config.py            # Configurações de ambiente
│   │
│   ├── models/              # Modelos de dados do SQLAlchemy
│   │   └── document.py
│   │
│   ├── schemas/             # Schemas de validação do Marshmallow
│   │   └── document_schema.py
│   │
│   ├── routes/              # Definição dos endpoints da API
│   │   └── document_routes.py
│   │
│   ├── services/            # Lógica de negócio da aplicação
│   │   └── document_service.py
│   │
│   ├── utils/               # Funções auxiliares
│   │   └── geo_utils.py
│   │
│   └── database/
│       └── connection.py    # Configuração da conexão com o banco de dados
│
├── reports/
│   └── test_report.html
├── tests/                   # Testes unitários e de integração
│   └── test_document.py
│
├── requirements.txt         # Dependências do projeto
├── README.md                # Documentação do projeto
└── .env                     # Arquivo de configuração de ambiente
```

---

## 4️⃣ Instalação e Execução

##### Siga os passos abaixo para executar o projeto.

* Certifique-se de ter **Python** e **Git** instalados.

* Caso ocorra algum erro de módulo, rode `pip install nome-do-modulo`.

1. **Clone o repositório:**
   **Bash**

   ```
   git clone https://github.com/IltonBJSilva/desafio-python-busca-dados.git
   cd desafio-python-busca-dados
   ```
2. **Crie e ative um ambiente virtual:**
   **Bash**

   ```
   python -m venv venv
   # No Windows: venv\Scripts\activate
   # No Linux/Mac: source venv/bin/activate
   ```
3. **Instale as dependências:**
   **Bash**

   ```
   pip install -r requirements.txt
   ```
4. **Inicie a aplicação:**
   **Bash**

   ```
   python -m app.main
   ```

   A API estará disponível em `http://12-7.0.0.1:5000`.

---

## 5️⃣ Endpoints da API

### 5.1 POST /documentos

Cria um novo documento no banco de dados.

**Exemplo de JSON**

**JSON**

```
{
  "titulo": "Carros antigos em Porto Alegre",
  "autor": "João Mecânico",
  "conteudo": "Um encontro será realizado com carros antigos e clássicos na cidade de Porto Alegre.",
  "data": "2025-01-15",
  "latitude": "-30.0330",
  "longitude": "-51.2300"
}
```

**Exemplo de Resposta (código 201 - Created):**

**JSON**

```
{
  "id": 1,
  "titulo": "Carros antigos em Porto Alegre",
  "autor": "João Mecânico",
  "conteudo": "Um encontro será realizado com carros antigos e clássicos na cidade de Porto Alegre.",
  "data": "2025-01-15",
  "latitude": -30.03,
  "longitude": -51.23
}
```

**Regras de Validação:**

* `titulo`: Obrigatório (string).
* `conteudo`: Obrigatório (string).
* `data`: Obrigatório, no formato `"YYYY-MM-DD"`.
* `autor`, `latitude`, `longitude`: Opcionais.

### 5.2 GET /documentos

Busca documentos com base em parâmetros de consulta.

**Parâmetros de Consulta (Query Parameters):**

* `palavraChave` (opcional): Uma palavra-chave para buscar no título, autor ou conteúdo.
* `busca` (opcional): Uma frase completa para busca.
* `latitude` e `longitude` (opcionais): Coordenadas para ordenar os resultados por proximidade.

**Exemplo de Requisição:**

```
http://127.0.0.1:5000/documentos?palavraChave=carros&latitude=-30.0300&longitude=-51.2290
```

**Exemplo de Resposta (código 200 - OK):**

**JSON**

```
[
  {
    "id": 2,
    "titulo": "Guia de bicicletas urbanas",
    "autor": "Carlos Ciclista",
    "conteudo": "Este guia foca em bicicletas, mas menciona brevemente carros como alternativa urbana.",
    "data": "2025-03-10",
    "latitude": -30.02,
    "longitude": -51.22
  },
  {
    "id": 1,
    "titulo": "Carros antigos em Porto Alegre",
    "autor": "João Mecânico",
    "conteudo": "Um encontro será realizado com carros antigos e clássicos na cidade de Porto Alegre.",
    "data": "2025-01-15",
    "latitude": -30.0330,
    "longitude": -51.2300
  }
]
```

**Regras de Validação:**

* É obrigatório fornecer `palavraChave` ou `busca`.
* Se `latitude` for fornecida, `longitude` também deve ser, para que a ordenação por proximidade funcione.

A solução implementa todas as funcionalidades solicitadas no desafio:

* **Criação de Documentos:** Endpoint `POST /documentos` para persistir novos documentos em um banco de dados relacional.
* **Busca por Palavra-Chave:** O endpoint `GET /documentos` permite a busca por uma palavra-chave no título, conteúdo ou autor do documento.
* **[Bônus 1] Ordenação por Localização:** A busca pode ser refinada com os parâmetros `latitude` e `longitude`, que ordenam os resultados do mais próximo ao mais distante, utilizando a fórmula de **Haversine** para precisão.
* **[Bônus 2] Busca por Expressões (Frases Inteiras):** A lógica de busca foi aprimorada para aceitar **frases completas** (e não apenas uma palavra), de modo semelhante ao Google.

  Agora, a API busca a **expressão exata** dentro dos campos `titulo`, `conteudo` e `autor`, retornando todos os documentos que contenham a frase informada.

---

**Requisição:**

<pre class="overflow-visible!" data-start="1152" data-end="1212"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>GET /documentos?busca=Carros+antigos+em+porto+alegre
</span></span></code></div></div></pre>

**Resposta:**

**JSON**

```
[
  {
    "titulo": "Novo encontro de Antiguidades!",
    "autor": "João Mecânico",
    "conteudo": "Nessa sexta-feira (08), acontecerá o encontro de histórico carros antigos na cidade de Porto Alegre. Todos são bem-vindos!",
    "data": "2025-01-01"
  },
  {
    "titulo": "Carros antigos em Porto Alegre",
    "autor": "Maria Historiadora",
    "conteudo": "Um evento sobre a história dos veículos clássicos no RS.",
    "data": "2024-12-15"
  }
]
```

---

### ⚙️ Como Funciona

* A busca por frases utiliza o operador SQL `LIKE '%<frase>%'` em múltiplos campos (`titulo`, `conteudo`, `autor`);
* A filtragem é feita de forma **case-insensitive** (ignora maiúsculas e minúsculas);
* Pode ser combinada com **latitude** e **longitude** para ordenar os resultados por distância;
* É  **compatível com o parâmetro `palavraChave`** , mantendo retrocompatibilidade com a versão anterior do endpoint.

---

## 6️⃣ Modelo de Dados

A tabela `documents` no banco de dados é definida com a seguinte estrutura:

**Python**

```
class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    autor = Column(String(255), nullable=True)
    conteudo = Column(Text, nullable=False)
    data = Column(Date, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
```

## 7️⃣ Testes

O projeto conta com uma suíte de testes robusta para garantir a qualidade e a estabilidade do código. O relatório de testes (`reports/test_report.html`) indica que  **todos os 13 testes passaram com sucesso** .

Os testes implementados cobrem as seguintes áreas:

* **Testes Funcionais:** Validação das funcionalidades de criação (`create_document`) e busca (`search_documents`) de documentos.
* **Testes de Segurança:** Proteção contra tentativas de SQL Injection.
* **Testes de Performance:** Validação de inserções em lote e busca em grandes volumes de dados.
* **Testes de Resiliência:** Garantia de que a aplicação trata dados inválidos sem falhar.
* **Testes de Ordenação Geográfica:** Validação da correta ordenação de documentos por proximidade.
* **Testes de Busca  *Case-Insensitive* :** A busca funciona independentemente de letras maiúsculas ou minúsculas.

✅ A implementação desses testes demonstra um compromisso com as boas práticas de desenvolvimento, arquitetura de software e qualidade de código.
