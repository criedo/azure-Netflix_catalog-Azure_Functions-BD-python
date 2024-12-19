# Gerenciador de Catálogos da Netflix com Azure Functions

Este repositório contém um projeto de exemplo para criar um Gerenciador de Catálogos da Netflix usando **Azure Functions** e **Azure Cosmos DB**. Este projeto permite criar, buscar, atualizar e deletar itens de um catálogo, oferecendo uma API REST para gerenciamento.

---

## Estrutura do Projeto

```plaintext
netflix_catalog_manager/
├── function_app/
│   ├── CreateCatalog/         # Função para criar novos catálogos
│   │   ├── __init__.py
│   │   └── function.json
│   ├── GetCatalog/            # Função para buscar catálogos
│   │   ├── __init__.py
│   │   └── function.json
│   ├── UpdateCatalog/         # Função para atualizar catálogos
│   │   ├── __init__.py
│   │   └── function.json
│   └── DeleteCatalog/         # Função para deletar catálogos
│       ├── __init__.py
│       └── function.json
├── requirements.txt           # Dependências do projeto
└── README.md                  # Instruções detalhadas
```

---

## Requisitos

- Conta no [Microsoft Azure](https://azure.microsoft.com/)
- Python 3.9 ou superior
- Azure Functions Core Tools
- Azure CLI

---

## Passo a Passo para Configuração

### 1. Configuração do Ambiente no Azure

#### 1.1. Criar os Recursos Necessários

1. **Crie um Resource Group:**

   ```bash
   az group create --name netflixCatalogGroup --location eastus
   ```

2. **Crie um banco de dados Cosmos DB com API para NoSQL:**

   ```bash
   az cosmosdb create --name netflixCatalogDB --resource-group netflixCatalogGroup --kind MongoDB
   ```

3. **Crie um Database e um Container:**

   ```bash
   az cosmosdb mongodb database create --account-name netflixCatalogDB --resource-group netflixCatalogGroup --name CatalogDatabase
   az cosmosdb mongodb collection create --account-name netflixCatalogDB --resource-group netflixCatalogGroup --database-name CatalogDatabase --name CatalogCollection --partition-key-path "/id"
   ```

4. **Crie uma Azure Function App:**
   ```bash
   az functionapp create \
       --resource-group netflixCatalogGroup \
       --consumption-plan-location eastus \
       --runtime python \
       --functions-version 4 \
       --name netflixCatalogFunctionApp \
       --storage-account <STORAGE_ACCOUNT_NAME>
   ```

---

### 2. Configuração do Projeto

#### 2.1. Clonar o Repositório e Navegar para o Diretório

```bash
git clone https://github.com/devcaiada/netflix-catalog-manager.git
cd netflix-catalog-manager
```

#### 2.2. Instalar as Dependências

```bash
pip install -r requirements.txt
```

#### 2.3. Configurar Variáveis de Ambiente no Azure

1. **Adicione as variáveis de ambiente no Azure Function App:**
   ```bash
   az functionapp config appsettings set --name netflixCatalogFunctionApp \
       --resource-group netflixCatalogGroup \
       --settings COSMOS_ENDPOINT=<COSMOS_DB_ENDPOINT> COSMOS_KEY=<COSMOS_DB_KEY>
   ```

---

### 3. Desenvolvimento das Funções

As funções estão organizadas em pastas, cada uma com um arquivo `__init__.py` contendo o código da função e um arquivo `function.json` para configurações.

- **`CreateCatalog`:** Permite criar itens no catálogo.
- **`GetCatalog`:** Permite buscar todos os itens.
- **`UpdateCatalog`:** Permite atualizar itens existentes.
- **`DeleteCatalog`:** Permite deletar itens por ID.

---

### 4. Deploy para o Azure

1. **Faça o deploy do projeto para o Azure Functions:**

   ```bash
   func azure functionapp publish netflixCatalogFunctionApp
   ```

2. **Teste os Endpoints:**
   Use ferramentas como Postman ou cURL para testar as rotas:

   - **Criar:** `POST /api/CreateCatalog`
   - **Buscar:** `GET /api/GetCatalog`
   - **Atualizar:** `PUT /api/UpdateCatalog`
   - **Deletar:** `DELETE /api/DeleteCatalog`

---

## Exemplos de Uso

### Criar um Novo Item

**Requisição:**

```http
POST /api/CreateCatalog HTTP/1.1
Content-Type: application/json

{
    "id": "1",
    "title": "Stranger Things",
    "genre": "Sci-Fi",
    "release_year": 2016
}
```

**Resposta:**

```json
{
  "message": "Catalog item created successfully!"
}
```

### Buscar Itens

**Requisição:**

```http
GET /api/GetCatalog HTTP/1.1
```

**Resposta:**

```json
[
  {
    "id": "1",
    "title": "Stranger Things",
    "genre": "Sci-Fi",
    "release_year": 2016
  }
]
```

### Atualizar um Item

**Requisição:**

```http
PUT /api/UpdateCatalog HTTP/1.1
Content-Type: application/json

{
    "id": "1",
    "title": "Stranger Things",
    "genre": "Drama",
    "release_year": 2016
}
```

**Resposta:**

```json
{
  "message": "Catalog item updated successfully!"
}
```

### Deletar um Item

**Requisição:**

```http
DELETE /api/DeleteCatalog?id=1&partition_key=1 HTTP/1.1
```

**Resposta:**

```json
{
  "message": "Catalog item deleted successfully!"
}
```

---

## Tecnologias Utilizadas

- **Azure Functions**: Para criar as APIs REST serverless.
- **Azure Cosmos DB**: Banco de dados NoSQL para armazenamento do catálogo.
- **Python**: Linguagem de programação usada no desenvolvimento das funções.
- **Azure CLI**: Ferramenta de linha de comando para gerenciar recursos do Azure.

---

## Contribuições <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" alt="Rocket" width="25" height="25" />

Contribuições são bem-vindas! Siga as instruções abaixo:

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature: `git checkout -b minha-feature`.
3. Faça o commit das alterações: `git commit -m 'Minha nova feature'`.
4. Envie para o repositório remoto: `git push origin minha-feature`.
5. Abra um Pull Request.

---

Desenvolvido por [Caio Arruda](https://github.com/devcaiada).
