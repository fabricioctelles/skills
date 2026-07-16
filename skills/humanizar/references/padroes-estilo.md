# Padrões de estilo e formatação

Padrões que denunciam texto gerado por IA pela forma visual e estrutural, não pelo conteúdo. Ferramentas de detecção usam esses marcadores como sinais de alta confiança.

> **Regra transversal:** correção de estilo altera somente apresentação, pontuação e organização. Preserve fatos, números, fontes, causalidade, prazo, estado temporal, modalidade e perfil de voz. Nunca compense a retirada de um recurso visual com dado, opinião, humor ou certeza inexistentes.

---

### Travessão (em-dash) excessivo

**Problema:** IA usa 15-25 travessões por texto médio. Humano brasileiro usa 2-3, e geralmente prefere vírgula, ponto ou parênteses.

**Antes (IA):**
> O projeto — que começou em 2022 — trouxe resultados impressionantes — especialmente na área de dados — e agora está sendo expandido — mesmo com orçamento limitado — para outras regionais.

**Depois (humano):**
> O projeto começou em 2022 e trouxe resultados impressionantes, especialmente na área de dados. Mesmo com orçamento limitado, agora está sendo expandido para outras regionais.

**Evitar em PT-BR:**
- Mais de 2 travessões por parágrafo
- Travessão onde vírgula resolve
- Encadeamento de apartes com travessão (— X — Y — Z)

**Sinais adicionais de detecção:**
- Travessões usados para **tudo**: apartes, conclusões, reformulações, exemplos
- Texto onde >10% dos sinais de pontuação são travessões
- Travessão duplo usado como parênteses em toda ocorrência

**Técnicas avançadas de correção:**
- **Limite de 2 travessões por parágrafo** — se passar, converter os extras em vírgulas, pontos ou parênteses
- Diferenciar uso: travessão para contraste forte, parênteses para comentário lateral, vírgula para aparte leve
- Ao trocar a pontuação, preservar a relação entre oração principal, ressalva, causa e contraste
- "Teste do editor" — se um editor humano teria cortado o travessão, cortar

---

### Negrito excessivo

**Problema:** IA aplica negrito em toda palavra-chave como se o texto fosse uma apresentação. Texto corrido com negrito em cada substantivo importante parece catálogo de produto, não escrita humana.

**Antes (IA):**
> A **plataforma** oferece **integração nativa** com os principais **CRMs do mercado**, garantindo **escalabilidade** e **segurança** para equipes de **vendas** e **marketing**.

**Depois (humano):**
> A plataforma oferece integração nativa com os principais CRMs do mercado, garantindo escalabilidade e segurança para equipes de vendas e marketing.

**Regra contextual canônica:**
- Em prosa corrida, e-mail, artigo e texto autoral, usar negrito apenas quando houver contraste editorial deliberado ou quando a fonte já trouxer ênfase relevante
- Em documentação, material didático, interfaces e listas de consulta, o negrito pode marcar rótulos e hierarquia quando isso melhora a navegação
- Não aplicar cotas simultâneas por parágrafo e por seção. O excesso é funcional: ocorre quando a marcação se repete sem hierarquia e faz vários trechos competirem pela mesma atenção

**Sinais adicionais de detecção:**
- Negrito em substantivos comuns (plataforma, equipe, resultado) sem razão editorial
- Negrito usado como substituto de hierarquia de informação (quando a estrutura deveria fazer o trabalho)
- Negrito espalhado por tantas palavras que deixa de indicar prioridade

**Técnicas avançadas de correção:**
- Usar negrito apenas para **contraste intencional**: "O problema não é a ferramenta — é o **processo**"
- Se o negrito está tentando compensar falta de clareza, **reestruturar a frase** em vez de negritar
- Preservar negritos funcionais do gênero; remover os decorativos sem alterar as palavras ou a ênfase semântica do trecho
- "Teste de hierarquia" — ao olhar a página, fica claro por que cada destaque existe?

---

### Listas com rótulo em negrito

**Problema:** IA produz listas onde todo item começa com um termo em negrito seguido de dois-pontos, mesmo quando não há hierarquia real. Em documentação e material de consulta, esse formato pode ser legítimo; o sinal é seu uso automático em prosa ou em categorias artificiais.

**Antes (IA):**
> - **Agilidade:** O time reduziu o ciclo de entrega em 40%.
> - **Qualidade:** Os bugs em produção caíram pela metade.
> - **Engajamento:** A satisfação do time subiu 12 pontos no eNPS.

**Depois (humano):**
> - Agilidade: a equipe reduziu o ciclo de entrega em 40%.
> - Qualidade: os bugs em produção caíram pela metade.
> - Engajamento: a satisfação da equipe subiu 12 pontos no eNPS.

