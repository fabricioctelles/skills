---
name: humanizar
description: |
  Reescreve textos em português brasileiro para soarem mais humanos e naturais,
  reduzindo padrões típicos de escrita gerada por IA sem alterar fatos, argumento
  ou intenção. Use quando o texto em PT-BR parecer genérico, burocrático ou gerado
  por IA, ou quando o usuário pedir para "humanizar", "dar vida", "tirar cara de
  IA", "remover AI slop" ou "reescrever com voz". Para textos em inglês, use a
  skill-irmã `human-ai`.
metadata:
  author: https://ft.ia.br
  version: "1.3.0"
  date: 2026-06-17
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
  category: code-quality-and-review
---

# Humanizar: Escrita Viva em Português Brasileiro

Atue como editor. Remova sinais de escrita mecânica e recupere ritmo, precisão e voz sem criar uma nova história. O objetivo é melhorar o texto, não enganar detectores; nenhuma reescrita pode garantir que uma ferramenta classificará o resultado como humano.

## Proteções obrigatórias

1. **TRAVA FACTUAL — definição canônica.** Trate o texto-fonte como imutável. Preserve nomes, números, datas, citações, fontes, exemplos, relações causais, modalidade (certeza, dúvida, obrigação ou possibilidade), estado temporal, argumento, intenção, código e notação. Pode condensar, reorganizar e reformular; não pode acrescentar, retirar ou alterar esses elementos sem autorização explícita do usuário. Nunca invente vivência pessoal, anedota, estatística, fonte ou exemplo para dar concretude.
2. **Concretude sem invenção.** Reutilize detalhes já presentes. Se faltar um dado essencial, preserve a generalidade, peça o dado ao usuário ou marque `[DADO OU EXEMPLO REAL NECESSÁRIO]`. Só crie conteúdo fictício quando o usuário pedir, e identifique-o como fictício.
3. **Argumento preservado.** Mantenha a posição e a conclusão do autor, mesmo que discorde delas.
4. **Registro preservado.** Não force informalidade, primeira pessoa, humor ou opinião. O perfil de voz orienta a forma; não autoriza conteúdo novo.
5. **Precisão antes de estilo.** Preserve integralmente código, fórmulas, citações e trechos normativos. Em contexto crítico, aceite um resultado menos solto para não introduzir ambiguidade.
6. **Sem infantilização.** Simplificar a forma não significa simplificar o raciocínio.

Toda verificação posterior de **TRAVA FACTUAL** remete a esta definição. Em caso de conflito com exemplos ou referências, estas proteções prevalecem.

## Triagem obrigatória

Executar antes de diagnosticar ou reescrever:

1. Confirmar que há texto e que ele está em PT-BR. Para inglês, usar [`human-ai`](../human-ai/SKILL.md). Em texto multilíngue, atuar apenas nos trechos em PT-BR e preservar os demais.
2. Não reescrever bulas, procedimentos médicos, manuais de aviação ou outros textos de segurança crítica.
3. Não reescrever contratos, leis, cláusulas ou documentos legais que sejam a própria referência normativa. O perfil Jurídico serve para comentários, resumos e peças autorais, não para alterar texto normativo.
4. Em traduções literais bilíngues ou conteúdo avaliado por correspondência exata, não variar a redação.
5. Em textos técnicos, identificar antes da reescrita os trechos protegidos: código, equações, comandos, citações e identificadores.
6. Quando a tarefa estiver fora do escopo, explicar o risco e oferecer apenas revisão superficial se isso for seguro e o usuário autorizar.

## Modos de operação

O modo altera o nível do relatório e o número máximo de tentativas; não altera as proteções.

| Modo | Quando usar | Tentativas máximas | Entrega |
|---|---|---:|---|
| `modo_completo` (padrão) | Pedido comum de humanização | 3 | Texto final, pontuação e resumo das mudanças |
| `modo_direto` | Fluxo automatizado ou pedido de rapidez | 1 | Texto final e relatório sintético; sem repetição automática |
| `modo_revisão` | Auditoria de texto produzido por outro agente | 3 | Texto final, diagnóstico e relatório detalhado |

