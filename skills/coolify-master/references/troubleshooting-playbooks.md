# Playbooks de troubleshooting no Coolify

## Sintoma: `No available server`

Verifique nesta ordem:
1. health check falhando
2. app escutando na porta errada
3. app escutando em `localhost` em vez de `0.0.0.0`
4. proxy apontando para a porta errada

Perguntas chave:
- Qual porta a app realmente usa?
- O recurso no Coolify usa a mesma porta?
- O endpoint de health check responde `200`?

## Sintoma: `404` apos deploy

Verifique:
1. health check bloqueando roteamento
2. path-based routing incorreto
3. dominio cadastrado apontando para recurso errado
4. app subiu, mas nao ficou saudável

## Sintoma: app funciona no container, mas nao no dominio

Suspeitas principais:
- binding em `127.0.0.1`
- porta divergente
- dominio ou DNS incorreto
- certificado ainda nao emitido

## Sintoma: SSL quebrado ou certificado self-signed

Verifique:
1. DNS resolvendo para o servidor correto
2. dominio cadastrado com `https://`
3. falha de emissao Let's Encrypt

Nao comece assumindo erro da aplicacao.

## Sintoma: rolling update nao acontece

Verifique:
1. se ha health check configurado e funcional
2. se o deploy e baseado em `Docker Compose`
3. se a estrategia escolhida depende de nomes padrao de container

## Sintoma: deploy falha depois de mudar env vars

Verifique:
1. variavel marcada como build quando deveria ser runtime
2. segredo com caracteres especiais sem tratamento adequado
3. valor obrigatorio ausente
4. diferenca entre env de preview e producao

## Sintoma: app SSR/hybrid foi publicada como estatica

Sinal comum:
- paginas estaticas funcionam, mas endpoints server-side falham

Correcao:
- reclassificar o deploy para `Dockerfile` ou outra estrategia server-side apropriada

## Fluxo recomendado de diagnostico

1. Confirmar sintoma observavel.
2. Confirmar dominio, DNS, porta e binding.
3. Confirmar health check.
4. Confirmar build pack escolhido.
5. Confirmar env vars de build e runtime.
6. So entao entrar no codigo da app.

## Atalho mental util

Em Coolify, muitos problemas que parecem bug de framework sao na verdade uma destas quatro classes:
- porta errada
- binding errado
- health check errado
- dominio/DNS errado
