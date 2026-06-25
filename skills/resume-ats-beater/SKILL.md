---
name: resume-ats-beater
description: Este skill deve ser usado para reescrever currículos com foco em compatibilidade ATS e impacto para recrutadores, e/ou auditar perfis LinkedIn para maximizar visibilidade e conversão profissional. Acionar em pedidos de otimização de currículo, melhoria para ATS, reescrita profissional do CV, adaptação para vaga-alvo, auditoria de compatibilidade ATS, aumento de taxa de entrevista, auditoria de perfil LinkedIn, otimização de headline/about/experiências LinkedIn, análise de SSI, ou alinhamento CV+LinkedIn.
metadata:
  author: ft.ia.br
  version: "2.0"
  date: 2026-06-25
  repository: https://github.com/fabriciotelles/skills
  license: Apache 2.0
  language: pt-BR
---

# Resume ATS Beater + LinkedIn Optimizer

## Contexto ATS no Brasil

Aplicar as orientações deste skill considerando o cenário brasileiro de ATS (Gupy, Vagas.com, PandaPé e Sólides), no qual o ranqueamento combina parsing do currículo, aderência semântica à vaga, requisitos eliminatórios, histórico de progressão e desempenho em testes da plataforma. Tratar o processo como otimização de score e ordenação, não como aprovação binária.

Aplicar avaliação com perspectiva dupla: especialista técnico em ATS e recrutador experiente no `cargo_alvo` e `industria_alvo`. Conciliar as duas lentes para maximizar parse/ranqueamento ATS e impacto na leitura humana de 6 segundos.

## Modos de execução

Executar em um dos modos abaixo. Quando não especificado, adotar `modo_completo` como padrão e informar o usuário.

1. `modo_diagnostico`: analisar currículo atual e apontar melhorias ATS sem reescrita integral.
2. `modo_reescrita`: reescrever currículo completo sem entregar diagnóstico detalhado.
3. `modo_completo`: executar diagnóstico estruturado e, em seguida, entregar reescrita final.
4. `modo_linkedin`: auditoria completa do perfil LinkedIn com score, findings, fix prompts e mega-prompt de reescrita.
5. `modo_unificado`: executa `modo_completo` (CV) + `modo_linkedin` em sequência, garantindo consistência entre ambos.

## Parâmetros de entrada

### Obrigatórios

Coletar antes de qualquer outra ação. Se `curriculo_atual` estiver ausente em modos CV, solicitá-lo imediatamente e não prosseguir.

- `curriculo_atual` (texto ou arquivo): conteúdo completo do currículo atual. Obrigatório em modos CV (diagnostico, reescrita, completo, unificado).
- `cargo_alvo` (texto): cargo principal buscado.
- `industria_alvo` (texto): segmento/mercado alvo.
- `nivel_senioridade_alvo` (texto): júnior, pleno, sênior, liderança etc.
- `idioma_curriculo` (texto): idioma final do currículo.
- `requisitos_eliminatorios` (lista): critérios mandatórios da vaga (ex.: inglês fluente, cidade, certificação, disponibilidade).
- `modo_execucao` (texto): `modo_diagnostico`, `modo_reescrita`, `modo_completo`, `modo_linkedin` ou `modo_unificado`.

### Obrigatórios para modo LinkedIn / unificado

- `perfil_linkedin` (texto ou URL): conteúdo do perfil LinkedIn (headline, about, experiências, skills, featured, configurações) ou URL para análise.

### Recomendados

