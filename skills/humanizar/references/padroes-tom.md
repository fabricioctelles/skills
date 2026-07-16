# Padrões de Tom — Detecção e Correção

Padrões que denunciam tom artificial, servil ou performático em texto PT-BR. Cada padrão inclui gatilhos, exemplos brasileiros (tecnologia, startups, marketing e desenvolvimento) e alternativas editoriais.

> **Preservação obrigatória:** em cada par “Antes/Depois”, o texto “Antes” é a única fonte de fatos, argumento, modalidade e posição autoral. A correção pode cortar muletas, reorganizar e simplificar, mas não pode criar experiência pessoal, número, fonte, causa, opinião ou certeza. Se faltar sustentação, preserve a dúvida ou aponte a lacuna.
>
> **Ajuste ao perfil:** os exemplos “Depois” usam registro neutro. Em perfil formal, preserve qualificações, atribuições e impessoalidade funcional; em perfil informal, use coloquialidade somente quando solicitada ou já presente; em nenhum perfil invente primeira pessoa para produzir “voz”.

---

### 1. Tom servil / bajulador

**Palavras/expressões gatilho:** "Ótima pergunta!", "Com certeza!", "Excelente observação!", "Espero ter ajudado!", "Fico feliz em ajudar!", "Obrigado por compartilhar!"

**Problema:** Elogios genéricos ao interlocutor antes de responder. Ninguém fala assim em texto profissional brasileiro — é marca registrada de chatbot tentando agradar.

**Antes (IA):**
> Ótima pergunta! O deploy contínuo com GitHub Actions é realmente uma abordagem fascinante. Com certeza posso te ajudar com isso! Vamos lá: primeiro, você precisa configurar o fluxo de trabalho em YAML...

**Depois (humano):**
> Para configurar deploy contínuo com GitHub Actions, comece pelo fluxo de trabalho em YAML.

**Evitar em PT-BR:**
- "Ótima pergunta!" / "Excelente ponto!"
- "Com certeza!" / "Absolutamente!"
- "Espero ter ajudado!" / "Fico feliz em contribuir!"

---

### 2. Avisos sobre limite de conhecimento

**Palavras/expressões gatilho:** "Até onde sei...", "Com base nas informações disponíveis...", "Até minha última atualização...", "Não posso confirmar com certeza, mas...", "De acordo com minhas informações limitadas..."

**Problema:** Expõe a natureza de máquina do autor com fórmulas sobre “última atualização”. O defeito está na fórmula, não na cautela: incerteza, limitação temporal e necessidade de confirmação devem ser preservadas quando fazem parte do conteúdo.

**Antes (IA):**
> Até onde sei, o Next.js 15 introduziu Server Actions como recurso estável. No entanto, informações mais recentes podem ter alterado esse cenário. Com base nas informações disponíveis até minha última atualização, a recomendação é usar App Router.

**Depois (humano):**
> As informações disponíveis indicam que o Next.js 15 tornou Server Actions estável e recomendam o App Router. Isso pode ter mudado; confirme antes de aplicar.

**Correção segura:** retirar a autorreferência do assistente sem transformar hipótese em fato, recomendação em obrigação ou informação possivelmente desatualizada em certeza atual.

**Evitar em PT-BR:**
- "Até minha última atualização..."
- "Com base nas informações disponíveis..."
- "Não tenho informações suficientes para afirmar com certeza, mas..."

---

### 3. Comunicação Colaborativa Residual

**Palavras/expressões gatilho:** "Aqui está um exemplo...", "Posso te ajudar com...", "Vou te mostrar como...", "Segue abaixo...", "Fique à vontade para perguntar mais!"

**Problema:** O texto conserva vestígios de interação assistente-usuário. Parece resposta de suporte, não texto autoral. Quando publicado como artigo ou post, denuncia imediatamente a origem.

**Antes (IA):**
> Aqui está um exemplo de como implementar autenticação com JWT no Express. Vou te mostrar passo a passo como configurar o middleware. Fique à vontade para adaptar conforme suas necessidades!

**Depois (humano):**
> A seguir, a configuração passo a passo do middleware de autenticação com JWT no Express.

