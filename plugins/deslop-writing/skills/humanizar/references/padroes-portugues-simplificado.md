# Padrões de Português Simplificado (PT-BR)

Referência para o perfil de voz **📋 Português Simplificado**. Define operações de simplificação, substituições lexicais, métricas de referência e regras de escrita para produzir texto acessível sem infantilizar o conteúdo.

> **Preservação obrigatória:** simplificar a forma nunca autoriza alterar fatos, argumento, modalidade ou posição autoral. Quando a simplificação criar ambiguidade factual ou técnica, manter a forma mais complexa e anotar no relatório. Toda operação está subordinada à **TRAVA FACTUAL**.
>
> **Princípio central:** clareza máxima com precisão intacta. Simplificar é tornar acessível, não é tornar raso.

---

## 1. Fundamentos

Este perfil sintetiza três fontes complementares:

| Fonte | Escopo | Contribuição principal |
|---|---|---|
| **PorSimples** (NILC/USP, 2007–2010) | Simplificação textual automática para inclusão digital | 7 operações sintáticas + 2 níveis (Natural/Strong) + corpus alinhado |
| **Lei 15.263/2025** (Política Nacional de Linguagem Simples) | Comunicação pública acessível | 18 técnicas prescritivas para órgãos governamentais |
| **NILC-Metrix** (2008–2023) | 200 métricas de complexidade textual para PT-BR | Limites quantitativos e validação empírica |

### Referências técnicas