- `descricao_vaga` (texto): descrição da vaga alvo para extração de palavras-chave.
- `especificacao_vaga_completa` (texto): vaga completa (requisitos, responsabilidades, habilidades, empresa, benefícios e contexto).
- `metricas_por_experiencia` (lista): resultados por cargo (%, R$, tempo, volume, NPS, SLA etc.).
- `localizacao_alvo` (texto): país/região/cidade para adaptar vocabulário e contexto.
- `skills_prioritarias` (lista): competências estratégicas a enfatizar.
- `plataforma_ats_alvo` (texto): Gupy, Vagas.com, PandaPé, Sólides ou "não informado". Quando informada, priorizar vocabulário e critérios específicos da plataforma.
- `historico_linkedin` (objeto): datas/cargos/empresas para checagem de consistência com currículo.
- `detalhes_educacao` (objeto): GPA/CR, honras, certificações, projetos acadêmicos.
- `status_testes_plataforma` (objeto): testes exigidos e resultado atual (lógica, português, fit cultural etc.).
- `secoes_prioritarias_cv` (lista): seções que exigem otimização imediata.
- `ssi_scores` (objeto): pontuação SSI do LinkedIn (4 pilares + total). Opcional; quando fornecido, enriquece diagnóstico.
- `mercado_alvo` (texto): `brasil`, `gringa` ou `ambos`. Afeta idioma, formato de headline e vocabulário.
- `cargo_preset` (texto): preset de cargo para aplicar padrões específicos. Exemplos disponíveis em `references/presets-formatos.md`. O usuário pode definir qualquer cargo — presets são apenas atalhos.

### Restrições de segurança factual

- Não inventar conquistas, números, certificações ou responsabilidades.
- Solicitar complementos quando faltarem métricas relevantes.
- Preservar todos os cargos e formações existentes; alterar apenas quando correção factual for solicitada pelo usuário.
- Para LinkedIn: não fabricar endorsements, recomendações ou métricas de engajamento.

---

## Workflow operacional — CV (modos diagnostico, reescrita, completo)

### Etapa 1 — Validar objetivo e contexto

1. Confirmar `curriculo_atual`; solicitar imediatamente se ausente.
2. Confirmar `cargo_alvo`, `industria_alvo`, `nivel_senioridade_alvo` e `idioma_curriculo`.
3. Solicitar `descricao_vaga` se não fornecida; informar ao usuário que a análise será mais genérica sem ela.
4. Coletar `requisitos_eliminatorios` e sinalizar riscos de eliminação prática.
5. Identificar lacunas críticas de dados, especialmente métricas por experiência.
6. Confirmar `modo_execucao`; adotar `modo_completo` se não especificado.
7. Pausar e coletar dados mínimos antes de avançar.

### Etapa 2 — Diagnosticar currículo e aderência ATS

> Executar esta etapa em `modo_diagnostico` e `modo_completo`. Pular para Etapa 3 em `modo_reescrita`.

1. Mapear estrutura atual (resumo, experiência, educação, skills).
2. Medir aderência semântica com a vaga (competências, termos técnicos e contexto).
3. Identificar hard skills, soft skills e palavras-chave ausentes de alta prioridade.
4. Identificar bullets fracos (tarefa sem impacto), jargões vazios e habilidades obsoletas.
5. Verificar sinais de progressão de carreira e lacunas temporais.
6. Confirmar consistência com `historico_linkedin`, quando fornecido.
7. Aplicar os quatro eixos de análise definidos em `references/diagnostico-ats.md`.
8. Quando `descricao_vaga` ou `especificacao_vaga_completa` disponível, aplicar também o diagnóstico avançado definido em `references/diagnostico-avancado.md`.

### Etapa 3 — Reescrever do zero com padrão ATS

> Executar em `modo_reescrita` e `modo_completo`. Em `modo_diagnostico`, encerrar na Etapa 2.

1. Reconstruir o currículo integralmente; não fazer edição superficial.
2. Manter todos os cargos e entradas de educação existentes.
3. Produzir `Resumo Profissional` em 3–4 linhas com identidade, anos de experiência, forças centrais e proposta de valor.
4. Reescrever cada experiência com 4–6 bullets orientados a resultado.
5. Priorizar verbos de ação e impacto mensurável.
6. Inserir palavras-chave do alvo de forma natural.
7. Escrever datas por extenso (ex.: "Janeiro de 2020 – Dezembro de 2021") para reduzir erro de cálculo de experiência.
8. Manter layout de coluna única e leitura linear.

Formato por experiência:

```
Cargo
Empresa | Local | Datas

• Bullet orientado a impacto
• Bullet orientado a impacto
• Bullet orientado a impacto
• Bullet orientado a impacto
```

### Etapa 4 — Otimizar educação e competências

