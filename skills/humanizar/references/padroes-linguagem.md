# Padrões de Linguagem e Gramática (PT-BR)

Padrões que denunciam texto gerado por IA no nível da escolha de palavras, construções gramaticais e estrutura de frase. Equivalentes brasileiros dos padrões 7-12 da skill original + tropos de tropes.fyi.

---

### 1. Vocabulário de IA em PT-BR

**Palavras/expressões gatilho:** crucial, fundamental, cenário, landscape/panorama, no âmbito de, no bojo de, nesse diapasão, destarte, outrossim, mister se faz, em última análise, inegável, indubitavelmente, exponencialmente, de forma exponencial, disruptivo, paradigma, holístico, sinergia, alavancar, robusto, escalável, ecossistema (abstrato), jornada (figurativo), mergulhar em (delve into), desbloquear (unlock), desvendar insights (uncover insights), rica tapeçaria (rich tapestry), um testemunho de (a testament to), serve como um lembrete (serves as a reminder), na paisagem/cenário em constante evolução (ever-evolving landscape), navegar [complexidades] (navigate), ponta de lança (spearhead), sem costura/sem fricção (seamless), multifacetado, catalisador, orquestrar, delinear

**Problema:** LLMs em PT-BR abusam de um vocabulário pomposo e repetitivo que nenhum brasileiro usa em conversas normais — nem em textos profissionais. São equivalentes tupiniquins do "delve", "crucial" e "landscape" do inglês. Muitos são traduções diretas de slop em inglês que soam ainda mais artificiais em português — ninguém fala "rica tapeçaria" ou "desbloquear potencial" no Brasil.

**Antes (IA):**
> É fundamental destacar que o ecossistema de startups brasileiro passa por um momento crucial de maturação. No âmbito da inovação, diversas empresas estão alavancando soluções disruptivas que prometem transformar o panorama do mercado de forma exponencial.

**Depois (humano):**
> O mercado de startups no Brasil amadureceu. Tem empresa criando coisa boa — mas "disruptivo" virou palavra vazia. A maioria está resolvendo problemas que já existiam com tecnologia que já existia. E tá tudo bem.

**Evitar em PT-BR:**
- "É fundamental/crucial/inegável destacar que..."
- "No âmbito/bojo/cenário de..."
- "Alavancar soluções robustas e escaláveis"
- "Mergulhar em/Mergulhar fundo em" → "explorar" / "ver de perto" / "entrar em"
- "Desbloquear o potencial" → "aproveitar" / "usar melhor"
- "Desvendar insights" → "descobrir" / "achar" / "perceber"
- "Rica tapeçaria de experiências" → cortar (sempre é enchimento)
- "É um testemunho de/da" → "mostra que" / "prova que"
- "Serve como um lembrete de que" → "lembra que" / cortar
- "No cenário/paisagem em constante evolução" → cortar o cenário, ir direto ao ponto
- "Navegar as complexidades de" → "lidar com" / "resolver"
- "Sem costura" / "sem fricção" → "fluido" / "que funciona bem" / "redondo"
- "Catalisador de mudanças" → "o que mudou" / "o que fez acontecer"
- "Orquestrar a transformação" → "coordenar" / "fazer acontecer"

---

### 2. Evitação de Copulativas (Copula Avoidance)

**Palavras/expressões gatilho:** configura-se como, constitui, representa, figura como, posiciona-se como, desponta como, consolida-se como, atua como, funciona como, opera como, se estabelece como

**Problema:** IA evita "é", "são" e "tem" como se fossem palavras proibidas. Substitui por construções rebuscadas que nenhum humano usaria numa conversa. Em PT-BR isso soa como texto jurídico ou dissertação de vestibular ruim.

**Antes (IA):**
> O Nubank configura-se como a maior fintech da América Latina. A plataforma desponta como referência em experiência do usuário e consolida-se como alternativa aos bancos tradicionais.

**Depois (humano):**
> O Nubank é a maior fintech da América Latina. A experiência do app é boa — e é por isso que tanta gente largou o bancão.

**Evitar em PT-BR:**
- "Configura-se como / consolida-se como"
- "Desponta como referência em"
- "Posiciona-se como alternativa a"

---

### 3. Paralelismos Negativos

**Palavras/expressões gatilho:** não é apenas X, mas também Y; não se trata apenas de X, trata-se de Y; mais do que X, é Y; vai muito além de X; transcende o simples X; não é meramente X, é sobretudo Y

**Problema:** Construção formulaica que infla importância artificialmente. Cria uma falsa dicotomia onde o autor finge rejeitar algo para depois abraçar algo maior — mas ambas as partes dizem a mesma coisa. LLMs adoram porque simula profundidade sem exigir raciocínio real.

**Antes (IA):**
> Produto não é apenas sobre features. Não se trata meramente de entregar código — trata-se de resolver problemas reais. O PM vai muito além de escrever user stories; ele é, sobretudo, um tradutor entre negócio e tecnologia.