- Corpus PorSimplesSent: [github.com/sidleal/porsimplessent](https://github.com/sidleal/porsimplessent) (CC BY 4.0)
- SIMPLEX-PB (simplificação lexical): [github.com/nathanshartmann/SIMPLEX-PB](https://github.com/nathanshartmann/SIMPLEX-PB)
- NILC-Metrix (200 métricas): [github.com/sidleal/nilcmetrix](https://github.com/sidleal/nilcmetrix) (AGPL-3.0)
- Gov-Lang-BR (1.703 pares governo): Scalercio et al., ACL 2025

---

## 2. Operações de simplificação sintática

Baseadas nas 10 operações do editor de anotação do PorSimples, consolidadas em 7 operações aplicáveis por um editor humano ou IA:

### 2.1. Dividir períodos compostos

Quebrar sentenças com mais de uma oração em frases independentes. Cada frase carrega uma ideia.

**Antes:**
> O governo anunciou o programa ontem, que prevê investimentos de R$ 2 bilhões em infraestrutura urbana, beneficiando 15 milhões de pessoas em todo o país.

**Depois:**
> O governo anunciou o programa ontem. O programa prevê investimentos de R$ 2 bilhões em infraestrutura urbana. O objetivo é beneficiar 15 milhões de pessoas em todo o país.

**Regra:** se a frase tem mais de 25 palavras e contém vírgula seguida de pronome relativo ("que", "o qual", "onde") ou conjunção subordinativa, dividir.

---

### 2.2. Converter voz passiva em voz ativa

A voz ativa explicita quem faz a ação. Usar passiva somente quando o agente for irrelevante, desconhecido ou quando a ativa criar ambiguidade.

**Antes:**
> A proposta foi aprovada pelo Senado após seis meses de tramitação.

**Depois:**
> O Senado aprovou a proposta após seis meses de tramitação.

**Antes (passiva justificada — manter):**
> O corpo foi encontrado na margem do rio.

**Manter:** o agente é desconhecido; forçar ativa inventaria informação.

---

### 2.3. Reordenar para SVO (Sujeito-Verbo-Objeto)

Eliminar inversões sintáticas que dificultam a compreensão. A ordem canônica do português é SVO.

**Antes:**
> Preocupa o comitê a possibilidade de atraso na entrega.

**Depois:**
> A possibilidade de atraso na entrega preocupa o comitê.

**Antes:**
> Aos beneficiários será garantido o acesso integral ao sistema.

**Depois:**
> Os beneficiários terão acesso integral ao sistema.

---

### 2.4. Substituir marcadores discursivos complexos por simples

Trocar conectivos eruditos ou ambíguos por equivalentes diretos.

| Complexo | Simples |
|---|---|
| não obstante | mas / porém |
| outrossim | também / além disso |
| destarte | por isso |
| em que pese | apesar de |
| haja vista | já que / porque |
| mister se faz | é preciso / é necessário |
| no que tange a | sobre / em relação a |
| em face de | por causa de / diante de |
| à medida que | conforme / enquanto |
| conquanto | embora |
| porquanto | porque |
| sem prejuízo de | mantendo / sem afetar |
| por intermédio de | por meio de / com |

---

### 2.5. Eliminar apostos longos

Apostos com mais de 5 palavras viram frase separada. Apostos curtos (até 5 palavras) podem permanecer.

**Antes:**
> Sandra Aluísio, professora titular do Instituto de Ciências Matemáticas e de Computação da USP em São Carlos, coordenou o projeto PorSimples.

**Depois:**
> Sandra Aluísio coordenou o projeto PorSimples. Ela é professora titular do Instituto de Ciências Matemáticas e de Computação da USP, em São Carlos.

**Aposto curto — manter:**
> O NILC, centro de linguística computacional, desenvolveu as ferramentas.

---

### 2.6. Substituir palavras raras por sinônimos frequentes

Trocar vocabulário de baixa frequência por equivalentes comuns, sem perder precisão técnica. Termos de domínio devem ser explicados na primeira ocorrência, não eliminados.

**Antes:**
> A implementação de políticas públicas que visem à mitigação dos impactos socioeconômicos configura-se como desafio premente.

**Depois:**
> Criar políticas públicas para reduzir os impactos sociais e econômicos é um desafio urgente.

**Termo técnico — explicar, não eliminar:**
> O churn (taxa de cancelamento de clientes) aumentou 15% no trimestre.

---

### 2.7. Explicitar sujeitos ocultos e referências ambíguas

Quando o sujeito oculto ou o pronome puder gerar dúvida sobre quem age, explicitar.

**Antes:**
> O ministro reuniu-se com o secretário. Disse que o prazo seria ampliado.

**Depois:**
> O ministro reuniu-se com o secretário. O ministro disse que o prazo seria ampliado.

**Sujeito oculto claro — não forçar:**
> O sistema recebeu a atualização e já está funcionando.

Neste caso, "já está funcionando" refere-se obviamente ao sistema. Explicitar seria redundante.

---

## 3. Substituições lexicais

Tabela de substituições frequentes baseadas no SIMPLEX-PB e na Lei 15.263. Usar somente quando o substituto não alterar a precisão do texto-fonte.

### 3.1. Vocabulário burocrático → direto

| Evitar | Preferir |
|---|---|
| implementar | fazer / criar / colocar em prática |
| operacionalizar | fazer funcionar / executar |
| viabilizar | permitir / tornar possível |
| otimizar | melhorar |
| priorizar | dar prioridade a / fazer primeiro |
| protocolar | registrar / entregar |
| subsidiar | dar informações para / apoiar |
| deliberar | decidir |
| aferir | medir / verificar |
| pleitear | pedir |
| ensejar | causar / dar origem a |
| auferir | receber / obter |
| prospectar | buscar / procurar |
| dirimir | resolver / esclarecer |
| perfectibilizar | melhorar |

### 3.2. Locuções → formas diretas

| Evitar | Preferir |
|---|---|
| no âmbito de | em |
| no que diz respeito a | sobre |
| no tocante a | sobre |
| com vistas a | para |
| a fim de que | para que |
| em virtude de | por causa de / porque |
| por intermédio de | por meio de / com |
| com o fito de | para |
| a nível de | em (ou cortar) |
| via de regra | geralmente |
| de forma que | então / por isso |
| tendo em vista que | porque / já que |
| em consonância com | de acordo com |
| face ao exposto | por isso |

### 3.3. Adjetivos inflados → precisos

| Evitar | Preferir |
|---|---|
| exponencial (figurativo) | grande / rápido / [número real] |
| robusto (figurativo) | completo / forte / confiável |
| holístico | completo / abrangente |
| disruptivo | novo / que muda tudo |
| inovador (vazio) | [descrever a novidade] |
| paradigmático | que muda o padrão / importante |
| multifacetado | com vários aspectos |
| emblemático | representativo / simbólico |

### 3.4. Quando NÃO substituir

- **Termos técnicos do domínio do leitor:** "API", "endpoint", "deploy", "churn" → manter em texto para desenvolvedores
- **Termos jurídicos em peças jurídicas:** "litisconsórcio", "agravo" → manter no perfil Jurídico
- **Termos médicos em textos para profissionais de saúde:** "dispneia", "hemodinâmica" → manter
- **Nomes próprios e siglas estabelecidas:** "INSS", "FGTS", "SUS" → manter (explicar na primeira ocorrência para público leigo)

---

## 4. Métricas de referência

Valores derivados do corpus PorSimples e das categorias do NILC-Metrix. Usar como guia, não como regra rígida — o gênero e o público-alvo modulam os limites.

### 4.1. Comprimento de sentença (ASL — Average Sentence Length)

| Nível PorSimples | ASL (palavras/frase) | Público-alvo |
|---|---|---|
| Original | ~20 | Letramento pleno |
| Natural | ~16 | Letramento básico |
| **Strong** | **~13** | **Letramento rudimentar** |

**Meta para este perfil:** ASL entre 13 e 18 palavras, dependendo do domínio.
- Governo/saúde para público geral: ≤15
- Documentação técnica para não-especialistas: ≤18
- FAQ/onboarding: ≤13

### 4.2. Classificação de frases por comprimento (NILC-Metrix)

| Classificação | Palavras |
|---|---|
| Curta | até 11 |
| Média | 11–12 |
| Longa | 12–15 |
| Muito longa | acima de 15 |

**Meta:** maioria das frases entre curtas e longas. Minimizar frases "muito longas" (> 15 palavras). Se uma frase passar de 25, quase sempre pode ser dividida.

### 4.3. Diversidade lexical (TTR — Type-Token Ratio)

| Nível | TTR |
|---|---|
| Original | 0.19 |
| Natural | 0.17 |
| Strong | 0.16 |

TTR mais baixo indica mais repetição de palavras — e no contexto de simplificação, isso é desejável. Não forçar sinônimos diferentes para a mesma coisa; repetição deliberada ajuda a compreensão.

### 4.4. Complexidade sintática

Indicadores do NILC-Metrix que sinalizam texto complexo:

| Indicador | Texto complexo | Texto simples |
|---|---|---|
| Orações por sentença | > 2.3 | ≤ 1.5 |
| Palavras antes do verbo principal | > 1.5 | ≤ 1.0 |
| Proporção de orações não-SVO | > 0.33 | ≤ 0.15 |
| Proporção de orações relativas | > 0.13 | ≤ 0.05 |
| Proporção de orações subordinadas | > 0.44 | ≤ 0.20 |
| Proporção de voz passiva | alto | baixo |

---

## 5. Regras de escrita

15 regras prescritivas para o perfil Português Simplificado, inspiradas na Lei 15.263/2025 e nas operações do PorSimples. Cada regra tem prioridade (1 = sempre aplicar; 2 = aplicar quando possível; 3 = aplicar conforme o gênero).

### Prioridade 1 — Sempre aplicar

| # | Regra |
|---|---|
| R1 | **Uma ideia por frase.** Se a frase contém duas proposições independentes, dividir. |
| R2 | **Ordem direta (SVO).** Sujeito antes do verbo, verbo antes do complemento. Inverter somente com razão estilística forte. |
| R3 | **Voz ativa.** Converter passiva em ativa quando o agente for conhecido e relevante. |
| R4 | **Palavras comuns.** Preferir o sinônimo mais frequente quando não houver perda de precisão. |
| R5 | **Frases curtas.** Máximo de 25 palavras por frase. Meta: 13–18. |
| R6 | **Conectivos explícitos e simples.** "Porque", "por isso", "então", "mas", "e", "também". |

### Prioridade 2 — Aplicar quando possível

| # | Regra |
|---|---|
| R7 | **Explicar termos técnicos na primeira ocorrência.** Entre parênteses ou em frase curta seguinte. |
| R8 | **Evitar dupla negação.** "Não é impossível" → "É possível" (somente se não alterar a modalidade). |
| R9 | **Evitar subjuntivo desnecessário.** "Caso haja necessidade" → "Se for necessário". |
| R10 | **Listas para 3+ itens.** Se uma frase enumera três ou mais elementos, usar lista com marcadores. |
| R11 | **Sujeito explícito.** Quando o sujeito oculto puder causar ambiguidade, explicitar. |
| R12 | **Sem orações intercaladas longas.** Apostos > 5 palavras viram frase nova. |

### Prioridade 3 — Conforme o gênero

| # | Regra |
|---|---|
| R13 | **Sem estrangeirismos fora do domínio.** Manter termos consagrados no domínio do leitor; remover os que o público-alvo não conhece. |
| R14 | **Repetição deliberada.** Repetir o substantivo em vez de usar pronome quando o referente estiver distante (> 2 frases). |
| R15 | **Estrutura visual.** Usar subtítulos, tabelas e destaques para organizar informação densa. Não converter toda prosa em bullets. |

---

## 6. Domínios de aplicação

### 6.1. Governo e comunicação pública

Foco: cidadão comum, letramento variado. Seguir integralmente a Lei 15.263.

**Antes:**
> Os beneficiários do programa deverão comparecer à unidade de atendimento munidos de documento de identificação com foto, comprovante de residência atualizado e número de inscrição no Cadastro Único, sob pena de indeferimento do requerimento.

**Depois:**
> Se você é beneficiário do programa, vá até a unidade de atendimento. Leve:
> - Documento com foto (RG ou CNH)
> - Comprovante de endereço atualizado
> - Número do Cadastro Único (CadÚnico)
>
> Sem esses documentos, o pedido será negado.

---

### 6.2. Saúde para público leigo

Foco: pacientes e familiares. Evitar jargão médico; quando necessário, explicar.

**Antes:**
> A administração de anti-inflamatórios não esteroidais pode ocasionar efeitos adversos gastrointestinais, incluindo dispepsia, náuseas e, em casos mais graves, úlcera péptica.

**Depois:**
> Anti-inflamatórios como ibuprofeno podem causar problemas no estômago. Os mais comuns são:
> - Dor ou queimação no estômago (dispepsia)
> - Enjoo (náusea)
>
> Em casos mais graves, podem causar feridas no estômago (úlcera). Tome com alimento para reduzir o risco.

---

### 6.3. Documentação técnica para não-especialistas

Foco: usuários finais de software, manuais de produto, onboarding.

**Antes:**
> Para efetuar a configuração do webhook, o usuário deverá acessar o painel administrativo, navegar até a seção de integrações e inserir a URL do endpoint que receberá as notificações, certificando-se de que o servidor de destino esteja configurado para aceitar requisições POST com payload em formato JSON.

**Depois:**
> Para configurar o webhook:
>
> 1. Acesse o painel administrativo
> 2. Vá até **Integrações**
> 3. Cole a URL do seu endpoint (o endereço que vai receber as notificações)
>
> Certifique-se de que seu servidor aceita requisições POST com dados em JSON.

---

### 6.4. Educação e material didático

Foco: estudantes. Ordem clara, exemplos concretos, progressão do simples ao complexo.

**Antes:**
> A fotossíntese consiste em um processo bioquímico mediante o qual organismos autotróficos fotossintetizantes convertem energia luminosa em energia química, utilizando dióxido de carbono e água como reagentes e produzindo glicose e oxigênio como produtos.

**Depois:**
> Fotossíntese é o processo que as plantas usam para produzir seu próprio alimento.
>
> Como funciona:
> - A planta absorve luz do sol, água e gás carbônico (CO₂)
> - Com esses ingredientes, ela produz glicose (açúcar) e oxigênio (O₂)
>
> A glicose alimenta a planta. O oxigênio é liberado no ar — o mesmo que a gente respira.

---

## 7. Integração com TRAVA FACTUAL

### 7.1. Quando NÃO simplificar

| Situação | Razão | Ação |
|---|---|---|
| Simplificação altera relação causal | "A causou B" pode virar "A e B aconteceram" | Manter a forma complexa |
| Simplificação remove qualificação necessária | "Possivelmente eficaz" virar "eficaz" | Manter modalidade |
| Simplificação elimina exceção | "Exceto em casos de X" desaparece ao dividir | Preservar a exceção em frase separada |
| Termo técnico é o nome oficial | Substituir "litisconsórcio" por "várias partes" em petição | Manter o termo; explicar se público for leigo |
| Dado numérico exige contexto adjacente | "15% a mais que 2023" perde sentido separado de "2023" | Manter na mesma frase |

### 7.2. Marcação de conflito

Quando a simplificação ideal conflitar com a preservação factual:

```
⚠️ CONFLITO SIMPLIFICAÇÃO × TRAVA FACTUAL: [descrever o trecho].
Mantida forma complexa para preservar [precisão / modalidade / causalidade / exceção].
```

### 7.3. Simplificação de citações e dados

- **Citações diretas:** nunca simplificar. Preservar ipsis litteris.
- **Dados numéricos:** manter todos. Pode-se acrescentar explicação entre parênteses se a fonte permitir.
- **Nomes próprios e siglas:** manter. Expandir sigla na primeira ocorrência.

---

## 8. Diferença entre perfis

| Aspecto | 📋 Português Simplificado | 🧑‍🏫 Didático | 📰 Jornalístico |
|---|---|---|---|
| Foco principal | Acessibilidade por simplificação formal | Explicação com exemplos | Informação factual concisa |
| Frases | ≤ 25 palavras, meta 13-18 | Variadas, com ritmo pedagógico | Curtas, ordem direta |
| Vocabulário | Comum; técnico explicado | Acessível mas com progressão | Preciso, sem adjetivação |
| Listas | Sim, para 3+ itens | Sim, com passos numerados | Não (exceto infográfico) |
| Exemplos | Somente se existirem na fonte | Incentivados (mas não inventados) | Não cabem |
| Repetição | Deliberada para clareza | Permitida em reforço | Evitada (concisão) |
| Estrutura visual | Subtítulos, tabelas, bullets | Pergunta → explicação → exemplo | Lide + pirâmide invertida |

---

## 9. Checklist de verificação

Usar ao final da reescrita no perfil Português Simplificado:

| # | Verificação | ✓/✗ |
|---|---|---|
| 1 | Todas as frases têm ≤ 25 palavras? | |
| 2 | Maioria das frases está em ordem SVO? | |
| 3 | Voz passiva aparece somente onde justificada? | |
| 4 | Termos técnicos foram explicados na primeira ocorrência? | |
| 5 | Conectivos são simples e explícitos? | |
| 6 | Enumerações de 3+ itens estão em lista? | |
| 7 | Apostos longos foram transformados em frase separada? | |
| 8 | Sujeitos ambíguos foram explicitados? | |
| 9 | Nenhuma informação foi removida ou adicionada? (TRAVA FACTUAL) | |
| 10 | Modalidade preservada? ("pode" não virou "vai", "talvez" não sumiu) | |
| 11 | Citações diretas permanecem intactas? | |
| 12 | Dados numéricos completos e no contexto correto? | |