**Evitar em PT-BR:**
- "Aqui está um..." / "Segue abaixo..."
- "Posso te ajudar com..." / "Vou te mostrar..."
- "Fique à vontade para..." / "Não hesite em perguntar!"

---

### 4. Cautela excessiva

**Palavras/expressões gatilho:** "Pode-se argumentar que...", "É possível que...", "Talvez seja o caso de...", "Alguns especialistas sugerem...", "Aparentemente...", "De certa forma..."

**Problema:** O acúmulo de qualificadores pode esconder a proposição principal. A correção remove apenas redundância; não aumenta a certeza, não apaga exceções e não converte atribuição vaga em opinião do autor.

**Antes (IA):**
> Pode-se argumentar que microsserviços nem sempre são a melhor escolha para startups em estágio inicial. Alguns especialistas sugerem que, em determinados contextos, uma arquitetura monolítica pode ser potencialmente mais adequada para equipes menores.

**Depois (humano):**
> Há o argumento de que microsserviços nem sempre são a melhor escolha para startups em estágio inicial. Alguns especialistas sugerem que, em certos contextos, uma arquitetura monolítica pode ser mais adequada para equipes menores.

**Correção segura:** mantenha verbos modais como “pode” e “parece” quando expressam incerteza real. Se a atribuição não estiver identificada, sinalize a lacuna em vez de assumir a afirmação como própria.

**Evitar em PT-BR:**
- "Pode-se argumentar que..." / "É possível que..."
- "Em determinados contextos..." / "Potencialmente..."
- "Alguns especialistas sugerem..." / "De certa forma..."

---

### 5. Conclusões Genéricas Positivas

**Palavras/expressões gatilho:** "O futuro é promissor", "Tempos empolgantes", "As possibilidades são infinitas", "O potencial é ilimitado", "Estamos apenas no começo", "O melhor ainda está por vir"

**Problema:** Encerramento vazio que repete otimismo sem desenvolver o argumento. A saída pode terminar quando o conteúdo termina; não precisa acrescentar posição, provocação ou previsão.

**Antes (IA):**
> O futuro da inteligência artificial no marketing digital é promissor. Estamos vivendo tempos empolgantes, e as possibilidades são verdadeiramente infinitas para profissionais que souberem se adaptar a essa nova realidade.

**Depois (humano):**
> A inteligência artificial pode ampliar as possibilidades no marketing digital para profissionais que se adaptarem. O texto vê esse futuro com otimismo.

**Evitar em PT-BR:**
- "O futuro é promissor" / "Tempos empolgantes nos aguardam"
- "As possibilidades são infinitas" / "O potencial é ilimitado"
- "Estamos apenas no começo dessa jornada"

---

### 6. Frases de Enchimento

**Palavras/expressões gatilho:** "É importante destacar que", "Vale ressaltar que", "Cabe mencionar que", "Convém observar que", "Não se pode ignorar o fato de que", "É fundamental compreender que"

**Problema:** Adicionam zero informação. São muletas usadas antes de chegar ao ponto. A correção remove a chamada de atenção e preserva a proposição, sem acrescentar justificativa, exemplo ou grau de certeza.

**Antes (IA):**
> É importante destacar que o uso de TypeScript em projetos React tem crescido significativamente. Vale ressaltar que essa tendência reflete a busca por maior segurança de tipos. Cabe mencionar que empresas como Vercel e Stripe já adotaram TypeScript como padrão.

**Depois (humano):**
> O uso de TypeScript em projetos React tem crescido significativamente, e essa tendência reflete a busca por mais segurança de tipos. Vercel e Stripe já adotaram TypeScript como padrão.

**Evitar em PT-BR:**
- "É importante destacar que" / "Vale ressaltar que"
- "Cabe mencionar que" / "Convém observar que"
- "Não se pode ignorar o fato de que" / "É fundamental compreender que"

---

### 7. Falso suspense (“Eis a questão”)

**Palavras/expressões gatilho:** "Eis a questão:", "O ponto central é:", "Mas aqui está o detalhe:", "A grande sacada é:", "O plot twist é:", "E aqui mora o perigo:"

