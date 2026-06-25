# Auditoria de Perfil LinkedIn — Regras por Área

> Referência para auditoria de perfis LinkedIn de profissionais especializados (qualquer área).
> Não é específico para devs — aplica-se a marketing, produto, dados, design, finanças, operações, etc.

---

## 1. Headline

### Formato obrigatório

```
Posição | Áreas fortes | Ferramentas · Metodologias · Certificações
```

**Exemplos:**

- `Product Manager | Growth & Monetization | Amplitude · SQL · Lean Six Sigma`
- `Data Analyst | BI & Analytics | Power BI · Python · dbt`
- `UX Designer | Mobile & SaaS | Figma · Design Systems · WCAG`

### Regras de auditoria

| Condição | Severidade |
|---|---|
| Headline vazia | critical |
| Fora do padrão 3 blocos (Posição \| Áreas \| Ferramentas) | critical |
| Sem keywords do cargo-alvo | critical |
| Curta < 40 caracteres | warning |
| Contém buzzwords rejeitadas | warning |

### Buzzwords rejeitadas

**EN:** passionate, results-driven, hard-working, team player, self-motivated, guru, ninja, rockstar, wizard, thought leader, synergy, go-getter, detail-oriented, motivated

**PT:** apaixonado, proativo, dinâmico, comprometido, esforçado

---

## 2. Language

### Regras de auditoria

| Condição | Severidade |
|---|---|
| Mercado internacional e English não listado em Languages | critical |
| Perfil escrito em PT para mercado internacional | critical |

### Detecção de idioma

Contar stopwords PT vs EN no conteúdo do perfil:

- **PT:** de, da, do, em, para, com, que, uma, os, as, no, na
- **EN:** the, and, to, of, in, for, with, that, on, is, at, by

Se ratio PT > 60% e mercado-alvo é internacional → critical.

---

## 3. About

### Regras de auditoria

| Condição | Severidade |
|---|---|
| Vazio | critical |
| < 300 caracteres | warning |
| Sem keywords do cargo-alvo | warning |
| Sem métricas quantificáveis | warning |

### Modelo de estrutura

```
1. Abertura: anos de experiência + foco principal
2. Empresa atual: o que faz + escala (equipe, receita, usuários)
3. Áreas de atuação / especialidades
4. Experiência anterior com provas (métricas, resultados)
5. Lista de competências / stack / ferramentas
```

### Tamanho ideal

- Mínimo aceitável: 300 caracteres
- Ideal: 1000–2000 caracteres
- Máximo útil: 2600 caracteres (limite do LinkedIn)

---

## 4. Experiences

### Regras de auditoria

| Condição | Severidade |
|---|---|
| Nenhuma experiência listada | critical |
| Experiência sem bullets descritivos | warning |
| Mais de 5 bullets por experiência | warning |
| Nenhum bullet com métrica quantificada | warning |
| Título atual ≠ cargo-alvo | warning |
| Poucos verbos de ação nos bullets | info |
| Bullet > 320 caracteres | info |

### Formato ideal de bullet

```
Verbo de ação + métrica + ferramentas/metodologia + impacto
```

- ~3 linhas por bullet
- Máximo 5 bullets por experiência
- Pelo menos 1 bullet com número concreto

**Exemplos:**

- `Reduzi churn em 18% implementando modelo preditivo com Python e Amplitude, gerando R$240k/ano em receita retida`
- `Liderei redesign do checkout mobile com Figma e A/B testing, aumentando conversão de 2.1% para 3.4%`
- `Gerenciei portfólio de 12 projetos (R$8M budget) usando Jira e OKRs, entregando 94% no prazo`

---

## 5. Skills

### Regras de auditoria

| Condição | Severidade |
|---|---|
| > 3 skills listadas e nenhuma bate com keywords do cargo | info |

> **Nota:** O PDF exportado do LinkedIn mostra apenas as top 3 skills. Não auditar quantidade total — focar em relevância das primeiras.

### Recomendação

Reordenar skills para que as 3 primeiras sejam exatamente as keywords mais importantes do cargo-alvo.

---

## 6. Education

### Regras de auditoria

| Condição | Severidade |
|---|---|
| Sem formação listada | info |
| Sem certificações relevantes | info |

### Recomendação

Incluir certificações relevantes para a área (ex: PMP, AWS, CFA, Google Analytics, Scrum Master, etc.).

---

## 7. Featured

> **Nota:** Seção Featured não aparece no PDF exportado. Auditoria via dica fixa.

