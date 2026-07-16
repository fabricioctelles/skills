# Padrões de Conteúdo

Padrões onde a IA infla importância, fabrica autoridade ou encerra textos com fórmulas previsíveis. São fáceis de detectar porque soam como comunicado de assessoria de imprensa — ninguém fala assim.

> **TRAVA FACTUAL neste arquivo:** tratar o texto "Antes" como universo factual fechado. No "Depois", preservar proposições, entidades, números, datas, fontes, causalidade, modalidade e registro. Não preencher lacunas com exemplos, dados, fontes ou experiência pessoal. Quando faltar sustentação, preservar a alegação e apontar a lacuna no relatório; só cortar, qualificar ou corrigir com autorização do usuário.

---

### 1. Ênfase indevida em significância, legado e tendências

**Palavras/expressões gatilho:** representa um marco, é um testemunho de, papel fundamental/crucial/vital, ressalta a importância, reflete uma tendência mais ampla, simbolizando o/a, contribuindo para o/a, preparando o terreno para, moldando o futuro de, cenário em constante evolução, ponto de inflexão, marca indelével, profundamente enraizado, redefine o paradigma

**Problema:** A IA transforma qualquer fato mundano numa revolução. Um CRUD vira "um marco na transformação digital". Um pivô de startup vira "um ponto de inflexão no ecossistema de inovação". Nenhum ser humano escreve assim sobre coisas normais.

**Antes (IA):**
> O Nubank representa um marco fundamental na transformação do cenário financeiro brasileiro, moldando ativamente o futuro das fintechs na América Latina e preparando o terreno para uma nova era de inclusão bancária digital.

**Depois (humano):**
> O Nubank tem papel central na transformação do setor financeiro brasileiro. A empresa influencia o desenvolvimento das fintechs na América Latina e contribui para a inclusão bancária digital.

**Evitar em PT-BR:**
- "representa um marco na evolução de..."
- "moldando o futuro do ecossistema de..."
- "em um cenário em constante transformação"

**Sinais adicionais de detecção:**
- Superlativos absolutos sem quantificação ("maior", "melhor", "sem precedentes", "inédito")
- Verbos de transformação grandiosa ("redefinir", "moldar", "preparar o terreno")
- Texto que descreve qualquer coisa como "ponto de inflexão" sem dizer o que muda depois

**Técnicas avançadas de correção:**
- Converter superlativos em **dados concretos somente quando o dado já estiver na entrada**. Sem dado, preservar a força da avaliação e registrar a falta de sustentação no relatório
- Substituir verbos grandiosos por **verbos de ação já descritos no original**. Se o original não informar a ação, usar formulação direta que preserve a alegação sem criar evento novo
- "Teste do jornalista" — se um repórter leria a frase e perguntaria "como assim?", o termo é vazio

---

### 2. Ênfase forçada em notabilidade e cobertura de mídia

**Palavras/expressões gatilho:** amplamente reconhecido, coberto pelos principais veículos, destaque na mídia especializada, presença ativa nas redes sociais, segundo especialistas do setor, referência no mercado

**Problema:** A IA lista veículos e prêmios como prova de importância, sem dizer o que foi dito ou por que importa. Vira um Lattes turbinado — impressiona no vácuo mas não informa nada.

**Antes (IA):**
> A empresa foi destaque na Exame, Valor Econômico, TechCrunch e Bloomberg. Amplamente reconhecida como referência no mercado de SaaS B2B brasileiro, mantém presença ativa nas redes sociais com mais de 200 mil seguidores.

**Depois (humano):**
> A empresa apareceu na Exame, no Valor Econômico, no TechCrunch e na Bloomberg. É amplamente reconhecida no mercado brasileiro de SaaS B2B e soma mais de 200 mil seguidores nas redes sociais.

**Evitar em PT-BR:**
- "amplamente reconhecido(a) como referência em..."
- "destaque nos principais veículos do setor"
- "mantém presença ativa nas redes com X seguidores"

**Sinais adicionais de detecção:**
- Listagem de veículos sem citação de matéria específica (data, título, link)
- "Presença ativa nas redes" sem métrica (seguidores, engajamento)
- Menção a prêmios ou rankings sem fonte verificável

