## Command Reference

### Endpoints Disponíveis

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| POST | `/auth` | Obter token JWT | client_id + client_secret |
| GET | `/lighthouse/tenancies/{tenancy_id}/contexts` | Listar contextos | Bearer Token |
| GET | `/lighthouse/tenancies/{tenancy_id}/workspaces` | Listar workspaces | Bearer Token |
| GET | `/lighthouse/tenancies/{tenancy_id}/workspaces/{id}` | Obter workspace específico | Bearer Token |
| GET | `/lighthouse/tenancies/{tenancy_id}/workspaces/{workspace_id}/views` | Listar visualizações | Bearer Token |
| GET | `/lighthouse/tenancies/{tenancy_id}/views/{id}` | Obter visualização | Bearer Token |
| GET | `/lighthouse/tenancies/{tenancy_id}/views/{id}/data` | Obter dados de visualização | Bearer Token |

### Parâmetros de Query Comuns

**Paginação**:
- `page`: Número da página (padrão: 1)
- `page_size`: Itens por página (máximo: 100, padrão: 10)

**Ordenação**:
- `sort_field`: Campo para ordenar (`name`, `created_at`)
- `sort_order`: Ordem de ordenação (`ASC`, `DESC`)

### Estrutura de Resposta Padrão

**Sucesso**:
```json
{
  "code": "success",
  "data": {
    // Dados do recurso
  },
  "meta": {
    // Metadados (paginação, etc)
  }
}
```

**Erro**:
```json
{
  "code": "error-code",
  "message": "Descrição do erro"
}
```

### Códigos de Status HTTP

| Código | Significado | Ação |
|--------|-------------|------|
| 200 | OK | Requisição bem-sucedida |
| 201 | Created | Recurso criado (autenticação) |
| 400 | Bad Request | Parâmetros inválidos |
| 401 | Unauthorized | Token inválido ou expirado |
| 403 | Forbidden | Sem permissão de acesso |
| 404 | Not Found | Recurso não encontrado |
| 429 | Too Many Requests | Rate limit excedido |
| 500 | Internal Server Error | Erro no servidor |

## Exemplos de uso

Este guia contém workflows detalhados para usar a API Pier Cloud com exemplos práticos.
## Workflow 1: Autenticação e Obtenção de Token

**Objetivo**: Obter um token JWT válido para usar em requisições à API

**Endpoint**: `POST /auth`

**Script disponível**: `scripts/pier-cloud-auth.py`

**Uso**:
```bash
python scripts/pier-cloud-auth.py
```

**O que o script faz**:
1. Carrega credenciais do arquivo `.env`
2. Faz requisição POST para `/auth`
3. Extrai e exibe o token JWT
4. Mostra tempo de expiração

**Resposta esperada**:
```json
{
  "code": "success",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expires_in": 3600,
    "token_type": "Bearer"
  }
}
```

---
## Workflow 2: Listar Contextos

**Objetivo**: Obter lista de contextos (ambientes de dados como AWS) disponíveis

**Endpoint**: `GET /lighthouse/tenancies/{tenancy_id}/contexts`

**Script disponível**: `scripts/pier-cloud-list-contexts.py`

**Uso**:
```bash
python scripts/pier-cloud-list-contexts.py
```

**O que o script faz**:
1. Autentica automaticamente
2. Lista todos os contextos disponíveis
3. Exibe: ID, nome, provider, moeda, se é padrão

**Resposta esperada**:
```json
{
  "code": "success",
  "data": {
    "contexts": [
      {
        "id": "ctx-uuid-001",
        "name": "Amazon Web Services",
        "provider": "aws",
        "currency": "USD",
        "is_default": true
      }
    ]
  }
}
```

---
## Workflow 3: Listar Workspaces

**Objetivo**: Obter lista de workspaces com paginação

**Endpoint**: `GET /lighthouse/tenancies/{tenancy_id}/workspaces`

**Parâmetros**:
- `page`: Número da página (padrão: 1)
- `page_size`: Itens por página (máximo: 100)
- `sort_field`: Campo para ordenação (`name` ou `created_at`)
- `sort_order`: Ordem (`ASC` ou `DESC`)

**Script disponível**: `scripts/pier-cloud-list-workspaces.py`

**Uso**:
```bash
# Listar primeira página (10 itens)
python scripts/pier-cloud-list-workspaces.py

# Listar página específica com mais itens
python scripts/pier-cloud-list-workspaces.py --page 2 --page-size 50

# Ordenar por data de criação
python scripts/pier-cloud-list-workspaces.py --sort-field created_at --sort-order DESC
```

**O que o script faz**:
1. Autentica automaticamente
2. Lista workspaces com paginação
3. Exibe: ID, nome, descrição, número de visualizações, acesso, data de criação
4. Mostra informações de paginação (total, página atual)

