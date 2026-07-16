# Padrões de Composição — Tropos IA em PT-BR

Padrões estruturais que denunciam texto gerado por IA ao nível da **composição** — como o texto é montado, não o que ele diz. Inclui tropos catalogados pelo [tropes.fyi](https://tropes.fyi/directory) e o conceito de **Ablação Semântica** (The Register, fev 2026).

> **TRAVA FACTUAL neste arquivo:** alterar a composição, não o conteúdo. Tratar o texto "Antes" como universo factual fechado e preservar proposições, entidades, números, datas, fontes, causalidade, modalidade e registro no "Depois". Não introduzir analogia, exemplo, dado, experiência, opinião ou detalhe ausente. Quando uma lacuna impedir a concretização, manter a generalidade e apontar a lacuna no relatório.

---

## Tropos de Composição

### Resumos Fractais

**Problema:** IA anuncia o que vai dizer, diz, e depois resume o que disse — em cada seção, subseção e parágrafo. Texto vira recursão infinita de meta-comentário.

**Antes (IA):**
> Nesta seção, vamos explorar como a inteligência artificial está transformando o setor financeiro. Veremos três aspectos principais: automação de processos, análise preditiva e atendimento ao cliente.
>
> [... 3 parágrafos ...]
>
> Como vimos nesta seção, a inteligência artificial está transformando o setor financeiro por meio da automação de processos, da análise preditiva e do atendimento ao cliente. Na próxima seção, abordaremos os desafios dessa transformação.

**Depois (humano):**
> A inteligência artificial transforma o setor financeiro por meio da automação de processos, da análise preditiva e do atendimento ao cliente. A seção seguinte examina os desafios dessa transformação.

**Evitar em PT-BR:**
- "Nesta seção, veremos..."
- "Como vimos anteriormente..."
- "A seguir, abordaremos..."
- "Conforme mencionado na seção anterior..."
- "Para resumir o que foi discutido..."

**Sinais adicionais de detecção:**
- Recursividade de meta-nível: quando cada seção tem introdução → desenvolvimento → mini-conclusão, e cada parágrafo dentro da seção também tem essa estrutura
- Palavras-chave de meta-comentário: "como discutido", "retomando", "para recapitular", "em resumo desta seção"
- Presença de conectivos de transição entre subseções que referenciam o próprio texto ("No tópico anterior vimos...")

**Técnicas avançadas de correção:**
- Reescrever eliminando a recursão: a conclusão do texto é UMA — no final. As subseções não precisam de mini-conclusões
- Converter meta-comentário em afirmação direta: "Como vimos nesta seção, a IA transforma o setor" → "A IA transforma o setor de três formas"
- Se o texto tem 3+ subseções com mini-conclusões, fundir as subseções em um único bloco com fluxo contínuo

---

### Metáfora Morta

**Problema:** IA encontra uma metáfora no início e repete ad nauseam como se fosse a espinha do texto. "Ecossistema" aparece 30 vezes. "Jornada" aparece em cada parágrafo. A metáfora perde qualquer poder — vira ruído.

**Antes (IA):**
> O ecossistema de startups brasileiro está amadurecendo. Nesse ecossistema, os players precisam se adaptar. O ecossistema exige novas competências. Para sobreviver neste ecossistema, empreendedores devem construir redes sólidas. O futuro do ecossistema depende de políticas públicas que fomentem a inovação dentro do próprio ecossistema.

**Depois (humano):**
> O ecossistema de startups brasileiro está amadurecendo. Esse processo exige que seus participantes desenvolvam novas competências e que os empreendedores construam redes sólidas. O futuro do setor também depende de políticas públicas de incentivo à inovação.

**Evitar em PT-BR:**
- Repetir "ecossistema", "jornada", "cenário", "panorama" ou "paisagem" mais de 2x num texto
- Usar a mesma metáfora-base em mais de 3 parágrafos seguidos
- Forçar coerência metafórica artificial ("nessa jornada... o próximo passo da jornada... ao longo da jornada...")

**Sinais adicionais de detecção:**
- Frequência de repetição da mesma palavra-metafórica (contagem >2 no texto inteiro, >1 por parágrafo)
- Metáforas que são semanticamente vazias no contexto ("ecossistema" para qualquer coisa que tenha mais de duas partes)
- Metáforas que não suportam raciocínio — o autor usa "jornada" mas não desenvolve nenhuma etapa da jornada

**Técnicas avançadas de correção:**
- Criar um **mapa metafórico**: listar todas as metáforas usadas → se houver sobreposição semântica (ex: "ecossistema", "cenário", "paisagem" no mesmo texto), escolher UMA e eliminar as demais
- Substituir metáforas genéricas por formulação direta baseada nas proposições existentes. Usar imagem concreta somente se ela já estiver na entrada ou for apresentada, com autorização, como hipótese explícita
- Quando a metáfora não serve a um argumento real, cortar e ir direto ao ponto

---

### Empilhamento de Analogias Históricas

**Problema:** IA lista 5 empresas ou revoluções históricas em sequência para dar "peso" ao argumento. Parece erudição, mas é preenchimento — nenhuma analogia é desenvolvida o suficiente pra provar algo.

**Antes (IA):**
> Assim como a revolução industrial transformou a manufatura, como a eletricidade mudou a infraestrutura urbana, como a internet redefiniu a comunicação, como o iPhone revolucionou a computação móvel, e como o Netflix disruputou a mídia — a inteligência artificial generativa está prestes a transformar fundamentalmente o modo como trabalhamos.

**Depois (humano):**
> A revolução industrial transformou a manufatura; a eletricidade, a infraestrutura urbana; a internet, a comunicação; o iPhone, a computação móvel; e a Netflix, a mídia. Da mesma forma, a inteligência artificial generativa está prestes a transformar fundamentalmente o modo como trabalhamos.

**Evitar em PT-BR:**
- "Assim como [empresa/revolução 1], como [empresa/revolução 2], como [empresa/revolução 3]..."
- "Da mesma forma que a revolução industrial..."
- "Se olharmos para a história — do rádio à TV, da TV à internet, da internet ao mobile —"
- Listar mais de 2 analogias históricas sem desenvolver nenhuma

**Sinais adicionais de detecção:**
- Sequências de 3+ analogias com a mesma estrutura sintática (coordenação com "como" ou "assim como")
- Analogias que terminam em conclusão genérica idêntica ("...está transformando fundamentalmente o modo como trabalhamos")
- Analogias sem especificidade temporal (não diz quando a revolução industrial aconteceu, quanto durou, qual setor)

**Técnicas avançadas de correção:**
- Condensar analogias repetitivas sem apagar proposições distintas. Descartar apenas a analogia que for decorativa e não acrescentar conteúdo ao argumento
- Desenvolver especificidade temporal ou causal somente com dados já presentes na entrada
- Se a analogia não tiver sustentação, qualificá-la como comparação do autor ou apontar a lacuna no relatório; não ancorá-la com dados externos inventados

---

### Diluição de Ponto Único

**Problema:** O texto tem UM argumento. Mas a IA o reformula 10 vezes com conectivos diferentes, esticando pra 4000 palavras o que caberia em 400. Cada parágrafo diz a mesma coisa com roupa diferente.

**Antes (IA):**
> A transformação digital é essencial para a competitividade empresarial. De fato, empresas que não adotarem tecnologias digitais correm o risco de ficar para trás. Nesse sentido, a digitalização dos processos se torna uma prioridade estratégica. Além disso, a modernização tecnológica permite que organizações se adaptem com mais agilidade. Por outro lado, empresas que resistem à mudança digital enfrentam desafios crescentes de eficiência. Diante disso, fica claro que a transformação digital não é mais uma opção — é uma necessidade.

**Depois (humano):**
> A transformação digital é essencial para a competitividade. Empresas que não adotam tecnologias digitais podem perder competitividade e enfrentar problemas de eficiência. Por isso, digitalizar processos e modernizar a tecnologia são necessidades estratégicas para aumentar a agilidade e a capacidade de adaptação.

**Evitar em PT-BR:**
- Parágrafo que começa com "De fato," seguido da repetição da mesma ideia
- "Nesse sentido," introduzindo a mesma ideia de novo
- "Em outras palavras," (literalmente admitindo que vai repetir)
- "Isso significa que..." (reformulação disfarçada)
- Texto com mais de 3 parágrafos onde cada um pode ser resumido pela mesma frase

**Sinais adicionais de detecção:**
- Parágrafos com a mesma informação expressa em palavras diferentes (sinonímia redundante)
- Conectivos de reformulação: "em outras palavras", "ou seja", "isso significa que", "dito de outro modo"
- Texto com TTR (Type-Token Ratio) artificialmente baixo — muita repetição lexical com sinônimos

**Técnicas avançadas de correção:**
- **Algoritmo de compressão**: identificar o núcleo proposicional de cada parágrafo → se dois parágrafos compartilham o mesmo núcleo, fundir em um
- Eliminar conectivos de reformulação — se o leitor precisa que você repita de outro jeito, o primeiro jeito provavelmente já era ruim
- Aplicar "regra de 3": se o argumento precisa de 3 reformulações para ser entendido, ele provavelmente é fraco

---

### Conclusão Sinalizada

**Problema:** IA não sabe terminar sem anunciar que vai terminar. Usa marcadores explícitos que telegrafam "aqui acaba" — quebrando qualquer possibilidade de final com impacto.

**Antes (IA):**
> Em conclusão, a inteligência artificial generativa representa uma oportunidade transformadora para o mercado brasileiro. Em suma, as empresas que souberem aproveitar esse potencial estarão melhor posicionadas para o futuro. Para finalizar, é importante ressaltar que o equilíbrio entre inovação e responsabilidade será determinante para o sucesso dessa jornada.

**Depois (humano):**
> A inteligência artificial generativa é uma oportunidade transformadora para o mercado brasileiro. As empresas que aproveitarem esse potencial estarão mais bem posicionadas, e o equilíbrio entre inovação e responsabilidade será determinante para o sucesso.

**Evitar em PT-BR:**
- "Em conclusão,"
- "Em suma,"
- "Para finalizar,"
- "Concluindo,"
- "Portanto, podemos afirmar que..."
- "Diante do exposto,"
- "À luz do que foi apresentado,"

**Sinais adicionais de detecção:**
- Marcadores explícitos de encerramento em sequência ("Em conclusão... Para finalizar...")
- Conclusões que apenas repetem o que já foi dito sem acrescentar ideia nova
- Parágrafo final com tom otimista genérico ("o futuro é promissor")

**Técnicas avançadas de correção:**
- Escolher o fechamento apenas entre materiais já presentes no texto:
  1. **Virada reflexiva** — converter uma dúvida já existente em pergunta
  2. **Detalhe concreto** — reutilizar dado já fornecido na entrada
  3. **Contradição** — preservar limite ou tensão já expresso pelo autor
  4. **Silêncio** — retirar o marcador e simplesmente encerrar
- Se a conclusão começa com "Em conclusão", cortar as 3 primeiras palavras e ver se o resto sobrevive

---

### "Apesar dos Desafios..."

**Problema:** Fórmula rígida de acknowledge→dismiss. IA reconhece um problema só pra descartá-lo imediatamente com otimismo vazio. Não há tensão real — o "desafio" nunca ameaça a tese.

**Antes (IA):**
> Apesar dos desafios regulatórios, a adoção de IA no setor de saúde segue em ritmo acelerado. Embora existam preocupações legítimas sobre privacidade de dados, as oportunidades superam amplamente os riscos. Mesmo com as limitações atuais de infraestrutura, o potencial transformador da tecnologia é inegável.

**Depois (humano):**
> A adoção de IA no setor de saúde avança em ritmo acelerado. Há preocupações com a privacidade de dados e limitações de infraestrutura; ainda assim, as oportunidades superam amplamente os riscos, e o potencial transformador da tecnologia é inegável.

**Evitar em PT-BR:**
- "Apesar dos desafios, [coisa positiva]"
- "Embora existam preocupações legítimas, as oportunidades superam..."
- "Mesmo com as limitações, o potencial é..."
- "Não obstante os obstáculos, o caminho é promissor"
- "Reconhecendo os riscos, mas focando nas possibilidades..."

**Sinais adicionais de detecção:**
- Estrutura "reconhece → descarta" em 1-2 frases
- Adjetivos que neutralizam o problema: "desafios legítimos", "limitações atuais", "obstáculos naturais"
- O "desafio" nunca tem consequência concreta — é abstrato

**Técnicas avançadas de correção:**
- Explicitar custo, risco ou consequência somente quando esses elementos já estiverem na entrada. Se não estiverem, manter o desafio nos termos originais e apontar a lacuna no relatório
- Se o original já expressar uma tensão, **não descartá-la**: preservar o dado, a dúvida sobre a fonte e a decisão em aberto sem criar nenhum desses elementos
- Aplicar "teste de consequência" — se o desafio não tiver custo, risco ou contrapartida explícita na entrada, não inventar um; manter a formulação geral ou apontar a lacuna no relatório

---

### Listicle Disfarçado de Prosa

**Problema:** O texto é uma lista numerada fingindo ser parágrafo corrido. Cada item começa com "O primeiro aspecto...", "O segundo ponto...", "O terceiro elemento...". Não há fluxo — é enumeração com pontuação de prosa.

**Antes (IA):**
> O primeiro aspecto a considerar é a escalabilidade da solução. O segundo ponto relevante diz respeito à integração com sistemas legados. O terceiro elemento fundamental é a experiência do usuário final. O quarto fator a ser levado em conta é o custo total de propriedade. Por fim, o quinto aspecto envolve a governança de dados.

**Depois (humano):**
> A solução deve ser avaliada por cinco aspectos: escalabilidade, integração com sistemas legados, experiência do usuário, custo total de propriedade e governança de dados.

**Evitar em PT-BR:**
- "O primeiro aspecto..."
- "O segundo ponto..."
- "O terceiro elemento..."
- "O quarto fator..."
- "Por fim, o quinto..."
- Qualquer sequência ordinal disfarçada de argumentação

**Sinais adicionais de detecção:**
- Sequência ordinal implícita: "Primeiro... Depois... Em seguida... Por fim..."
- Frases com estrutura sintática idêntica (mesmo comprimento, mesma ordem de constituintes)
- Texto que pode ser reformatado como lista numerada sem perder sentido

**Técnicas avançadas de correção:**
- Se o conteúdo merece lista → **formatar como lista real** (mais honesto)
- Se o conteúdo não merece lista → **reorganizar como raciocínio causal**: causa → efeito → consequência
- Quebrar a simetria sintática sem mudar o registro nem acrescentar fragmentos que não estejam no texto
- Reordenar os itens somente quando a nova ordem preservar relações lógicas e ênfase do original

---

## Ablação Semântica — Restauração de Entropia

Conceito do The Register (fev 2026): quando IA "melhora" um texto, ela faz **ablação semântica** — remove informação de alta entropia (os trechos únicos, específicos, surpreendentes) e substitui por sequências genéricas de alta probabilidade. O resultado é um "JPEG de pensamento": parece coerente, mas perdeu a densidade original.

A humanização não é só remover padrões ruins — é **preservar o que ainda existe**. Restaurar conteúdo apagado exige uma versão-fonte fornecida pelo usuário; sem ela, não reconstruir por inferência.

---

### Limpeza Metafórica

**Problema:** IA identifica metáforas originais, imagens viscerais e comparações inesperadas como "ruído" e substitui por clichês seguros. Metáforas vivas viram metáforas mortas. A especificidade sensorial desaparece.

**Antes (IA):**
> O mercado de trabalho está passando por uma profunda transformação. As empresas estão navegando em águas turbulentas e buscando se adaptar ao novo cenário. É preciso abraçar a mudança e trilhar novos caminhos para alcançar o sucesso.

**Depois (humano):**
> O mercado de trabalho passa por uma transformação profunda. As empresas enfrentam instabilidade, buscam adaptação e precisam mudar para alcançar o sucesso.

**Restaurar:**
- Metáforas sensoriais (visuais, táteis, sonoras) que já estejam na entrada ou em uma versão-fonte fornecida
- Comparações concretas que já façam parte do material autorizado
- Imagens e reações presentes no original, sem criar desconforto ou surpresa por conta própria
- Especificidade: em vez de "cenário", descrever apenas o que a entrada já informa; se não houver detalhe, usar formulação direta e apontar a lacuna no relatório

**Sinais adicionais de detecção:**
- Metáforas substituídas por **clichês corporativos** ("ponto de inflexão", "navegar as complexidades")
- Perda de especificidade sensorial: texto que antes tinha cor/luz/cheiro e agora tem só conceito
- Metáforas que poderiam ser aplicadas a QUALQUER assunto ("transformação profunda", "novo capítulo")

**Técnicas avançadas de correção:**
- **Escala de concretude**: classificar cada imagem em 1-5 (1 = abstrata, 5 = sensorial). Se a média do texto < 2, simplificar a abstração com o material existente e apontar a falta de concretude no relatório
- Substituir clichês por formulação direta. Usar referência cultural brasileira apenas se ela já estiver na entrada ou for autorizada como hipótese explícita
- "Teste do bar" — se a metáfora não funcionaria numa conversa de bar, ela é genérica demais

---

### Achatamento Lexical

**Problema:** Jargão preciso e terminologia de domínio são substituídos por termos genéricos "acessíveis". Token de 1-em-10.000 vira token de 1-em-100. O texto perde densidade informacional — diz menos com mais palavras.

**Antes (IA):**
> A empresa implementou uma solução de análise de dados que permite monitorar indicadores de desempenho e tomar decisões mais informadas. A ferramenta oferece visualizações intuitivas que ajudam a equipe a entender melhor os resultados.

**Depois (humano):**
> A empresa implementou uma solução de análise de dados para monitorar indicadores de desempenho, apoiar decisões mais informadas e visualizar resultados. As visualizações ajudam a equipe a compreender melhor esses resultados.

**Restaurar:**
- Nomes próprios de ferramentas, frameworks e metodologias que já estejam na entrada ou em uma versão-fonte fornecida
- Métricas e siglas de domínio já presentes no material autorizado
- Verbos técnicos precisos que já estejam na entrada ou em uma versão-fonte fornecida; sem essa base, preservar a ação genérica
- Dados concretos já fornecidos: preservar números, porcentagens e intervalos temporais; se estiverem ausentes, não criá-los

**Sinais adicionais de detecção:**
- Substituição de jargão técnico por sinônimos genéricos ("ORM" → "ferramenta de mapeamento objeto-relacional" → "solução de banco de dados")
- Perda de siglas do domínio (substitui "SaaS" por "software como serviço", depois por "plataforma digital")
- Texto que soa como tradução de material introdutório para público leigo, mesmo quando o público é técnico

**Técnicas avançadas de correção:**
- **Mapeamento de domínio**: identificar o campo (dev, marketing, jurídico) → preservar o vocabulário técnico existente, sem inferir ferramenta, métrica ou sigla ausente
- Se o texto generalizou demais, reintroduzir sigla ou termo somente a partir de uma versão-fonte fornecida; caso contrário, apontar a perda de precisão no relatório
- "Teste de precisão" — se um especialista do domínio lê e diz "isso tá vago", o texto perdeu densidade

---

### Colapso Estrutural

**Problema:** Raciocínio complexo, não linear e cheio de voltas é forçado no molde previsível de baixa perplexidade: introdução → 3 pontos → conclusão. Digressões são eliminadas. Contradições são "resolvidas". Nuance vira item de lista.

**Antes (IA):**
> A adoção de metodologias ágeis no Brasil apresenta três benefícios principais. Em primeiro lugar, aumenta a produtividade das equipes. Em segundo lugar, melhora a qualidade das entregas. Em terceiro lugar, promove uma cultura de melhoria contínua. Dessa forma, as empresas que adotam práticas ágeis tendem a obter melhores resultados.

**Depois (humano):**
> No Brasil, a adoção de metodologias ágeis aumenta a produtividade das equipes, melhora a qualidade das entregas e promove uma cultura de melhoria contínua. Por isso, as empresas que adotam essas práticas tendem a obter resultados melhores.

**Restaurar:**
- Digressões produtivas que já estejam na entrada ou em uma versão-fonte fornecida
- Contradições internas efetivamente expressas pelo autor
- Qualificações, exceções e dúvidas presentes no material autorizado
- Perguntas sem resposta somente quando preservarem uma dúvida já existente
- Estrutura que surpreende: começar por contra-argumento ou detalhe já existente, sem alterar a ênfase do autor

**Sinais adicionais de detecção:**
- Estrutura perfeitamente simétrica: parágrafos com 3-4 frases cada, todos com a mesma ordem (tópico → desenvolvimento → conclusão)
- Ausência de digressões, parênteses ou tangentes
- Texto que parece ter sido gerado por outline rígido sem desvios

**Técnicas avançadas de correção:**
- Reposicionar uma tangente já existente sem criar comentário ou argumento novo
- Usar parênteses apenas para material lateral já presente no texto
- Quebrar simetria por divisão ou combinação de frases existentes, preservando o registro
- Variar a estrutura somente quando isso não alterar ênfase, modalidade ou voz do original