Preservar sempre o modo escolhido pelo usuário. Se nenhum modo foi informado e o diagnóstico encontrar cinco ou mais sinais graves, usar `modo_revisão`. Em textos com mais de 500 palavras, trabalhar por blocos semânticos e fazer uma verificação global depois de recompor o texto.

## Perfis de voz

Os perfis de voz orientam escolhas de ritmo e registro. Os exemplos são amostras fictícias de estilo, não autorização para acrescentar fatos ao texto-fonte.

### 🖋️ Crônica

Tom de cronista brasileiro. Coloquialidade controlada, ironia, observação do cotidiano transformada em reflexão. Mistura de registros alto e baixo. Virada reflexiva no final.
Aplicar somente quando o texto-fonte ou o pedido forem autorais; não tratar este perfil como padrão universal.

**Características:**
- "A gente" convive com mais-que-perfeito simples
- Fragmentos de frase como pausa dramática
- Humor seco e autoironia quando já pertencem à voz ou foram pedidos
- Posição autoral explícita, sem criar opinião nova
- Perguntas retóricas que ficam sem resposta

**Exemplo:**
> Todo mundo conhece aquele colega que automatizou o próprio trabalho e não contou pra ninguém. Ficou meses fingindo que digitava. Pois é. Agora a empresa inteira virou esse colega — só que usando ChatGPT em vez de scripts em Python. A diferença é que ninguém tá fingindo. E aí fica a dúvida: eficiência ou preguiça? Sei lá. Provavelmente os dois.

### 📰 Jornalístico

Tom de reportagem da Folha ou Piauí. Clareza máxima, dados concretos, sem firula.

**Características:**
- Sujeito + verbo + complemento (nessa ordem)
- Números e datas quando presentes no texto-fonte
- Atribuição somente às fontes existentes no texto-fonte
- Sem adjetivos avaliativos
- Sem primeira pessoa (exceto coluna assinada)

**Exemplo:**
> A empresa demitiu 40 pessoas da área de atendimento em maio. Dois ex-funcionários atribuíram os cortes à substituição por chatbots. A assessoria não comentou. A área tinha 120 pessoas no início do ano.

### 🎓 Acadêmico

Formal mas não burocrático. Rigor terminológico sem oficialês.

**Características:**
- Vocabulário preciso de domínio
- Qualificações legítimas (não ressalvas vazias)
- Preservação exata de autores e estudos citados na fonte
- Evita clichês: "faz-se necessário", "cumpre salientar", "no âmbito de"

**Exemplo:**
> A convergência para um registro médio pode ser examinada pela variação lexical em textos submetidos a ciclos sucessivos de refinamento. Nesse contexto, a ablação semântica não acrescenta falsidade; reduz a especificidade.

### 💬 Corporativo Informal

E-mail de startup, Slack profissional. Direto, leve, sem gerundismo.

**Características:**
- Frases curtas e diretas
- "A gente" em vez de "nós" quando cabe
- Verbos de ação no lugar de locução verbal
- Estrangeirismos naturais (deploy, sprint, feedback)

**Exemplo:**
> Pessoal, atualizando: o hotfix foi deployado ontem à noite, já tá em prod. O bug de duplicação parou desde as 23h. Vou monitorar mais 48h e, se zerar, fechamos a issue. Me pingam se aparecer algo.

### 📱 Post de Rede Social

LinkedIn ou Twitter BR. Curto, opinativo, com gancho na primeira linha.

**Características:**
- Primeira frase é o gancho
- Parágrafos de 1-2 linhas
- Posição autoral clara, sem criar opinião nova
- Pode usar "eu" quando a fonte já usa primeira pessoa ou o usuário pede
- Chamada para ação sutil ou nenhuma

**Exemplo:**
> Eu demiti o ChatGPT do meu fluxo de escrita.
>
> Não porque é ruim. Porque tudo que eu publicava soava igual a todo mundo.
>
> Voltei a escrever na mão. Demora 3x mais. Mas as pessoas respondem agora.
>
> Eficiência sem voz não é vantagem. É invisibilidade.

### 📲 Mensagem de WhatsApp

Oralidade máxima. Fluxo de consciência permitido.

**Características:**
- Frases incompletas ok
- Abreviações naturais (vc, tb, mto)
- Gírias regionais aceitas
- Zero preocupação com norma culta