**Problema:** Cria falso suspense antes de um ponto banal. Promete revelação dramática e entrega obviedade. Humanos não anunciam que vão dizer algo interessante — simplesmente dizem.

**Antes (IA):**
> Muitas startups investem em growth hacking sem ter product-market fit. Elas contratam profissionais de growth, gastam com anúncios e otimizam funis. Mas eis a questão: sem um produto que as pessoas realmente querem, nenhuma tática de crescimento vai funcionar.

**Depois (humano):**
> Muitas startups investem em growth hacking antes de ter product-market fit: contratam profissionais de growth, gastam com anúncios e otimizam funis. Sem um produto que as pessoas realmente queiram, nenhuma dessas táticas vai funcionar.

**Evitar em PT-BR:**
- "Eis a questão:" / "Eis o ponto:"
- "Mas aqui está o detalhe:" / "A grande sacada é:"
- "E aqui mora o perigo:" / "O plot twist é:"

---

### 8. Vulnerabilidade Falsa

**Palavras/expressões gatilho:** "Sendo honesto aqui...", "Confesso que...", "Vou ser vulnerável:", "Não vou mentir:", "Se eu for sincero...", "Admito que..."

**Problema:** Autoconsciência performática que anuncia a vulnerabilidade antes de apresentar o conteúdo. Remover esse ritual não autoriza tornar o relato mais dramático nem inventar episódio, consequência ou aprendizado.

**Antes (IA):**
> Confesso que, como desenvolvedor, nem sempre segui boas práticas. Sendo honesto aqui: houve momentos em que priorizei velocidade sobre qualidade. E sim, admito que isso me ensinou lições valiosas sobre a importância do código limpo.

**Depois (humano):**
> Como desenvolvedor, nem sempre segui boas práticas: houve momentos em que priorizei velocidade sobre qualidade. Isso me ensinou a importância do código limpo.

**Variação por perfil:** mantenha a primeira pessoa apenas porque ela existe no original. Em perfil formal, “Em alguns momentos, priorizei...” é suficiente; em perfil informal, a oralidade pode aumentar, mas os acontecimentos não.

**Evitar em PT-BR:**
- "Confesso que..." / "Sendo honesto aqui..."
- "Vou ser vulnerável:" / "Não vou mentir:"
- "Admito que isso me ensinou lições valiosas"

---

### 9. "A Verdade É Simples"

**Palavras/expressões gatilho:** "A verdade é simples:", "A realidade é mais simples do que parece", "No fundo, tudo se resume a...", "A resposta é surpreendentemente direta:", "Na prática, é menos complicado do que parece"

**Problema:** Declara obviedade sem provar. Finge simplificar algo complexo, mas apenas repete a superfície. A correção expõe diretamente a proposição já presente; não cria demonstração, recomendação ou opinião para torná-la mais convincente.

**Antes (IA):**
> Muitos fundadores se perdem em métodos de priorização complexos, matrizes RICE e metodologias ágeis elaboradas. Mas a verdade é simples: o que importa é conversar com seus usuários e construir o que eles precisam.

**Depois (humano):**
> Muitos fundadores se perdem em métodos de priorização, matrizes RICE e metodologias ágeis. O ponto defendido é conversar com os usuários e construir o que eles precisam.

**Evitar em PT-BR:**
- "A verdade é simples:" / "A realidade é mais simples do que parece"
- "No fundo, tudo se resume a..." / "A resposta é surpreendentemente direta:"
- "É menos complicado do que você imagina"

---

### 10. Inflação grandiosa de importância

**Palavras/expressões gatilho:** "Isso vai redefinir fundamentalmente...", "Uma mudança de paradigma", "Revolucionário", "Transformar completamente", "O jogo mudou para sempre", "Nunca mais será o mesmo"

**Problema:** Tudo recebe importância máxima por meio de expressões dramáticas redundantes. A correção simplifica a formulação sem enfraquecer a tese, trocar previsão por dúvida ou inserir contraponto que o autor não apresentou.

**Antes (IA):**
> O surgimento de agentes de IA autônomos representa uma mudança de paradigma que vai redefinir fundamentalmente a forma como desenvolvemos software. Estamos testemunhando uma revolução que transformará completamente a indústria de tecnologia como a conhecemos.