1. Manter grau, instituição e ano de conclusão.
2. Melhorar clareza e padronização da seção de educação.
3. Incluir honras, cursos relevantes, certificações e projetos apenas quando informados pelo usuário.
4. Organizar competências por categorias (`Técnicas`, `Ferramentas`, `Interpessoais`, `Idiomas`).
5. Remover competências desatualizadas ou desalinhadas com o `cargo_alvo`.

### Etapa 5 — Validar conformidade ATS

1. Usar cabeçalhos padrão: `Resumo Profissional`, `Experiência Profissional`, `Formação Acadêmica`, `Competências`. Evitar títulos criativos.
2. Evitar tabelas, múltiplas colunas, gráficos, caixas de texto, ícones e fotos.
3. Garantir legibilidade linear para parser ATS.
4. Garantir consistência de datas, verbos e densidade de palavras-chave ao longo do documento.
5. Usar termos exatos da vaga e, quando útil, variações com siglas e nomes completos.
6. Confirmar formato de arquivo final: DOCX ou PDF textual, nunca imagem escaneada.

### Etapa 6 — Entregar saída final CV

Estruturar a entrega conforme `references/template-saida.md`, respeitando o escopo do `modo_execucao`:

- **Todos os modos CV**: itens 1–5 (currículo reescrito, resumo de melhorias, palavras-chave, checklist eliminatórios, riscos de ranking).
- **`modo_diagnostico` / `modo_completo`**: adicionar diagnóstico padrão (eixos I–V).
- **Qualquer modo com vaga definida**: adicionar diagnóstico avançado (PARTES A, B e C).

---

## Workflow operacional — LinkedIn (modo_linkedin, modo_unificado)

### Etapa L1 — Coletar perfil e contexto

1. Confirmar `perfil_linkedin` (conteúdo textual ou URL).
2. Confirmar `cargo_alvo`, `industria_alvo`, `nivel_senioridade_alvo`.
3. Identificar `mercado_alvo` (brasil/gringa/ambos) — afeta idioma e formato.
4. Coletar `ssi_scores` se disponível; informar que enriquece a análise mas não é obrigatório.
5. Verificar se há `cargo_preset` aplicável ou definir padrões genéricos.

### Etapa L2 — Auditar por área

Auditar cada área do perfil LinkedIn aplicando regras de severidade. Para cada finding, classificar como:

| Severidade | Penalidade | Significado |
|---|---|---|
| `critical` | -15 pts | Problema grave que prejudica visibilidade ou causa impressão negativa imediata |
| `warning` | -6 pts | Oportunidade perdida significativa |
| `info` | -2 pts | Melhoria incremental recomendada |
| `ok` | 0 pts | Área adequada, sem ação necessária |

**Áreas auditadas:**

1. **Foto e banner**: presença, qualidade profissional, alinhamento com área.
2. **Headline**: formato, keywords, diferenciação — ver formato obrigatório abaixo.
3. **About/Resumo**: estrutura, storytelling, CTA, keywords, comprimento.
4. **Experiências**: bullets com impacto, métricas, verbos de ação, progressão.
5. **Idioma do perfil**: coerência com `mercado_alvo`.
6. **Skills & Endorsements**: quantidade, relevância, ordenação.
7. **Featured/Destaques**: presença, qualidade, atualização.
8. **Configurações de visibilidade**: Open to Work, Creator Mode, URL customizada.
9. **Recomendações**: quantidade, diversidade (recebidas e dadas).
10. **Atividade/Engajamento**: frequência de posts, comentários, artigos.

#### Formato obrigatório de headline

```
Posição | Áreas fortes | Competências-chave (separadas por ·)
```

**Exemplos por área:**

- Marketing: `Head de Growth | Aquisição · CRO · Dados | Google Ads · HubSpot · SQL`
- Finanças: `Controller Sênior | FP&A · Tesouraria · M&A | SAP · Power BI · IFRS`
- Engenharia Civil: `Gerente de Obras | Infraestrutura · Orçamento · Planejamento | MS Project · AutoCAD · BIM`
- Dados: `Data Engineer Sênior | Pipelines · Lakehouse · MLOps | Spark · dbt · Airflow`
- Jurídico: `Advogado Tributarista | Planejamento Fiscal · Contencioso · M&A | Thomson Reuters · SPED`
- Dev: `Staff Engineer | Backend · Plataforma · Observabilidade | Go · K8s · Terraform`

