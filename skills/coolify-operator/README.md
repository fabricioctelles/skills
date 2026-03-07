# Coolify Operator Skill

Skill especializado em operar instâncias Coolify através da API REST e CLI oficial.

## O que é Coolify?

Coolify é uma plataforma self-hosted open-source alternativa ao Heroku, Vercel e Netlify. Permite fazer deploy de aplicações, databases e serviços na sua própria infraestrutura.

## O que este skill faz?

Este skill ensina o Claude a:

- ✅ Conectar em instâncias Coolify (API e CLI)
- ✅ Configurar e gerenciar múltiplos contextos (ambientes)
- ✅ Listar e gerenciar aplicações, servidores, databases e serviços
- ✅ Fazer deploy, restart e stop de recursos
- ✅ Ver logs e status de deployments
- ✅ Gerenciar variáveis de ambiente
- ✅ Troubleshooting de problemas comuns (403, 401, tokens com pipe, etc)

## Documentação incluída

- Autenticação segura (API e CLI)
- Operações CRUD completas para applications, servers, databases e services
- Workflows comuns (deploy, redeploy, monitoramento multi-ambiente)
- Troubleshooting detalhado
- Exemplos de código em Bash/cURL

## Casos de teste incluídos

8 cenários realistas:

1. Configurar contexto inicial com CLI
2. Listar e reiniciar aplicação
3. Troubleshooting de erro 403
4. Deploy multi-ambiente (dev/staging/prod)
5. Atualizar variáveis de ambiente
6. Monitorar logs de deploy
7. Resolver problema de token com pipe (|)
8. Listar e reiniciar databases

## Como foi criado

Documentação obtida via Context7 MCP:
- `/websites/coolify_io_api-reference` - API REST completa
- `/coollabsio/coolify-cli` - CLI oficial
- `/llmstxt/coolify_io_llms-full_txt` - Documentação geral

## Referências

- **Site oficial**: https://coolify.io
- **Documentação**: https://coolify.io/docs
- **API Reference**: https://coolify.io/docs/api-reference
- **CLI GitHub**: https://github.com/coollabsio/coolify-cli
- **Coolify Core**: https://github.com/coollabsio/coolify

## Estrutura do skill

```
coolify-operator/
├── SKILL.md           # Skill principal com todas as instruções
├── evals/
│   └── evals.json     # 8 casos de teste
└── README.md          # Este arquivo
```

## Uso

O skill é ativado automaticamente quando o usuário menciona:
- "coolify"
- "deploy no coolify" 
- "reiniciar aplicação coolify"
- "listar serviços coolify"
- "conectar no coolify"
- E outros termos relacionados

O Claude automaticamente consulta o skill e fornece instruções precisas baseadas na documentação oficial.
