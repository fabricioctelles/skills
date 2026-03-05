---
name: resume-ats-beater
description: Este skill deve ser usado para reescrever currículos com foco em compatibilidade ATS e impacto para recrutadores. Acionar em pedidos de otimização de currículo, melhoria para ATS, reescrita profissional do CV, adaptação para vaga-alvo, auditoria de compatibilidade ATS ou aumento de taxa de entrevista.
metadata:
  author: ft.ia.br
  version: "1.2"
  date: 2026-03-05
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
  language: pt-BR
---

# Resume ATS Beater

## Contexto ATS no Brasil

Aplicar as orientações deste skill considerando o cenário brasileiro de ATS (Gupy, Vagas.com, PandaPé e Sólides), no qual o ranqueamento combina parsing do currículo, aderência semântica à vaga, requisitos eliminatórios, histórico de progressão e desempenho em testes da plataforma. Tratar o processo como otimização de score e ordenação, não como aprovação binária.

Aplicar avaliação com perspectiva dupla: especialista técnico em ATS e recrutador experiente no `cargo_alvo` e `industria_alvo`. Conciliar as duas lentes para maximizar parse/ranqueamento ATS e impacto na leitura humana de 6 segundos.

## Modos de execução

Executar em um dos modos abaixo. Quando não especificado, adotar `modo_completo` como padrão e informar o usuário.

1. `modo_diagnostico`: analisar currículo atual e apontar melhorias ATS sem reescrita integral.
2. `modo_reescrita`: reescrever currículo completo sem entregar diagnóstico detalhado.
3. `modo_completo`: executar diagnóstico estruturado e, em seguida, entregar reescrita final.

## Parâmetros de entrada

### Obrigatórios

Coletar antes de qualquer outra ação. Se `curriculo_atual` estiver ausente, solicitá-lo imediatamente e não prosseguir.

- `curriculo_atual` (texto ou arquivo): conteúdo completo do currículo atual.
- `cargo_alvo` (texto): cargo principal buscado.
- `industria_alvo` (texto): segmento/mercado alvo.
- `nivel_senioridade_alvo` (texto): júnior, pleno, sênior, liderança etc.
- `idioma_curriculo` (texto): idioma final do currículo.
- `requisitos_eliminatorios` (lista): critérios mandatórios da vaga (ex.: inglês fluente, cidade, certificação, disponibilidade).
- `modo_execucao` (texto): `modo_diagnostico`, `modo_reescrita` ou `modo_completo`.

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

### Restrições de segurança factual

- Não inventar conquistas, números, certificações ou responsabilidades.
- Solicitar complementos quando faltarem métricas relevantes.
- Preservar todos os cargos e formações existentes; alterar apenas quando correção factual for solicitada pelo usuário.

## Workflow operacional

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

### Etapa 6 — Entregar saída final

Estruturar a entrega conforme `references/template-saida.md`, respeitando o escopo do `modo_execucao`:

- **Todos os modos**: itens 1–5 (currículo reescrito, resumo de melhorias, palavras-chave, checklist eliminatórios, riscos de ranking).
- **`modo_diagnostico` / `modo_completo`**: adicionar diagnóstico padrão (eixos I–V).
- **Qualquer modo com vaga definida**: adicionar diagnóstico avançado (PARTES A, B e C).

## Checklist de qualidade

Verificar antes de entregar:

- [ ] Resumo profissional objetivo, específico e alinhado ao `cargo_alvo`.
- [ ] Experiências com foco em resultado e impacto; métricas incluídas quando disponíveis.
- [ ] Nenhuma invenção factual; fatos preservados do currículo original.
- [ ] Estrutura ATS-safe: coluna única, cabeçalhos padrão, sem elementos gráficos.
- [ ] Alinhamento explícito com cargo, indústria e senioridade alvo.
- [ ] Requisitos eliminatórios mapeados e confrontados com status claro.
- [ ] Datas por extenso, coerentes e sem lacunas inexplicadas.
- [ ] Consistência com LinkedIn validada quando dados fornecidos.
- [ ] Equilíbrio entre ranqueamento ATS e poder de convencimento em leitura humana rápida.