**Exemplo:**
> cara tu viu o que o time de dados fez?
>
> meteram um modelo em prod sem avisar ninguém
>
> aí começou a mandar e-mail errado pra cliente
>
> mó treta

### ⚖️ 🆕 Jurídico / Oficialesco

Petições, pareceres, notificações. Registro formal com tiques próprios que, quando usados *deliberadamente*, soam mais autênticos que a imitação genérica da IA.

**Características:**
- Estrutura: preâmbulo → fatos → fundamentos → pedido
- Uso controlado de clichês do gênero ("data venia", "ante o exposto", "é cediço que")
- Citação de artigos, súmulas, jurisprudência
- Voz ativa quando possível para evitar burocratês vazio

**Sinais de IA nesse registro:**
- Excesso de "cumpre salientar", "faz-se mister", "no âmbito desta análise"
- Citações genéricas sem número de artigo ou lei
- Parágrafos perfeitamente simétricos (3-4 frases idênticas)

**Exemplo (IA → Humano):**
> *IA*: "Nos termos do art. 14 do CDC, cumpre salientar que a responsabilidade do fornecedor é objetiva no caso em tela."
>
> *Humano*: "O art. 14 do CDC estabelece a responsabilidade objetiva do fornecedor neste caso."

**O que preservar (não é sinal de IA):**
- Seções em CAPS ("DOS FATOS", "DO DIREITO", "DOS PEDIDOS") — é formatação esperada em petições
- Numeração de itens em pedidos e fundamentos
- Citação de artigos com número de lei e data (Art. 14, CDC; Súmula 362/STJ)
- Estrutura preâmbulo → fatos → fundamentos → pedido — é o gênero, não molde de IA

**Sinal de revisão nesse registro:** atribuição vaga como "conforme entendimento consolidado". Se a fonte não trouxer artigo, súmula ou precedente específico, apontar a lacuna; nunca criar a referência.

### 🧑‍🏫 🆕 Didático / Explicador

Textos de edtech, apostilas, tutoriais, documentação técnica amigável.

**Características:**
- Padrão: pergunta → explicação → exemplo concreto → reforço
- Vocabulário acessível mas preciso (sem infantilizar)
- Exemplos específicos já presentes na fonte ou fornecidos pelo usuário
- Transições explícitas: "Então", "Agora", "Vamos ver na prática"

**Sinais de IA nesse registro:**
- Exemplos genéricos e artificiais
- Tom enciclopédico sem interação com o leitor
- "Neste capítulo, abordaremos X, Y e Z" → molde vazio

**Exemplo:**
> Vamos direto ao ponto: *callback* é uma função que você passa como argumento pra outra função, pra ela te "chamar de volta" quando terminar. Parece complicado, mas é só isso. Imagine que você pediu um delivery: em vez de ficar ligando a cada 5 minutos pra saber se chegou, você deixa seu número e o entregador te avisa quando estiver na porta. Seu número é o callback.

### 📋 🆕 Português Simplificado

Texto acessível para público amplo. Inspirado nas operações do PorSimples (NILC/USP) e nas técnicas da Lei 15.263/2025 (Política Nacional de Linguagem Simples). Clareza máxima sem infantilizar o raciocínio.

**Quando usar:**
- Documentação técnica para público não-especialista
- Comunicação institucional e governamental
- Manuais de produto, FAQs, onboarding de usuários
- Textos para públicos com letramento funcional variado
- Quando o usuário pedir "simplificar", "linguagem simples", "mais claro", "acessível"

**Características:**
- Frases curtas em ordem direta (SVO) — meta: 13-18 palavras, máximo 25
- Uma ideia por frase
- Vocabulário comum; termo técnico explicado na primeira ocorrência
- Voz ativa (passiva apenas quando o agente for irrelevante ou desconhecido)
- Listas e estrutura visual para 3+ itens em sequência
- Conectivos explícitos e simples ("porque", "por isso", "então", "mas")
- Sem orações intercaladas longas (apostos > 5 palavras viram frase nova)
- Repetição deliberada para clareza (não forçar sinônimos variados)

**Operações de simplificação (baseadas no PorSimples):**
1. Dividir períodos compostos em frases independentes
2. Converter passiva → ativa
3. Reordenar para SVO quando houver inversão
4. Substituir marcadores discursivos complexos por simples
5. Eliminar apostos longos (transformar em frase separada)
6. Substituir palavras raras por sinônimos frequentes (sem perder precisão)
7. Explicitar sujeitos ocultos quando houver ambiguidade

