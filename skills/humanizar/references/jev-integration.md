# Integração com TypeSafe Jev

Documentação de como a skill `humanizar` detecta e usa Jev para avaliação calibrada.

## O que é o Jev

Jev é o modelo flagship da TypeSafe AI — o primeiro **System One Model**. Diferente de LLMs que geram texto, o Jev retorna decisões tipadas com probabilidades calibradas.

**Características:**
- Não gera texto — apenas classifica, pontua e decide
- Probabilidades calibradas (quando diz 70%, é 70% mesmo)
- Latência: 70-500ms para dezenas de perguntas paralelas
- Custo: $0.042/M tokens de entrada, output grátis
- ~50-100x mais barato que avaliação via GPT-4

## Por que usar Jev nos passos de avaliação

| Aspecto | Avaliação LLM | Avaliação Jev |
|---------|---------------|---------------|
| Consistência | Varia entre chamadas | Determinístico |
| Calibração | P(70%) ≠ 70% real | P(70%) = 70% real |
| Custo | ~$0.01-0.05/avaliação | ~$0.0001-0.0002/avaliação |
| Latência | 1-5s | 70-500ms |
| Output | Texto (precisa parsing) | Estruturado nativo |

**Jev é ideal para diagnóstico, verificação e scoring. O LLM continua fazendo a reescrita.**

---

## Protocolo de Descoberta

A skill **não assume** que Jev está disponível. Ela segue um protocolo de descoberta para detectar o que o harness oferece.

### Ordem de Prioridade

```
1. MCP Tool `jev_eval` já configurado no harness
   ↓ (não encontrado)
2. Modelo `typesafe/jev-latest` via OpenRouter
   ↓ (não disponível)
3. Modelo `jev-latest` em slot auxiliar (Hermes, Devin)
   ↓ (não configurado)
4. Fallback: avaliação inline via LLM atual do harness
```

### Como Detectar

#### Passo 1: Verificar MCP Tools

```
Pergunte ao harness: "Quais MCP tools estão disponíveis?"

Se existir tool com nome contendo "jev" ou "typesafe":
  → Usar essa tool para avaliação
  → Pular para execução
```

#### Passo 2: Verificar OpenRouter

```
Se o harness usa OpenRouter como provider:
  → Verificar se `typesafe/jev-latest` está no catálogo
  → Se sim, solicitar esse modelo para chamadas de avaliação
```

#### Passo 3: Verificar Slots Auxiliares (Hermes, Devin)

```
Em Hermes Agent:
  → Verificar se slot `approval` está configurado com Jev
  → Se sim, usar esse slot para avaliação

Em Devin:
  → Verificar se existe subagent profile com model: jev-latest
  → Se sim, delegar avaliação para esse subagent
```

#### Passo 4: Fallback para LLM

```
Se nenhuma opção Jev disponível:
  → Executar avaliação inline usando o LLM atual
  → Usar os mesmos critérios, mas via prompt engineering
```

---

## Instruções por Harness

### Claude Code

```markdown
## Descoberta de Jev

1. Verificar MCP: execute `mcp list` ou consulte .claude/mcp.json
2. Se `jev-eval` MCP server configurado → usar tool `jev_avaliar`
3. Se não → avaliação inline via Claude
```

### Cursor

```markdown
## Descoberta de Jev

1. Verificar se OpenRouter está configurado como provider
2. Se sim, solicitar modelo `typesafe/jev-latest` para avaliação
3. Se não → avaliação inline via modelo atual
```

### Devin

```markdown
## Descoberta de Jev

1. Verificar custom subagent profiles em agents/
2. Se existir profile com `model: typesafe/jev-latest`:
   → Delegar avaliação: "avalie usando subagent jev-eval"
3. Se não → avaliação inline
```

### Hermes Agent

```markdown
## Descoberta de Jev

1. Verificar config.yaml → auxiliary.approval
2. Se configurado com `model: typesafe/jev-latest`:
   → Avaliação usará slot approval automaticamente
3. Se não → avaliação inline via modelo principal
```

### Kiro / Copilot / Cline / Aider

```markdown
## Descoberta de Jev

1. Verificar MCP servers configurados
2. Verificar se provider suporta modelo Jev
3. Fallback → avaliação inline
```

---

## Formato das Perguntas Jev

