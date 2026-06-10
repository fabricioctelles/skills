# Padrões de Conteúdo

Padrões onde a IA infla importância, fabrica autoridade, ou encerra textos com fórmulas previsíveis. São os mais fáceis de detectar porque soam como release de assessoria de imprensa — ninguém fala assim.

---

### 1. Ênfase indevida em significância, legado e tendências

**Palavras/expressões gatilho:** representa um marco, é um testemunho de, papel fundamental/crucial/vital, ressalta a importância, reflete uma tendência mais ampla, simbolizando o/a, contribuindo para o/a, preparando o terreno para, moldando o futuro de, cenário em constante evolução, ponto de inflexão, marca indelével, profundamente enraizado, redefine o paradigma

**Problema:** A IA transforma qualquer fato mundano numa revolução. Um CRUD vira "um marco na transformação digital". Um pivô de startup vira "um ponto de inflexão no ecossistema de inovação". Nenhum ser humano escreve assim sobre coisas normais.

**Antes (IA):**
> O Nubank representa um marco fundamental na transformação do cenário financeiro brasileiro, moldando ativamente o futuro das fintechs na América Latina e preparando o terreno para uma nova era de inclusão bancária digital.

**Depois (humano):**
> O Nubank começou oferecendo cartão de crédito sem anuidade por um app. Funcionou porque os bancões cobravam caro e atendiam mal. Hoje tem banco digital completo com 90 milhões de clientes.

**Evitar em PT-BR:**
- "representa um marco na evolução de..."
- "moldando o futuro do ecossistema de..."
- "em um cenário em constante transformação"

**Sinais adicionais de detecção:**
- Superlativos absolutos sem quantificação ("maior", "melhor", "sem precedentes", "inédito")
- Verbos de transformação grandiosa ("redefinir", "moldar", "preparar o terreno")
- Texto que descreve qualquer coisa como "ponto de inflexão" sem dizer o que muda depois

**Técnicas avançadas de correção:**
- Converter superlativos em **dados concretos**: "maior fintech" → "80 milhões de clientes"
- Substituir verbos grandiosos por **verbos de ação específica**: "preparar o terreno" → "contratar 3 engenheiros"
- "Teste do jornalista" — se um repórter leria a frase e perguntaria "como assim?", o termo é vazio

---

### 2. Ênfase forçada em notabilidade e cobertura de mídia

**Palavras/expressões gatilho:** amplamente reconhecido, coberto pelos principais veículos, destaque na mídia especializada, presença ativa nas redes sociais, segundo especialistas do setor, referência no mercado

**Problema:** A IA lista veículos e prêmios como prova de importância, sem dizer o que foi dito ou por que importa. Vira um Lattes turbinado — impressiona no vácuo mas não informa nada.

**Antes (IA):**
> A empresa foi destaque na Exame, Valor Econômico, TechCrunch e Bloomberg. Amplamente reconhecida como referência no mercado de SaaS B2B brasileiro, mantém presença ativa nas redes sociais com mais de 200 mil seguidores.

**Depois (humano):**
> Em entrevista ao Valor em 2024, o CEO disse que o ARR triplicou depois que passaram a vender para o mid-market em vez de focar só em enterprise.

**Evitar em PT-BR:**
- "amplamente reconhecido(a) como referência em..."
- "destaque nos principais veículos do setor"
- "mantém presença ativa nas redes com X seguidores"

**Sinais adicionais de detecção:**
- Listagem de veículos sem citação de matéria específica (data, título, link)
- "Presença ativa nas redes" sem métrica (seguidores, engajamento)
- Menção a prêmios ou rankings sem fonte verificável

**Técnicas avançadas de correção:**
- Se há fonte real → citar com data e link: "Segundo matéria da Exame de 12/03/2025 (link)"
- Se não há fonte → cortar a alegação de notabilidade
- "Teste de verificabilidade" — se o leitor não pode checar em 30 segundos, a informação é puffery