**O que NÃO fazer:**
- Não eliminar raciocínio complexo — simplificar a forma, não o conteúdo
- Não remover terminologia de domínio — explicar, não substituir
- Não transformar toda prosa em lista de bullets indiscriminadamente
- Não adicionar exemplos fictícios para "ajudar" — usar apenas os da fonte
- Não reduzir modalidade: "pode causar" não vira "causa"

**Exemplo:**
> *Antes:* "A implementação de políticas públicas que visem à mitigação dos impactos socioeconômicos decorrentes da automação de processos produtivos configura-se como desafio premente para gestores em todas as esferas do poder público."
>
> *Depois:* "A automação muda como as pessoas trabalham. Isso traz problemas sociais e econômicos. Os governos precisam criar políticas para reduzir esses problemas. Esse é um desafio urgente em todas as esferas — federal, estadual e municipal."

## Processo de Humanização

Executar primeiro a **Triagem obrigatória**. Manter `texto_fonte` imutável durante todo o processo.

### Passo 1 — 🎯 Seleção do perfil de voz

Se o usuário não especificou um perfil, detectar pelo conteúdo:

| Sinal no texto | Perfil sugerido |
|---|---|
| Citações legais, artigos de lei, "art.", "§", "REsp", petição | ⚖️ Jurídico |
| Título informativo, lide, atribuições, falas de fontes ou estrutura de reportagem | 📰 Jornalístico |
| Referências acadêmicas ("et al.", metodologia, hipótese, valor-p) | 🎓 Acadêmico |
| Tutorial, documentação amigável, "passo a passo" ou "vamos ver" | 🧑‍🏫 Didático |
| E-mail ou mensagem profissional com jargão técnico e nomes de ferramentas | 💬 Corporativo Informal |
| Texto ≤100 palavras, frases incompletas, abreviações, gírias | 📲 WhatsApp |
| Texto curto (<300 palavras), opinativo, em 1ª pessoa, sem estrutura formal | 📱 Post de Rede Social |
| ≥1500 palavras, narrativo, sem jargão dominante | 🖋️ Crônica |
| Texto institucional/governamental, manual de produto, FAQ, pedido de "simplificar" ou "linguagem simples" | 📋 Português Simplificado |
| **Nenhum sinal claro** | Voz neutra — preservar o registro original e apenas remover padrões mecânicos |

**Regras de decisão:**

1. O perfil explícito define os limites do gênero e nunca é substituído automaticamente.
2. Dentro desses limites, a amostra fornecida controla as escolhas finas de estilo. Sem perfil explícito, a amostra tem prioridade sobre a detecção.
3. Sem perfil nem amostra, usar o perfil detectado; sem sinal claro, usar voz neutra.
4. Em conflito material, perguntar ao usuário nos modos completo e revisão. No `modo_direto`, escolher o registro mais próximo do texto-fonte, agir de modo conservador e registrar a ambiguidade.
5. Em texto com múltiplos registros, manter um perfil principal e ajustar apenas os trechos que pertencem a outro gênero.

> **Saída no relatório**: `🎯 Tipo detectado: [tipo] → Perfil: [perfil]`

### Passo 2 — 🔍 Diagnóstico com lista estruturada

Percorrer sistematicamente cada categoria. Marcar ✓ (encontrado) ou ✗ (ausente).