**Técnicas avançadas de correção:**
- Se a entrada já trouxer fonte, data ou link → preservar e citar esses mesmos elementos, sem completar o que estiver ausente
- Se não houver fonte → preservar a alegação e sua atribuição, apontando a lacuna no relatório; só cortar ou qualificar com autorização
- "Teste de verificabilidade" — se o leitor não pode checar em 30 segundos, a informação é puffery

---

### 3. Análises superficiais com gerúndio/particípio

**Palavras/expressões gatilho:** ressaltando a importância de, demonstrando o compromisso com, refletindo a tendência de, contribuindo para o fortalecimento de, evidenciando o potencial de, impulsionando a inovação, fomentando o crescimento, consolidando sua posição como

**Problema:** A IA gruda frases com gerúndio no final das sentenças pra parecer que está analisando algo, mas não está. É firula sintática — enche linguiça sem adicionar informação. Tipo aquele estagiário que escreve 3 páginas pra dizer "funcionou".

**Antes (IA):**
> A RD Station lançou integração nativa com WhatsApp Business, demonstrando seu compromisso com a inovação no marketing digital brasileiro e consolidando sua posição como líder no segmento, impulsionando a transformação digital das PMEs.

**Depois (humano):**
> A RD Station lançou integração nativa com WhatsApp Business. O lançamento demonstra seu compromisso com a inovação no marketing digital brasileiro, consolida sua posição de liderança no segmento e impulsiona a transformação digital das PMEs.

**Evitar em PT-BR:**
- "demonstrando o compromisso da empresa com..."
- "consolidando sua posição como líder em..."
- "contribuindo para o fortalecimento do ecossistema"

**Sinais adicionais de detecção:**
- Frases que terminam com gerúndio como se fosse conclusão de análise
- Construções "verbo composto + gerúndio" em sequência ("vem demonstrando", "vai estar consolidando")
- Gerúndio usado como adjetivo ("inovando", "transformando", "impulsionando")

**Técnicas avançadas de correção:**
- Converter a oração gerundial em **oração finita** com sujeito claro, preservando a alegação: "demonstrando compromisso" → "o lançamento demonstra o compromisso"
- Se o gerúndio é puramente decorativo, **cortar**: "impulsionando a transformação" → (nada — a frase principal já diz)
- "Teste do podcast" — ler a frase em voz alta; se soa como narração de vídeo institucional, o gerúndio é excessivo

---

### 4. Linguagem promocional e de propaganda

**Palavras/expressões gatilho:** solução inovadora, experiência única, ecossistema robusto, revolucionário, disruptivo, estado da arte, de ponta, excelência, sinergia, empoderar, potencializar, alavancar, impulsionar, viabilizar, transformador, game-changer, seamless (usado em PT)

**Problema:** A IA escreve como copywriter de página de produto. Tudo é "inovador", "revolucionário" e "de ponta". Nenhuma pessoa normal descreve o próprio trabalho assim — soa como pitch deck desesperado pra anjo investidor.

**Antes (IA):**
> A plataforma oferece uma solução inovadora e disruptiva que empodera equipes de produto a potencializarem seus resultados, entregando uma experiência seamless e de estado da arte para alavancar a transformação digital das organizações.

**Depois (humano):**
> A plataforma oferece uma solução inovadora e disruptiva. Ela dá às equipes de produto meios para melhorar seus resultados, oferece uma experiência integrada e de alto nível e apoia a transformação digital das organizações.

**Evitar em PT-BR:**
- "solução inovadora e disruptiva que empodera..."
- "experiência única de ponta/estado da arte"
- "potencializar/alavancar a transformação digital"

**Sinais adicionais de detecção:**
- Combinação de 2+ buzzwords na mesma frase ("solução inovadora e disruptiva de ponta")
- Adjetivos que são autocontraditórios ("seamless mas robusto", "simples mas poderoso")
- Texto que poderia ser usado como copy de qualquer produto sem mudar nada

**Técnicas avançadas de correção:**
- Reduzir adjetivos puramente decorativos sem apagar uma alegação substantiva. Quando a alegação não tiver evidência na entrada, qualificá-la como descrição da empresa ou do texto
- Substituir adjetivos por **dados ou comparações somente quando esses elementos já estiverem na entrada**. Sem evidência, preservar a avaliação e apontar a lacuna no relatório
- "Teste do pitch deck" — se a frase apareceria em qualquer slide de qualquer startup, ela é genérica demais

