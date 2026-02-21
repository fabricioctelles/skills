# 🧠 Agent Skills by ft.ia.br

Coleção de skills para agentes de IA (Kiro, Cursor, Windsurf, Claude Code e outros). Cada skill é um módulo reutilizável que ensina o agente a executar tarefas complexas com contexto, estrutura e boas práticas.

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

## Instalacao

### Via [Skills.sh](https://skills.sh/docs)

```bash
npx skills add fabricioctelles/skills
```

Ou instale uma skill especifica:

```bash
npx skills add fabricioctelles/skills@premium-proposal-builder
npx skills add fabricioctelles/skills@geo-optimization
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

# Exemplo para Claude Code
cp -r skills/premium-proposal-builder .claude/skills/
cp -r skills/geo-optimization .claude/skills/

# Exemplo para Kiro
cp -r skills/premium-proposal-builder .kiro/skills/
cp -r skills/geo-optimization .kiro/skills/
```

Veja a [lista completa de plataformas](https://www.agentskills.in/docs/getting-started) com todos os 42+ agentes suportados e seus diretorios.

## Estrutura do Repositório

```
skills/
├── premium-proposal-builder/
│   └── SKILL.md
└── geo-optimization/
    └── SKILL.md
```

Cada skill contém um arquivo `SKILL.md` com o frontmatter de configuração e toda a documentação que o agente precisa para executar.

## Autor

Criado por [ft.ia.br](https://ft.ia.br)

## Licença

MIT