| Categoria | Sinal | Peso (1-3) | ✓/✗ | Ação |
|---|---|---|---|---|
| **Conteúdo** | Atribuição vaga ("estudos mostram", "especialistas dizem") | 3 | | Preservar a atribuição; especificar somente se a fonte já estiver na entrada e, caso contrário, sinalizar a lacuna no relatório |
| | Ênfase inflada sem base ("revolucionário", "sem precedentes") | 3 | | Preservar força e autoria da avaliação; sugerir redução no relatório, sem alterá-la sem autorização |
| | Dados possivelmente fabricados ou imprecisos | 3 | | Preservar no texto e sinalizar para verificação; corrigir apenas com fonte ou autorização do usuário |
| **Linguagem** | Vocabulário genérico ("impacto", "contexto", "cenário") | 3 | | Trocar por termo preciso já sustentado pela fonte |
| | Perífrases rebuscadas para evitar "ser", "ter" ou "estar" | 2 | | Restaurar o verbo simples quando natural ao registro |
| | Paralelismo perfeito em 3+ itens | 2 | | Quebrar a simetria |
| **Tom** | Ressalva excessiva ("pode ser que talvez", "parece que") | 2 | | Cortar redundância sem aumentar a certeza |
| | Autorreferência de IA ("como modelo de linguagem...") | 3 | | Remover o aviso padrão sem criar opinião |
| | Inflação de gravidade ("questão crucial para a humanidade") | 2 | | Reduzir a escala sem criar comparação nova |
| **Composição** | Molde introdutório ("Neste artigo, exploraremos...") | 3 | | Cortar e ir direto ao conteúdo existente |
| | Conclusão em molde ("em resumo", "conclui-se que") | 3 | | Enxugar ou reorganizar a conclusão existente |
| | Transições artificiais ("primeiramente", "em segundo lugar") | 2 | | Usar conectivos naturais |
| **Estilo** | Formatação excessiva (negrito ou travessão em excesso) | 1 | | Moderar conforme o gênero |
| | Emoji em cada item (padrão ChatGPT) | 1 | | Remover os que não têm função |
| | Markdown não solicitado (títulos e listas automáticas em prosa) | 2 | | Remover quando não servir ao gênero |
| **PT-BR** | Oficialês ("cumpre salientar", "no âmbito de") | 2 | | Substituir por construção direta |
| | Gerundismo ("vamos estar analisando") | 2 | | Converter para forma verbal direta |
| | ENEM-ismo (frase de efeito genérica no final) | 2 | | Trocar por reflexão específica |
| **Estrangeirismos** | Tradução forçada de termos de tecnologia | 2 | | Restaurar o termo consagrado no domínio |
| | Uso artificial de anglicismos fora de contexto técnico | 1 | | Remover |

> **Regra de decisão**: cada linha detectada conta como um sinal, independentemente do número de repetições. Se cinco ou mais sinais de peso 3 forem encontrados e o usuário não tiver escolhido um modo, usar `modo_revisão`.

> **Nota sobre o perfil Jurídico**: sinais de oficialês podem ser deliberados nesse gênero. Avaliar repetição mecânica e falta de função, não a mera presença da expressão.

#### Indicadores quantitativos opcionais

Usar somente quando o usuário pedir métricas ou houver ferramenta confiável para calculá-las. Nunca estimar números. Em textos curtos, fragmentados ou com menos de 200 palavras, marcar `não medido`.

Indicadores possíveis:

- razão entre tipos e ocorrências de palavras (TTR), com tokenização declarada;
- desvio-padrão do comprimento das frases;
- entropia lexical, com método declarado;
- contagem de palavras terminadas em `-mente`;
- contagem de formas em `-ando`, `-endo` e `-indo` com `\w+(?:ando|endo|indo)\b`;
- repetição de palavras genéricas e de estruturas sintáticas.

Tratar os resultados como pistas dependentes de gênero e tamanho. Eles não aprovam ou reprovam o texto, não entram na pontuação e não provam autoria humana ou artificial. Não assumir que toda variedade lexical deve subir: repetição deliberada pode ser mais natural que ciclagem forçada de sinônimos.

### Passo 3 — 🧹 Remoção de padrões

Começar pelas referências das categorias marcadas ✓ no diagnóstico:

| Categoria com ✓ no Passo 2 | Arquivo inicial |
|---|---|
| Conteúdo | `references/padroes-conteudo.md` — atribuições vagas, ênfase inflada |
| Linguagem | `references/padroes-linguagem.md` — vocabulário IA, copulativas, paralelismos |
| Tom | `references/padroes-tom.md` — adulação, ressalvas e inflação de gravidade |
| Composição | `references/padroes-composicao.md` — moldes e conclusões previsíveis |
| Estilo | `references/padroes-estilo.md` — formatação, travessão, negrito e emojis |
| PT-BR ou Estrangeirismos | `references/padroes-exclusivos-pt-br.md` — gerundismo, oficialês e ENEM-ismo |
| Português Simplificado (perfil ativo) | `references/padroes-portugues-simplificado.md` — operações, substituições lexicais e métricas |

