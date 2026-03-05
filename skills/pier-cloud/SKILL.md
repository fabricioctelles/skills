---
name: "pier-cloud"
description: "Este skill deve ser usado quando o usuário precisar consumir a API Pier Cloud (Lighthouse) para gerenciamento de custos em nuvem — incluindo autenticação JWT, listagem de contextos, workspaces e visualizações de dados FinOps. Acionar sempre que houver necessidade de integrar, automatizar ou depurar chamadas à plataforma Pier Cloud via Python, Node.js ou cURL."
metadata:
  author: ft.ia.br
  version: "1.1"
  date: 2026-03-05
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
  keywords: ["pier", "piercloud", "lighthouse", "api", "finops", "cloud", "custos"]
---

# Pier Cloud API

## Pré-requisitos

### Credenciais

Localizar o arquivo `.env` no diretório do skill com as seguintes variáveis:

```env
PIERCLOUD_CLIENT_ID=seu_client_id
PIERCLOUD_CLIENT_SECRET=seu_client_secret
PIERCLOUD_TENANCY_ID=seu_tenancy_id
```

Caso o arquivo `.env` não exista, informar ao usuário que é necessário obter as credenciais na plataforma Pier Cloud antes de continuar. Não prosseguir sem o arquivo `.env`.

> Nota: `PIERCLOUD_TENANCY_ID` equivale ao antigo `PIERCLOUD_BUSINESS_ID`. Os scripts aceitam ambos como fallback.

### Dependências Python

```bash
pip install requests python-dotenv
```

## Configuração Básica

A API utiliza autenticação JWT. Fluxo obrigatório:

1. Autenticar via `POST /auth` com `client_id` e `client_secret` para obter token JWT
2. Incluir o token em todas as requisições: `Authorization: Bearer {token}`
3. Renovar o token ao expirar (validade padrão: 1 hora)

**URL Base**: `https://api.piercloud.io`

Verificar a conexão executando:

```bash
python scripts/pier-cloud-auth.py
```

## Scripts Disponíveis

Scripts prontos para uso em `scripts/`. Consultar `scripts/README.md` para instruções detalhadas.

| Script | Descrição |
|--------|-----------|
| `pier-cloud-auth.py` | Autenticar e obter token JWT |
| `pier-cloud-list-contexts.py` | Listar contextos disponíveis |
| `pier-cloud-list-workspaces.py` | Listar workspaces com paginação |
| `pier-cloud-get-workspace.py` | Obter detalhes de workspace específico |
| `pier-cloud-get-all-workspaces.py` | Obter todos os workspaces (paginação automática) |
| `pier-cloud-list-views.py` | Listar visualizações de um workspace |
| `pier-cloud-get-view.py` | Obter informações de visualização específica |
| `pier-cloud-get-view-data.py` | Obter dados de visualização com filtros |
| `pier_cloud_client.py` | Cliente robusto com CLI e biblioteca reutilizável |

> Nota: Scripts de workspace-groups (`pier-cloud-list-workspace-groups.py`, `pier-cloud-get-workspace-group.py`) não funcionam — os endpoints correspondentes não existem na API atual.

## Workflows

Seguir os workflows detalhados com exemplos de requisição e resposta em `references/REFERENCE.md`:

- **Workflow 1** — Autenticação e Obtenção de Token
- **Workflow 2** — Listar Contextos
- **Workflow 3** — Listar Workspaces
- **Workflow 4** — Obter Detalhes de Workspace
- **Workflow 5** — Obter Todos os Workspaces (Paginação Automática)
- **Workflow 6** — Cliente Robusto com Retry e Renovação de Token
- **Workflow 9** — Listar Visualizações de Workspace
- **Workflow 10** — Obter Informações de Visualização
- **Workflow 11** — Obter Dados de Visualização com Filtros

Para referência de endpoints, parâmetros, estruturas de resposta e exemplos com cURL, consultar `references/REFERENCE.md`.

Para diagnóstico de erros (401, 403, 404, timeout, rate limiting), consultar `references/TROUBLESHOOTING.md`.

## Recursos Adicionais

- **API Docs**: https://docs.piercloud.com/api-docs-pier-cloud
- **Plataforma Pier Cloud**: https://piercloud.com/en/

## Checklist de Qualidade

- [ ] Arquivo `.env` presente com `PIERCLOUD_CLIENT_ID`, `PIERCLOUD_CLIENT_SECRET` e `PIERCLOUD_TENANCY_ID`
- [ ] Dependências Python instaladas (`requests`, `python-dotenv`)
- [ ] Autenticação bem-sucedida (token JWT obtido sem erros)
- [ ] Endpoint correto sendo utilizado (padrão `/lighthouse/tenancies/{tenancy_id}/...`)
- [ ] Token sendo renovado antes de expirar em sessões longas
- [ ] IDs de workspace/view confirmados via listagem antes de usar diretamente
- [ ] Erros tratados conforme `references/TROUBLESHOOTING.md`
