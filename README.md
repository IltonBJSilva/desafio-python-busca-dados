# 📄 Documentação do Projeto – Microsserviço de Documentos

## 1️⃣ Descrição do Projeto

O microsserviço permite criar, armazenar e buscar documentos textuais em um banco de dados tradicional (SQLite/PostgreSQL/etc.), oferecendo suporte a:

* Criação de documentos via POST.
* Busca de documentos por palavra-chave ou frase completa via GET.
* Ordenação por proximidade geográfica (latitude/longitude).
* Persistência dos dados em banco real (não em memória).

O projeto é desenvolvido em  **Python 3** , utilizando  **Flask** , **SQLAlchemy** e **Marshmallow** para validação.

## 2️⃣🗂️ Estrutura do Projeto

```bash
desafio-python-busca-dados/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # ponto de entrada da aplicação (FastAPI, Flask, etc)
│   ├── config.py            # configs de ambiente (DB, etc)
│   │
│   ├── models/              # modelos do banco de dados
│   │   ├── __init__.py
│   │   └── document.py
│   │
│   ├── schemas/             # validação (Pydantic ou Marshmallow)
│   │   ├── __init__.py
│   │   └── document_schema.py
│   │
│   ├── routes/              # endpoints da API
│   │   ├── __init__.py
│   │   └── document_routes.py
│   │
│   ├── services/            # lógica de negócio (busca, ordenação, etc)
│   │   ├── __init__.py
│   │   └── document_service.py
│   │
│   ├── utils/               # funções auxiliares (ex: cálculo de distância)
│   │   ├── __init__.py
│   │   └── geo_utils.py
│   │
│   └── database/
│       ├── __init__.py
│       └── connection.py    # conexão com o banco (SQLAlchemy, psycopg, etc)
│
├── tests/                   # testes unitários e de integração
│   ├── __init__.py
│   └── test_document.py
│
├── requirements.txt          # dependências do projeto
├── README.md                 # documentação
└── .env.example              # exemplo de variáveis de ambiente (DB_URL, etc)
```

## 3️⃣ Instalação e Configuração

1. Clone o repositório:

<pre class="overflow-visible!" data-start="1584" data-end="1656"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span>clone</span><span> <URL_DO_REPOSITORIO>
</span><span>cd</span><span> desafio-python-busca-dados
</span></span></code></div></div></pre>

2. Crie e ative o ambiente virtual:

<pre class="overflow-visible!" data-start="1694" data-end="1794"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m venv venv
</span><span># Windows</span><span>
venv\Scripts\activate
</span><span># Linux/Mac</span><span>
</span><span>source</span><span> venv/bin/activate
</span></span></code></div></div></pre>

3. Instale as dependências:

<pre class="overflow-visible!" data-start="1824" data-end="1867"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install -r requirements.txt
</span></span></code></div></div></pre>

4. Configure o arquivo `.env` (opcional):

<pre class="overflow-visible!" data-start="1911" data-end="1954"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>DATABASE_URL</span><span>=sqlite:///./desafio.db
</span></span></code></div></div></pre>

5. Inicie a aplicação:

<pre class="overflow-visible!" data-start="1979" data-end="2009"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m app.main
</span></span></code></div></div></pre>

* A aplicação vai rodar em `http://127.0.0.1:5000`.

---

## 4️⃣ Endpoints

### 4.1 POST – Criar Documento

**URL:** `/documentos`

**Método:** POST

**Descrição:** Cria um novo documento no banco de dados.

**Exemplo de JSON:**

<pre class="overflow-visible!" data-start="2243" data-end="2506"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"titulo"</span><span>:</span><span></span><span>"Carros antigos em Porto Alegre"</span><span>,</span><span>
  </span><span>"autor"</span><span>:</span><span></span><span>"João Mecânico"</span><span>,</span><span>
  </span><span>"conteudo"</span><span>:</span><span></span><span>"Um encontro será realizado com carros antigos e clássicos na cidade de Porto Alegre."</span><span>,</span><span>
  </span><span>"data"</span><span>:</span><span></span><span>"2025-01-15"</span><span>,</span><span>
  </span><span>"latitude"</span><span>:</span><span></span><span>-30.0330</span><span>,</span><span>
  </span><span>"longitude"</span><span>:</span><span></span><span>-51.2300</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

**Exemplo de resposta:**

<pre class="overflow-visible!" data-start="2533" data-end="2807"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"id"</span><span>:</span><span></span><span>1</span><span>,</span><span>
  </span><span>"titulo"</span><span>:</span><span></span><span>"Carros antigos em Porto Alegre"</span><span>,</span><span>
  </span><span>"autor"</span><span>:</span><span></span><span>"João Mecânico"</span><span>,</span><span>
  </span><span>"conteudo"</span><span>:</span><span></span><span>"Um encontro será realizado com carros antigos e clássicos na cidade de Porto Alegre."</span><span>,</span><span>
  </span><span>"data"</span><span>:</span><span></span><span>"2025-01-15"</span><span>,</span><span>
  </span><span>"latitude"</span><span>:</span><span></span><span>-30.0330</span><span>,</span><span>
  </span><span>"longitude"</span><span>:</span><span></span><span>-51.2300</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

**Validações:**

* `titulo` e `conteudo` obrigatórios.
* `data` obrigatória, formato `"YYYY-MM-DD"`.
* `autor`, `latitude` e `longitude` opcionais.

---

### 4.2 GET – Buscar Documentos

**URL:** `/documentos`

**Método:** GET

**Descrição:** Busca documentos por palavra-chave ou frase completa, podendo ordenar por proximidade geográfica.

**Query Parameters:**

