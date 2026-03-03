---
name: resume-ats-beater
description: Este skill deve ser usado para reescrever currículos com foco em compatibilidade ATS e impacto para recrutadores. Acionar em pedidos de otimização de currículo, melhoria para ATS, reescrita profissional do CV, adaptação para vaga-alvo ou aumento de taxa de entrevista.
metadata:
  author: ft.ia.br
  version: "1.1"
  date: 2026-03-03
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
  language: pt-BR
---

# Resume ATS Beater

Reescrever currículos do zero para maximizar legibilidade por ATS e atratividade para recrutadores, sem inventar fatos.

## Contexto ATS no Brasil

Aplicar as orientações deste skill considerando o cenário brasileiro de ATS (Gupy, Vagas.com, PandaPé e Sólides), no qual o ranqueamento costuma combinar:
- parsing do currículo;
- aderência semântica à vaga;
- requisitos eliminatórios;
- histórico de progressão;
- desempenho em testes da plataforma (quando aplicável).

Tratar o processo como otimização de score e ordenação, não como aprovação binária.

## Lente de avaliação combinada

Aplicar avaliação com perspectiva dupla:
- especialista técnico em ATS;
- recrutador experiente no `cargo_alvo` e `industria_alvo`.

Conciliar as duas lentes para maximizar:
- parse e ranqueamento ATS;
- impacto na leitura humana de 6 segundos.

## Quando usar

Acionar este skill quando houver pedido de:
- reescrever currículo;
- otimizar currículo para ATS;
- adaptar currículo para vaga, indústria, senioridade ou região;
- melhorar bullets de experiência com foco em impacto.

Acionar também quando houver pedido de:
- auditar compatibilidade ATS do currículo atual;
- identificar lacunas de palavras-chave para cargo-alvo;
- revisar formatação para parsing ATS;
- gerar diagnóstico estruturado antes da reescrita.

Acionar também quando houver pedido de:
- avaliar currículo para leitura rápida de recrutador;
- equilibrar otimização ATS com persuasão humana;
- mapear palavras-chave da vaga para trechos exatos do currículo.

## Modos de execução

Executar em um dos modos abaixo, conforme objetivo da solicitação:

1. `modo_diagnostico`: analisar currículo atual e apontar melhorias ATS sem reescrita integral.
2. `modo_reescrita`: reescrever currículo completo com base no diagnóstico e no alvo.
3. `modo_completo`: executar diagnóstico estruturado e, em seguida, entregar reescrita final.

## Parâmetros de entrada

Coletar estes parâmetros antes de iniciar a reescrita.

### Obrigatórios

- `curriculo_atual` (texto ou arquivo): conteúdo completo do currículo atual.
- `cargo_alvo` (texto): cargo principal buscado.
- `industria_alvo` (texto): segmento/mercado alvo.
- `nivel_senioridade_alvo` (texto): júnior, pleno, sênior, liderança etc.
- `idioma_curriculo` (texto): idioma final do currículo.
- `requisitos_eliminatorios` (lista): critérios mandatórios da vaga (ex.: inglês fluente, cidade, certificação, disponibilidade).
- `modo_execucao` (texto): `modo_diagnostico`, `modo_reescrita` ou `modo_completo`.

### Recomendados

- `localizacao_alvo` (texto): país/região/cidade para adaptar vocabulário e contexto.
- `descricao_vaga` (texto): descrição da vaga alvo para extração de palavras-chave.
- `especificacao_vaga_completa` (texto): vaga completa (requisitos, responsabilidades, habilidades, empresa, benefícios e contexto).
- `metricas_por_experiencia` (lista): resultados por cargo (%, R$, tempo, volume, NPS, SLA etc.).
- `detalhes_educacao` (objeto): GPA/CR, honras, certificações, projetos acadêmicos.
- `skills_prioritarias` (lista): competências estratégicas a enfatizar.
- `plataforma_ats_alvo` (texto): Gupy, Vagas.com, PandaPé, Sólides ou "não informado".
- `historico_linkedin` (objeto): datas/cargos/empresas para checagem de consistência com currículo.
- `status_testes_plataforma` (objeto): testes exigidos e resultado atual (lógica, português, fit cultural etc.).
- `secoes_prioritarias_cv` (lista): seções do currículo que exigem otimização imediata (ex.: resumo, experiência, competências).

### Restrições de segurança factual

- Não inventar conquistas, números, certificações ou responsabilidades.
- Solicitar complementos quando faltarem métricas relevantes.
- Preservar cargos e formações existentes, salvo correção factual solicitada.

## Workflow operacional

### Etapa 1 — Validar objetivo e contexto