### Recomendação fixa

Ter pelo menos 1 item em Featured:
- Certificação relevante
- Projeto com resultado mensurável
- Artigo/publicação da área
- Case study ou apresentação

---

## 8. Job Preferences

### Regras de auditoria

| Condição | Severidade |
|---|---|
| Open to Work não ativado (ou ativado para todos) | info |
| Start date não configurado como Immediately | info |
| Profile language diferente do idioma do país-alvo | info |

### Recomendação

- Ativar Open to Work como **Recruiters only** (não mostra badge público)
- Start date: **Immediately** (sinaliza disponibilidade)
- Profile language: idioma do mercado-alvo

---

## Cálculo do Score

```
score = 100 - soma_penalidades
```

| Severidade | Penalidade |
|---|---|
| critical | -15 |
| warning | -6 |
| info | -2 |

- Score mínimo: **0** (não vai negativo)
- Score ≥ 80: perfil competitivo
- Score 60–79: precisa ajustes
- Score < 60: requer reescrita significativa

---

## Verbos de Ação Aceitos

### Inglês

led, built, designed, shipped, launched, scaled, reduced, increased, improved, automated, migrated, delivered, owned, drove, created, implemented, optimized, architected, managed

### Português

liderei, construí, criei, reduzi, aumentei, automatizei, entreguei, implementei, otimizei, escalei, desenvolvi

---

## Regex de Métricas

Padrão para detectar quantificação em bullets:

```regex
(\d+[\d.,]*\s?%|\$\s?\d|\bR\$\s?\d|\b\d[\d.,]*\s?(k|m|mi|mil|million|users|clientes|x)\b|\b\d+\b)
```

### Exemplos que matcham

- `18%`, `3.4%`
- `$2M`, `R$240k`
- `500k users`, `12 clientes`
- `3x`, `94`

---

## Mapa de Onde Editar no LinkedIn

| Seção | Caminho no LinkedIn |
|---|---|
| Headline | Perfil → ícone lápis no card principal → Headline |
| About | Perfil → seção "About" → ícone lápis |
| Experience | Perfil → seção "Experience" → + ou lápis na posição |
| Skills | Perfil → seção "Skills" → + Add skill / reordenar |
| Language | Perfil → seção "Languages" → + Add language |
| Education | Perfil → seção "Education" → + ou lápis |
| Featured | Perfil → seção "Featured" → + Add featured |
| Open to Work | Perfil → botão "Open to" → Finding a new job → Recruiters only |
| Profile language | Settings → Account → Site preferences → Language |
| SSI | [linkedin.com/sales/ssi](https://www.linkedin.com/sales/ssi) |

---

## Fix Prompt Individual — Template

Para cada finding gerado pela auditoria, produzir um prompt standalone com a estrutura abaixo:

```markdown
## Fix: [Nome da Seção] — [Descrição curta do problema]

**Onde editar:** [caminho no LinkedIn da tabela acima]

**Contexto:** O objetivo é [cargo-alvo] no mercado [país/região].

**Problema identificado:** [descrição do finding]

**Conteúdo atual:**
> [texto atual do perfil nessa seção, se disponível]

**Regras desta seção:**
- [regras específicas da área auditada]

**Tarefa:**
1. Explique por que isso prejudica o perfil
2. Forneça texto pronto para colar no LinkedIn, seguindo o formato obrigatório

**Texto sugerido:**
> [texto otimizado pronto para copiar e colar]
```

### Exemplo de Fix Prompt gerado

```markdown
## Fix: Headline — Fora do padrão 3 blocos

**Onde editar:** Perfil → ícone lápis no card principal → Headline

**Contexto:** O objetivo é Product Manager no mercado EUA.

**Problema identificado:** Headline atual não segue o formato
`Posição | Áreas | Ferramentas`. Está usando formato livre com buzzwords.

**Conteúdo atual:**
> "Passionate Product Leader driving results"

**Regras desta seção:**
- Formato: `Posição | Áreas fortes | Ferramentas · Metodologias`
- Sem buzzwords (passionate, results-driven, etc.)
- Deve conter keywords do cargo-alvo
- Mínimo 40 caracteres

**Tarefa:**
1. "Passionate" e "driving results" são buzzwords genéricas que não ajudam ATS nem recruiters. O formato 3 blocos permite scanning rápido.
2. Texto pronto:

**Texto sugerido:**
> Product Manager | Growth · Monetization · B2B SaaS | Amplitude · SQL · Mixpanel
```