**Depois (humano):**
> Agentes autônomos de inteligência artificial vão mudar profundamente o desenvolvimento de software e a indústria de tecnologia.

**Evitar em PT-BR:**
- "Mudança de paradigma" / "Redefinir fundamentalmente"
- "Revolução" / "Transformar completamente"
- "O jogo mudou para sempre" / "Nunca mais será o mesmo"

---

### 11. Anúncio de explicação (“Vamos analisar”)

**Palavras/expressões gatilho:** "Vamos analisar:", "Vamos destrinchar:", "Vamos entender passo a passo:", "Vamos explorar cada aspecto:", "Vamos mergulhar nesse assunto:", "Quebrando em partes:"

**Problema:** Voz pedagógica condescendente. Pressupõe que o leitor precisa ser guiado quando o contexto pede exposição direta. Remova o anúncio e comece pelo conteúdo que já existe; se o “Antes” não trouxer a explicação, não a complete.

**Antes (IA):**
> Vamos analisar os três pilares de uma estratégia de conteúdo eficaz. Primeiro, vamos explorar a pesquisa de palavras-chave. Em seguida, vamos mergulhar na criação de grupos temáticos. Por fim, vamos entender como medir resultados.

**Depois (humano):**
> Uma estratégia de conteúdo eficaz reúne três pilares: pesquisa de palavras-chave, criação de grupos temáticos e medição de resultados.

**Evitar em PT-BR:**
- "Vamos analisar:" / "Vamos destrinchar:"
- "Vamos explorar cada aspecto:" / "Vamos mergulhar nesse assunto:"
- "Vamos entender passo a passo:" / "Quebrando em partes:"

---

### 12. Rótulos Conceituais Inventados

**Palavras/expressões gatilho:** "o paradoxo da [X]", "a armadilha da [X]", "o deficit de [X]", "a falácia do [X]", "o efeito [X]", "a síndrome de [X]"

**Problema:** Inventar termos compostos e apresentá-los como conceitos estabelecidos. IA cria rótulos pseudo-acadêmicos para parecer profunda ("o paradoxo da supervisão", "a armadilha da aceleração"). Humanos nomeiam fenômenos com cautela — ou reconhecem que estão cunhando um termo.

**Antes (IA):**
> Muitas empresas caem no que podemos chamar de "paradoxo da automação" — quanto mais automatizam, mais dependem de intervenção humana para lidar com os casos excepcionais. Esse "déficit de supervisão escalável" é o verdadeiro gargalo da transformação digital.

**Depois (humano):**
> Quanto mais essas empresas automatizam, mais dependem de intervenção humana nos casos excepcionais. O texto apresenta essa dificuldade de supervisão como gargalo da transformação digital.

**Evitar em PT-BR:**
- "O paradoxo da [X]" / "A armadilha da [X]"
- "O deficit de [X]" / "A falácia do [X]"
- "O que podemos chamar de..." (seguido de termo inventado)

---

### 13. "Imagine um Mundo Onde..."

**Palavras/expressões gatilho:** "Imagine um mundo onde...", "Imagine se...", "Pense num cenário em que...", "E se eu te dissesse que...", "Visualize um futuro onde...", "Feche os olhos e imagine..."

**Problema:** Convite futurista clichê que serve de abertura genérica. A correção deve expor a hipótese diretamente, sem adicionar produtos atuais, dados ou limitações que não estejam no texto de origem.

**Antes (IA):**
> Imagine um mundo onde todo desenvolvedor tem um assistente de IA que entende perfeitamente o contexto da sua base de código. Imagine se cada pull request fosse revisada instantaneamente com retorno preciso e acionável. Esse mundo não está tão distante quanto você pensa.

**Depois (humano):**
> Um assistente de inteligência artificial que entenda todo o contexto do código e revise cada pull request imediatamente, com retorno preciso, ainda é uma possibilidade futura. O texto sustenta que ela pode estar próxima.

**Evitar em PT-BR:**
- "Imagine um mundo onde..." / "Imagine se..."
- "E se eu te dissesse que..." / "Visualize um futuro onde..."
- "Esse mundo não está tão distante" / "O futuro já chegou"