---

### 3. Análises superficiais com gerúndio/particípio

**Palavras/expressões gatilho:** ressaltando a importância de, demonstrando o compromisso com, refletindo a tendência de, contribuindo para o fortalecimento de, evidenciando o potencial de, impulsionando a inovação, fomentando o crescimento, consolidando sua posição como

**Problema:** A IA gruda frases com gerúndio no final das sentenças pra parecer que está analisando algo, mas não está. É firula sintática — enche linguiça sem adicionar informação. Tipo aquele estagiário que escreve 3 páginas pra dizer "funcionou".

**Antes (IA):**
> A RD Station lançou integração nativa com WhatsApp Business, demonstrando seu compromisso com a inovação no marketing digital brasileiro e consolidando sua posição como líder no segmento, impulsionando a transformação digital das PMEs.

**Depois (humano):**
> A RD Station lançou integração com WhatsApp Business. Faz sentido — a maioria dos leads de PME brasileira entra por WhatsApp, não por formulário de site.

**Evitar em PT-BR:**
- "demonstrando o compromisso da empresa com..."
- "consolidando sua posição como líder em..."
- "contribuindo para o fortalecimento do ecossistema"

**Sinais adicionais de detecção:**
- Frases que terminam com gerúndio como se fosse conclusão de análise
- Construções "verbo composto + gerúndio" em sequência ("vem demonstrando", "vai estar consolidando")
- Gerúndio usado como adjetivo ("inovando", "transformando", "impulsionando")

**Técnicas avançadas de correção:**
- Converter a oração gerundial em **oração finita** com sujeito claro: "demonstrando compromisso" → "mostra que se compromete"
- Se o gerúndio é puramente decorativo, **cortar**: "impulsionando a transformação" → (nada — a frase principal já diz)
- "Teste do podcast" — ler a frase em voz alta; se soa como narração de vídeo institucional, o gerúndio é excessivo

---

### 4. Linguagem promocional e de propaganda

**Palavras/expressões gatilho:** solução inovadora, experiência única, ecossistema robusto, revolucionário, disruptivo, estado da arte, de ponta, excelência, sinergia, empoderar, potencializar, alavancar, impulsionar, viabilizar, transformador, game-changer, seamless (usado em PT)

**Problema:** A IA escreve como copywriter de página de produto. Tudo é "inovador", "revolucionário" e "de ponta". Nenhuma pessoa normal descreve o próprio trabalho assim — soa como pitch deck desesperado pra anjo investidor.

**Antes (IA):**
> A plataforma oferece uma solução inovadora e disruptiva que empodera equipes de produto a potencializarem seus resultados, entregando uma experiência seamless e de estado da arte para alavancar a transformação digital das organizações.

**Depois (humano):**
> A plataforma automatiza o onboarding de usuário. Você configura os passos, ela mostra tooltips e checklists. Reduziu o tempo de ativação de 7 pra 2 dias nos clientes que testaram.

**Evitar em PT-BR:**
- "solução inovadora e disruptiva que empodera..."
- "experiência única de ponta/estado da arte"
- "potencializar/alavancar a transformação digital"

**Sinais adicionais de detecção:**
- Combinação de 2+ buzzwords na mesma frase ("solução inovadora e disruptiva de ponta")
- Adjetivos que são autocontraditórios ("seamless mas robusto", "simples mas poderoso")
- Texto que poderia ser usado como copy de qualquer produto sem mudar nada

**Técnicas avançadas de correção:**
- **Regra de 1 adjetivo por substantivo** — se o texto tem "solução inovadora, disruptiva e transformadora", cortar para "solução que funciona"
- Substituir adjetivos por **dados ou comparações**: "de ponta" → "roda em 40ms vs 120ms do concorrente"
- "Teste do pitch deck" — se a frase apareceria em qualquer slide de qualquer startup, ela é genérica demais

---

### 5. Atribuições vagas e weasel words

