[![skills.sh](https://skills.sh/b/fabricioctelles/skills)](https://skills.sh/fabricioctelles/skills)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?logo=cloudflare&logoColor=white)
![Astro](https://img.shields.io/badge/Astro-BC52EE?logo=astro&logoColor=white)
![Coolify](https://img.shields.io/badge/Coolify-6B16ED?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQTEwIDEwIDAgMCAwIDIgMTJhMTAgMTAgMCAwIDAgMTAgMTAgMTAgMTAgMCAwIDAgMTAtMTBBMTAgMTAgMCAwIDAgMTIgMnoiLz48L3N2Zz4=&logoColor=white)
![Google Analytics](https://img.shields.io/badge/Google%20Analytics-E37400?logo=googleanalytics&logoColor=white)
![Google Search Console](https://img.shields.io/badge/Search%20Console-458CF5?logo=google&logoColor=white)
![Substack](https://img.shields.io/badge/Substack-FF6719?logo=substack&logoColor=white)
![SEO](https://img.shields.io/badge/SEO%20%2F%20GEO-4285F4?logo=google&logoColor=white)
![AI Agents](https://img.shields.io/badge/AI%20Agents-8B5CF6?logo=openai&logoColor=white)
![LGPD](https://img.shields.io/badge/LGPD%20%2F%20Privacy-059669?logo=shieldsdotio&logoColor=white)
![Security](https://img.shields.io/badge/Security-DC2626?logo=owasp&logoColor=white)

# 🧠 Agent Skills by ft.ia.br

Colecao de [Agent Skills](https://agentskills.io) para agentes de IA (Kiro, Cursor, Windsurf, Claude Code e outros). Cada skill e um modulo reutilizavel que ensina o agente a executar tarefas complexas com contexto, estrutura e boas praticas.

Agent Skills sao um formato aberto e leve para estender as capacidades de agentes de IA com conhecimento especializado e workflows. Cada skill e uma pasta com um arquivo `SKILL.md` contendo metadados e instrucoes que os agentes carregam sob demanda via progressive disclosure. Saiba mais em [agentskills.io](https://agentskills.io/what-are-skills.md).

## Skills Disponíveis

### 🔍 GEO Optimization (Generative Engine Optimization) · `code-quality-and-review`
Otimiza conteúdo digital e estratégias de marketing para Generative Engines (LLMs, AI agents) visando maximizar citações em respostas de IA.

**Quando usar:** melhorar visibilidade em respostas de IA (ChatGPT, Perplexity, Google AI Overview), medir citation rate, alinhar terminologia para LLMs, auditar páginas para IA, criar roundups e FAQs otimizadas.

**Melhorias na v1.1 (Mar 2026):**
- Princípios Orientadores e contexto de casos movidos para `references/guiding-principles.md`
- Linguagem em segunda pessoa corrigida para forma imperativa
- Adicionado comportamento padrão explícito (Full GEO Audit) quando nenhuma ação específica é solicitada
- Seção Edge Cases convertida em Checklist de Qualidade estruturado com checkboxes
- Description otimizada para maior concisão e acionabilidade (8 Mar)

📄 [Ver documentação completa](skills/geo-optimization/SKILL.md)

---

### 📰 Substack Expert · `library-and-api-reference`
Especialista na plataforma Substack. Orienta formatação de posts, otimização SEO (títulos, slugs, meta descriptions), estratégias nativas de engajamento (Notes, Chat) e conversão para assinaturas pagas.

**Quando usar:** formatar e otimizar posts no Substack, melhorar SEO de newsletters (títulos, slugs, meta descriptions), crescer audiência com Notes e recomendações, converter leitores gratuitos em assinantes pagos, personalizar homepage e emails de boas-vindas.

**Melhorias na v1.1 (Mar 2026):**
- Removida seção Overview duplicada e artefato em português com code fence órfão
- Dicas de formatação movidas para `references/formatting-best-practices.md`
- Exemplos de Input/Output movidos para `references/seo-output-example.md`
- Adicionada tabela de Parâmetros com defaults para tópico, objetivo e idioma
- Adicionado passo explícito de Clarificação de Escopo para pedidos ambíguos
- Adicionado Checklist de Qualidade com 8 pontos de verificação pré-entrega

📄 [Ver documentação completa](skills/substack-expert/SKILL.md)

---

### ☁️ Pier Cloud API · `library-and-api-reference`
Guia completo para consumir a API Pier Cloud (Lighthouse) com autenticação, gerenciamento de contextos, workspaces e visualizações de dados.

**Quando usar:** autenticar na Pier Cloud, listar contextos disponíveis (AWS, etc), gerenciar workspaces, acessar visualizações de análise de custos, executar scripts de FinOps.

**Melhorias na v1.1 (Mar 2026):**
- Descrição reescrita no formato de gatilho em terceira pessoa
- Seção Overview verbatim que duplicava a descrição removida
- Seção Pré-requisitos quebrada e incompleta corrigida e consolidada
- Linguagem em segunda pessoa convertida para forma imperativa
- Links de workflow limpos para delegar corretamente ao `references/REFERENCE.md`
- Adicionado Checklist de Qualidade

📄 [Ver documentação completa](skills/pier-cloud/SKILL.md)

---

### 🎨 Ultimate Design System Master · `code-scaffolding-and-templates`
Gera entregáveis de design no nível Apple/Pentagram/frog/Vercel/Figma usando 10 prompts especializados com role-play. Cobre Design Systems, Brand Identity, UI/UX Patterns, Marketing Assets, Figma Specs, Design Critique, Trend Analysis, Accessibility Audit, Design-to-Code e Apresentações Executivas.

**Quando usar:** criar design system, construir identidade de marca, gerar padrões UI/UX, produzir assets de marketing, escrever specs para Figma, obter crítica de design, analisar tendências de design, rodar auditoria de acessibilidade, traduzir design para código, criar decks de apresentação.

**Melhorias na v2.1 (Mar 2026):**
- Descrição reescrita no formato de gatilho em terceira pessoa
- Questionário de Briefing com 18 perguntas movido para `references/briefing-questionnaire.md`
- Adicionado Checklist de Qualidade com 5 condições concretas de verificação
- Frase de introdução que duplicava a descrição do frontmatter removida

**Melhorias na v2.2 (8 Mar 2026):**
- Description reescrita com frases de acionamento que usuários realmente falam para melhor ativação da skill
- License Apache 2.0 adicionada ao metadata
- Conformidade 100% com Guia Oficial Anthropic para Agent Skills alcançada

📄 [Ver documentação completa](skills/ultimate-design-system-master/SKILL.md)

---

### 🗂️ Front-End Checklist _(movido)_

> **Esta skill foi aposentada.** O projeto original agora oferece 385 skills independentes (uma por regra) cobrindo HTML, CSS, JavaScript, Performance, Acessibilidade, SEO, Segurança, Imagens, Testing, Privacidade e Internacionalização — muito mais completo do que mantínhamos aqui.
>
> 👉 **Instale direto da fonte:** https://github.com/thedaviddias/Front-End-Checklist/tree/main/skills
>
> ```bash
> npx skills add frontendchecklist/skills
> ```

---

### 🚀 Coolify Operator · `ci-cd-and-deployment`
Operador mestre do Coolify — plataforma self-hosted open-source de deployment (alternativa ao Heroku/Vercel/Netlify). Gerencia aplicações, servidores, databases e serviços via API REST e CLI oficial.

**Quando usar:** conectar em instâncias Coolify, fazer deploy/restart/stop de aplicações, gerenciar variáveis de ambiente, listar servidores e databases, monitorar logs de deployment, gerenciar múltiplos ambientes (dev/staging/prod), troubleshooting de conexão e autenticação.

**Melhorias na v1.1 (8 Mar 2026):**
- Description otimizada para clareza e brevidade (350→250 caracteres)
- License MIT adicionada ao metadata
- Quality Checklist com 10 pontos de verificação adicionado
- README.md interno removido para conformidade total com Guia Oficial Anthropic
- Conformidade 100% com Guia Oficial Anthropic para Agent Skills alcançada

📄 [Ver documentação completa](skills/coolify-operator/SKILL.md)

---

### 📄 Resume ATS Beater + LinkedIn Optimizer · `code-scaffolding-and-templates`
Reescreve currículos para compatibilidade ATS e audita perfis LinkedIn para posicionamento profissional. Cobre otimização de CV para plataformas ATS brasileiras (Gupy, Vagas.com, PandaPé, Sólides) e auditoria LinkedIn com score heurístico, análise de SSI, fix prompts e mega-prompts de reescrita por LLM. Funciona para qualquer profissão especializada — não é exclusivo para devs.

**Quando usar:** otimizar currículo para ATS, auditar perfil LinkedIn (headline, about, experiências, SSI), adaptar CV para cargo/indústria alvo, gerar fix prompts por problema encontrado, alinhar CV e LinkedIn em modo unificado, fortalecer bullets com resultados mensuráveis. Integra com skill `humanizar` para seções narrativas.

**Melhorias na v2.0 (Jun 2026):**
- Adicionados `modo_linkedin` (auditoria completa com scoring) e `modo_unificado` (CV + LinkedIn com verificação de consistência)
- Auditoria LinkedIn: formato obrigatório de headline (Posição | Áreas | Ferramentas·), estrutura de about, bullets de experiência, idioma, skills, featured, SSI
- Sistema de score punitivo: 100 - (critical×15 + warning×6 + info×2)
- Análise SSI com 4 pilares, classificação por faixa e tips acionáveis
- Fix prompts por finding (prompts standalone para qualquer LLM)
- Mega-prompt para reescrita completa do perfil por LLM
- 18 presets de cargo: tecnologia, dados, marketing, finanças, engenharia, jurídico, vendas, RH, produto
- Integração com skill `humanizar` (escopo restrito a About/Resumo Profissional)
- 3 novos arquivos de referência: `auditoria-linkedin.md`, `ssi.md`, `presets-formatos.md`

📄 [Ver documentação completa](skills/resume-ats-beater/SKILL.md)

---

### 🤖 Agent Ready — Cloudflare Scanner · `product-verification`
Audita qualquer website para prontidão de agentes de IA usando o scanner [isitagentready.com](https://isitagentready.com) da Cloudflare. Verifica 18 checks em 5 categorias (Discoverability, Content, Bot Access Control, API/Auth/MCP Discovery, Commerce), atribui um nível (0–5) e gera prompts de correção copy-paste para cada check que falha. Inclui 20 sub-skills de implementação cobrindo robots.txt, sitemap, Markdown for Agents, Content Signals, MCP Server Card, A2A Agent Card, Agent Skills Index, OAuth, WebMCP e mais.

**Quando usar:** escanear site para prontidão de agentes, verificar score agent-ready, corrigir checks que falham, implementar MCP Server Card, adicionar Content Signals, publicar Agent Skills index, configurar Markdown for Agents, escanear múltiplos domínios em batch, melhorar descoberta por agentes de IA.

📄 [Ver documentação completa](skills/agent-ready-cloudflare/README.md)

---

### ✅ DESIGN.md Validator · `product-verification`
Valida arquivos DESIGN.md contra a [especificação oficial do Google](https://github.com/google-labs-code/design.md) usando o CLI `@google/design.md`. Funciona com arquivos locais e URLs remotas. Sempre usa `npx` para rodar a versão mais recente — nunca desatualizado.

**Quando usar:** validar DESIGN.md contra a spec, checar contraste WCAG, encontrar referências de tokens quebradas, comparar duas versões de design system, exportar tokens para Tailwind v3/v4 ou W3C DTCG, auditar schema do frontmatter.

📄 [Ver documentação completa](skills/design-md-validator/SKILL.md)

---

### 🔁 Ralph Loop for Kiro Specs · `code-scaffolding-and-templates`
Runner iterativo automatizado para desenvolvimento baseado em specs no [Kiro](https://kiro.dev). Encapsula o `kiro-cli` em um loop bash auto-corretivo que pega tasks de uma Kiro spec, implementa uma por vez, verifica contra critérios de saída e acumula correções e padrões de codebase entre iterações. Baseado em [ralph-loop-kiro-specs](https://github.com/mreferre/ralph-loop-kiro-specs) por [mreferre](https://github.com/mreferre).

**Quando usar:** automatizar implementação de tasks de Kiro specs, rodar kiro-cli em loop, levar uma spec até a conclusão através de iterações repetidas do agente, configurar ou fazer troubleshooting do workflow Ralph Loop, entender progress tracking, correções, padrões de codebase e o dashboard de resumo.

📄 [Ver documentação completa](skills/ralph-loop-kiro-specs/SKILL.md)

---

### 🏗️ Loop Architect — Coach de Design de Agent Loops · `code-scaffolding-and-templates`
Projeta loops agenticos bem estruturados com coaching de boas práticas e gates de revisão cross-model antes de executá-los. Entrevista você, critica seu design contra rubrics internas, configura reviewers/judges, e emite artefatos portáveis (`loop.yaml`, `RUN_IN_SESSION.md`, `run-loop.py`). Integra nativamente com `/goal` e subagent review loops do Kiro CLI. Baseado em [Looper](https://github.com/ksimback/looper) por [Kevin Simback](https://github.com/ksimback).

**Quando usar:** projetar um agent loop, configurar um loop de self-review ou LLM-as-judge, construir um council multi-modelo, criar workflows iterativos com review gates, ou scaffoldar um processo orientado a `/goal` com verificação tipada e guardas de terminação.

📄 [Ver documentação completa](skills/loop-architect/SKILL.md)

---

### ✍️ Humanizar — Humanizador de Texto IA para Português Brasileiro · `code-quality-and-review`
Reescreve texto em português brasileiro para soar humano, natural e indetectável por ferramentas de IA. Remove padrões de AI slop, restaura entropia semântica e injeta voz e personalidade. Nasceu da skill `humanizer` em inglês mas evoluiu para algo muito mais completo — com 55+ padrões específicos do PT-BR que nenhuma outra fonte catalogou.

**Como nasceu:** Parti da skill [humanizer](https://github.com/blader/humanizer) em inglês por [@blader](https://github.com/blader) (baseada no artigo da Wikipedia "Signs of AI writing"), pesquisei o que torna texto de IA detectável especificamente em português brasileiro, descobri que existia *zero* material consolidado sobre padrões de IA em PT-BR, cataloguei 55+ padrões do zero (incluindo 10 exclusivos do português brasileiro como gerundismo, officialese e hedging estilo ENEM), incorporei o diretório [tropes.fyi](https://tropes.fyi) e o conceito de [ablação semântica](https://www.theregister.com/2026/02/16/semantic_ablation_ai_writing/) (The Register, 2026), e construí uma skill que não apenas remove padrões ruins — restaura a entropia que a IA arrancou.

**Por que é melhor para PT-BR que a original:**
- 55+ padrões vs 25 (incluindo 10 que só existem em português brasileiro)
- Restauração de entropia semântica com alertas explícitos (não só remoção)
- 6 presets de voz calibrados para contextos brasileiros (crônica, jornalístico, acadêmico, corporativo, rede social, WhatsApp)
- Exemplos culturalmente brasileiros, não traduções do inglês
- Preserva estrangeirismos naturalizados (feedback, deploy, churn) — combater purismo linguístico é em si um sinal de humanização
- Usa a tradição literária da *crônica* brasileira como padrão-ouro de escrita natural

**Quando usar:** humanizar texto PT-BR, remover AI slop, reescrever com voz, corrigir tom genérico/burocrático, revisar texto de outro agente, "tirar cara de IA", "dar vida ao texto".

**Melhorias na v1.2 (Jun 2026):**
- Adicionada detecção automática de tipo de documento com fallback (Passo 0.5) — seleciona o melhor preset de voz automaticamente
- Adicionado scoring pós-reescrita com 5 dimensões ponderadas (Passo 5.5) — gate de qualidade quantificável
- Adicionado loop iterativo com fallback de estratégia — retenta com abordagens diferentes quando score < 60
- Protocolo de loop compatível com skills de orquestração externas (ralph-wiggum, goal)
- Inspirado na skill [humanize-it](https://github.com/smallnest/goal-workflow/blob/master/skills/humanize-it/SKILL.md) de [@smallnest](https://github.com/smallnest)

**Novidades na v1.3 (Jul 2026):**
- Adicionado perfil de voz **📋 Português Simplificado** — escrita acessível inspirada no PorSimples (NILC/USP) e na Lei 15.263/2025 (Política Nacional de Linguagem Simples)
- 7 operações de simplificação sintática baseadas na pesquisa do PorSimples (divisão de sentenças, passiva→ativa, reordenação SVO, substituição de marcadores discursivos, remoção de apostos, simplificação lexical, explicitação de sujeitos)
- Novo arquivo de referência `references/padroes-portugues-simplificado.md` com ~50 substituições lexicais, métricas quantitativas do NILC-Metrix (ASL, TTR, complexidade sintática), 15 regras de escrita em 3 níveis de prioridade, e 4 domínios de aplicação (governo, saúde, tecnologia, educação)
- Integração com TRAVA FACTUAL: regras explícitas de quando NÃO simplificar (modalidade, causalidade, exceções)
- Agora são 10 perfis de voz (eram 9): Crônica, Jornalístico, Acadêmico, Corporativo Informal, Post de Rede Social, WhatsApp, Jurídico, Didático, **Português Simplificado** e Voz Neutra

📄 [Ver documentação completa](skills/humanizar/SKILL.md)

---

### 🌐 Human-AI — Humanizador de Texto IA para Inglês · `code-quality-and-review`
Reescreve texto em inglês para soar humano, natural e indetectável por ferramentas de IA. Combina detecção de padrões (43 padrões em 3 tiers), medição estatística (burstiness, TTR, entropia) e injeção de voz em uma skill iterativa. Construída com base em pesquisas do RAID Benchmark (ACL 2024), NeurIPS 2023, e testes reais que provaram que bans de vocabulário FALHAM — reestruturação estrutural é o que realmente engana detectores.

**Como nasceu:** Skill-irmã da `humanizar` (PT-BR), mas 100% trabalho original para inglês. Sintetiza o melhor de três skills open-source: [blader/humanizer](https://github.com/blader/humanizer) (10.6K stars, 29 padrões), [brandonwise/humanizer](https://github.com/brandonwise/humanizer) (filtro de 560 termos, sinais estatísticos), e [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill) (43 padrões, P31-P43 descobertas de 2026). Vai além de todas adicionando: baselines empíricas calibradas por pesquisa, scoring iterativo com fallback de estratégia, 7 presets de voz, `scripts/measure.py` para métricas determinísticas, e o insight crítico de que trocar sinônimos piora enquanto reestruturação estrutural derruba acurácia de detectores de 70.3% para 4.6%.

**Por que é diferente das skills humanizer existentes:**
- 43 padrões (incluindo P31-P43, padrões emergentes de pesquisa comunitária 2026)
- Métricas com base em pesquisa: TTR humano 0.553 vs AI 0.455 (SSRN), burstiness +0.70 vs 0.00 (GPTZero)
- `scripts/measure.py` — cálculo determinístico de TTR/burstiness/entropia (zero dependências)
- 7 presets de voz calibrados para contextos em inglês (essay, journalistic, academic, corporate, social, casual, legal, instructional)
- Proibição de troca de sinônimos: Step 2 exige reestruturação completa da frase, não substituição de palavras
- 7 gotchas documentados de falhas reais de skills humanizer
- Loop iterativo com scoring (0-100) e tabela de fallback de estratégia
- Compõe com skills de loop externas (ralph-wiggum, goal)

**Quando usar:** humanize English text, remove AI slop, de-slop content, make text sound human, add voice, fix bland/generic tone, bypass AI detection, pass GPTZero/Originality.ai, review text from another agent, rewrite naturally.

📄 [Ver documentação completa](skills/human-ai/SKILL.md)

---

### 🔐 auth.md — Protocolo de Autenticação para Agentes · `library-and-api-reference`
Gera, valida e explica arquivos [auth.md](https://auth-md.com) — o protocolo aberto que permite agentes de IA registrarem-se em serviços em nome de usuários sem formulários de signup. Suporta o fluxo Agent Verified (assertions de identidade ID-JAG via providers confiáveis como OpenAI, Anthropic, Cursor) e o fluxo User Claimed (registro baseado em OTP com entrypoints anonymous start ou email required). Estende o RFC 9728 (Protected Resource Metadata) com suporte a CIMD.

**Quando usar:** tornar sua app agent-ready publicando um `auth.md`, gerar Protected Resource Metadata e Authorization Server metadata com bloco `agent_auth`, validar um `auth.md` existente contra a spec do protocolo, implementar endpoints de registro de agentes (`/agent/auth`, `/agent/auth/claim`, `/agent/auth/revoke`), entender como o protocolo auth.md funciona, configurar verificação de ID-JAG e trust lists, configurar cerimônias de claim OTP.

📄 [Ver documentação completa](skills/auth-md/SKILL.md) | 🌐 [auth-md.com](https://auth-md.com)

---

### 📦 OKF — Open Knowledge Format · `library-and-api-reference`
Cria, valida e enriquece bundles no [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — spec aberta (v0.1, anunciada 12 Jun 2026 por Sam McVeety & Amir Hormati, Google Cloud) que formaliza o pattern "LLM Wiki" num formato portável e interoperável para conhecimento organizacional. Arquivos Markdown com YAML frontmatter, consumíveis por qualquer agente IA sem SDK. Inclui script bash de validação, guias de conversão (Notion, Obsidian, CSV) e integração com Google Cloud Knowledge Catalog via kcmd CLI/MCP.

**Quando usar:** criar bundles OKF, validar conformidade, enriquecer conceitos com schema/citations/cross-links, converter conhecimento existente (exports Notion, vaults Obsidian, planilhas) para OKF, estruturar base de conhecimento para agentes IA, gerar index.md e log.md, enviar bundles para o Knowledge Catalog via kcmd.

📄 [Ver documentação completa](skills/okf-open-knowledge-format/SKILL.md) | 🌐 [okf.md](https://okf.md)

---

### 🌐 Website Spec _(movido)_

> **Esta skill foi aposentada.** O projeto original agora oferece uma skill mais completa com 140+ tópicos, atualizações live via MCP server, re-audits incrementais e integração com MDN — muito além do que mantínhamos aqui.
>
> 👉 **Use a skill oficial:** https://specification.website/.well-known/agent-skills/specification-website/SKILL.md
>
> MCP endpoint: `https://mcp.specification.website/mcp`

---

### 🔒 LGPD Check
> **Migrado** → Esta skill foi movida para [github.com/lgpd-app/skills](https://github.com/lgpd-app/skills)
Audita websites para conformidade com a LGPD brasileira (Lei 13.709/2018). Valida política de privacidade, consentimento de cookies, minimização de dados, transferência internacional, direitos do titular, scripts de terceiros e analytics. Gera relatório de conformidade com score e correções prioritárias. Totalmente em português.

**Quando usar:** auditar um site para conformidade LGPD, validar política de privacidade contra a lei brasileira, verificar implementação de consentimento de cookies, checar canais de direitos do titular, avaliar transferências internacionais de dados, revisar scripts de terceiros quanto a riscos de privacidade, gerar score de conformidade LGPD.


---

---

### 📊 Skill Evaluation · `code-quality-and-review`
Avalia qualquer skill de agente contra um framework combinado — best practices do Claude Code (Anthropic) + metodologia writing-great-skills do Matt Pocock — em 4 eixos (Trigger, Structure, Steering, Pruning). Produz um scorecard com evidências citadas (0–100), nota geral ponderada e modos de falha diagnosticados com correções priorizadas.

**v2.2 — Trigger Eval (empírico):** agora inclui um step de teste empírico de triggering inspirado na palestra de Philipp Schmid (Google DeepMind) ["Don't Ship Skills Without Evals"](https://www.youtube.com/watch?v=0vphxNt4wyk). Gera 5 prompts que deveriam triggerar + 5 que não deveriam, executa via sub-agentes independentes, e mede se a description da skill realmente causa invocação — conectando análise estática de qualidade com validação em runtime.

**Quando usar:** avaliar uma skill, dar nota para skill, auditar SKILL.md, comparar duas skills, scorecard de qualidade, verificar compliance com best practices, ou checar se uma skill está production-ready.

**18 critérios em 4 eixos:** Invocation design · Description quality · Steps vs. reference clarity · Branch-aware disclosure · Conciseness · Coherent scope · Leading words · Completion criteria · Gotchas · Grounded in expertise · Avoids railroading · No-ops · Single source of truth · Relevance & sediment + 4 condicionais (Setup flow · Memory · Scripts · Hooks)

**5 bonus patterns (medidos, sem impacto na nota):** Validation loops · Output templates · Procedures over declarations · Defaults over menus · Trace-checkable steering

**Diferença do [agentskills.io evals](https://agentskills.io/skill-creation/evaluating-skills) e [skill-creator benchmark](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills):**

| | Esta skill | agentskills.io evals | skill-creator benchmark |
|---|---|---|---|
| Avalia | Qualidade da **estrutura** + **trigger** empírico | Qualidade do **output** | Output + regressão + obsolescência |
| Método | Inspeção estática + trigger eval via sub-agentes | Test cases + grading | Comparação A/B cega + multi-agent |
| Quando | Está bem construída? Triggera corretamente? | Funciona? | Regrediu? Ainda necessária? |
| Saída | Scorecard + grade A-F + hit/leak rates de trigger | pass_rate, tokens, time | benchmark.json + veredito comparador |
| Plataforma | Qualquer agente | Qualquer agente | Claude Code only (plugin) |

Use em sequência: **skill-evaluation** (design review + teste de trigger) → **evals** (validação funcional) → **benchmark** (monitoramento contínuo).

📄 [Ver documentação completa](skills/skill-evaluation/SKILL.md)

---

### 🧹 Slop Eval — Avaliador de Slop em Design · `code-quality-and-review`
Avalia objetivamente um design de UI/web contra [a lei anti-slop da pols.dev](https://pols.dev/slop.md): varre um catálogo de tells de slop com IDs em 6 famílias (cor & luz, tipografia, componentes, layout, motion, execução), checa 6 regras absolutas de execução e pontua 8 eixos ponderados — incluindo um eixo de Assinatura com peso 3x e gate rígido, para que uma página "limpa mas vazia" não se esconda atrás da contenção. Emite um Slop Report com Slop Index 0–100 e nota A–F. Todo achado segue **cite-or-cut**: sem evidência concreta (hex, nome de fonte, file:line, região do screenshot), o tell não entra.

**Como avalia:** URL viva (SOP de automação de browser: capturas full-page em dois viewports, passada de interação, crops com zoom), screenshots estáticos, código (varredura guiada por grep) ou export de Figma — o que não for observável é marcado Unverifiable, nunca inferido. Pontuação determinística via `scripts/score.py`, com gate de CI `--fail-below` para bloquear PRs pela qualidade do preview deploy.

**Quando usar:** avaliar slop de design, gerar relatório de slop, checar se um design parece genérico/gerado por IA, auditar landing page, revisão de-slop, comparar dois designs (antes/depois).

**Companheiras:** método inspirado na [skill-evaluation](skills/skill-evaluation/SKILL.md); para texto (não design), quem faz o de-slop é a [human-ai](skills/human-ai/SKILL.md) e a [humanizar](skills/humanizar/SKILL.md).

📄 [Ver documentação completa](skills/slop-eval/SKILL.md)

---

### 🛡️ Security Specialist · `runbooks`
Agente completo de segurança de aplicações — executa SAST (análise estática de código), DAST (testes dinâmicos contra apps rodando), threat modeling, triagem de vulnerabilidades, remediação e penetration testing. Combina revisão de código com testes ao vivo contra servidores dev locais ou targets de produção para correlação completa de evidências.

**Quando usar:** escanear repositório por segurança, revisar PR por vulnerabilidades, construir threat model, triar findings, corrigir bug de segurança, fazer pentest em app web, validar fix de segurança, exportar findings para GitHub/Jira/Linear, gerar relatório de segurança.

**Funcionalidades:**
- **SOP baseado em input**: path → SAST + DAST dev; path + URL → SAST + dev + prod; URL → DAST
- **12 steering workflows**: full-scan, diff-review, pentest, hunting, threat-model, attack-paths, discovery, triage, remediation, tracking, validation, reporting
- **Pipeline de 6 fases** (full-scan): Recon → Hunt → Validate → Report → Schema → Verify — com agentes paralelos e validação adversarial
- **9 attack classes**: Injection, Access Control, Resource/File, Cryptography, Business Logic, Feature Abuse, Chained Attacks, Wildcard, Obvious Things
- **Hunting methodology com 12 ângulos**: sad path, boundaries, component assumptions, wrong ordering, concurrency, parser disagreements, round-trip fidelity, config control, privilege tracing, leaked context, parameter overrides, unverified claims
- **Validação adversarial**: agentes separados tentam DISPROVAR findings (5 gates: exploitation, impact, baseline, mitigation, parser/runtime)
- **Structured JSON output**: findings.json validado contra JSON schema com trace (entrypoint→propagation→sink), conditions, execution, confidence
- **Schema validator**: script Node.js zero-deps (`validate-findings.cjs`) para integração CI
- **Multi-run additive coverage**: cada run targeta gaps dos runs anteriores; single run encontra ~50% do total
- **5 scripts utilitários**: SQLite scan DB, ranqueador de arquivos, finalizador de relatório, automação de pentest, validador de schema
- **Cascata de ferramentas**: nmap → python-nmap → socket; nikto → wapiti3 → header checks; gobuster → dirsearch → urllib
- **Correlação em 3 camadas**: finding no source → exploit no dev → confirmação no prod
- **Calibração de baseline dinâmico**: compara patterns contra aplicações comparáveis do mercado

**Arquitetura:**
```
security-specialist/
├── SKILL.md              (router + core principles + anti-patterns)
├── steering/             (12 workflow docs incluindo hunting methodology)
├── scripts/              (5 tools: Python + Node.js validator)
└── references/           (5 spec docs: finding format, report format, severity policy, artifacts, report-schema.json)
```

**Melhorias na v2.0 (Jun 2026):**
- Pipeline de auditoria de 6 fases com agentes paralelos (inspirado no Cloudflare security-audit-skill)
- Adicionado `steering/hunting.md` com 9 attack classes e hunting methodology de 12 ângulos
- Validação adversarial (Phase 3) e verificação independente (Phase 6)
- Adicionado `references/report-schema.json` para findings estruturados com trace, conditions, execution, confidence
- Adicionado `scripts/validate-findings.cjs` validador de schema zero-deps
- Estratégia de multi-run additive coverage
- 10 anti-patterns a evitar em auditorias de segurança
- Calibração de baseline dinâmico na severity policy
- Finding format dual: simples (SQLite) + estruturado (JSON pipeline)

📄 [Ver documentação completa](skills/security-specialist/SKILL.md)

---

### 🚀 Astro Sites Manager · `ci-cd-and-deployment`
Skill completa para construir, migrar e manter projetos Astro v7. Cobre o ciclo completo: boas práticas, migração v6→v7 com plano estruturado, validação de breaking/deprecated patterns, dev server com AI (background mode, JSON logging), advanced routing com src/fetch.ts, route caching, Sätteri Markdown, compilador Rust, Starlight docs, Pagefind search, SEO, testes e deploy em 8+ plataformas incluindo Coolify.

**Quando usar:** construir sites Astro, atualizar para v7, deploy no Coolify/Vercel/Netlify/Cloudflare, validar breaking changes, configurar Starlight docs, configurar Pagefind search, usar background dev server como agente IA, configurar route caching.

**Destaques:**
- Integração com MCP Astro Docs (acesso à documentação em tempo real)
- 10 arquivos de referência cobrindo migração, validação, testes, deploy, Starlight e mais
- Guia de deploy no Coolify battle-tested com padrões de 17 projetos em produção
- Feature detection: features v7 ativam só quando disponíveis (seguro no v6)

📄 [Ver documentação completa](skills/astro-sites-manager/SKILL.md)

---

### 💰 Revenue-Centric Design · `runbooks`
Playbook de 101 princípios baseados em evidência para desenhar produtos SaaS e startups que convertem, retêm e monetizam — landing pages & CRO, onboarding/ativação, redução de churn, psicologia de pricing, ciência comportamental, disciplina de features, posicionamento/ICP, go-to-market e diferenciação na era da IA. Cada princípio nomeia seu mecanismo (efeito decoy, Zeigarnik, níveis de consciência de Schwartz…) e linka de volta ao post original. Inclui scripts de matemática de receita (sample size de A/B, churn→LTV, CAC por deal fechado), template de auditoria, memória por projeto (`rcd-log.md`) e guardrail hooks que fazem enforcement da licença.

**Como nasceu:** Richard ([@richardrx](https://x.com/richardrx), "Design for startups" — ex-Volkswagen, PayPal, IBM) publicou esses princípios em 101 posts em português no X. [Helio Costa](https://github.com/heliocosta-dev) obteve a permissão do autor, extraiu os posts via API do X, traduziu para inglês e destilou tudo na skill original ([heliocosta-dev/revenue-centric-design](https://github.com/heliocosta-dev/revenue-centric-design)). Este repositório hospeda um derivado evoluído desse trabalho.

**Evolução medida com a [skill-evaluation](skills/skill-evaluation/SKILL.md):** a skill como baixada marcou **60/100 (B, na divisa com C)**; um passe de melhorias depois, **73/100 (B)**:

| Critério | antes | depois |
|---|---|---|
| Scripts & libraries | 0 | 75 |
| Seção de Gotchas | 35 | 88 |
| Escopo coerente | 55 | 72 |
| Progressive disclosure | 78 | 90 |
| Description para trigger | 78 | 90 |
| Peso no repo | 39 MB | 176 KB |

Depois da comparação, a skill ainda ganhou o template de auditoria, o log por projeto, compliance completo de licença e guardrails via hooks — cada item fechando um finding que o scorecard havia priorizado. É exatamente o loop para o qual a skill-evaluation foi construída: **avaliar → corrigir os top findings → reavaliar → comparar.**

**Quando usar:** melhorar conversão de landing page, corrigir ativação/onboarding, reduzir churn, desenhar tabelas de pricing e upgrade paths, afiar ICP/posicionamento, aplicar mecanismos de ciência comportamental, validar rigor de A/B tests, diferenciar na era da IA.

**⚠️ Licença:** source-available, **não** Apache 2.0 — atribuição ao @richardrx obrigatória, e **uso em apostas/cassino/gambling é proibido** (com enforcement em runtime via hooks embutidos). Veja a [LICENSE da skill](skills/revenue-centric-design/LICENSE).

📄 [Ver documentação completa](skills/revenue-centric-design/SKILL.md)

---

> **Skills revisadas em março de 2026** seguindo o padrão Anthropic para estrutura e qualidade de Agent Skills.
> Fonte: [Improving Skill Creator: Test, Measure and Refine Agent Skills](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)

## Instalacao

Voce pode instalar estas skills usando qualquer instalador compativel ou manualmente. Abaixo estao as opcoes mais populares.

### Via [Skills.sh](https://skills.sh/docs)

```bash
npx skills add https://github.com/fabricioctelles/skills
```

Ou instale uma skill especifica:

```bash
npx skills add https://github.com/fabricioctelles/skills -s geo-optimization
npx skills add https://github.com/fabricioctelles/skills -s substack-expert
npx skills add https://github.com/fabricioctelles/skills -s pier-cloud
npx skills add https://github.com/fabricioctelles/skills -s ultimate-design-system-master
npx skills add https://github.com/fabricioctelles/skills -s resume-ats-beater
npx skills add https://github.com/fabricioctelles/skills -s coolify-operator
npx skills add https://github.com/fabricioctelles/skills -s agent-ready-cloudflare
npx skills add https://github.com/fabricioctelles/skills -s ralph-loop-kiro-specs
npx skills add https://github.com/fabricioctelles/skills -s loop-architect
npx skills add https://github.com/fabricioctelles/skills -s humanizar
npx skills add https://github.com/fabricioctelles/skills -s auth-md
npx skills add https://github.com/fabricioctelles/skills -s security-specialist
npx skills add https://github.com/fabricioctelles/skills -s slop-eval
npx skills add https://github.com/fabricioctelles/skills -s revenue-centric-design
```

### Via [Agent Skills CLI](https://www.agentskills.in/docs)

```bash
npm install -g agent-skills-cli
```

Depois instale as skills:

```bash
skills add https://github.com/fabricioctelles/skills
```

Ou use sem instalar globalmente:

```bash
npx agent-skills-cli install https://github.com/fabricioctelles/skills
```

### Instalacao Manual

1. Clone este repositorio:
```bash
git clone https://github.com/fabricioctelles/skills.git
```

2. Copie a pasta da skill desejada para o diretorio de skills do seu agente:
```bash
# Exemplo para Cursor
cp -r skills/geo-optimization .cursor/skills/
cp -r skills/substack-expert .cursor/skills/
cp -r skills/pier-cloud .cursor/skills/
cp -r skills/ultimate-design-system-master .cursor/skills/
cp -r skills/resume-ats-beater .cursor/skills/
cp -r skills/coolify-operator .cursor/skills/
cp -r skills/agent-ready-cloudflare .cursor/skills/
cp -r skills/ralph-loop-kiro-specs .cursor/skills/
cp -r skills/loop-architect .cursor/skills/
cp -r skills/humanizar .cursor/skills/
cp -r skills/auth-md .cursor/skills/

# Exemplo para Claude Code
cp -r skills/geo-optimization .claude/skills/
cp -r skills/substack-expert .claude/skills/
cp -r skills/pier-cloud .claude/skills/
cp -r skills/ultimate-design-system-master .claude/skills/
cp -r skills/resume-ats-beater .claude/skills/
cp -r skills/coolify-operator .claude/skills/
cp -r skills/agent-ready-cloudflare .claude/skills/
cp -r skills/ralph-loop-kiro-specs .claude/skills/
cp -r skills/loop-architect .claude/skills/
cp -r skills/humanizar .claude/skills/
cp -r skills/auth-md .claude/skills/

# Exemplo para Kiro
cp -r skills/geo-optimization .kiro/skills/
cp -r skills/substack-expert .kiro/skills/
cp -r skills/pier-cloud .kiro/skills/
cp -r skills/ultimate-design-system-master .kiro/skills/
cp -r skills/resume-ats-beater .kiro/skills/
cp -r skills/coolify-operator .kiro/skills/
cp -r skills/agent-ready-cloudflare .kiro/skills/
cp -r skills/ralph-loop-kiro-specs .kiro/skills/
cp -r skills/loop-architect .kiro/skills/
cp -r skills/humanizar .kiro/skills/
cp -r skills/auth-md .kiro/skills/
```

O formato Agent Skills e universal e funciona com qualquer agente compativel. Veja a [especificacao oficial](https://agentskills.io/specification.md) para detalhes.

## Estrutura do Repositório

```
skills/
├── geo-optimization/
│   ├── SKILL.md
│   └── references/        # princípios orientadores e casos de estudo
├── substack-expert/
│   ├── SKILL.md
│   └── references/        # boas práticas de formatação, exemplo de saída SEO
├── pier-cloud/
│   ├── SKILL.md
│   ├── scripts/           # scripts Python para consumo da API
│   └── references/        # referência da API, guia de troubleshooting
├── resume-ats-beater/
│   ├── SKILL.md
│   └── references/        # templates de diagnóstico, estrutura de saída
├── coolify-operator/
│   ├── SKILL.md
│   └── evals/             # 8 cenários de teste
└── ultimate-design-system-master/
    ├── SKILL.md
    └── references/        # questionário de briefing, 10 arquivos de prompt especializados
├── agent-ready-cloudflare/
│   ├── README.md          # documentação legível com exemplos
│   ├── SKILL.md           # skill principal (docs da API, fluxo operacional, templates de prompt)
│   └── */SKILL.md         # 20 sub-skills de implementação (robots-txt, mcp-server-card, etc.)
├── ralph-loop-kiro-specs/
│   ├── SKILL.md
│   ├── scripts/           # script bash do loop runner
│   └── references/        # template do prompt do agente Ralph
├── loop-architect/
│   ├── SKILL.md           # coach de design de loops (adaptado de Looper por ksimback)
│   ├── scripts/           # compilador e detecção de modelos
│   ├── templates/         # runner Python portável
│   ├── references/        # rubrics (goal, verificação, council, controle)
│   ├── schemas/           # JSON schema do loop.yaml
│   └── examples/          # exemplo ai-workflow-mapping
├── humanizar/
│   ├── SKILL.md
│   └── references/        # 55+ padrões de IA específicos do português brasileiro (6 arquivos)
├── auth-md/
│   ├── SKILL.md
│   └── references/        # template do protocolo, regras de validação, schema de metadata, exemplo, guia de implementação
│   ├── SKILL.md
│   └── references/        # 6 módulos de verificação de conformidade (política de privacidade, cookies, minimização, transferências, direitos, scripts)
```

## Autor

Criado por [ft.ia.br](https://ft.ia.br)

## References

- [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) — Framework de categorias de skills da Anthropic (9 tipos)
- [Best practices for skill creators](https://agentskills.io/skill-creation/best-practices) — Guia de escrita da spec Agent Skills
- [Evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills) — Iteração com evals, test cases e benchmarks

## Licenca

Apache 2.0 — veja [LICENSE](LICENSE) para detalhes — **exceto quando o diretório de uma skill contém seu próprio arquivo LICENSE, que passa a reger aquela skill.**

⚠️ **Exceção:** [`skills/revenue-centric-design/`](skills/revenue-centric-design/LICENSE) é **source-available, não open-source**. As ideias são propriedade intelectual do Richard ([@richardrx](https://x.com/richardrx)), usadas com permissão, e **não podem ser usadas em produtos de apostas, cassino ou gambling**. Essa restrição sobrevive a qualquer cópia ou derivado e não é dispensada pela licença Apache 2.0 deste repositório.