**Evitar em PT-BR:**
- Estrutura "**Palavra:** frase explicativa" repetida em série sem hierarquia real
- Listas de 3+ itens onde o gênero não pede consulta rápida e a prosa preserva melhor as relações
- Forçar categorias artificiais para criar itens

**Sinais adicionais de detecção:**
- Estrutura repetitiva: "**Termo:** frase explicativa" em 3+ itens consecutivos
- Itens que são minitópicos de documentação, não pontos argumentativos
- A lista poderia ser uma tabela 2xN

**Técnicas avançadas de correção:**
- Se a informação é factual e tabular → converter em **tabela**, preservando rótulos, valores e correspondências
- Se a informação é argumentativa → converter em **prosa corrida** sem criar relação causal ou conclusão nova
- Se a lista é inevitável → usar marcadores simples sem cabeçalho em negrito
- Manter cabeçalhos em negrito quando forem rótulos funcionais do gênero, conforme a regra contextual canônica
- "Teste do slide" — se a lista parece um slide de apresentação, formatar como slide (ou reescrever como parágrafo)

---

### Title Case em títulos

**Problema:** Em inglês, Title Case é comum em headings. Em português brasileiro, não. A norma é capitalizar só a primeira palavra e nomes próprios. Title Case em PT-BR é sinal claro de texto gerado por modelo treinado em inglês.

**Antes (IA):**
> ## Estratégias De Marketing Digital Para Pequenas Empresas

**Depois (humano):**
> ## Estratégias de marketing digital para pequenas empresas

**Evitar em PT-BR:**
- Capitalizar preposições (De, Para, Com, Em)
- Capitalizar substantivos comuns em títulos (Empresas, Estratégias, Resultados)
- Qualquer padrão que lembre capa de livro americano

**Sinais adicionais de detecção:**
- Títulos onde preposições e artigos estão capitalizados
- Títulos que parecem capa de livro americano ("Estratégias De Marketing Para Pequenas Empresas")
- Mistura de Title Case com sentenças em minúsculo no mesmo documento

**Técnicas avançadas de correção:**
- Aplicar **regra ABNT**: só a primeira letra do título e nomes próprios em maiúsculas
- Exceção: se o documento é explicitamente para público americano, Title Case é aceitável
- "Teste do jornal brasileiro" — abrir matéria da Folha ou Piauí; os títulos usam minúsculas em preposições

---

### Emojis decorativos

**Problema:** IA enfia emojis em títulos e itens como enfeite. Brasileiro usa emoji em mensagem informal, não em título de seção ou tópico técnico. A presença de 🚀💡✅🎯 em texto profissional é assinatura de máquina.

**Antes (IA):**
> 🚀 **Lançamento:** Produto entra no ar em setembro
> 💡 **Observação:** Usuários preferem onboarding curto
> ✅ **Próximos passos:** Agendar reunião com stakeholders
> 🎯 **Meta:** Crescer 30% no trimestre

**Depois (humano):**
> Lançamento: o produto entra no ar em setembro.
> Observação: os usuários preferem um onboarding curto.
> Próximos passos: agendar uma reunião com os stakeholders.
> Meta: crescer 30% no trimestre.

**Evitar em PT-BR:**
- Emoji antes de título ou item quando for puramente decorativo
- 🚀💡✅🎯📊 como decoração de estrutura
- Emoji incompatível com o perfil de voz ou sem função comunicativa

**Sinais adicionais de detecção:**
- Emojis em headings de seção, títulos de artigo, ou como marcadores em texto profissional
- Sequência de emojis sem função comunicativa (decoração pura)
- Emoji em texto que não é mensagem pessoal ou post de rede social

**Técnicas avançadas de correção:**
- Em texto formal ou técnico, remover emoji puramente decorativo; preservar ícone que comunique estado, alerta ou categoria funcional
- Em WhatsApp e rede social, manter emojis compatíveis com o perfil de voz e retirar apenas repetição mecânica
- Ao remover o emoji, não acrescentar humor, ironia, surpresa nem nova ênfase para compensar
- "Teste do canal" — o emoji cumpre uma função aceita nesse gênero ou serve apenas de enfeite?

---

### Aspas curvas vs retas

**Problema:** ChatGPT e Claude usam aspas curvas tipográficas (" ") por padrão. A maioria dos brasileiros digita aspas retas (" ") porque é o que o teclado produz. Aspas curvas em texto informal ou técnico são bandeira de IA.

**Antes (IA):**
> O gestor disse que o projeto está "no caminho certo" e que a equipe está "engajada".

**Depois (humano):**
> O gestor disse que o projeto está "no caminho certo" e que a equipe está "engajada".