1. Confirmar `cargo_alvo`, `industria_alvo`, `nivel_senioridade_alvo` e `idioma_curriculo`.
2. Solicitar `descricao_vaga` se não houver.
3. Coletar `requisitos_eliminatorios` e sinalizar riscos de eliminação prática.
4. Identificar lacunas críticas de dados (principalmente métricas por experiência).
5. Pausar reescrita até coletar dados mínimos necessários.

### Etapa 2 — Diagnosticar aderência ATS-BR

1. Medir aderência semântica inicial com a vaga (competências, termos técnicos e contexto).
2. Mapear hard skills, soft skills e palavras-chave ausentes de alta prioridade.
3. Verificar sinais de progressão de carreira e possíveis lacunas temporais.
4. Confirmar consistência com `historico_linkedin`, quando fornecido.
5. Priorizar correções que elevem ranking em processos com alto volume de candidaturas.

### Etapa 3 — Diagnosticar o currículo atual

1. Mapear estrutura atual (resumo, experiência, educação, skills).
2. Identificar bullets fracos (descrição de tarefa sem impacto).
3. Listar palavras-chave ausentes frente ao alvo.
4. Identificar possíveis redundâncias, jargões vazios e habilidades obsoletas.

Aplicar, no mínimo, os quatro eixos de análise:

1. `Compatibilidade Geral ATS`: classificar como baixa, média ou alta e justificar em uma frase.
2. `Otimização de Palavras-chave`:
  - listar 5–10 palavras-chave ausentes relevantes ao `cargo_alvo`;
  - avaliar densidade (termos subutilizados e sobreutilizados);
  - recomendar posicionamento ideal (resumo, experiências, competências).
3. `Análise de Formatação`:
  - validar formato de arquivo ideal (DOCX ou PDF textual);
  - validar fonte/estilo legível e ausência de elementos que quebram parsing;
  - validar cabeçalhos padrão ATS;
  - validar consistência de bullets e listas.
4. `Clareza e Legibilidade`:
  - identificar jargões e siglas pouco reconhecíveis;
  - fortalecer verbos de ação;
  - sugerir inclusão de resultados quantificáveis;
  - validar consistência de datas e sinalizar lacunas temporais.

Executar também diagnóstico avançado em três partes quando houver `descricao_vaga` ou `especificacao_vaga_completa`:

1. `PARTE A — Otimização ATS`:
  - extrair 20 palavras-chave/frases críticas da vaga e ranquear de 1 a 20 por relevância;
  - mapear em quais seções cada palavra-chave deve aparecer e frequência sugerida;
  - propor 5 trocas terminológicas específicas para elevar aderência semântica;
  - sinalizar problemas de estrutura/formatação que prejudicam parsing.
2. `PARTE B — Engajamento Humano`:
  - pontuar de 1 a 10 a eficácia de leitura em 6 segundos;
  - identificar 3 pontos de subvalorização de resultados;
  - propor 2 formas de adicionar personalidade profissional sem perder objetividade;
  - recomendar hierarquia ideal de informação para o `cargo_alvo`.
3. `PARTE C — Estratégia de Integração`:
  - demonstrar como inserir palavras-chave naturalmente em bullets de conquista;
  - fornecer exemplos específicos de transformação de bullet fraco em bullet forte.

### Etapa 4 — Reescrever do zero com padrão ATS

1. Reconstruir o currículo integralmente; não fazer edição superficial.
2. Manter todos os cargos e entradas de educação existentes.
3. Produzir `Resumo Profissional` em 3–4 linhas com identidade, anos de experiência, forças centrais e proposta de valor.
4. Reescrever cada experiência com 4–6 bullets orientados a resultado.
5. Priorizar verbos de ação e impacto mensurável.
6. Inserir palavras-chave do alvo de forma natural.
7. Escrever datas por extenso para reduzir erro de cálculo de experiência (ex.: "Janeiro de 2020 - Dezembro de 2021").
8. Manter layout de coluna única e leitura linear.

Formato por experiência:

Cargo
Empresa | Local | Datas

• Bullet orientado a impacto
• Bullet orientado a impacto
• Bullet orientado a impacto
• Bullet orientado a impacto

### Etapa 5 — Otimizar educação e competências

1. Manter grau, instituição e ano de conclusão.
2. Melhorar clareza e padronização da seção de educação.
3. Incluir honras, cursos relevantes, certificações e projetos apenas quando informados.
4. Organizar competências por categorias (`Técnicas`, `Ferramentas`, `Interpessoais`, `Idiomas`, etc.).
5. Remover competências desatualizadas ou desalinhadas.

### Etapa 6 — Validar conformidade ATS