---
## Workflow 4: Obter Detalhes de Workspace

**Objetivo**: Obter informações detalhadas de um workspace específico, incluindo visualizações

**Endpoint**: `GET /lighthouse/tenancies/{tenancy_id}/workspaces/{workspace_id}`

**Script disponível**: `scripts/pier-cloud-get-workspace.py`

**Uso**:
```bash
python scripts/pier-cloud-get-workspace.py --workspace-id 5102
```

**O que o script faz**:
1. Autentica automaticamente
2. Busca detalhes do workspace especificado
3. Exibe informações completas do workspace
4. Lista todas as visualizações (views) incluídas

---
## Workflow 5: Obter Todos os Workspaces (Paginação Automática)

**Objetivo**: Obter todos os workspaces automaticamente, iterando por todas as páginas

**Script disponível**: `scripts/pier-cloud-get-all-workspaces.py`

**Uso**:
```bash
# Obter todos e exibir no terminal
python scripts/pier-cloud-get-all-workspaces.py

# Salvar em arquivo JSON
python scripts/pier-cloud-get-all-workspaces.py --output workspaces.json

# Salvar em CSV
python scripts/pier-cloud-get-all-workspaces.py --output workspaces.csv --format csv
```

**O que o script faz**:
1. Autentica automaticamente
2. Itera por todas as páginas automaticamente
3. Coleta todos os workspaces
4. Opcionalmente salva em arquivo (JSON ou CSV)
5. Exibe progresso e total de workspaces obtidos

---
## Workflow 6: Cliente Robusto com Retry e Renovação

**Objetivo**: Implementação completa com tratamento de erros, retry e renovação automática de token

**Script disponível**: `scripts/pier_cloud_client.py`

**Uso como CLI**:
```bash
# Listar contextos
python scripts/pier_cloud_client.py --action list-contexts

# Listar workspaces
python scripts/pier_cloud_client.py --action list-workspaces --page 1 --page-size 20

# Obter workspace específico
python scripts/pier_cloud_client.py --action get-workspace --workspace-id 5102

# Obter todos os workspaces
python scripts/pier_cloud_client.py --action get-all-workspaces --output results.json
```

**Uso como biblioteca**:
```python
from scripts.pier_cloud_client import PierCloudClient

# Criar cliente
client = PierCloudClient()

# Listar contextos
contexts = client.list_contexts()

# Listar workspaces
workspaces = client.list_workspaces(page=1, page_size=50)

# Obter workspace
workspace = client.get_workspace(workspace_id=5102)
```

**Recursos do cliente**:
- ✅ Autenticação automática
- ✅ Renovação automática de token antes de expirar
- ✅ Retry com backoff exponencial
- ✅ Tratamento robusto de erros
- ✅ Logging configurável
- ✅ Timeouts configuráveis
- ✅ Validação de configuração

---
## Exemplos com cURL

### Autenticar
```bash
TOKEN=$(curl -s -X POST https://api.piercloud.io/auth \
  -H "Content-Type: application/json" \
  -d "{\"client_id\": \"$PIERCLOUD_CLIENT_ID\", \"client_secret\": \"$PIERCLOUD_CLIENT_SECRET\"}" \
  | jq -r '.data.access_token')
```

### Listar Contextos
```bash
curl -X GET "https://api.piercloud.io/lighthouse/tenancies/$PIERCLOUD_TENANCY_ID/contexts" \
  -H "Authorization: Bearer $TOKEN" | jq '.'
```

### Listar Workspaces
```bash
curl -X GET "https://api.piercloud.io/lighthouse/tenancies/$PIERCLOUD_TENANCY_ID/workspaces?page=1&page_size=20" \
  -H "Authorization: Bearer $TOKEN" | jq '.'
```

### Obter Workspace
```bash
curl -X GET "https://api.piercloud.io/lighthouse/tenancies/$PIERCLOUD_TENANCY_ID/workspaces/16969" \
  -H "Authorization: Bearer $TOKEN" | jq '.'
```

---

### Workflow 7: Listar Grupos de Workspaces ❌

**Status**: ❌ Endpoint não disponível

**Endpoint esperado**: `GET /lighthouse/tenancies/{tenancy_id}/workspace-groups`

**Erro retornado**: `Cannot GET /workspace-groups`

**Script**: `scripts/pier-cloud-list-workspace-groups.py` (não funciona)

---

### Workflow 8: Obter Detalhes de Grupo de Workspace ❌

**Status**: ❌ Endpoint não disponível

**Endpoint esperado**: `GET /lighthouse/tenancies/{tenancy_id}/workspace-groups/{id}`

**Erro retornado**: `Cannot GET /tenancies/{tenancy_id}/workspace-groups/{id}`

**Script**: `scripts/pier-cloud-get-workspace-group.py` (não funciona)

---
## Workflow 9: Listar Visualizações de Workspace

