# Padrões de Composição — Tropos IA em PT-BR

Padrões estruturais que denunciam texto gerado por IA ao nível da **composição** — como o texto é montado, não o que ele diz. Inclui tropos catalogados pelo [tropes.fyi](https://tropes.fyi/directory) e o conceito de **Ablação Semântica** (The Register, fev 2026).

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
> O Itaú cortou 40% do time de back-office em dois anos. Não foi layoff — foi automação comendo as beiradas. Processo de crédito que levava uma semana virou algo que roda em quatro horas. O analista que sobrou não faz análise: supervisiona o modelo que faz.

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
> O cenário de startups no Brasil mudou — de garagem com pitch deck pra coisa séria, com governança e board cobrando resultado. Quem começou em 2019 achando que era só ter ideia boa e captar rodada agora enfrenta investidor que quer ver unit economics. A festa acabou; o trampo de verdade começou.

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
- Substituir metáforas genéricas por **imagens concretas do cotidiano brasileiro**: em vez de "navegar o ecossistema", "atravessar o trânsito de SP às 18h" (se o ponto é complexidade)
- Quando a metáfora não serve a um argumento real, cortar e ir direto ao ponto

---

### Empilhamento de Analogias Históricas

**Problema:** IA lista 5 empresas ou revoluções históricas em sequência para dar "peso" ao argumento. Parece erudição, mas é preenchimento — nenhuma analogia é desenvolvida o suficiente pra provar algo.

**Antes (IA):**
> Assim como a revolução industrial transformou a manufatura, como a eletricidade mudou a infraestrutura urbana, como a internet redefiniu a comunicação, como o iPhone revolucionou a computação móvel, e como o Netflix disruputou a mídia — a inteligência artificial generativa está prestes a transformar fundamentalmente o modo como trabalhamos.

**Depois (humano):**
> Todo mundo compara IA generativa com a revolução industrial. A analogia é preguiçosa — ignora que a revolução industrial levou 60 anos pra mudar a vida do trabalhador médio e começou com gente perdendo dedos em tear. Se a comparação for honesta, a gente tá em 1785: muita promessa, pouca infraestrutura, e ninguém sabe quem vai se ferrar primeiro.

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
- Regra de **1 analogia por texto** — e se usada, deve ser desenvolvida com especificidade temporal e causal
- Quando a IA lista 5 analogias, escolher a **mais relevante para o público** e descartar as demais
- Se a analogia é inevitável, ancorá-la com dados: "A revolução industrial (1760-1840) levou 80 anos para mudar a vida do trabalhador médio — IA generativa pode fazer em 8"

---

### Diluição de Ponto Único

**Problema:** O texto tem UM argumento. Mas a IA o reformula 10 vezes com conectivos diferentes, esticando pra 4000 palavras o que caberia em 400. Cada parágrafo diz a mesma coisa com roupa diferente.

**Antes (IA):**
> A transformação digital é essencial para a competitividade empresarial. De fato, empresas que não adotarem tecnologias digitais correm o risco de ficar para trás. Nesse sentido, a digitalização dos processos se torna uma prioridade estratégica. Além disso, a modernização tecnológica permite que organizações se adaptem com mais agilidade. Por outro lado, empresas que resistem à mudança digital enfrentam desafios crescentes de eficiência. Diante disso, fica claro que a transformação digital não é mais uma opção — é uma necessidade.

**Depois (humano):**
> Empresa que não digitalizou ainda tá com os dias contados? Depende. Boteco de esquina não precisa de ERP. Mas se você vende pra mais de 50 clientes e ainda controla pedido em planilha, o problema não é se vai dar merda — é quando.

**Evitar em PT-BR:**
- Parágrafo que começa com "De fato," seguido de restatement
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
> Daqui a cinco anos, a gente vai olhar pra trás e rir de como usava IA em 2026 — do mesmo jeito que ri de site com contador de visitas. A tecnologia vai amadurecer. A questão é se a gente amadurece junto ou fica repetindo buzzword em painel de evento.

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
- Conclusões que apenas restate o que já foi dito sem adicionar insight novo
- Parágrafo final com tom otimista genérico ("o futuro é promissor")

**Técnicas avançadas de correção:**
- **Quatro tipos de final humano** para substituir conclusões sinalizadas:
  1. **Virada reflexiva** — pergunta que deixa o leitor pensando
  2. **Detalhe concreto** — dado específico que ancora o argumento
  3. **Contradição** — reconhecer que o próprio argumento tem limites
  4. **Silêncio** — simplesmente parar (o leitor que conclua)
- Se a conclusão começa com "Em conclusão", cortar as 3 primeiras palavras e ver se o resto sobrevive

---

### "Apesar dos Desafios..."

**Problema:** Fórmula rígida de acknowledge→dismiss. IA reconhece um problema só pra descartá-lo imediatamente com otimismo vazio. Não há tensão real — o "desafio" nunca ameaça a tese.

**Antes (IA):**
> Apesar dos desafios regulatórios, a adoção de IA no setor de saúde segue em ritmo acelerado. Embora existam preocupações legítimas sobre privacidade de dados, as oportunidades superam amplamente os riscos. Mesmo com as limitações atuais de infraestrutura, o potencial transformador da tecnologia é inegável.

**Depois (humano):**
> A LGPD existe desde 2020 e a maioria dos hospitais ainda não sabe onde guarda prontuário digital. Isso não é "desafio regulatório" — é negligência. Implementar IA em cima disso é construir em areia movediça. Vai dar certo? Talvez. Mas o "talvez" tem nome: processo judicial.

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
- Converter o "desafio" em **pergunta real com custo**: "O problema é LGPD — quanto custa adequar o sistema? R$ 300 mil. E se não adequar, multa de até 2% do faturamento."
- Se o desafio é legítimo, **não descartar** — explorar a tensão: "O dado é bom, mas a fonte é duvidosa. A gente usa mesmo assim?"
- Aplicar "teste de consequência" — se o desafio não tem custo, risco ou trade-off explícito, ele é enfeite

---

### Listicle Disfarçado de Prosa

**Problema:** O texto é uma lista numerada fingindo ser parágrafo corrido. Cada item começa com "O primeiro aspecto...", "O segundo ponto...", "O terceiro elemento...". Não há fluxo — é enumeração com pontuação de prosa.

**Antes (IA):**
> O primeiro aspecto a considerar é a escalabilidade da solução. O segundo ponto relevante diz respeito à integração com sistemas legados. O terceiro elemento fundamental é a experiência do usuário final. O quarto fator a ser levado em conta é o custo total de propriedade. Por fim, o quinto aspecto envolve a governança de dados.

**Depois (humano):**
> Escala é o primeiro teste — se não aguenta 10x o tráfego atual, não serve. Mas antes disso tem uma pergunta mais chata: o ERP de 2014 conversa com isso? Porque se não conversa, o projeto bonito vira Frankenstein. E nem adianta resolver backend se o cara na ponta precisa de 7 cliques pra fazer o que fazia em 2.

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
- Quebrar a simetria sintática: alternar frases curtas com longas, inserir fragmentos, mudar o sujeito
- Aplicar "desordenação intencional" — reordenar os itens fora da sequência ordinal e conectar com transições naturais

---

## Ablação Semântica — Restauração de Entropia

Conceito do The Register (fev 2026): quando IA "melhora" um texto, ela faz **ablação semântica** — remove informação de alta entropia (os trechos únicos, específicos, surpreendentes) e substitui por sequências genéricas de alta probabilidade. O resultado é um "JPEG de pensamento": parece coerente, mas perdeu a densidade original.

A humanização não é só remover padrões ruins — é **restaurar o que foi destruído**.

---

### Limpeza Metafórica

**Problema:** IA identifica metáforas originais, imagens viscerais e comparações inesperadas como "ruído" e substitui por clichês seguros. Metáforas vivas viram metáforas mortas. A especificidade sensorial desaparece.

**Antes (IA):**
> O mercado de trabalho está passando por uma profunda transformação. As empresas estão navegando em águas turbulentas e buscando se adaptar ao novo cenário. É preciso abraçar a mudança e trilhar novos caminhos para alcançar o sucesso.

**Depois (humano):**
> O mercado de trabalho tá com cara de rodízio às terças — tem muita cadeira e pouca gente sentando. Quem contrata tá com medo de contratar e quem procura tá com vergonha de dizer quanto tempo tá parado. Essa dança desajeitada rende: todo mundo fingindo que tá tudo bem no LinkedIn enquanto manda currículo no desespero pelo Indeed.

**Restaurar:**
- Metáforas sensoriais (visuais, táteis, sonoras) que o texto original tinha ou deveria ter
- Comparações inesperadas com coisas concretas do cotidiano brasileiro
- Imagens que causam desconforto ou surpresa — IA evita essas por design
- Especificidade: em vez de "cenário", descrever O QUÊ se vê nesse cenário

**Sinais adicionais de detecção:**
- Metáforas substituídas por **clichês corporativos** ("ponto de inflexão", "navegar as complexidades")
- Perda de especificidade sensorial: texto que antes tinha cor/luz/cheiro e agora tem só conceito
- Metáforas que poderiam ser aplicadas a QUALQUER assunto ("transformação profunda", "novo capítulo")

**Técnicas avançadas de correção:**
- **Escala de concretude**: classificar cada imagem em 1-5 (1 = abstrata, 5 = sensorial). Se a média do texto < 2, injetar imagens nível 4-5
- Substituir clichês por **referências culturais brasileiras**: "é tipo pegar o metrô lotado às 18h em SP" em vez de "navegar complexidades"
- "Teste do bar" — se a metáfora não funcionaria numa conversa de bar, ela é genérica demais

---

### Achatamento Lexical

**Problema:** Jargão preciso e terminologia de domínio são substituídos por termos genéricos "acessíveis". Token de 1-em-10.000 vira token de 1-em-100. O texto perde densidade informacional — diz menos com mais palavras.

**Antes (IA):**
> A empresa implementou uma solução de análise de dados que permite monitorar indicadores de desempenho e tomar decisões mais informadas. A ferramenta oferece visualizações intuitivas que ajudam a equipe a entender melhor os resultados.

**Depois (humano):**
> Plugaram um Metabase no data warehouse e agora o time de produto vê funil de conversão, cohort retention e LTV por canal sem pedir pra engenharia. O dashboard que mais usam? Um scatter plot de CAC vs payback period por campanha — porque mostra em 3 segundos quais canais pagos estão sangrando dinheiro.

**Restaurar:**
- Nomes próprios de ferramentas, frameworks e metodologias (Metabase, dbt, cohort analysis)
- Métricas específicas com siglas do domínio (CAC, LTV, churn, MRR, sprint velocity)
- Verbos técnicos precisos ("plugar", "deployar", "parsear") em vez de genéricos ("implementar", "utilizar")
- Dados concretos: números, porcentagens, timeframes — IA generaliza, humano cita

**Sinais adicionais de detecção:**
- Substituição de jargão técnico por sinônimos genéricos ("ORM" → "ferramenta de mapeamento objeto-relacional" → "solução de banco de dados")
- Perda de siglas do domínio (substitui "SaaS" por "software como serviço", depois por "plataforma digital")
- Texto que soa como tradução de material introdutório para público leigo, mesmo quando o público é técnico

**Técnicas avançadas de correção:**
- **Mapeamento de domínio**: identificar o campo (dev, marketing, jurídico) → restaurar o vocabulário técnico específico
- Se o texto generalizou demais, **reintroduzir a sigla + explicação entre parênteses** na primeira ocorrência
- "Teste de precisão" — se um especialista do domínio lê e diz "isso tá vago", o texto perdeu densidade

---

### Colapso Estrutural

**Problema:** Raciocínio complexo, não-linear e cheio de voltas é forçado no template previsível de baixa perplexidade: introdução → 3 pontos → conclusão. Digressões são eliminadas. Contradições são "resolvidas". Nuance vira bullet point.

**Antes (IA):**
> A adoção de metodologias ágeis no Brasil apresenta três benefícios principais. Em primeiro lugar, aumenta a produtividade das equipes. Em segundo lugar, melhora a qualidade das entregas. Em terceiro lugar, promove uma cultura de melhoria contínua. Dessa forma, as empresas que adotam práticas ágeis tendem a obter melhores resultados.

**Depois (humano):**
> Ágil no Brasil virou religião — tem evangelista, tem herege, tem gente fazendo waterfall e chamando de sprint. O que funciona de verdade? Depende de pra quem tu pergunta. Time de 4 devs numa startup? Funciona absurdamente bem, porque a alternativa é caos. Time de 200 num banco? Aí tu tem "ágil em escala", que é um jeito bonito de falar "burocracia com post-it". E a parte que ninguém fala: metade dos "ganhos de produtividade" que empresa reporta depois de implementar scrum é simplesmente porque começou a medir — não porque melhorou.

**Restaurar:**
- Digressões produtivas que revelam raciocínio real (o "aliás" que muda de direção)
- Contradições internas: humanos admitem que duas coisas conflitantes são verdadeiras
- Qualificações em cascata: afirmação → exceção → exceção da exceção
- Perguntas sem resposta: "Mas aí vem a dúvida: e se nenhum dos dois estiver certo?"
- Estrutura que surpreende: começar pelo contra-argumento, ou pelo detalhe micro antes do macro

**Sinais adicionais de detecção:**
- Estrutura perfeitamente simétrica: parágrafos com 3-4 frases cada, todos com a mesma ordem (tópico → desenvolvimento → conclusão)
- Ausência de digressões, parênteses ou tangentes
- Texto que parece ter sido gerado por outline rígido sem desvios

**Técnicas avançadas de correção:**
- Inserir **tangente produtiva**: um parágrafo que parece desvio mas retorna ao argumento
- Usar parênteses para comentário lateral: "O que os consultores não contam (e eu vou contar) é que metade dessas métricas são vanity"
- Quebrar simetria com **fragmentos deliberados**: frase de 3 palavras no meio de um parágrafo longo
- "Regra do parágrafo rebelde" — pelo menos um parágrafo no texto deve quebrar o padrão (ser mais curto, mais longo, ou estruturalmente diferente)
