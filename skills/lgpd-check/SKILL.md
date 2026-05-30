---
name: "LGPD Check"
version: "1.0.0"
description: "Audita websites para conformidade com a LGPD brasileira (Lei 13.709/2018). Valida política de privacidade, consentimento de cookies, minimização de dados, transferência internacional, direitos do titular, scripts de terceiros e analytics. Gera relatório com score de conformidade e correções prioritárias."
author: "ft.ia.br"
license: "Apache-2.0"
triggers:
  - "auditar LGPD"
  - "verificar LGPD"
  - "compliance LGPD"
  - "lgpd check"
  - "validar privacidade"
  - "auditoria de privacidade"
  - "site está em conformidade com a LGPD"
  - "checar LGPD"
  - "verificar proteção de dados"
references:
  - references/politica-de-privacidade.md
  - references/consentimento-cookies.md
  - references/minimizacao-dados.md
  - references/transferencia-internacional.md
  - references/direitos-do-titular.md
  - references/scripts-terceiros-analytics.md
---

# LGPD Check

Audita websites para conformidade total com a Lei Geral de Proteção de Dados (Lei 13.709/2018), incluindo regulamentações da ANPD vigentes em 2026.

## Parâmetros

| Parâmetro | Padrão | Descrição |
|---|---|---|
| `url` | (obrigatório) | URL do site a ser auditado |
| `escopo` | `completo` | `completo`, `politica`, `cookies`, `direitos`, `transferencias`, `scripts` |
| `formato_saida` | `relatorio` | `relatorio` (markdown completo), `checklist` (apenas itens), `score` (apenas pontuação) |
| `idioma_site` | `pt-br` | Idioma esperado do site auditado |

## Workflow

### Passo 1 — Coletar informações do site

Acessar a URL fornecida e identificar:

- Presença e localização da política de privacidade
- Banner/modal de consentimento de cookies
- Formulários que coletam dados pessoais
- Scripts de terceiros carregados
- Headers HTTP relevantes (CSP, Referrer-Policy)
- Presença de DPO/Encarregado identificado
- Sinal GPC (Global Privacy Control) sendo respeitado

### Passo 2 — Executar checks por categoria

Aplicar os checks de cada arquivo de referência:

1. **Política de Privacidade** → `references/politica-de-privacidade.md`
2. **Consentimento de Cookies** → `references/consentimento-cookies.md`
3. **Minimização de Dados** → `references/minimizacao-dados.md`
4. **Transferência Internacional** → `references/transferencia-internacional.md`
5. **Direitos do Titular** → `references/direitos-do-titular.md`
6. **Scripts de Terceiros e Analytics** → `references/scripts-terceiros-analytics.md`

### Passo 3 — Calcular score de conformidade

Classificar cada item como:

- ✅ **Conforme** — requisito atendido
- ⚠️ **Parcial** — implementado com falhas ou incompleto
- ❌ **Não conforme** — ausente ou incorreto
- ℹ️ **Não aplicável** — não se aplica ao contexto do site

Calcular score: `(conformes + parciais×0.5) / total_aplicáveis × 100`

### Passo 4 — Gerar relatório

Produzir relatório em markdown com:

```markdown
# Relatório de Conformidade LGPD
**Site:** [url]
**Data:** [data da auditoria]
**Score geral:** [X]%

## Resumo executivo
[2-3 frases sobre o estado geral de conformidade]

## Classificação de risco
- 🟢 90-100%: Conformidade alta
- 🟡 70-89%: Conformidade parcial — correções recomendadas
- 🟠 50-69%: Conformidade baixa — correções urgentes
- 🔴 0-49%: Não conforme — risco de sanção ANPD

## Resultados por categoria
### 1. Política de Privacidade [X/Y]
### 2. Consentimento de Cookies [X/Y]
### 3. Minimização de Dados [X/Y]
### 4. Transferência Internacional [X/Y]
### 5. Direitos do Titular [X/Y]
### 6. Scripts de Terceiros e Analytics [X/Y]

## Itens críticos (correção imediata)
[lista priorizada]

## Recomendações de melhoria
[lista com esforço estimado: baixo/médio/alto]

## Referências legais
[artigos da LGPD e resoluções ANPD aplicáveis]
```

## Contexto regulatório (2026)

- **ANPD** tornou-se agência reguladora independente (Resolução 33/2026)
- **Decisão de adequação mútua Brasil-UE** (Resolução 32/2026, jan 2026)
- **SCCs obrigatórias** para transferências fora do eixo Brasil-UE (Resolução 19/2024, vigente desde ago 2025)
- **Prioridades de fiscalização 2026–2027**: direitos do titular, proteção de crianças/adolescentes (ECA Digital), IA e tecnologias emergentes, publicidade direcionada
- **Sanções**: multa até 2% da receita no Brasil (teto R$50M por infração), suspensão de processamento, bloqueio de dados, publicização da infração

## Quality Checklist

Antes de entregar o relatório, verificar:

- [ ] Todos os 6 módulos de check foram executados
- [ ] Score calculado corretamente com base nos itens aplicáveis
- [ ] Itens críticos identificados e priorizados
- [ ] Referências legais citadas com artigos específicos da LGPD
- [ ] Recomendações incluem esforço estimado de implementação
- [ ] Relatório está inteiramente em português
- [ ] Nenhuma informação sensível do site foi exposta no relatório
