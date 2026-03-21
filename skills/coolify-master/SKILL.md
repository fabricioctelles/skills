---
name: coolify-master
description: Use when working with Coolify for deployment, operations, or troubleshooting of applications and services, including build pack selection, Git-based deploys, environment variables, domains, SSL, DNS, health checks, rolling updates, persistent storage, preview deployments, and errors like No available server, 404 after deploy, wrong port, or localhost binding.
metadata:
  author: ft.ia.br
  version: "1.1"
  date: 2026-03-21
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
---

# Coolify Master

## Overview

Use este skill quando a tarefa envolver Coolify como plataforma de deploy, operação ou diagnóstico.

Este skill cobre três frentes:
- Planejamento e execução de deploys.
- Operação de ambientes self-hosted.
- Troubleshooting de falhas recorrentes em aplicações e serviços.

Quando usar este skill:
- O usuário mencionar Coolify explicitamente.
- A tarefa envolver escolha entre `Dockerfile`, `Static`, `Nixpacks` ou `Docker Compose` dentro do Coolify.
- Houver configuração de domínios, HTTPS, health checks, env vars ou rolling updates.
- Houver falhas como `No available server`, `404` após deploy, SSL quebrado, DNS errado, porta incorreta ou app ouvindo apenas em localhost.
- O trabalho exigir definir boas práticas de deploy para Astro, Next.js, APIs, workers ou stacks web no Coolify.

Não use este skill para:
- Deploy em plataformas que não sejam Coolify.
- Debug de aplicação que não tenha relação com deploy, proxy, runtime ou operação.

## Onboarding

### 1. Carregue a referência certa primeiro

- Para entendimento de estrutura do Coolify: leia `references/coolify-concepts.md`.
- Para desenhar ou revisar deploy: leia `references/deploy-best-practices.md`.
- Para incidentes e falhas em produção: leia `references/troubleshooting-playbooks.md`.

### 2. Classifique a tarefa

Escolha um dos fluxos para seguir na seção de Exemplos de Uso:
1. **Deploy**: Use quando a tarefa for publicar, configurar ou revisar como a aplicação sobe no Coolify.
2. **Operação**: Use quando a tarefa for manter ambiente, revisar responsabilidades do self-hosting ou definir padrões operacionais.
3. **Troubleshooting**: Use quando a tarefa for diagnosticar erro, indisponibilidade, falha de proxy, health check, SSL, DNS ou porta.

## Available Scripts

> **Nota**: Não há scripts executáveis neste skill. Este skill baseia-se puramente em fluxos de conhecimento, workflows e diagnósticos para deploy e operação na plataforma Coolify.

## Usage Examples

### Fluxo de Deploy

1. Leia `references/coolify-concepts.md` e `references/deploy-best-practices.md`.
2. Classifique a aplicação:
   - 100% estática
   - SSR ou hybrid
   - API ou backend
   - stack multi-serviço
3. Escolha o build pack com o menor risco operacional (veja Regras de Decisão).
4. Defina porta, host, env vars, domínio e health check.
5. Verifique se rolling update é aplicável.
6. Trate persistência como exceção, não como padrão.

### Fluxo de Operação

1. Leia `references/coolify-concepts.md`.
2. Identifique se o contexto é self-hosted ou Coolify Cloud.
3. Separe o que é responsabilidade do app e o que é responsabilidade do servidor.
4. Revise:
   - domínios e DNS
   - proxy e SSL
   - health checks
   - uso de disco
   - variáveis sensíveis
   - storage persistente

**(Regra operacional)**: No modo self-hosted, o Coolify simplifica deploy e proxy, mas não substitui hardening do servidor, política de backup, atualização de sistema, firewall e monitoramento básico.

### Fluxo de Troubleshooting

1. Leia `references/troubleshooting-playbooks.md`.
2. Identifique o sintoma principal, não a teoria.
3. Comece por rede, proxy, porta e health check antes de assumir bug de código.
4. Procure por incompatibilidade entre:
   - porta esperada pelo Coolify
   - porta real da aplicação
   - `HOST` e `PORT`
   - health check configurado
   - domínio e DNS
5. Só depois avance para suspeitas no framework ou na aplicação.

## Checklist de Qualidade / Regras de Decisão

- [ ] **Build packs adequados**: 
  - **Dockerfile**: padrão recomendado quando a aplicação precisa de runtime explícito, health check confiável, imagem customizada.
  - **Static**: somente quando a saída final já é totalmente estática.
  - **Nixpacks**: aceitável para projetos convencionais sem Dockerfile.
  - **Docker Compose**: somente para stacks com vários serviços acoplados.
- [ ] Se houver `No available server` ou `404` após deploy, primeiro suspeite de health check, binding em localhost (`HOST=0.0.0.0` ausente) ou porta incorreta.
- [ ] Se a aplicação for `Docker Compose`, não presuma rolling update.
- [ ] Se a app for stateless, evite volume persistente no container web.
- [ ] Se um segredo é usado apenas em runtime, não marque como build variable.
- [ ] Se o domínio usa `https://`, confirme DNS e emissão de certificado antes de culpar a aplicação.
- [ ] O resultado esperado ao usar o skill deve deixar claro qual fluxo foi seguido, qual build pack configurado e os riscos operacionais.
