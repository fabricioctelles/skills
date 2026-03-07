---
name: coolify-operator
description: Operador mestre do Coolify - plataforma self-hosted de deployment. Use quando o usuário mencionar 'coolify', 'deploy', 'fazer deploy no coolify', 'listar serviços coolify', 'reiniciar aplicação', 'redeploy', 'restart aplicação coolify', 'ver logs coolify', 'conectar no coolify', 'API coolify', 'CLI coolify', 'servidores coolify', 'databases coolify', 'apps coolify', 'coolify context', ou quando precisar gerenciar deployments, servidores, aplicações ou databases em instâncias Coolify.
metadata:
  author: ft.ia.br
  version: "1.0"
  date: 2026-03-07
---

# Coolify Operator

Skill para operar instâncias Coolify através da **API REST** ou **CLI oficial**. Coolify é uma plataforma self-hosted open-source alternativa ao Heroku/Vercel/Netlify para deploy de aplicações, databases e serviços.

## Quando usar este skill

- Conectar em instâncias Coolify (via API ou CLI)
- Listar e gerenciar aplicações, serviços, databases e servidores
- Fazer deploy, restart ou stop de aplicações
- Ver logs e status de deployments
- Gerenciar variáveis de ambiente
- Operar múltiplas instâncias Coolify (contexts)
- Troubleshooting de conexão com Coolify

## Conceitos fundamentais

### Autenticação

**API REST:**
- Endpoint base: `https://SEU-HOST/api/v1` (sempre com `/api/v1` no final)
- Autenticação: `Authorization: Bearer SEU_TOKEN`
- Token obtido em: Coolify Dashboard → Keys & Tokens → API Tokens

**CLI:**
- Instala contextos que armazenam HOST + TOKEN
- HOST no contexto é SEM `/api/v1` (só a URL base)
- CLI adiciona `/api/v1` automaticamente

### Configuração com pipe no token

⚠️ **IMPORTANTE**: Tokens do Coolify frequentemente contêm `|` (ex: `3|abc123...`). Nunca use `source .env` pois isso quebra no shell.

**Leitura segura do .env:**
```bash
COOLIFY_KEY=$(sed -n 's/^COOLIFY_KEY=//p' .env)
COOLIFY=$(sed -n 's/^COOLIFY=//p' .env)
```

**Formato esperado no .env:**
```bash
COOLIFY_KEY=3|abc123def456...
COOLIFY=http://192.168.1.XXX:8000/api/v1
```

### UUIDs

Coolify usa UUIDs para identificar recursos:
- Applications: `app-uuid`
- Servers: `server-uuid`
- Databases: `db-uuid`
- Services: `service-uuid`

## Operações com CLI

### Setup inicial

```bash
# Ler token do .env de forma segura
COOLIFY_KEY=$(sed -n 's/^COOLIFY_KEY=//p' .env)

# Adicionar contexto (URL SEM /api/v1)
coolify context add -d -f meu-coolify http://192.168.1.XXX:8000 "$COOLIFY_KEY"

# Usar o contexto
coolify context use meu-coolify

# Verificar conexão
coolify context verify

# Ver versão da API
coolify context version
```

### Gerenciamento de contextos

```bash
# Listar contextos
coolify context list

# Adicionar múltiplos contextos
coolify context add prod https://prod.coolify.io "$PROD_TOKEN" --default
coolify context add staging https://staging.coolify.io "$STAGING_TOKEN"
coolify context add dev https://dev.coolify.io "$DEV_TOKEN"

# Trocar contexto padrão
coolify context use staging

# Usar contexto específico em um comando
coolify --context=prod app list

# Atualizar token de um contexto
coolify context set-token prod new-token-here

# Remover contexto
coolify context delete dev
```

### Operações com applications

