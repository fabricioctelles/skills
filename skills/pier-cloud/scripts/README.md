# Scripts da API Pier Cloud

Scripts prontos para consumir a API Pier Cloud (Lighthouse).

## Prerequisitos

```bash
pip install requests python-dotenv
```

## Configuracao

Crie arquivo `.env` na raiz do projeto:

```env
PIERCLOUD_CLIENT_ID=seu_client_id
PIERCLOUD_CLIENT_SECRET=seu_client_secret
PIERCLOUD_TENANCY_ID=seu_tenancy_id
```

> **Nota**: O `TENANCY_ID` corresponde ao antigo `BUSINESS_ID`. Se voce ja tem `PIERCLOUD_BUSINESS_ID` no `.env`, os scripts usam como fallback automaticamente.

## API - Mudanca de Endpoints (Fev 2026)

A API Pier Cloud atualizou seus endpoints:

- **Antes**: `/lighthouse/orgs/{org_id}/businesses/{business_id}/...`
- **Agora**: `/lighthouse/tenancies/{tenancy_id}/...`

O `PIERCLOUD_ORG_ID` nao e mais necessario. O `tenancy_id` equivale ao antigo `BUSINESS_ID`.

Documentacao oficial: https://docs.piercloud.com/api-docs-pier-cloud

## Scripts Disponiveis

### 1. pier-cloud-auth.py
Autentica e obtem token JWT.

```bash
python scripts/pier-cloud-auth.py
```

### 2. pier-cloud-list-contexts.py
Lista todos os contextos disponiveis.

```bash
python scripts/pier-cloud-list-contexts.py
```

### 3. pier-cloud-list-workspaces.py
Lista workspaces com paginacao.

```bash
# Padrao (pagina 1, 10 itens)
python scripts/pier-cloud-list-workspaces.py

# Pagina especifica
python scripts/pier-cloud-list-workspaces.py --page 2 --page-size 50

# Ordenar por data
python scripts/pier-cloud-list-workspaces.py --sort-field created_at --sort-order DESC
```

### 4. pier-cloud-get-workspace.py
Obtem detalhes de workspace especifico.

```bash
python scripts/pier-cloud-get-workspace.py --workspace-id 16969
```

### 5. pier-cloud-get-all-workspaces.py
Obtem todos os workspaces com paginacao automatica.

```bash
# Exibir no terminal
python scripts/pier-cloud-get-all-workspaces.py

# Salvar em JSON
python scripts/pier-cloud-get-all-workspaces.py --output workspaces.json

# Salvar em CSV
python scripts/pier-cloud-get-all-workspaces.py --output workspaces.csv --format csv
```

### 6. pier-cloud-list-views.py
Lista visualizacoes de um workspace.

```bash
python scripts/pier-cloud-list-views.py --workspace-id 16969
```

### 7. pier-cloud-get-view.py
Obtem informacoes de visualizacao especifica.

```bash
python scripts/pier-cloud-get-view.py --view-id 193195
```

### 8. pier-cloud-get-view-data.py
Obtem dados de uma visualizacao com filtros.

```bash
# Basico
python scripts/pier-cloud-get-view-data.py --view-id 193195

# Com periodo
python scripts/pier-cloud-get-view-data.py --view-id 193195 \
  --start-date 2026-01-01 --end-date 2026-01-31

# Com filtros
python scripts/pier-cloud-get-view-data.py --view-id 193195 \
  --filters '[{"name":"lineitem/usageaccountid","data_type":"string","role":"filter","filters":[{"expression":"IS","value":["123456"],"negative_expression":false}]}]'

# Salvar em arquivo
python scripts/pier-cloud-get-view-data.py --view-id 193195 \
  --start-date 2026-01-01 --end-date 2026-01-31 --output dados.json
```

### 9. pier_cloud_client.py
Cliente robusto com CLI e biblioteca reutilizavel.

**Como CLI**:
```bash
# Listar contextos
python scripts/pier_cloud_client.py --action list-contexts

# Listar workspaces
python scripts/pier_cloud_client.py --action list-workspaces --page 1 --page-size 20

# Obter workspace
python scripts/pier_cloud_client.py --action get-workspace --workspace-id 16969

# Obter todos
python scripts/pier_cloud_client.py --action get-all-workspaces --output results.json
```

### 10. appscript-pier-cloud.gs
Codigo Google Apps Script para integrar com Google Sheets.

Veja instrucoes no proprio arquivo.

## Endpoints da API (Atualizado Fev 2026)

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| POST | `/auth` | Obter token JWT |
| GET | `/lighthouse/tenancies/{tenancy_id}/contexts` | Listar contextos |
| GET | `/lighthouse/tenancies/{tenancy_id}/workspaces` | Listar workspaces |
| GET | `/lighthouse/tenancies/{tenancy_id}/workspaces/{id}` | Obter workspace |
| GET | `/lighthouse/tenancies/{tenancy_id}/workspaces/{workspace_id}/views` | Listar views |
| GET | `/lighthouse/tenancies/{tenancy_id}/views/{id}` | Obter view |
| GET | `/lighthouse/tenancies/{tenancy_id}/views/{id}/data` | Obter dados da view |

## Troubleshooting

### Erro: Variaveis faltando
Verifique se o arquivo `.env` existe e contem `PIERCLOUD_TENANCY_ID` (ou `PIERCLOUD_BUSINESS_ID` como fallback).

### Erro 401
Credenciais invalidas. Verifique CLIENT_ID e CLIENT_SECRET.

### Erro 403
Sem permissao. Verifique TENANCY_ID.

### Erro 404
Recurso nao encontrado. Verifique IDs fornecidos.