**Evitar em PT-BR:**
- " " (curvas) em qualquer contexto que não seja diagramação profissional
- ' ' (apóstrofos curvos) no lugar de ' '
- Misturar aspas curvas e retas no mesmo texto

**Sinais adicionais de detecção:**
- Mistura de aspas curvas e retas no mesmo documento
- Aspas curvas em texto que claramente veio de teclado brasileiro (onde o padrão é reta)
- Aspas curvas em mensagens de WhatsApp ou Slack (impossível no mobile)

**Técnicas avançadas de correção:**
- **Regra de consistência**: escolher um padrão e manter — se o texto é de teclado brasileiro, usar aspas retas
- Em diagramação profissional (livro, revista), aspas curvas são aceitáveis
- "Teste do WhatsApp" — se o texto parece conversa de app, aspas retas obrigatórias

---

### Decoração Unicode

**Problema:** IA usa caracteres Unicode decorativos como setas (→, ←, ↗), marcadores especiais (•, ▸, ▪), marcas de verificação (✓, ✗) e separadores (│, ─) que humanos brasileiros não digitam. Teclado brasileiro produz -, *, > e ponto final.

**Antes (IA):**
> Benefícios do novo processo:
> → Redução de 40% no tempo de resposta
> → Aumento na satisfação do cliente
> → Integração com sistemas legados
>
> Stack: React │ Node.js │ PostgreSQL

**Depois (humano):**
> Benefícios do novo processo:
> - Redução de 40% no tempo de resposta
> - Aumento na satisfação do cliente
> - Integração com sistemas legados
>
> Stack: React, Node.js, PostgreSQL

**Evitar em PT-BR:**
- → como marcador de item (usar - ou *)
- │ como separador (usar vírgula, barra ou ponto)
- ✓ e ✗ no corpo do texto quando não houver função; se houver, usar o estado textual equivalente sem inferi-lo

**Sinais adicionais de detecção:**
- Setas (→, ↗), marcadores especiais (▸, ▪), marcas de verificação (✓, ✗) e separadores (│, ─) que não são renderizados pelo teclado padrão brasileiro
- Uso de emojis como marcadores em texto formal
- Texto que parece ter sido copiado de um Notion com modelos de produtividade

**Técnicas avançadas de correção:**
- Converter setas em hífens ou asteriscos: "→" → "-"
- Remover separadores Unicode: "React │ Node.js │ PostgreSQL" → "React, Node.js, PostgreSQL"
- Converter marcas de verificação em texto somente quando houver equivalente explícito, preservando o estado original: aprovado, reprovado, sim, não ou pendente
- "Teste do terminal" — se o texto renderiza com caracteres quebrados num terminal sem Unicode, é decoração artificial

---

### Fragmentos curtos dramáticos

**Problema:** IA produz frases de 1-3 palavras isoladas como parágrafo para criar "impacto". Esse recurso existe em copywriting, mas IA abusa até em texto informativo. Brasileiro escreve assim no Twitter, não em artigo ou e-mail.

**Antes (IA):**
> O mercado mudou.
>
> Radicalmente.
>
> E quem não se adaptar vai ficar para trás. A pergunta não é se, mas quando. O futuro já chegou.
>
> Literalmente.

**Depois (humano):**
> O mercado mudou radicalmente. Quem não se adaptar vai ficar para trás. A pergunta não é se, mas quando: o futuro já chegou, literalmente.

**Evitar em PT-BR:**
- Palavra isolada como parágrafo sem função no perfil de voz ("Radicalmente.", "Literalmente.", "Ponto.")
- Sequência de fragmentos dramáticos sem função no perfil de voz
- Fragmento + ponto final para criar "peso" artificial

**Sinais adicionais de detecção:**
- Palavra ou frase de 1-3 palavras isolada como parágrafo inteiro
- Uso repetido (mais de 1 por texto) em contexto que não é Twitter
- Fragmento que não acrescenta informação — só "peso" artificial

**Técnicas avançadas de correção:**
- Em prosa neutra, integrar fragmentos ao período correspondente; em Crônica ou Rede Social, preservá-los quando fizerem parte da voz
- Integrar o fragmento sem perder o intensificador: "Mudou. Radicalmente." → "Mudou radicalmente."
- Se o fragmento é pura ênfase, ajustar a pontuação sem acrescentar urgência, conclusão ou avaliação
- "Teste do gênero" — o fragmento combina com o perfil de voz ou apenas simula impacto?

---

### Vírgula de Oxford (Oxford Comma)

**Problema:** IA treinada em inglês frequentemente insere vírgula antes do "e" final em enumerações (ex: "maçãs, bananas, e laranjas"). Em português brasileiro, essa vírgula é atípica e desnecessária — a norma é não usar vírgula antes de "e" em listas. Sua presença é marcador tipográfico de texto gerado por modelo anglófono.

