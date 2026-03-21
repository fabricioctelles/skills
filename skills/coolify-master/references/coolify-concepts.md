# Conceitos do Coolify

## Estrutura basica

- **Server**: maquina onde os containers rodam.
- **Project**: agrupador de recursos.
- **Environment**: recorte como `production`, `staging` ou `development`.
- **Resource**: aplicacao, servico ou banco.
- **Container**: unidade real de execucao; no Coolify tudo termina em container Docker.

## Proxy reverso

O Coolify usa proxy reverso para publicar aplicacoes e mapear dominios sem depender de portas expostas manualmente no host.

Consequencias praticas:
- A app precisa estar acessivel dentro do container pela porta correta.
- Health checks influenciam diretamente o roteamento.
- HTTPS pode ser emitido automaticamente quando o dominio e cadastrado com `https://`.

## Build packs suportados

- `Static`
- `Nixpacks`
- `Dockerfile`
- `Docker Compose`

Cada build pack muda o quanto voce controla build, runtime, health check e atualizacao.

## Responsabilidade compartilhada

O Coolify cuida do fluxo de deploy e do proxy, mas em ambiente self-hosted voce continua responsavel por:
- seguranca do servidor
- atualizacoes de sistema e Docker
- backup e restauracao
- monitoramento de disco e disponibilidade

## Preview deployments

Preview deployments sao uteis para revisar PRs, mas aumentam custo operacional, consumo de recursos e complexidade de dominio/env vars.

Use apenas quando houver necessidade real de revisao por ambiente efemero.

## Fontes oficiais recomendadas

- Introducao: https://coolify.io/docs/get-started/introduction
- Conceitos: https://coolify.io/docs/get-started/concepts
- CI/CD: https://coolify.io/docs/applications/ci-cd/introduction