---

### 5. Atribuições vagas e weasel words

**Palavras/expressões gatilho:** segundo especialistas, de acordo com analistas do setor, estudos apontam que, o mercado reconhece, é amplamente considerado, pesquisas indicam, fontes do setor afirmam, observadores notam que

**Problema:** A IA atribui afirmações a autoridades genéricas que não existem. "Especialistas dizem" — quais? "Estudos apontam" — qual estudo, de que ano, com que metodologia? É a versão corporativa de "meu primo falou".

**Antes (IA):**
> Segundo especialistas do setor, o modelo de negócios da empresa representa uma evolução significativa. Analistas de mercado reconhecem que a abordagem tem potencial para redefinir o segmento de healthtechs no Brasil.

**Depois (humano):**
> Especialistas do setor não identificados consideram o modelo de negócios uma evolução significativa. Analistas também não identificados avaliam que a abordagem pode redefinir o segmento de healthtechs no Brasil.

**Evitar em PT-BR:**
- "segundo especialistas do setor..."
- "analistas de mercado reconhecem que..."
- "estudos/pesquisas apontam/indicam que..."

**Sinais adicionais de detecção:**
- Quantificadores vagos: "muitos especialistas", "diversos estudos", "alguns analistas"
- Referências sem data: "pesquisas recentes mostram..."
- Ausência de fonte quando a afirmação é controversa ou específica

**Técnicas avançadas de correção:**
- Se a fonte já estiver na entrada → preservá-la com os mesmos autor, ano, título e link
- Se a fonte não estiver na entrada → manter a atribuição como não identificada e registrar a lacuna no relatório; só cortar ou qualificar com autorização
- Não converter atribuição vaga em opinião ou experiência pessoal do revisor
- "Teste da fonte" — se você não consegue encontrar a fonte em 2 minutos de busca, a atribuição é weasel

---

### 6. Conclusões formulaicas sobre desafios e perspectivas futuras

**Palavras/expressões gatilho:** apesar dos desafios, não obstante as dificuldades, o futuro é promissor, perspectivas animadoras, em um contexto de constante evolução, seguir crescendo, continuar inovando, trilhar um caminho de sucesso, superar obstáculos, rumo a um futuro, desafios e oportunidades

**Problema:** A IA encerra textos com uma seção "Desafios e Perspectivas" que não diz nada concreto. Primeiro lista problemas genéricos, depois diz que "apesar disso, o futuro é promissor". É o equivalente textual de shrug seguido de thumbs up.

**Antes (IA):**
> Apesar dos desafios inerentes ao mercado brasileiro — como a complexidade tributária e a concorrência acirrada — a startup segue trilhando um caminho de crescimento sustentável. Com perspectivas animadoras e um time comprometido com a inovação, a empresa está bem posicionada para continuar liderando a transformação do setor.

**Depois (humano):**
> A startup enfrenta a complexidade tributária e a concorrência acirrada, mas mantém uma trajetória de crescimento sustentável. Suas perspectivas são animadoras, o time é comprometido com a inovação e a empresa está bem posicionada para continuar liderando a transformação do setor.

**Evitar em PT-BR:**
- "apesar dos desafios, o futuro é promissor"
- "a empresa segue bem posicionada para continuar..."
- "trilhando um caminho de crescimento sustentável"

**Sinais adicionais de detecção:**
- Fórmula "Apesar de X, o futuro é Y" onde X é genérico e Y é otimista
- Uso de "perspectivas animadoras" sem dizer o que anima
- A conclusão poderia ser aplicada a QUALQUER empresa do setor

**Técnicas avançadas de correção:**
- Usar previsão, prazo ou plano somente quando esses elementos já estiverem na entrada. Se faltarem, nomear apenas os desafios existentes e apontar a ausência de evidência no relatório
- Se o original expressar incerteza, preservá-la sem criar cenário, consequência ou plano alternativo
- "Teste do horóscopo" — se a conclusão poderia aparecer no horóscopo de qualquer signo, ela é genérica demais
