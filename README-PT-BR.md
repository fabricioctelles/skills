# 🧠 Agent Skills by ft.ia.br

Colecao de [Agent Skills](https://agentskills.io) para agentes de IA (Kiro, Cursor, Windsurf, Claude Code e outros). Cada skill e um modulo reutilizavel que ensina o agente a executar tarefas complexas com contexto, estrutura e boas praticas.

Agent Skills sao um formato aberto e leve para estender as capacidades de agentes de IA com conhecimento especializado e workflows. Cada skill e uma pasta com um arquivo `SKILL.md` contendo metadados e instrucoes que os agentes carregam sob demanda via progressive disclosure. Saiba mais em [agentskills.io](https://agentskills.io/what-are-skills.md).

## Skills Disponíveis

### 🏆 Premium Proposal Builder
Cria e estrutura propostas premium, slide decks e sites scrolláveis otimizados para decisão de compra. Gera prompts eficazes para Lovable, Gamma, Pitch, Relume e ferramentas similares.

**Quando usar:** criar proposta comercial, melhorar pitch, gerar prompts para ferramentas de design, adaptar estrutura para diferentes indústrias (agências, SaaS, enterprise).

**Melhorias na v1.1 (Mar 2026):**
- Adicionada tabela de Parâmetros com defaults explícitos para tipo de cliente, modo de entrega e ferramenta
- Movidos perfis de formato, templates por tipo de cliente e estrutura de 9 seções para `references/proposal-formats-and-templates.md`
- Premium Design Tips convertido em Checklist de Qualidade acionável
- Linguagem em segunda pessoa corrigida para forma imperativa

📄 [Ver documentação completa](skills/premium-proposal-builder/SKILL.md)

---

### 🔍 GEO Optimization (Generative Engine Optimization)
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

### 📰 Substack Expert
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

### ☁️ Pier Cloud API
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

### 🎨 Ultimate Design System Master
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

### 🗂️ Front-End Checklist
Uma lista exaustiva de todos os elementos que você precisa ter ou testar antes de lançar seu site ou página HTML em produção. Inspirado no [Front-End-Checklist by thedaviddias](https://github.com/thedaviddias/Front-End-Checklist).

**Quando usar:** revisar código antes de ir para produção, validar acessibilidade, SEO, performance e garantir as melhores práticas de front-end.

**Melhorias na v1.1 (Mar 2026):**
- Descrição reescrita no formato de gatilho em terceira pessoa com frases de acionamento concretas
- Adicionada seção de Parâmetros com defaults explícitos para checklist e escopo
- Adicionado Checklist de Qualidade cobrindo itens de alta prioridade, correções acionáveis e separação de bloqueantes vs. não-bloqueantes
- Passos do workflow reestruturados para voz imperativa com fluxo de execução completo
- Adicionada seção de Referências documentando todos os 5 arquivos de referência

📄 [Ver documentação completa](skills/front-end-checklist/SKILL.md)

---

### 🚀 Coolify Operator
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

### 🧠 Coolify Master
Especialista em deploy, operações e troubleshooting no Coolify. Orienta a escolha de build packs, configurações de ambiente e diagnóstico de falhas como No available server ou erro 404.

**Quando usar:** planejar e executar deploys, configurar domínios/SSL/health checks, revisar operações de self-hosting, diagnosticar falhas na plataforma Coolify.

**Melhorias na v1.1:**
- Estrutura de documentação padronizada (Overview, Onboarding, Usage Examples)
- Integrado checklist de qualidade e regras de decisão
- Instruções soltas substituídas por workflows claros

📄 [Ver documentação completa](skills/coolify-master/SKILL.md)

---

### 📄 Resume ATS Beater
Reescreve currículos do zero para compatibilidade ATS e impacto para recrutadores, com workflow adaptado ao contexto de ATS no Brasil (Gupy, Vagas.com, PandaPé, Sólides).

**Quando usar:** otimizar currículo para ATS, adaptar CV para cargo/indústria alvo, fortalecer bullets com resultados mensuráveis, validar requisitos eliminatórios e aderência semântica.

**Melhorias na v1.2 (Mar 2026):**
- Etapas de diagnóstico sobrepostas (Etapas 2+3) mescladas em uma única etapa unificada
- Templates de saída do diagnóstico movidos para 3 novos arquivos: `diagnostico-ats.md`, `diagnostico-avancado.md`, `template-saida.md`
- Adicionado modo padrão explícito (`modo_completo`) quando o modo de execução não é especificado
- Adicionado guardrail: bloquear todo o workflow até que `curriculo_atual` seja fornecido
- Adicionada instrução de skip: `modo_reescrita` ignora a etapa de diagnóstico
- Adicionada nota comportamental para `plataforma_ats_alvo` quando a plataforma é conhecida

📄 [Ver documentação completa](skills/resume-ats-beater/SKILL.md)

---

> **Skills revisadas em março de 2026** seguindo o padrão Anthropic para estrutura e qualidade de Agent Skills.
> Fonte: [Improving Skill Creator: Test, Measure and Refine Agent Skills](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)

## Instalacao

Voce pode instalar estas skills usando qualquer instalador compativel ou manualmente. Abaixo estao as opcoes mais populares.

### Via [Skills.sh](https://skills.sh/docs)

```bash
npx skills add fabricioctelles/skills
```

Ou instale uma skill especifica:

```bash
npx skills add fabricioctelles/skills@premium-proposal-builder
npx skills add fabricioctelles/skills@geo-optimization
npx skills add fabricioctelles/skills@substack-expert
npx skills add fabricioctelles/skills@pier-cloud
npx skills add fabricioctelles/skills@ultimate-design-system-master
npx skills add fabricioctelles/skills@front-end-checklist
npx skills add fabricioctelles/skills@resume-ats-beater
npx skills add fabricioctelles/skills@coolify-operator
npx skills add fabricioctelles/skills@coolify-master
```

### Via [Agent Skills CLI](https://www.agentskills.in/docs)

```bash
npm install -g agent-skills-cli
```

Depois instale as skills:

```bash
skills add fabricioctelles/skills
```

Ou use sem instalar globalmente:

```bash
npx agent-skills-cli install fabricioctelles/skills
```

### Instalacao Manual

1. Clone este repositorio:
```bash
git clone https://github.com/fabricioctelles/skills.git
```

2. Copie a pasta da skill desejada para o diretorio de skills do seu agente:
```bash
# Exemplo para Cursor
cp -r skills/premium-proposal-builder .cursor/skills/
cp -r skills/geo-optimization .cursor/skills/
cp -r skills/substack-expert .cursor/skills/
cp -r skills/pier-cloud .cursor/skills/
cp -r skills/ultimate-design-system-master .cursor/skills/
cp -r skills/front-end-checklist .cursor/skills/
cp -r skills/resume-ats-beater .cursor/skills/
cp -r skills/coolify-operator .cursor/skills/
cp -r skills/coolify-master .cursor/skills/

# Exemplo para Claude Code
cp -r skills/premium-proposal-builder .claude/skills/
cp -r skills/geo-optimization .claude/skills/
cp -r skills/substack-expert .claude/skills/
cp -r skills/pier-cloud .claude/skills/
cp -r skills/ultimate-design-system-master .claude/skills/
cp -r skills/front-end-checklist .claude/skills/
cp -r skills/resume-ats-beater .claude/skills/
cp -r skills/coolify-operator .claude/skills/
cp -r skills/coolify-master .claude/skills/

# Exemplo para Kiro
cp -r skills/premium-proposal-builder .kiro/skills/
cp -r skills/geo-optimization .kiro/skills/
cp -r skills/substack-expert .kiro/skills/
cp -r skills/pier-cloud .kiro/skills/
cp -r skills/ultimate-design-system-master .kiro/skills/
cp -r skills/front-end-checklist .kiro/skills/
cp -r skills/resume-ats-beater .kiro/skills/
cp -r skills/coolify-operator .kiro/skills/
cp -r skills/coolify-master .kiro/skills/
```

O formato Agent Skills e universal e funciona com qualquer agente compativel. Veja a [especificacao oficial](https://agentskills.io/specification.md) para detalhes.

## Estrutura do Repositório

```
skills/
├── premium-proposal-builder/
│   ├── SKILL.md
│   └── references/        # perfis de formato, tipos de cliente, templates de proposta
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
├── front-end-checklist/
│   ├── SKILL.md
│   └── references/        # checklists de design, head e performance
├── resume-ats-beater/
│   ├── SKILL.md
│   └── references/        # templates de diagnóstico, estrutura de saída
├── coolify-operator/
│   ├── SKILL.md
│   └── evals/             # 8 cenários de teste
├── coolify-master/
│   ├── SKILL.md
│   └── references/        # coolify concepts, deploy best practices, troubleshooting playbooks
└── ultimate-design-system-master/
    ├── SKILL.md
    └── references/        # questionário de briefing, 10 arquivos de prompt especializados
```

## Autor

Criado por [ft.ia.br](https://ft.ia.br)

## Licenca

Apache 2.0 — veja [LICENSE](LICENSE) para detalhes.