```bash
# Listar todas as aplicações
coolify app list

# Ver detalhes de uma aplicação
coolify app get <uuid>

# --- LIFECYCLE ---
# Iniciar (deploy) aplicação
coolify app start <uuid>

# Parar aplicação
coolify app stop <uuid>

# Reiniciar aplicação
coolify app restart <uuid>

# --- LOGS ---
# Ver logs da aplicação
coolify app logs <uuid>

# --- VARIÁVEIS DE AMBIENTE ---
# Listar variáveis de ambiente
coolify app env list <uuid>

# Criar variável de ambiente
coolify app env create <uuid> --key API_KEY --value secret123

# Sincronizar variáveis de arquivo .env
coolify app env sync <uuid> --file .env
coolify app env sync <uuid> --file .env.production --build-time --preview
```

### Operações com servers

```bash
# Listar servidores
coolify server list

# Ver detalhes de um servidor (incluindo recursos)
coolify server get <uuid> --resources

# Adicionar novo servidor (com validação)
coolify server add myserver 192.168.1.100 <key-uuid> --validate
```

### Operações com team

```bash
# Listar teams disponíveis
coolify team list

# Ver team atual
coolify team current

# Listar membros do team
coolify team members list
```

### Flags globais

```bash
# Especificar contexto
coolify --context <name> ...

# Override do host
coolify --host <fqdn> ...

# Token direto (bypassa contexto)
coolify --token <token> ...

# Formato de saída (table, json, pretty)
coolify --format json ...

# Mostrar dados sensíveis
coolify -s ...
coolify --show-sensitive ...

# Forçar operação
coolify -f ...
coolify --force ...

# Debug mode
coolify --debug ...
```

## Operações com API REST

### Autenticação e teste

```bash
# Ler credenciais do .env de forma segura
COOLIFY_KEY=$(sed -n 's/^COOLIFY_KEY=//p' .env)
COOLIFY=$(sed -n 's/^COOLIFY=//p' .env)

# Testar conexão
curl -sS -i \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/version"

# Resultado esperado: HTTP 200 + {"version": "4.0.0-beta.xxx"}
```

### Applications

```bash
# Listar aplicações
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications"

# Ver detalhes de aplicação
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications/{uuid}"

# Iniciar (deploy) aplicação
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications/{uuid}/start"

# Flags query params:
# ?force=true          - Force rebuild
# ?instant_deploy=true - Skip queue

# Parar aplicação
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications/{uuid}/stop"

# Reiniciar aplicação
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications/{uuid}/restart"

# Response exemplo:
# {
#   "message": "Restart request queued.",
#   "deployment_uuid": "doogksw"
# }
```

### Deployments

```bash
# Listar todos os deployments em andamento
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/deployments"

# Listar deployments de uma aplicação (com paginação)
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/deployments/applications/{uuid}?skip=0&take=10"
```

### Servers

```bash
# Listar servidores
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/servers"

# Ver detalhes de servidor
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/servers/{uuid}"
```

### Databases

```bash
# Listar databases
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/databases"

# Iniciar database
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/databases/{uuid}/start"

# Parar database
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/databases/{uuid}/stop"

# Reiniciar database
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/databases/{uuid}/restart"
```

### Services

```bash
# Reiniciar serviço
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/services/{uuid}/restart"

# Query params:
# ?latest=true - Pull latest images

# Response:
# {"message": "Service restaring request queued."}
```

## Troubleshooting

### Erro: 403 "You are not allowed to access the API"

**Causa:** Token inválido ou sem permissão para a instância.

**Solução:**
1. Pedir para o usuário validar na instância em <URL_DA_INSTANCIA>/settings/advanced se a API está ativada e com o IP do cliente liberado
2. Regenerar token em: Dashboard → Keys & Tokens → API Tokens
3. Atualizar `.env` ou contexto CLI
4. Verificar que está usando a instância correta

### Erro: 401 "Unauthenticated"

**Causa:** Header de autenticação incorreto ou token não enviado.

**Solução:**
```bash
# Verificar que está usando Bearer (não só "Token")
Authorization: Bearer SEU_TOKEN

# CLI: verificar contexto
coolify context verify
```

### Erro: 404 no context verify

**Causa:** URL do contexto CLI está incorreta (provavelmente com `/api/v1` no lugar errado).

