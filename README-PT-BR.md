# 🧠 Agent Skills by ft.ia.br

Colecao de [Agent Skills](https://agentskills.io) para agentes de IA (Kiro, Cursor, Windsurf, Claude Code e outros). Cada skill e um modulo reutilizavel que ensina o agente a executar tarefas complexas com contexto, estrutura e boas praticas.

Agent Skills sao um formato aberto e leve para estender as capacidades de agentes de IA com conhecimento especializado e workflows. Cada skill e uma pasta com um arquivo `SKILL.md` contendo metadados e instrucoes que os agentes carregam sob demanda via progressive disclosure. Saiba mais em [agentskills.io](https://agentskills.io/what-are-skills.md).

## Skills Disponíveis

### 🏆 Premium Proposal Builder
Cria e estrutura propostas premium, slide decks e sites scrolláveis otimizados para decisão de compra. Gera prompts eficazes para Lovable, Gamma, Pitch, Relume e ferramentas similares.

**Quando usar:** criar proposta comercial, melhorar pitch, gerar prompts para ferramentas de design, adaptar estrutura para diferentes indústrias (agências, SaaS, enterprise).

📄 [Ver documentação completa](skills/premium-proposal-builder/SKILL.md)

---

### 🔍 GEO Optimization (Generative Engine Optimization)
Otimiza conteúdo digital e estratégias de marketing para Generative Engines (LLMs, AI agents) visando maximizar citações em respostas de IA.

**Quando usar:** melhorar visibilidade em respostas de IA (ChatGPT, Perplexity, Google AI Overview), medir citation rate, alinhar terminologia para LLMs, auditar páginas para IA, criar roundups e FAQs otimizadas.

📄 [Ver documentação completa](skills/geo-optimization/SKILL.md)

---

### 📰 Substack Expert
Especialista na plataforma Substack. Orienta formatação de posts, otimização SEO (títulos, slugs, meta descriptions), estratégias nativas de engajamento (Notes, Chat) e conversão para assinaturas pagas.

**Quando usar:** formatar e otimizar posts no Substack, melhorar SEO de newsletters (títulos, slugs, meta descriptions), crescer audiência com Notes e recomendações, converter leitores gratuitos em assinantes pagos, personalizar homepage e emails de boas-vindas.

📄 [Ver documentação completa](skills/substack-expert/SKILL.md)

---

### ☁️ Pier Cloud API
Guia completo para consumir a API Pier Cloud (Lighthouse) com autenticação, gerenciamento de contextos, workspaces e visualizações de dados.

**Quando usar:** autenticar na Pier Cloud, listar contextos disponíveis (AWS, etc), gerenciar workspaces, acessar visualizações de análise de custos, executar scripts de FinOps.

📄 [Ver documentação completa](skills/pier-cloud/SKILL.md)

---

### 🎨 Ultimate Design System Master
Gera entregáveis de design no nível Apple/Pentagram/frog/Vercel/Figma usando 10 prompts especializados com role-play. Cobre Design Systems, Brand Identity, UI/UX Patterns, Marketing Assets, Figma Specs, Design Critique, Trend Analysis, Accessibility Audit, Design-to-Code e Apresentações Executivas.

**Quando usar:** criar design system, construir identidade de marca, gerar padrões UI/UX, produzir assets de marketing, escrever specs para Figma, obter crítica de design, analisar tendências de design, rodar auditoria de acessibilidade, traduzir design para código, criar decks de apresentação.

📄 [Ver documentação completa](skills/ultimate-design-system-master/SKILL.md)

---

### 🗂️ Front-End Checklist
Uma lista exaustiva de todos os elementos que você precisa ter ou testar antes de lançar seu site ou página HTML em produção. Inspirado no [Front-End-Checklist by thedaviddias](https://github.com/thedaviddias/Front-End-Checklist).

**Quando usar:** revisar código antes de ir para produção, validar acessibilidade, SEO, performance e garantir as melhores práticas de front-end.

📄 [Ver documentação completa](skills/front-end-checklist/SKILL.md)

---

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

# Exemplo para Claude Code
cp -r skills/premium-proposal-builder .claude/skills/
cp -r skills/geo-optimization .claude/skills/
cp -r skills/substack-expert .claude/skills/
cp -r skills/pier-cloud .claude/skills/
cp -r skills/ultimate-design-system-master .claude/skills/
cp -r skills/front-end-checklist .claude/skills/

# Exemplo para Kiro
cp -r skills/premium-proposal-builder .kiro/skills/
cp -r skills/geo-optimization .kiro/skills/
cp -r skills/substack-expert .kiro/skills/
cp -r skills/pier-cloud .kiro/skills/
cp -r skills/ultimate-design-system-master .kiro/skills/
cp -r skills/front-end-checklist .kiro/skills/
```

O formato Agent Skills e universal e funciona com qualquer agente compativel. Veja a [especificacao oficial](https://agentskills.io/specification.md) para detalhes.

## Estrutura do Repositório

```
skills/
├── premium-proposal-builder/
│   └── SKILL.md
├── geo-optimization/
│   └── SKILL.md
├── substack-expert/
│   └── SKILL.md
├── pier-cloud/
│   └── SKILL.md
├── front-end-checklist/
│   ├── SKILL.md
│   └── references/        # design, head, performance checklists
└── ultimate-design-system-master/
    ├── SKILL.md
    └── references/        # 10 arquivos de prompt especializados
```

## Autor

Criado por [ft.ia.br](https://ft.ia.br)

## Licenca

Apache 2.0 — veja [LICENSE](LICENSE) para detalhes.