1. Usar títulos de seção simples e padronizados.
2. Evitar tabelas, múltiplas colunas, gráficos, caixas de texto, ícones e fotos.
3. Garantir legibilidade linear para parser ATS.
4. Garantir consistência de datas, verbos e densidade de palavras-chave.
5. Garantir uso de termos exatos da vaga e, quando útil, variações com siglas e nomes completos.
6. Reforçar compatibilidade de arquivo final (DOCX ou PDF textual, nunca imagem escaneada).

### Etapa 7 — Entregar saída final

Entregar obrigatoriamente:

1. Currículo completo reescrito e otimizado para ATS.
2. Resumo curto das principais melhorias aplicadas.
3. Lista das palavras-chave relevantes adicionadas.
4. Checklist de aderência aos requisitos eliminatórios da vaga (atende, não atende, pendente de evidência).
5. Riscos de ranking identificados (ex.: ausência de métrica, gap temporal não explicado, termo crítico faltante).

Quando `modo_execucao` incluir diagnóstico (`modo_diagnostico` ou `modo_completo`), entregar também:

6. `I. Avaliação Geral de Compatibilidade ATS`: nível (baixa/média/alta) + síntese.
7. `II. Otimização de Palavras-chave`:
  - `A. Palavras-chave Ausentes`
  - `B. Densidade de Palavras-chave`
  - `C. Posicionamento de Palavras-chave`
8. `III. Análise de Formatação`:
  - `A. Formato de Arquivo`
  - `B. Fonte e Estilo`
  - `C. Títulos de Seção`
  - `D. Listas e Bullets`
9. `IV. Clareza e Legibilidade`:
  - `A. Jargões e Siglas`
  - `B. Verbos de Ação`
  - `C. Resultados Quantificáveis`
  - `D. Datas e Lacunas`
10. `V. Recomendações Adicionais`: melhorias práticas de parsing (ex.: simplificar contato, remover cabeçalho/rodapé complexo, evitar elementos gráficos).

Quando `modo_execucao` incluir diagnóstico avançado com vaga definida, entregar adicionalmente:

11. `PARTE A — OTIMIZAÇÃO ATS`:
  - `20 palavras-chave críticas ranqueadas (1-20)`
  - `mapa de posicionamento por seção + frequência sugerida`
  - `5 trocas terminológicas recomendadas`
  - `problemas de parsing/estrutura`
12. `PARTE B — ENGAJAMENTO HUMANO`:
  - `nota de escaneabilidade em 6 segundos (1-10)`
  - `3 áreas de subvalorização`
  - `2 ajustes de personalidade profissional`
  - `hierarquia de informação recomendada`
13. `PARTE C — ESTRATÉGIA DE INTEGRAÇÃO`:
  - `exemplos de como tecer keywords em bullets de resultado`
  - `ações em bullets com exemplos concretos`

## Regras técnicas de parsing

- Priorizar estrutura em coluna única.
- Usar cabeçalhos padrão: `Resumo Profissional`, `Experiência Profissional`, `Formação Acadêmica`, `Competências`.
- Evitar títulos criativos que prejudiquem reconhecimento de seção.
- Evitar elementos visuais que dificultem extração automática.
- Priorizar fontes legíveis e convencionais ao orientar template.

## Checklist de qualidade

- Resumo profissional objetivo e específico.
- Experiências com foco em resultado e impacto.
- Métricas presentes sempre que disponíveis.
- Sem invenção factual.
- Estrutura compatível com ATS.
- Alinhamento explícito com cargo e indústria-alvo.
- Requisitos eliminatórios mapeados e confrontados explicitamente.
- Datas legíveis e coerentes para cálculo correto de tempo de experiência.
- Consistência curricular com LinkedIn validada quando dados forem fornecidos.
- Equilíbrio entre ranqueamento ATS e poder de convencimento em leitura humana rápida.
- Diagnóstico de palavras-chave com priorização explícita quando houver vaga-alvo.

## Perguntas de clarificação padrão

Fazer estas perguntas antes da reescrita quando houver lacunas:

1. Confirmar cargo exato para as próximas candidaturas.
2. Confirmar setor/indústria prioritário.
3. Solicitar resultados mensuráveis por experiência.
4. Confirmar existência de vaga específica para calibrar palavras-chave.
5. Mapear requisitos eliminatórios definidos na vaga.
6. Confirmar inclusão de GPA/CR, honras, certificações e projetos acadêmicos.
7. Verificar status de testes de plataforma (Gupy/Vagas/PandaPé/Sólides).
8. Confirmar escolha entre diagnóstico ATS, reescrita ou fluxo completo.
9. Priorizar seções do currículo para otimização imediata.
10. Confirmar disponibilidade da especificação completa da vaga para extrair e ranquear as 20 palavras-chave críticas.