**Antes (IA):**
> A plataforma oferece dashboards, relatórios customizados, e integração com APIs externas. O time trabalha com React, Node.js, e PostgreSQL.

**Depois (humano):**
> A plataforma oferece dashboards, relatórios customizados e integração com APIs externas. O time trabalha com React, Node.js e PostgreSQL.

**Evitar em PT-BR:**
- Vírgula antes de "e" no último item de lista: "A, B, e C" → "A, B e C"
- Vírgula antes de "ou" final: "X, Y, ou Z" → "X, Y ou Z"
- Exceção legítima: quando o "e" liga orações com sujeitos diferentes (vírgula de clareza, não de lista)

**Sinais adicionais de detecção:**
- Vírgula antes de "e" em listas de 3+ itens
- Vírgula antes de "ou" em alternativas
- Mistura de textos com e sem Oxford comma no mesmo documento

**Técnicas avançadas de correção:**
- **Regra PT-BR**: sem vírgula antes de "e"/"ou" em listas
- Exceção: quando a vírgula evita ambiguidade real (sujeitos diferentes nas orações)
- "Teste do vestibular" — se a frase passaria no ENEM como correta, a vírgula está certa

---

### Ponto final e aspas (convenção brasileira)

**Problema:** IA segue a convenção americana de colocar ponto final DENTRO das aspas, mesmo quando a citação não é frase completa. Em português brasileiro, o ponto vai FORA quando as aspas envolvem apenas parte da frase.

**Antes (IA — convenção americana):**
> O CEO disse que a empresa está "no caminho certo."
>
> A meta é atingir o que chamam de "product-market fit."

**Depois (humano — convenção brasileira):**
> O CEO disse que a empresa está "no caminho certo".
>
> A meta é atingir o que chamam de "product-market fit".

**Regra PT-BR:**
- Citação é frase completa e independente → ponto dentro: Ele disse: "Vamos resolver isso."
- Citação é parte da frase do autor → ponto fora: O plano é "escalar rápido".
- Na dúvida: ponto fora (é o padrão brasileiro em texto corrido)

**Sinais adicionais de detecção:**
- Ponto dentro das aspas quando a citação é parte da frase do autor
- Inconsistência: às vezes dentro, às vezes fora, no mesmo texto
- Citações de 1 palavra com ponto dentro ("impacto.")

**Técnicas avançadas de correção:**
- **Regra PT-BR**: se a citação é parte da frase → ponto fora. Se a citação é frase completa → ponto dentro
- Padronizar em todo o documento
- "Teste da citação" — se a citação termina com "que", o ponto vai fora

---

### Ressalva com preâmbulo (minimiza → infla)

**Problema:** Padrão de IA de 2025/2026 em que uma minimização genérica é seguida por inflação automática para compensar. O contraste pode ser legítimo e deve ser preservado; o sinal aparece quando a moldura se repete mecanicamente ou quando os dois lados não têm apoio no texto-fonte.

**Antes (IA):**
> Embora pareça um conceito simples, a consistência na publicação de conteúdo representa um dos pilares mais fundamentais e transformadores de qualquer estratégia de marketing digital moderna.
>
> À primeira vista, essa pode parecer uma mudança incremental, mas na verdade constitui uma transformação paradigmática na forma como organizações interagem com seus stakeholders.

**Depois (humano):**
> A consistência na publicação de conteúdo é um dos pilares mais fundamentais e transformadores de qualquer estratégia moderna de marketing digital. Mesmo assim, pode parecer um conceito simples.
>
> A mudança constitui uma transformação paradigmática na forma como as organizações interagem com seus stakeholders, embora à primeira vista possa parecer incremental.

**Evitar em PT-BR:**
- "Embora pareça simples, na verdade é [superlativo]"
- "À primeira vista... mas na verdade constitui..."
- "Pode parecer óbvio, porém [inflação]"
- "Apesar de ser um conceito básico, representa um dos mais [superlativo]"
- Qualquer estrutura que minimiza no preâmbulo e infla na oração principal

**Sinais adicionais de detecção:**
- Estrutura "minimiza → infla" em uma única frase: "Embora pareça simples, é transformador"
- Uso de "na verdade" como ponte entre minimização e inflação
- O preâmbulo é sempre genérico ("parece simples", "à primeira vista") e a inflação é sempre superlativa

**Técnicas avançadas de correção:**
- Preservar os dois lados quando o autor afirma um contraste; remover apenas a moldura repetitiva, sem escolher uma posição nova
- Se o contraste é legítimo, mostrar a tensão com dados somente quando esses dados já estiverem na fonte; caso contrário, manter a formulação qualitativa
- "Teste do podcast host" — se o apresentador diria isso sem soar como vendedor, a frase é honesta