**Depois (humano):**
> PM bom resolve problemas. PM ruim escreve tickets. A diferença não é filosófica — é prática. Olha pro backlog do cara e você descobre em 5 minutos.

**Evitar em PT-BR:**
- "Não se trata apenas de X, trata-se de Y"
- "Vai muito além de simplesmente..."
- "Mais do que X, é sobretudo Y"

---

### 4. Regra de Três / Tricolon Abuse

**Palavras/expressões gatilho:** clareza, concisão e coerência; inovação, tecnologia e transformação; planejar, executar e medir; qualquer tríade rítmica com "e" antes do terceiro item; três adjetivos em sequência; três substantivos abstratos agrupados

**Problema:** IA agrupa ideias em trios porque o tricolon é retoricamente satisfatório — mas quando aparece em todo parágrafo, vira cacoete. Texto humano agrupa em 2, em 4, em 1. Raramente em 3 repetidamente.

**Antes (IA):**
> Nossa cultura é baseada em transparência, colaboração e inovação. Buscamos agilidade, qualidade e impacto. Valorizamos autonomia, responsabilidade e aprendizado contínuo.

**Depois (humano):**
> A empresa valoriza autonomia. Isso na prática significa que ninguém vai te microgerenciar — mas também que ninguém vai te salvar se você travar numa decisão e não pedir ajuda.

**Evitar em PT-BR:**
- "Transparência, colaboração e inovação"
- "Planejamento, execução e controle"
- Três adjetivos ou substantivos abstratos em sequência, parágrafo após parágrafo

---

### 5. Variação Lexical Forçada / Elegant Variation

**Palavras/expressões gatilho:** ciclagem de sinônimos para o mesmo referente — ex: "a ferramenta" → "a solução" → "a plataforma" → "o sistema" → "o produto"; ou para pessoas: "o profissional" → "o colaborador" → "o especialista" → "o gestor"

**Problema:** LLMs têm penalidade de repetição interna que as força a usar sinônimos ciclados para evitar repetir a mesma palavra. Humanos repetem palavras quando fazem sentido — e a variação forçada confunde o leitor sobre se estamos falando da mesma coisa ou de coisas diferentes.

**Antes (IA):**
> O Slack revolucionou a comunicação corporativa. A ferramenta de mensagens oferece canais temáticos. A plataforma colaborativa integra com mais de 2.000 apps. A solução de produtividade é usada por 750 mil empresas.

**Depois (humano):**
> O Slack é usado por 750 mil empresas. Funciona: canais por tema, integração com tudo que existe, busca que acha mensagem de 3 anos atrás. Mas é viciante — e talvez isso seja o produto, não o bug.

**Evitar em PT-BR:**
- Ciclagem "ferramenta → solução → plataforma → sistema"
- "O profissional → o colaborador → o especialista"
- Trocar referente a cada frase quando poderia repetir ou usar pronome

---

### 6. Falsas Faixas (False Ranges)

**Palavras/expressões gatilho:** de X a Y; desde X até Y; abrangendo desde X até Y; vai de X a Y, passando por Z; cobre desde X até Y

**Problema:** LLMs criam faixas que soam amplas mas não representam uma escala real. Os extremos escolhidos não são opostos significativos — são apenas dois exemplos aleatórios com "de...a..." no meio para simular abrangência.

**Antes (IA):**
> O evento abordou desde inteligência artificial até gestão de pessoas, passando por marketing digital e produto. Os participantes variaram de estagiários a C-levels, de startups early-stage a corporações multinacionais.

**Depois (humano):**
> O evento misturou palestra de IA com workshop de gestão — público variado, maioria de startup. Uns 300 pessoas. O painel de produto foi o mais cheio.

**Evitar em PT-BR:**
- "Desde inteligência artificial até gestão de pessoas"
- "De estagiários a C-levels"
- "Abrangendo desde X até Y, passando por Z"

---

### 7. Anáfora Abusiva

**Palavras/expressões gatilho:** repetição do mesmo início em 3+ frases consecutivas — "É preciso...", "Precisamos...", "O futuro...", "A tecnologia...", "Esse é o momento de...", "Cada vez mais..."

**Problema:** Anáfora é recurso retórico legítimo — em discursos, manifestos, poesia. Mas LLMs a usam como muleta estrutural em textos expositivos onde a repetição não serve propósito estilístico. Vira eco robótico.

**Antes (IA):**
> Precisamos repensar a forma como contratamos. Precisamos questionar os processos legados. Precisamos ouvir mais e falar menos. Precisamos aceitar que o modelo antigo não funciona mais. Precisamos de coragem para mudar.