**Solução:**
```bash
# CLI context deve ter URL SEM /api/v1
coolify context add meu-coolify http://192.168.1.XXX:8000 "$TOKEN"

# API direta deve ter URL COM /api/v1
COOLIFY=http://192.168.1.XXX:8000/api/v1
```

### Túnel Cloudflare não é a causa

Se a API já retorna JSON válido do Coolify (mesmo que seja erro de auth), o túnel Cloudflare está funcionando. O problema é autenticação, não conexão.

### Token com pipe (|) quebra shell

```bash
# ❌ ERRADO - quebra com pipe
source .env

# ✅ CORRETO - leitura segura
COOLIFY_KEY=$(sed -n 's/^COOLIFY_KEY=//p' .env)
```

## Workflows comuns

### Deploy completo de nova aplicação

```bash
# 1. Conectar no Coolify
coolify context add prod https://coolify.seu-dominio.com "$TOKEN" --default
coolify context verify

# 2. Listar servidores disponíveis
coolify server list

# 3. Fazer deploy (via dashboard UI ou API)
# Nota: criação de apps é melhor via UI, API é para operações

# 4. Listar as apps para pegar UUID
coolify app list

# 5. Iniciar a aplicação
coolify app start <uuid>

# 6. Ver logs do deploy
coolify app logs <uuid>
```

### Redeploy com force rebuild

```bash
# Via CLI
coolify app restart <uuid>

# Via API com rebuild forçado
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications/{uuid}/start?force=true"
```

### Atualizar variáveis de ambiente

```bash
# Opção 1: Sincronizar de arquivo
coolify app env sync <uuid> --file .env.production

# Opção 2: Criar individual
coolify app env create <uuid> --key API_URL --value https://api.exemplo.com
coolify app env create <uuid> --key API_KEY --value secret123

# 3. Restart para aplicar mudanças
coolify app restart <uuid>
```

### Monitoramento multi-ambiente

```bash
# Produção
coolify --context=prod app list
coolify --context=prod app logs <prod-app-uuid>

# Staging
coolify --context=staging app list
coolify --context=staging app logs <staging-app-uuid>

# Development
coolify --context=dev app list
coolify --context=dev server list
```

## Recursos importantes

### Estrutura de resposta da API

**Application:**
```json
{
  "id": 123,
  "uuid": "app-uuid-123",
  "name": "minha-app",
  "fqdn": "app.exemplo.com",
  "status": "running",
  "git_repository": "https://github.com/user/repo",
  "git_branch": "main",
  "git_commit_sha": "abc123",
  "build_pack": "nixpacks",
  "ports_exposes": "3000",
  "health_check_enabled": true,
  "environment_id": 1,
  "destination_id": 1
}
```

**Server:**
```json
{
  "id": 1,
  "uuid": "server-uuid-123",
  "name": "servidor-principal",
  "ip": "192.168.1.100",
  "user": "root",
  "port": 22,
  "settings": {
    "is_reachable": true,
    "is_usable": true,
    "concurrent_builds": 1
  }
}
```

**Deployment:**
```json
{
  "id": 456,
  "uuid": "deployment-uuid-456",
  "status": "finished",
  "deployment_uuid": "dep-123",
  "application_id": 123
}
```

## Dicas de uso

1. **Sempre verificar UUIDs**: Use `coolify app list` ou API para confirmar UUIDs antes de operações
2. **Contextos para multi-ambiente**: Configure um contexto para cada ambiente (dev/staging/prod)
3. **Logs em tempo real**: Use `coolify app logs <uuid>` durante deploys
4. **Force rebuild quando necessário**: `?force=true` no start garante rebuild completo
5. **Segurança do token**: Nunca commitar tokens. Use `.env` com `.gitignore`
6. **Formato JSON para scripts**: Use `--format json` no CLI para parsear com `jq`

## Referências

- **Documentação oficial**: https://coolify.io/docs
- **API Reference**: https://coolify.io/docs/api-reference
- **CLI GitHub**: https://github.com/coollabsio/coolify-cli
- **Coolify Core**: https://github.com/coollabsio/coolify