* `palavraChave` (opcional se `busca` for usada) – Palavra que deve existir no título, autor ou conteúdo.
* `busca` (opcional) – Permite busca por frases completas.
* `latitude` e `longitude` (opcionais) – Ordenam os resultados pela distância do ponto fornecido.

**Exemplo de GET:**

<pre class="overflow-visible!" data-start="3463" data-end="3560"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>http:</span><span>//127.0.0.1:5000/documentos?palavraChave=carros&latitude=-30.0300&longitude=-51.2290</span><span>
</span></span></code></div></div></pre>

**Exemplo de resposta ordenada por proximidade:**

<pre class="overflow-visible!" data-start="3612" data-end="4189"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>[</span><span>
  </span><span>{</span><span>
    </span><span>"id"</span><span>:</span><span></span><span>2</span><span>,</span><span>
    </span><span>"titulo"</span><span>:</span><span></span><span>"Guia de bicicletas urbanas"</span><span>,</span><span>
    </span><span>"autor"</span><span>:</span><span></span><span>"Carlos Ciclista"</span><span>,</span><span>
    </span><span>"conteudo"</span><span>:</span><span></span><span>"Este guia foca em bicicletas, mas menciona brevemente carros como alternativa urbana."</span><span>,</span><span>
    </span><span>"data"</span><span>:</span><span></span><span>"2025-03-10"</span><span>,</span><span>
    </span><span>"latitude"</span><span>:</span><span></span><span>-30.0277</span><span>,</span><span>
    </span><span>"longitude"</span><span>:</span><span></span><span>-51.2287</span><span>
  </span><span>}</span><span>,</span><span>
  </span><span>{</span><span>
    </span><span>"id"</span><span>:</span><span></span><span>1</span><span>,</span><span>
    </span><span>"titulo"</span><span>:</span><span></span><span>"Carros antigos em Porto Alegre"</span><span>,</span><span>
    </span><span>"autor"</span><span>:</span><span></span><span>"João Mecânico"</span><span>,</span><span>
    </span><span>"conteudo"</span><span>:</span><span></span><span>"Um encontro será realizado com carros antigos e clássicos na cidade de Porto Alegre."</span><span>,</span><span>
    </span><span>"data"</span><span>:</span><span></span><span>"2025-01-15"</span><span>,</span><span>
    </span><span>"latitude"</span><span>:</span><span></span><span>-30.0330</span><span>,</span><span>
    </span><span>"longitude"</span><span>:</span><span></span><span>-51.2300</span><span>
  </span><span>}</span><span>
</span><span>]</span><span>
</span></span></code></div></div></pre>

**Validações:**

* Pelo menos `palavraChave` ou `busca` devem ser fornecidos.
* Se `latitude` ou `longitude` forem fornecidas, ambos devem existir para ordenar por proximidade.

---

## 5️⃣ Estrutura de Modelos

<pre class="overflow-visible!" data-start="4402" data-end="4793"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>class</span><span></span><span>Document</span><span>(</span><span>Base</span><span>):
    __tablename__ = </span><span>"documents"</span><span>
    </span><span>id</span><span> = Column(Integer, primary_key=</span><span>True</span><span>, index=</span><span>True</span><span>)
    titulo = Column(String(</span><span>255</span><span>), nullable=</span><span>False</span><span>)
    autor = Column(String(</span><span>255</span><span>), nullable=</span><span>True</span><span>)
    conteudo = Column(Text, nullable=</span><span>False</span><span>)
    data = Column(Date, nullable=</span><span>False</span><span>)
    latitude = Column(Float, nullable=</span><span>True</span><span>)
    longitude = Column(Float, nullable=</span><span>True</span><span>)
</span></span></code></div></div></pre>

---

## 6️⃣ Função de Distância (`geo_utils.py`)

<pre class="overflow-visible!" data-start="4845" data-end="5258"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>import</span><span> math

</span><span>def</span><span></span><span>distance_km</span><span>(</span><span>lat1, lon1, lat2, lon2</span><span>):
    </span><span># Fórmula de Haversine</span><span>
    R = </span><span>6371</span><span></span><span># Raio da Terra</span><span>
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/</span><span>2</span><span>)**</span><span>2</span><span> + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/</span><span>2</span><span>)**</span><span>2</span><span>
    c = </span><span>2</span><span>*math.atan2(math.sqrt(a), math.sqrt(</span><span>1</span><span>-a))
    </span><span>return</span><span> R * c
</span></span></code></div></div></pre>

---

## 7️⃣ Observações

* Banco de dados inicial: **SQLite** (mais fácil para testes), mas pode ser adaptado para  **PostgreSQL** ,  **MySQL** , etc.
* Todos os endpoints retornam JSON.
* Código organizado em  **MVC leve** : routes → services → models → schemas.
* Mensagens de erro padronizadas via JSON.


## Testes implementados

Durante o desenvolvimento deste projeto, foram implementados testes avançados para demonstrar robustez, segurança e performance:

- **Testes funcionais**: validação das funções de criação (`create_document`) e busca (`search_documents`) de documentos.
- **Testes de segurança**: proteção contra SQL Injection.
- **Testes de performance**: validação de inserções em lote e busca rápida em grandes volumes de dados.
- **Testes de resiliência e tratamento de erros**: garantia de que inputs inválidos não quebram a aplicação.
- **Testes de ordenação geográfica**: validação da ordenação correta de documentos próximos a coordenadas fornecidas.
- **Testes case-insensitive**: busca funciona independentemente de maiúsculas/minúsculas.

✅ Estes testes demonstram domínio de boas práticas de programação, organização, arquitetura e atenção à qualidade do código.