**Regras da headline:**
- Máximo 220 caracteres (limite LinkedIn).
- Sem buzzwords genéricas (ver constantes abaixo).
- Posição deve refletir o cargo almejado, não necessariamente o atual.
- Áreas fortes: 2–3 domínios de especialização.
- Competências-chave: 3–5 termos técnicos/ferramentas separados por `·`.

### Etapa L3 — Calcular score

Score punitivo: inicia em 100 e subtrai penalidades.

```
score_final = 100 - (qtd_critical × 15) - (qtd_warning × 6) - (qtd_info × 2)
```

**Classificação:**

| Faixa | Status |
|---|---|
| 90–100 | Excelente — perfil competitivo |
| 75–89 | Bom — ajustes pontuais |
| 60–74 | Regular — melhorias necessárias |
| 40–59 | Fraco — reescrita recomendada |
| < 40 | Crítico — perfil prejudica candidatura |

### Etapa L4 — Análise SSI (quando `ssi_scores` fornecido)

#### Como auxiliar o usuário a obter o SSI

Quando o usuário não informar `ssi_scores`, instruí-lo com:

> **Para consultar seu SSI:**
> 1. Acesse [linkedin.com/sales/ssi](https://www.linkedin.com/sales/ssi) (precisa estar logado no LinkedIn).
> 2. A página mostra 4 scores (cada um de 0 a 25) e o total:
>    - **Establish your professional brand** (Laranja)
>    - **Find the right people** (Roxo)
>    - **Engage with insights** (Verde)
>    - **Build relationships** (Verde-água)
> 3. Me informe os 4 valores com decimais. Exemplo: `17.42, 10.01, 11.00, 15.60`
>
> Não precisa ter Sales Navigator — o link funciona com qualquer conta LinkedIn.

**Se o usuário não conseguir acessar:** informar que a análise continua sem SSI, mas perde a camada de diagnóstico comportamental (rede, engajamento, relacionamentos). Prosseguir normalmente com as demais etapas.

**Formato aceito para `ssi_scores`:**
- 4 números separados por vírgula na ordem: marca profissional, encontrar pessoas, engajar insights, construir relacionamentos
- Ou objeto com as 4 chaves nomeadas
- Aceitar decimais com ponto ou vírgula (ex: `17.42` ou `17,42`)

---

O Social Selling Index mede 4 pilares (0–25 cada, total 0–100):

| Pilar | Descrição |
|---|---|
| Marca Profissional | Completude do perfil, publicações, engajamento recebido |
| Encontrar Pessoas | Uso de busca, visualização de perfis, conexões estratégicas |
| Engajar com Insights | Compartilhamento, comentários, artigos publicados |
| Construir Relacionamentos | Conexões de decisores, taxa de aceitação, InMail |

**Classificação por pilar:**

| Pontuação | Status | Ação |
|---|---|---|
| 20–25 | Excelente | Manter cadência |
| 15–19 | Bom | Otimizações pontuais |
| 10–14 | Regular | Plano de ação semanal |
| 0–9 | Fraco | Intervenção urgente |

Para cada pilar abaixo de 15, gerar 2–3 tips acionáveis específicos.

### Etapa L5 — Gerar relatório + fix prompts + mega-prompt

**Relatório de auditoria:**
1. Score final com breakdown de penalidades.
2. Findings organizados por severidade (critical primeiro).
3. Para cada finding: área, severidade, problema detectado, impacto.
4. Classificação SSI (quando disponível).

**Fix prompts individuais:**
Para cada finding critical ou warning, gerar um prompt autônomo que o usuário pode usar em qualquer LLM para corrigir aquele item específico. Formato:

```
## Fix: [Área] — [Problema resumido]
Severidade: critical|warning

### Contexto
[O que está errado e por que importa]

### Prompt para correção
"Reescreva minha [seção] do LinkedIn considerando que sou [cargo_alvo] com experiência em [áreas]. 
Meu perfil atual diz: [conteúdo atual].
Reescreva para: [critérios específicos da regra violada]."

### Onde editar no LinkedIn
[Caminho exato: Perfil → Editar → Seção → Campo]
```

**Mega-prompt de reescrita completa:**
Gerar um prompt único e consolidado para reescrever o perfil inteiro de uma vez, incorporando:
- Cargo alvo e mercado
- Formato de headline obrigatório
- Estrutura de about (storytelling + keywords + CTA)
- Padrão de bullets de experiência
- Skills priorizadas
- Idioma adequado ao `mercado_alvo`

### Etapa L6 — Mapa de edição no LinkedIn

Fornecer instruções de navegação para cada correção:

| Seção | Caminho no LinkedIn |
|---|---|
| Foto/Banner | Perfil → ícone de câmera |
| Headline | Perfil → ícone de lápis (intro) → Título |
| About | Perfil → Sobre → ícone de lápis |
| Experiência | Perfil → Experiência → + ou lápis |
| Skills | Perfil → Competências → + ou reordenar |
| Featured | Perfil → Destaques → + |
| URL customizada | Configurações → Visibilidade → Editar perfil público → URL |
| Open to Work | Perfil → botão "Disponível para" |
| Idioma | Perfil → lápis (intro) → "Nome do perfil em outro idioma" |

---

## Workflow — Modo unificado

No `modo_unificado`, executar sequencialmente:

1. Workflow CV completo (Etapas 1–6).
2. Workflow LinkedIn completo (Etapas L1–L6).
3. **Etapa de consistência**: verificar alinhamento entre CV e LinkedIn:
   - Cargos e datas idênticos.
   - Headline LinkedIn coerente com resumo profissional do CV.
   - Keywords presentes em ambos.
   - Sem contradições factuais.
4. Reportar divergências encontradas com sugestão de correção.

---

## Integração com skill `humanizar`

Quando a skill `humanizar` estiver disponível, aplicá-la **após a geração de conteúdo** e **antes da validação final**, com escopo restrito:

### Seções onde rodar `humanizar`
- About / Resumo do LinkedIn
- Resumo Profissional do CV
- Carta de apresentação (se houver)

### Seções onde NÃO rodar `humanizar`
- Headline LinkedIn (formato rígido 3 blocos)
- Bullets de experiência (formato ATS: verbo + métrica + ferramenta + impacto)
- Seção de competências / skills
- Educação e certificações
- Configurações (Open to Work, idioma, URL)

### Fluxo com `humanizar`

1. `resume-ats-beater` gera o conteúdo (reescrita/auditoria)
2. `humanizar` roda nas seções permitidas (preset sugerido: `corporativo-informal` ou `crônica` conforme tom do mercado)
3. `resume-ats-beater` valida pós-humanização:
   - Keywords do cargo-alvo ainda presentes?
   - Métricas/números intactos?
   - Comprimento dentro do range (About: 1000-2000 chars)?
   - Nenhuma informação factual removida?
4. Se validação falhar → restaurar trecho afetado da versão pré-humanização

### Quando NÃO invocar `humanizar`
- `modo_diagnostico` (não há reescrita)
- Quando o usuário pedir explicitamente tom formal/acadêmico
- Textos jurídicos ou regulatórios

---

## Constantes

### Buzzwords rejeitadas (não usar em headline, about ou bullets)

```
proativo, dinâmico, resiliente, apaixonado, entusiasta, inovador, 
criativo, visionário, guru, ninja, rockstar, evangelista, 
pensador estratégico, orientado a resultados (sem dados), 
profissional comprometido, busco novos desafios, em busca de recolocação
```

### Verbos de ação preferidos (usar em bullets de experiência)

```
Liderou, Implementou, Reduziu, Aumentou, Otimizou, Automatizou, 
Negociou, Estruturou, Escalou, Desenvolveu, Migrou, Consolidou, 
Projetou, Integrou, Reestruturou, Capacitou, Mensurou, Viabilizou,
Orquestrou, Acelerou, Recuperou, Transformou, Padronizou
```

### Regex de métricas (validar presença em bullets)

```
\d+%|\d+x|R\$[\d.,]+|US\$[\d.,]+|\d+\s*(pessoas|clientes|usuários|projetos|contratos|unidades|obras|operações)
```

Bullets sem match neste regex em pelo menos 50% das experiências geram warning `métricas_insuficientes`.

---

## Presets de cargo

Presets são atalhos opcionais com padrões de headline, skills priorizadas e vocabulário técnico. Disponíveis em `references/presets-formatos.md`.

O usuário pode definir qualquer cargo — presets apenas aceleram a configuração.

**Exemplos de presets disponíveis:**

| Preset | Área |
|---|---|
| `marketing_growth` | Marketing Digital / Growth |
| `dados_engenharia` | Engenharia de Dados |
| `dados_analytics` | Analytics / BI |
| `financas_controller` | Controladoria / FP&A |
| `financas_tesouraria` | Tesouraria / Cash Management |
| `engcivil_obras` | Gerência de Obras |
| `engcivil_projetos` | Projetos e Orçamento |
| `juridico_tributario` | Direito Tributário |
| `juridico_compliance` | Compliance / LGPD |
| `dev_backend` | Desenvolvimento Backend |
| `dev_fullstack` | Desenvolvimento Full Stack |
| `dev_platform` | Platform / SRE / DevOps |
| `produto_pm` | Product Manager |
| `produto_design` | Product Design / UX |
| `vendas_enterprise` | Vendas Enterprise / Key Account |
| `vendas_sdrbdr` | SDR / BDR |
| `rh_hrbp` | HR Business Partner |
| `rh_ta` | Talent Acquisition |

---

## Checklist de qualidade

Verificar antes de entregar:

### CV
- [ ] Resumo profissional objetivo, específico e alinhado ao `cargo_alvo`.
- [ ] Experiências com foco em resultado e impacto; métricas incluídas quando disponíveis.
- [ ] Nenhuma invenção factual; fatos preservados do currículo original.
- [ ] Estrutura ATS-safe: coluna única, cabeçalhos padrão, sem elementos gráficos.
- [ ] Alinhamento explícito com cargo, indústria e senioridade alvo.
- [ ] Requisitos eliminatórios mapeados e confrontados com status claro.
- [ ] Datas por extenso, coerentes e sem lacunas inexplicadas.
- [ ] Consistência com LinkedIn validada quando dados fornecidos.
- [ ] Equilíbrio entre ranqueamento ATS e poder de convencimento em leitura humana rápida.

### LinkedIn
- [ ] Headline segue formato obrigatório `Posição | Áreas | Competências·`.
- [ ] About com storytelling + keywords + CTA (não muro de texto genérico).
- [ ] Experiências com bullets de impacto (não descrição de cargo).
- [ ] Sem buzzwords rejeitadas em nenhuma seção.
- [ ] Regex de métricas aprovado em ≥50% dos bullets.
- [ ] Score calculado e classificado corretamente.
- [ ] Fix prompts gerados para todo finding critical/warning.
- [ ] Mega-prompt coerente com cargo_alvo e mercado_alvo.
- [ ] Mapa de edição fornecido com caminhos corretos.
- [ ] Idioma do perfil coerente com mercado_alvo.

### Modo unificado (adicional)
- [ ] Cargos e datas idênticos entre CV e LinkedIn.
- [ ] Keywords presentes em ambos os documentos.
- [ ] Sem contradições factuais entre perfil e currículo.
- [ ] Headline LinkedIn coerente com resumo profissional do CV.

---

## Referências

| Arquivo | Conteúdo |
|---|---|
| `references/diagnostico-ats.md` | Eixos de análise ATS (parsing, aderência, eliminatórios, progressão) |
| `references/diagnostico-avancado.md` | Diagnóstico avançado com vaga definida (PARTES A, B, C) |
| `references/template-saida.md` | Template de entrega final do CV |
| `references/auditoria-linkedin.md` | Regras detalhadas de auditoria LinkedIn por área, severidades, exemplos por cargo |
| `references/ssi.md` | Guia SSI: pilares, benchmarks por indústria, tips acionáveis por faixa |
| `references/presets-formatos.md` | Presets de cargo com headline, skills, vocabulário técnico por área |