Se surgir outro sinal durante a reescrita, houver dúvida de classificação ou sobreposição entre categorias, consultar também a referência relacionada. Não carregar todas por padrão. No `modo_revisão`, incluir sempre `padroes-exclusivos-pt-br.md`.

As referências detalham padrões, mas não substituem a **TRAVA FACTUAL**. Descartar qualquer exemplo de referência que exija informação ausente do texto-fonte.

### Passo 4 — ♻️ Restauração de especificidade

Onde o texto perdeu precisão ou ritmo:

| Problema | Solução | Exemplo |
|---|---|---|
| Metáfora morta | Cortar ou recuperar uma imagem já presente na fonte | "Ponto de inflexão" → descrever a mudança concreta que a fonte já informa |
| Termo genérico | Recuperar o vocabulário de domínio disponível | "Impacto positivo" → "queda no churn", somente se a fonte disser que o churn caiu |
| Molde previsível | Reorganizar o fluxo | Inverter ordem: exemplo → contexto → tese, sem mudar a relação entre eles |
| Abstração excessiva | Concretizar apenas com informação disponível | "Muitas pessoas sofrem" → "Muita gente passa por isso" |
| Ritmo monótono | Variar comprimento de frases | Alternar frases curtas com longas |

Se a concretude necessária não existir na fonte, manter a formulação honesta e anotar: `⚠️ Falta um dado ou exemplo real para tornar este trecho mais concreto.`

### Passo 5 — 💬 Aplicação da voz

Aplicar somente os recursos permitidos pelo perfil ativo:

| Perfil | Aplicar | Evitar |
|---|---|---|
| Voz neutra | Clareza, ritmo natural e transições discretas | Primeira pessoa, opinião, humor ou mudança de registro |
| Crônica | Ritmo irregular e ironia já sustentada pela fonte ou pedida pelo usuário | Inventar lembrança, sentimento ou observação pessoal |
| Jornalístico | Ordem direta, atribuição precisa e linguagem sóbria | Adjetivação avaliativa, primeira pessoa e fontes novas |
| Acadêmico | Terminologia de domínio e qualificações necessárias | Novas referências, certezas maiores que as da fonte e coloquialidade gratuita |
| Corporativo Informal | Frases diretas, leveza e estrangeirismos naturais do domínio | Criar status, prazo, promessa, chamada para ação ou experiência pessoal |
| Post de Rede Social | Gancho baseado na tese existente e parágrafos curtos | Criar opinião, história pessoal ou chamada para ação ausente |
| WhatsApp | Oralidade compatível com o canal e abreviações naturais | Alterar compromisso, data, destinatário ou grau de certeza |
| Jurídico | Formalidade controlada, estrutura e termos do gênero | Criar artigo, súmula, precedente, fato ou fundamento |
| Didático | Ordem clara e explicação acessível | Criar analogia, personagem, dado ou exemplo não fornecido |
| Português Simplificado | SVO, frases ≤25 palavras, vocabulário comum, listas para 3+ itens e termos técnicos explicados | Eliminar conteúdo, reduzir modalidade, inventar exemplo ou remover terminologia de domínio |

Quando o usuário fornecer amostra de voz, espelhar comprimento de frases, nível vocabular, início de parágrafos, pontuação e uso de estrangeirismos. Não copiar fatos, opiniões, personagens ou experiências da amostra para o texto reescrito.

### Passo 6 — 🔥 Verificação final

Verificar cada item. Marcar ✓, ✗ ou N/A conforme o perfil e o tamanho do trecho.

| # | Verificação | ✓/✗ |
|---|---|---|
| 1 | **TRAVA FACTUAL** atendida integralmente conforme a definição canônica? | |
| 2 | Argumento, intenção, modalidade e trechos protegidos permanecem intactos? | |
| 3 | Transições e padrões mecânicos detectados foram corrigidos? | |
| 4 | Termos vagos foram precisados somente quando a fonte fornecia material para isso? | |
| 5 | Ritmo e comprimento das frases combinam com o perfil? Em parágrafo com menos de três frases, não exigir três tamanhos distintos. | |
| 6 | Opinião, dúvida, sentimento e primeira pessoa aparecem somente se já existiam ou foram solicitados? | |
| 7 | Perfil de voz e registro permanecem consistentes em cada trecho? | |
| 8 | Estrangeirismos naturais do domínio foram preservados sem tradução forçada? | |
| 9 | Abertura, fechamento e formatação servem ao gênero, sem molde genérico desnecessário? | |
| 10 | Lido em voz alta, o texto soa natural dentro do gênero e do público pretendido? | |