**Objetivo**: Obter lista de visualizações (views) de um workspace

**Endpoint**: `GET /lighthouse/tenancies/{tenancy_id}/workspaces/{workspace_id}/views`

**Script disponível**: `scripts/pier-cloud-list-views.py`

**Uso**:
```bash
python scripts/pier-cloud-list-views.py --workspace-id 5102
```

**O que o script faz**:
1. Autentica automaticamente
2. Lista todas as visualizações do workspace
3. Exibe: ID, nome, descrição, data de criação

**Resposta esperada**:
```json
{
  "code": "success",
  "data": {
    "views": [
      {
        "id": 1,
        "name": "Nome da visualização",
        "description": null,
        "created_at": "2025-01-01T00:00:00.911Z"
      }
    ],
    "total": 1
  }
}
```

---
## Workflow 10: Obter Informações de Visualização

**Objetivo**: Obter detalhes de uma visualização específica

**Endpoint**: `GET /lighthouse/tenancies/{tenancy_id}/views/{id}`

**Script disponível**: `scripts/pier-cloud-get-view.py`

**Uso**:
```bash
python scripts/pier-cloud-get-view.py --view-id 123
```

**O que o script faz**:
1. Autentica automaticamente
2. Busca informações da visualização
3. Exibe: ID, nome, descrição, workspace associado

**Resposta esperada**:
```json
{
  "code": "success",
  "data": {
    "id": 123,
    "name": "Nome da visualização",
    "description": null,
    "workspace": {
      "id": 1234,
      "name": "Nome do workspace"
    }
  }
}
```

---
## Workflow 11: Obter Dados de Visualização

**Objetivo**: Obter dados reais de uma visualização com filtros e período

**Endpoint**: `GET /lighthouse/tenancies/{tenancy_id}/views/{id}/data`

**Parâmetros**:
- `start_date`: Data inicial (YYYY-MM-DD) - padrão: início do mês
- `end_date`: Data final (YYYY-MM-DD) - padrão: fim do mês
- `date_type`: Tipo de filtro (`date` ou `month`)
- `filters`: Filtros em formato JSON

**Script disponível**: `scripts/pier-cloud-get-view-data.py`

**Uso**:
```bash
# Básico (mês atual)
python scripts/pier-cloud-get-view-data.py --view-id 123

# Com período específico
python scripts/pier-cloud-get-view-data.py --view-id 123 \
  --start-date 2025-01-01 --end-date 2025-01-31

# Com filtros
python scripts/pier-cloud-get-view-data.py --view-id 123 \
  --start-date 2025-01-01 --end-date 2025-01-31 \
  --filters '[{"name":"lineitem/usageaccountid","data_type":"string","role":"filter","filters":[{"expression":"IS","value":["123456"],"negative_expression":false}]}]'

# Salvar em arquivo
python scripts/pier-cloud-get-view-data.py --view-id 123 \
  --start-date 2025-01-01 --end-date 2025-01-31 \
  --output dados.json
```

**Formato de Filtros**:
```json
[
  {
    "name": "lineitem/usageaccountid",
    "data_type": "string",
    "role": "filter",
    "filters": [
      {
        "expression": "IS",
        "value": ["12345678901"],
        "negative_expression": false
      }
    ]
  }
]
```

**Expressões disponíveis**:
- `IS`: Igual a
- `CONTAINS`: Contém

**O que o script faz**:
1. Autentica automaticamente
2. Busca dados da visualização com filtros aplicados
3. Exibe primeiros registros
4. Opcionalmente salva todos os dados em arquivo JSON

**Resposta esperada**:
```json
{
  "code": "success",
  "data": [
    {
      "key_1": "value_1",
      "key_2": "value_2",
      "key_3": "value_3"
    }
  ]
}
```

---
## Exemplos Avançados

### Obter Dados de Custos por Conta AWS

```bash
python scripts/pier-cloud-get-view-data.py --view-id 123 \
  --start-date 2025-01-01 --end-date 2025-01-31 \
  --filters '[{"name":"lineitem/usageaccountid","data_type":"string","role":"filter","filters":[{"expression":"IS","value":["123456789012"],"negative_expression":false}]}]' \
  --output custos_conta_janeiro.json
```

### Obter Dados Agrupados por Mês

```bash
python scripts/pier-cloud-get-view-data.py --view-id 123 \
  --start-date 2025-01-01 --end-date 2025-12-31 \
  --date-type month \
  --output custos_2025_mensal.json
```

### Filtrar Múltiplas Contas

```bash
python scripts/pier-cloud-get-view-data.py --view-id 123 \
  --filters '[{"name":"lineitem/usageaccountid","data_type":"string","role":"filter","filters":[{"expression":"IS","value":["111111111111","222222222222","333333333333"],"negative_expression":false}]}]' \
  --output custos_multiplas_contas.json
```

---