**Depois (humano):**
> O processo de contratação da maioria das empresas de tech é ruim. Todo mundo sabe — e continua fazendo igual porque "sempre foi assim". A primeira coisa concreta que muda algo: cortar etapas inúteis. Menos entrevistas, mais trabalho real avaliado.

**Evitar em PT-BR:**
- "Precisamos..." repetido 3+ vezes
- "É hora de..." repetido em sequência
- "Cada vez mais..." como abertura de múltiplos parágrafos

---

### 8. 'O X? Um Y.' (Perguntas Retóricas Auto-respondidas)

**Palavras/expressões gatilho:** "O resultado? [Substantivo/frase dramática]." / "A resposta? [Afirmação categórica]." / "O segredo? [Revelação]." / "O problema? [Diagnóstico]." / "A solução? [Receita]." / "O impacto? [Superlativo]."

**Problema:** Estrutura de pergunta+resposta curta que imita texto de copywriting. Quando usada uma vez, funciona. Quando LLMs repetem em todo parágrafo, vira tique nervoso de redator de LinkedIn. O texto inteiro vira uma sequência de pseudo-revelações.

**Antes (IA):**
> O desafio? Escalar sem perder cultura. A solução? Contratar por valores, não por currículo. O resultado? Um time coeso que entrega 3x mais. O segredo? Autonomia com accountability. O futuro? Uma empresa que não depende de um fundador.

**Depois (humano):**
> A empresa cresceu de 12 pra 80 pessoas em dois anos e a cultura sobreviveu — em parte. Contratação por valores ajudou, mas o que realmente funcionou foi manter squads pequenos com autonomia real. Nem toda decisão precisa passar pelo fundador. As melhores nunca passaram.

**Evitar em PT-BR:**
- "O resultado? Um time coeso."
- "O segredo? Consistência."
- "A resposta? Simplicidade." (especialmente em sequência)

---

### 9. Decalques Sintáticos (Anglicismos Ocultos)

**Palavras/expressões gatilho:** "endereçar um problema" (to address), "no final do dia" (at the end of the day), "performar" (to perform), "fazer sentido" (em excesso — to make sense), "estar no lugar" (to be in place), "correr um experimento" (to run an experiment), "levantar uma questão" (to raise a question), "colocar de outra forma" (to put it another way), "em termos de" (in terms of), "baseado em" sem sujeito (based on)

**Problema:** Diferente dos estrangeirismos legítimos (deploy, feedback, sprint), os decalques são **estruturas do inglês traduzidas literalmente** que quebram a naturalidade sintática do português. A IA faz isso porque pensa em inglês e traduz — e o resultado parece texto de legendista apressado. Brasileiro de verdade usa o jargão inglês cru OU a expressão portuguesa equivalente — nunca a tradução literal da estrutura.

**Antes (IA):**
> Precisamos endereçar esse problema antes do próximo sprint. No final do dia, o que importa é se a feature performa bem em produção. Temos todas as peças no lugar para correr esse experimento. Isso levanta uma questão importante em termos de escalabilidade.

**Depois (humano):**
> Precisamos resolver isso antes do próximo sprint. No fim das contas, o que importa é se a feature roda bem em prod. Tá tudo pronto pra rodar o experimento. Isso abre uma dúvida sobre escalabilidade.

**Evitar em PT-BR:**
- "Endereçar um problema" → "resolver" / "tratar" / "atacar"
- "No final do dia" → "no fim das contas" / "no fundo" / "na prática"
- "Performar" (como verbo intransitivo) → "funcionar" / "rodar" / "se sair"
- "Fazer sentido" em excesso (1-2x ok; 5x no texto = cacoete de tradução)
- "Estar no lugar" / "ter no lugar" → "estar pronto" / "ter configurado"
- "Correr um experimento" → "rodar" / "fazer" / "executar"
- "Levantar uma questão" → "abrir uma dúvida" / "criar uma pergunta" / "trazer um ponto"
- "Colocar de outra forma" → "dizendo de outro jeito" / "ou seja"
- "Em termos de" → "sobre" / "quanto a" / "de" (geralmente dá pra cortar)
- "Baseado em" sem sujeito ("Baseado nisso, decidimos...") → "Com base nisso" / "A partir disso"
- "Dar uma olhada em" (to take a look at) → "ver" / "conferir" / "olhar"
- "Estar na mesma página" (to be on the same page) → "estar alinhado" / "ter combinado"

**Alternativas naturais:**
- Preferir o verbo português que o brasileiro usa na fala: "resolver", "rodar", "funcionar"
- Quando o jargão inglês é mais natural que a tradução literal, usar o inglês: "roda o A/B test" é melhor que "correr um experimento"
- Testar lendo em voz alta: se soa como legenda de série, é decalque

**Nota:** "Fazer sentido" é caso especial — já se naturalizou no PT-BR. O problema é a frequência: 1-2x num texto é normal; 5+ vezes é fingerprint de IA traduzindo "makes sense" mecanicamente.