Falha nos itens 1 ou 2 invalida a candidata. Nos demais itens, corrigir apenas se ainda houver tentativa disponível; não distorcer o gênero para satisfazer a lista. O controle de tentativas do Passo 8 impede repetição indefinida.

### Passo 7 — 📊 Avaliação pós-reescrita

Validar a **TRAVA FACTUAL** antes da pontuação. Se falhar, descartar a candidata e registrar pontuação `nula`; naturalidade nunca compensa alteração factual ou semântica.

Se a validação factual passar, avaliar quatro dimensões de 0 a 100, sempre em relação ao perfil ativo:

| Dimensão | Peso | Critério de avaliação |
|---|---|---|
| **Remoção de padrões IA** | 35% | Quantos padrões do Passo 2 foram eliminados? Algum remanescente? |
| **Naturalidade** | 30% | O ritmo combina com o gênero? A voz aparece somente na medida permitida? |
| **Consistência de voz** | 20% | O perfil foi mantido do início ao fim, respeitando trechos de outro registro? |
| **Legibilidade** | 15% | Frases fluem? Conectivos naturais? Lógica clara? |

**Pontuação final** = Σ (dimensão × peso)

Usar o `limiar` solicitado pelo usuário ou 80 como padrão. Se a pontuação ficar abaixo do limiar e houver nova tentativa, atuar nas dimensões mais baixas. Com pontuação abaixo de 60, mudar a abordagem sem trocar perfil explícito. Indicadores quantitativos opcionais nunca alteram a pontuação.

### Passo 8 — 📦 Controle de tentativas e entrega

Executar a seleção de perfil e o diagnóstico uma vez. Em cada tentativa, produzir uma candidata a partir do melhor texto seguro disponível e compará-la sempre ao `texto_fonte` imutável. Executar os Passos 3–6 antes de calcular a pontuação.

```text
texto_fonte = entrada original imutável
texto_atual = entrada atual ou texto_fonte
limiar = valor solicitado ou 80
tentativas_maximas = limite do modo
melhor_texto = nenhum
melhor_pontuacao = -1

para cada tentativa:
    gerar candidata a partir de texto_atual
    verificar TRAVA FACTUAL e argumento contra texto_fonte

    se a candidata falhar:
        descartar candidata sem calcular pontuação
        continuar somente se houver nova tentativa

    calcular pontuação
    se pontuação > melhor_pontuacao:
        guardar candidata como melhor_texto
        texto_atual = melhor_texto

    se pontuação >= limiar:
        estado = concluida
        entregar

se não houver candidata segura:
    estado = reprovada_trava_factual
    melhor_texto = texto_fonte
    pontuação = nula
senão:
    estado = melhor_resultado
    entregar melhor_texto com nota de limitação
```

No `modo_direto`, produzir exatamente uma candidata e não repetir. Se ela falhar na TRAVA FACTUAL, devolver o texto-fonte com estado `reprovada_trava_factual`.

Quando houver nova tentativa, escolher a alternativa pelo problema dominante:

| Problema da candidata anterior | Próxima abordagem |
|---|---|
| Padrões mecânicos remanescentes | Reforçar a remoção dos padrões detectados |
| Voz excessiva ou artificial | Reduzir intervenções e aproximar do registro original |
| Estrutura previsível | Reordenar apenas as proposições existentes |
| Texto longo inconsistente | Trabalhar por blocos semânticos e validar o conjunto |
| Perfil detectado inadequado | Mudar somente se o usuário não o escolheu e houver evidência no texto-fonte |

### Contrato de saída

Em pipelines ou quando houver pedido de saída estruturada, usar:

```yaml
estado: concluida
texto: "texto final ou texto-fonte seguro"
modo: modo_completo
perfil_de_voz: voz_neutra
limiar: 80
pontuacao: 86
convergiu: true
trava_factual:
  estado: intacta
  violacoes: []
tentativas:
  usadas: 2
  maximas: 3
relatorio: {}
```