Quando Jev está disponível, usar o arquivo `scripts/jev_questions.json` que contém:

### Diagnóstico (52 perguntas Noul)

Cada padrão de IA mapeado para pergunta binária (P(sim) entre 0-1):

| Categoria | Qtd | Exemplo |
|-----------|-----|---------|
| Composição | 9 | "O texto anuncia o que vai dizer, diz, e depois resume?" |
| Tom | 14 | "O texto usa elogios genéricos como 'Ótima pergunta!'?" |
| Linguagem | 9 | "O texto abusa de vocabulário pomposo típico de IA?" |
| Conteúdo | 7 | "O texto transforma fatos mundanos em revolução?" |
| Estilo | 10 | "O texto usa travessão excessivamente como aparte?" |
| PT-BR | 8 | "O texto usa gerundismo corporativo?" |

### Verificação (4 perguntas Noul)

| Verificação | Crítico | Pergunta |
|-------------|---------|----------|
| TRAVA FACTUAL | ✓ | "Algum fato foi alterado, adicionado ou removido?" |
| Argumento | ✓ | "O argumento e posição do autor foram preservados?" |
| Modalidade | | "A modalidade foi preservada?" |
| Primeira pessoa | | "Opinião ou primeira pessoa foram adicionados?" |

### Avaliação (4 perguntas Score)

| Dimensão | Peso | Níveis |
|----------|------|--------|
| Remoção de padrões | 35% | 5 níveis (0-20 a 81-100) |
| Naturalidade | 30% | 5 níveis |
| Consistência de voz | 20% | 5 níveis |
| Legibilidade | 15% | 5 níveis |

---

## Estrutura de Request/Response Jev

### Request

```json
{
  "state": {
    "texto_fonte": "O texto original...",
    "texto_reescrito": "A candidata..."
  },
  "model": "jev-latest",
  "questions": {
    "composicao_resumos_fractais": {
      "type": "noul",
      "instructions": "O texto anuncia o que vai dizer, diz, e depois resume?",
      "labels": {
        "yes": "Contém resumos fractais",
        "no": "Fluxo direto"
      }
    },
    "score_naturalidade": {
      "type": "score",
      "instructions": "O texto_reescrito soa natural?",
      "levels": ["Muito artificial (0-20)", "...", "Muito natural (81-100)"]
    }
  }
}
```

### Response

```json
{
  "answers": {
    "composicao_resumos_fractais": {
      "type": "noul",
      "noul": 0.23
    },
    "score_naturalidade": {
      "type": "score",
      "score": 3.2,
      "probabilities": {"0": 0.02, "1": 0.05, "2": 0.15, "3": 0.48, "4": 0.30},
      "confidence": 0.78
    }
  },
  "usage": {"input_tokens": 1523, "output_tokens": 0}
}
```

---

## Interpretação dos Resultados

### Noul (Diagnóstico/Verificação)

- **P(sim) ≥ 0.5**: Padrão detectado / Violação detectada
- **P(sim) < 0.5**: Padrão ausente / Verificação passou

### Score (Avaliação)

- **Pontuação final** = Σ(dimensão × peso)
- **Convergiu**: pontuação ≥ limiar (default: 80)

### Decisões

| Resultado | Ação |
|-----------|------|
| TRAVA FACTUAL violada | Descartar candidata, retornar texto_fonte |
| Argumento alterado | Descartar candidata |
| Pontuação < limiar | Iterar ou retornar melhor_resultado |
| Pontuação ≥ limiar | Convergiu, retornar candidata |

---

## Arquivos da Integração

| Arquivo | Descrição |
|---------|-----------|
| `scripts/jev_questions.json` | 56 perguntas tipadas (Noul + Score) |
| `references/jev-integration.md` | Este documento |

O arquivo `jev_questions.json` contém todas as perguntas no formato esperado pela API Jev. Harnesses que têm acesso ao Jev (via MCP, OpenRouter ou slots) podem usar esse arquivo diretamente para construir requests.

---

## Referências

- [TypeSafe AI Docs](https://docs.typesafe.ai)
- [Jev API Reference](https://docs.typesafe.ai/api)
- [OpenRouter - Jev](https://openrouter.ai/typesafe/jev-latest)
- `scripts/jev_questions.json` - Perguntas tipadas
- `scripts/jev_eval.py` - Script de avaliação
