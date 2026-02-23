---
name: "pier-cloud"
description: "Guia completo para consumir a API Pier Cloud (Lighthouse) com autenticação, gerenciamento de contextos, workspaces e visualizações. Inclui exemplos em Python, Node.js e cURL."
metadata:
  author: ft.ia.br
  version: "1.0"
  date: 2026-02-20
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
  keywords: ["pier", "piercloud", "lighthouse", "api", "finops", "cloud", "custos"]
---

# Pier Cloud API

## Overview

A API Pier Cloud (Lighthouse) é uma plataforma para gerenciamento de dados em nuvem que oferece recursos para análise de custos e governança financeira. Esta skill fornece documentação completa sobre como autenticar, listar contextos (ambientes como AWS), gerenciar workspaces e acessar visualizações de dados.

A API utiliza autenticação JWT (Bearer Token) e retorna dados em formato JSON. Todos os endpoints requerem credenciais de cliente (client_id e client_secret) que devem ser obtidas através da plataforma Pier Cloud.

Este guia inclui workflows detalhados, scripts prontos para uso e exemplos práticos em Python, Node.js e cURL.
## Onboarding

### Prerequisites

Para usar a API Pier Cloud, você precisa:

## Ferramentas de desenvolvimento

  - Python 3.7+ com `requests` e `python-dotenv`

## Arquivo .env presente

O arquivo .env deve estar no mesmo diretório que o skill.md. 

Não prosseguir sem o arquivo .env

### Installation

#### Configurar Variáveis de Ambiente

Procure pelo arquivo .env com as credenciais de cliente (PIERCLOUD_CLIENT_ID, PIERCLOUD_CLIENT_SECRET e PIERCLOUD_TENANCY_ID).

Caso não exista, informe ao usuário que ele precisa obter as credenciais através da plataforma Pier Cloud e criar esse arquivo .env. antes de usar o Skill.

O arquivo .env deve estar no mesmo diretório que o skill.md.  

Não prosseguir sem o arquivo .env

#### Instalar Dependências Python

```bash
pip install requests python-dotenv
```

### Basic Configuration

A API Pier Cloud usa autenticação JWT. O fluxo básico é:

1. **Autenticar** com `client_id` e `client_secret` para obter token JWT
2. **Usar o token** em todas as requisições subsequentes no header `Authorization: Bearer {token}`
3. **Renovar o token** quando expirar (geralmente após 1 hora)

**URL Base da API**: `https://api.piercloud.io`

### Verification

Teste a conexão com a API usando o script de autenticação:

```bash
python scripts/pier-cloud-auth.py
```

Se o token for exibido, a configuração está correta!



## Scripts Disponíveis

Scripts prontos para uso estão disponíveis em `scripts/`:

**Autenticação e Contextos**:
- **pier-cloud-auth.py** - Autenticar e obter token JWT ✅
- **pier-cloud-list-contexts.py** - Listar contextos ✅

**Workspaces**:
- **pier-cloud-list-workspaces.py** - Listar workspaces com paginação ✅
- **pier-cloud-get-workspace.py** - Obter detalhes de workspace específico ✅
- **pier-cloud-get-all-workspaces.py** - Obter todos os workspaces automaticamente ✅

**Visualizações**:
- **pier-cloud-list-views.py** - Listar visualizações de um workspace ✅
- **pier-cloud-get-view.py** - Obter informações de visualização específica ✅
- **pier-cloud-get-view-data.py** - Obter dados de visualização com filtros ✅

**Cliente Robusto**:
- **pier_cloud_client.py** - Cliente robusto com CLI e biblioteca reutilizável ✅

**⚠️ Nota Importante**: Scripts de grupos de workspaces (workspace-groups) não estão disponíveis pois os endpoints não existem na API atual da Pier Cloud.

Consulte `scripts/README.md` para instruções de uso detalhadas.

## Documentação de Referência

Reunimos informações mais técnicas e de solução de problemas em documentos separados para manter este guia principal conciso:

- **Solução de Problemas:** [Troubleshooting](references/TROUBLESHOOTING.md) 
- **Referência de Comandos e Endpoints:** [Reference](references/REFERENCE.md)


### Workflows Disponíveis

- **[Workflow 1: Autenticação e Obtenção de Token](references/REFERENCE.md#workflow-1-autenticação-e-obtenção-de-token)**: Obter um token JWT válido para usar em requisições à API
- **[Workflow 2: Listar Contextos](references/REFERENCE.md#workflow-2-listar-contextos)**: Obter lista de contextos (ambientes de dados como AWS) disponíveis
- **[Workflow 3: Listar Workspaces](references/REFERENCE.md#workflow-3-listar-workspaces)**: Obter lista de workspaces com paginação
- **[Workflow 4: Obter Detalhes de Workspace](references/REFERENCE.md#workflow-4-obter-detalhes-de-workspace)**: Obter informações detalhadas de um workspace específico, incluindo visualizações
- **[Workflow 5: Obter Todos os Workspaces (Paginação Automática)](references/REFERENCE.md#workflow-5-obter-todos-os-workspaces-(paginação-automática))**: Obter todos os workspaces automaticamente, iterando por todas as páginas
- **[Workflow 6: Cliente Robusto com Retry e Renovação](references/REFERENCE.md#workflow-6-cliente-robusto-com-retry-e-renovação)**: Implementação completa com tratamento de erros, retry e renovação automática de token
- **[Workflow 7: Listar Grupos de Workspaces ❌](references/REFERENCE.md#workflow-7-listar-grupos-de-workspaces-❌)**: ❌ Endpoint não disponível
- **[Workflow 8: Obter Detalhes de Grupo de Workspace ❌](references/REFERENCE.md#workflow-8-obter-detalhes-de-grupo-de-workspace-❌)**: ❌ Endpoint não disponível
- **[Workflow 9: Listar Visualizações de Workspace](references/REFERENCE.md#workflow-9-listar-visualizações-de-workspace)**: Obter lista de visualizações (views) de um workspace
- **[Workflow 10: Obter Informações de Visualização](references/REFERENCE.md#workflow-10-obter-informações-de-visualização)**: Obter detalhes de uma visualização específica
- **[Workflow 11: Obter Dados de Visualização](references/REFERENCE.md#workflow-11-obter-dados-de-visualização)**: Obter dados reais de uma visualização com filtros e período

## Additional Resources

### Documentação Oficial

- **API Docs**: https://docs.piercloud.com/api-docs-pier-cloud
- **URL Base**: https://api.piercloud.io
- **Plataforma Pier Cloud**: Acesse para obter credenciais e gerenciar recursos  https://piercloud.com/en/


### Suporte

Para questões sobre a API Pier Cloud:
- Contate o time da Pier Cloud
- Consulte a documentação oficial
- Verifique os logs de erro para debugging

---