Usar os valores conforme o estado final:

| `estado` | `convergiu` | `pontuacao` | `texto` |
|---|---:|---:|---|
| `concluida` | `true` | Número ≥ limiar | Candidata segura aprovada |
| `melhor_resultado` | `false` | Melhor número abaixo do limiar | Melhor candidata segura |
| `reprovada_trava_factual` | `false` | `null` | `texto_fonte` |
| `entrada_invalida` | `false` | `null` | Entrada sem reescrita |

Em conversa, apresentar primeiro o texto e depois o relatório no nível do modo:

| Modo | Conteúdo do relatório |
|---|---|
| `modo_completo` | Pontuação, padrões corrigidos, ressalvas e indicadores opcionais se calculados |
| `modo_direto` | Uma linha por padrão corrigido, pontuação e estado |
| `modo_revisão` | Diagnóstico completo, pontuação, ressalvas e indicadores opcionais se calculados |

### Integração com ciclos externos

Na primeira chamada, usar o texto recebido como `texto_fonte` e `texto_atual`. Nas chamadas seguintes, manter `texto_fonte` inalterado e realimentar somente o campo `texto` como `texto_atual`:

```yaml
proxima_entrada:
  texto_fonte: "original imutável"
  texto_atual: "saída.texto"
  perfil_de_voz: "mesmo perfil"
  limiar: 80
```

Nunca realimentar relatório, pontuação ou o envelope inteiro como se fossem parte do texto. Toda chamada continua comparando o resultado ao `texto_fonte` original.

## Estrangeirismos

Brasileiro de tech fala com estrangeirismos. Isso é **marca de autenticidade**, não erro. A skill preserva:

`feedback, deploy, sprint, churn, feature, bug, hotfix, pipeline, stakeholder, deadline, call, onboarding, pitch, runway, burn rate, product-market fit, growth, awareness, branding, lead, funnel, conversion, landing page, copywriting, UX, UI, framework, stack, backend, frontend, fullstack, DevOps, SaaS, API, endpoint, webhook, dashboard, KPI, OKR, ROI, ROAS, CRM, MVP`

Forçar tradução desses termos é sinal de IA purista — o oposto de humano.

> **Regra de ouro**: se o termo é usado no dia a dia do domínio em PT-BR, mantenha. Se é anglicismo artificial sem necessidade, remova.

## Suíte de testes de regressão

Conjunto mínimo para validar evoluções futuras. Rodar cada caso em `modo_completo` e conferir preservação semântica antes de julgar estilo.

| # | Tipo | Antes (IA) | Depois esperado (síntese) |
|---|---|---|---|
| T1 | E-mail corporativo | "Venho por meio deste informar que o relatório será encaminhado oportunamente" | "O relatório será enviado oportunamente." |
| T2 | Parágrafo acadêmico | "Diversos autores discutem a questão da linguagem de forma ampla" | "Diversos autores discutem a linguagem em termos amplos." |
| T3 | Texto jurídico | "É cediço que a responsabilidade civil objetiva se aplica no âmbito das relações de consumo" | "A responsabilidade civil objetiva aplica-se às relações de consumo." |
| T4 | Modelo de abertura de blog | "Neste artigo, exploraremos 5 estratégias essenciais para otimizar seu workflow" | "Neste artigo, vamos explorar cinco estratégias essenciais para otimizar seu workflow." |
| T5 | Ressalva excessiva de IA | "Como modelo de linguagem, não posso afirmar com certeza, mas parece que talvez o sistema esteja funcionando" | "O sistema parece estar funcionando, mas ainda não é possível afirmar com certeza." |
| T6 | Didático genérico | "João tem 3 maçãs e Maria tem 5. Quantas têm ao todo?" | "João tem 3 maçãs e Maria tem 5. Quantas maçãs os dois têm ao todo?" |

> **Critério de regressão**: se uma evolução piora o resultado de qualquer teste T1-T6, a mudança deve ser reavaliada.
>
> **TRAVA FACTUAL nos casos de teste:** nenhuma saída esperada pode adicionar, retirar ou alterar conteúdo protegido. Resultado mais contido é preferível a uma versão mais vistosa que invente informação.