**Palavras/expressões gatilho:** segundo especialistas, de acordo com analistas do setor, estudos apontam que, o mercado reconhece, é amplamente considerado, pesquisas indicam, fontes do setor afirmam, observadores notam que

**Problema:** A IA atribui afirmações a autoridades genéricas que não existem. "Especialistas dizem" — quais? "Estudos apontam" — qual estudo, de que ano, com que metodologia? É a versão corporativa de "meu primo falou".

**Antes (IA):**
> Segundo especialistas do setor, o modelo de negócios da empresa representa uma evolução significativa. Analistas de mercado reconhecem que a abordagem tem potencial para redefinir o segmento de healthtechs no Brasil.

**Depois (humano):**
> No relatório de 2024 da Distrito, a empresa aparece entre as 10 healthtechs com maior crescimento de receita. O faturamento foi de R$ 45M, contra R$ 18M no ano anterior.

**Evitar em PT-BR:**
- "segundo especialistas do setor..."
- "analistas de mercado reconhecem que..."
- "estudos/pesquisas apontam/indicam que..."

**Sinais adicionais de detecção:**
- Quantificadores vagos: "muitos especialistas", "diversos estudos", "alguns analistas"
- Referências sem data: "pesquisas recentes mostram..."
- Ausência de fonte quando a afirmação é controversa ou específica

**Técnicas avançadas de correção:**
- Se a fonte existe → citar especificamente (autor, ano, título, link)
- Se a fonte não existe → **admitir incerteza**: "Não achei fonte — pode ser que sim, pode ser que não"
- Converter "segundo especialistas" em **opinião pessoal**: "Eu acho que..." ou "Na minha experiência..."
- "Teste da fonte" — se você não consegue encontrar a fonte em 2 minutos de busca, a atribuição é weasel

---

### 6. Conclusões formulaicas sobre desafios e perspectivas futuras

**Palavras/expressões gatilho:** apesar dos desafios, não obstante as dificuldades, o futuro é promissor, perspectivas animadoras, em um contexto de constante evolução, seguir crescendo, continuar inovando, trilhar um caminho de sucesso, superar obstáculos, rumo a um futuro, desafios e oportunidades

**Problema:** A IA encerra textos com uma seção "Desafios e Perspectivas" que não diz nada concreto. Primeiro lista problemas genéricos, depois diz que "apesar disso, o futuro é promissor". É o equivalente textual de shrug seguido de thumbs up.

**Antes (IA):**
> Apesar dos desafios inerentes ao mercado brasileiro — como a complexidade tributária e a concorrência acirrada — a startup segue trilhando um caminho de crescimento sustentável. Com perspectivas animadoras e um time comprometido com a inovação, a empresa está bem posicionada para continuar liderando a transformação do setor.

**Depois (humano):**
> O problema imediato é tributário: a reforma muda o cálculo de PIS/Cofins sobre SaaS a partir de 2026 e ninguém sabe ainda quanto vai impactar na margem. O plano é absorver o custo no primeiro ano e repassar gradualmente, mas depende de como a regulamentação sair.

**Evitar em PT-BR:**
- "apesar dos desafios, o futuro é promissor"
- "a empresa segue bem posicionada para continuar..."
- "trilhando um caminho de crescimento sustentável"

**Sinais adicionais de detecção:**
- Fórmula "Apesar de X, o futuro é Y" onde X é genérico e Y é otimista
- Uso de "perspectivas animadoras" sem dizer o que anima
- A conclusão poderia ser aplicada a QUALQUER empresa do setor

**Técnicas avançadas de correção:**
- Substituir a fórmula por **previsão específica com prazo**: "Se a reforma tributária passar, o impacto será X até 2027"
- Se o futuro é incerto, **dizer que é incerto**: "Ninguém sabe como a regulamentação vai cair. O plano B é absorver custo"
- "Teste do horóscopo" — se a conclusão poderia aparecer no horóscopo de qualquer signo, ela é genérica demais
