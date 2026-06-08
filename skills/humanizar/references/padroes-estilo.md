# Padrões de estilo e formatação

Padrões que denunciam texto gerado por IA pela forma visual e estrutural, não pelo conteúdo. Ferramentas de detecção usam esses marcadores como sinais de alta confiança.

---

### Travessão (em-dash) excessivo

**Problema:** IA usa 15-25 travessões por texto médio. Humano brasileiro usa 2-3, e geralmente prefere vírgula, ponto ou parênteses.

**Antes (IA):**
> O projeto — que começou em 2022 — trouxe resultados impressionantes — especialmente na área de dados — e agora está sendo expandido — mesmo com orçamento limitado — para outras regionais.

**Depois (humano):**
> O projeto começou em 2022 e trouxe bons resultados na área de dados. Agora está sendo expandido para outras regionais, mesmo com orçamento apertado.

**Evitar em PT-BR:**
- Mais de 2 travessões por parágrafo
- Travessão onde vírgula resolve
- Encadeamento de apartes com travessão (— X — Y — Z)

---

### Negrito excessivo

**Problema:** IA aplica bold em toda palavra-chave como se o texto fosse um slide. Texto corrido com negrito em cada substantivo importante parece catálogo de produto, não escrita humana.

**Antes (IA):**
> A **plataforma** oferece **integração nativa** com os principais **CRMs do mercado**, garantindo **escalabilidade** e **segurança** para equipes de **vendas** e **marketing**.

**Depois (humano):**
> A plataforma se integra com os principais CRMs do mercado. Funciona bem para equipes de vendas e marketing que precisam escalar sem perder controle de acesso.

**Evitar em PT-BR:**
- Bold em mais de 1-2 termos por parágrafo
- Negrito em palavras comuns (plataforma, equipe, resultado)
- Negrito como substituto de boa estrutura frasal

---

### Listas com cabeçalho inline (bold-first bullets)

**Problema:** IA produz listas onde cada item começa com um termo em negrito seguido de dois-pontos e uma frase descritiva. Parece documentação interna, não texto para leitura.

**Antes (IA):**
> - **Agilidade:** O time reduziu o ciclo de entrega em 40%.
> - **Qualidade:** Os bugs em produção caíram pela metade.
> - **Engajamento:** A satisfação do time subiu 12 pontos no eNPS.

**Depois (humano):**
> O ciclo de entrega caiu 40%, os bugs em produção reduziram pela metade, e o eNPS do time subiu 12 pontos.

**Evitar em PT-BR:**
- Estrutura "**Palavra:** frase explicativa" repetida em série
- Listas de 3+ itens onde prosa corrida resolve
- Forçar categorias artificiais para criar bullets

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

---

### Emojis decorativos

**Problema:** IA enfia emojis em headers e bullets como enfeite. Brasileiro usa emoji em mensagem informal, não em título de seção ou tópico técnico. A presença de 🚀💡✅🎯 em texto profissional é assinatura de máquina.

**Antes (IA):**
> 🚀 **Lançamento:** Produto entra no ar em setembro
> 💡 **Insight:** Usuários preferem onboarding curto
> ✅ **Próximos passos:** Agendar reunião com stakeholders
> 🎯 **Meta:** Crescer 30% no trimestre

**Depois (humano):**
> O produto entra no ar em setembro. A pesquisa mostrou que onboarding curto converte melhor. Próximo passo: reunião com os envolvidos para alinhar a meta de 30%.

**Evitar em PT-BR:**
- Emoji antes de heading ou bullet point
- 🚀💡✅🎯📊 como decoração de estrutura
- Qualquer emoji em texto que não seja mensagem pessoal ou post de rede social

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

---

### Decoração Unicode

**Problema:** IA usa caracteres Unicode decorativos como setas (→, ←, ↗), bullets especiais (•, ▸, ▪), checks (✓, ✗), e separadores (│, ─) que humanos brasileiros não digitam. Teclado brasileiro produz -, *, > e ponto final.

**Antes (IA):**
> Benefícios do novo processo:
> → Redução de 40% no tempo de resposta
> → Aumento na satisfação do cliente
> → Integração com sistemas legados
>
> Stack: React │ Node.js │ PostgreSQL

**Depois (humano):**
> Benefícios do novo processo:
> - Tempo de resposta caiu 40%
> - Satisfação do cliente subiu
> - Integra com sistemas legados
>
> Stack: React, Node.js, PostgreSQL

**Evitar em PT-BR:**
- → como bullet point (usar - ou *)
- │ como separador (usar vírgula, barra ou ponto)
- ✓ e ✗ no corpo do texto (usar "sim/não" ou "funciona/não funciona")

---

### Fragmentos curtos dramáticos

**Problema:** IA produz frases de 1-3 palavras isoladas como parágrafo para criar "impacto". Esse recurso existe em copywriting, mas IA abusa até em texto informativo. Brasileiro escreve assim no Twitter, não em artigo ou email.

**Antes (IA):**
> O mercado mudou.
>
> Radicalmente.
>
> E quem não se adaptar vai ficar para trás. A pergunta não é se, mas quando. O futuro já chegou.
>
> Literalmente.

**Depois (humano):**
> O mercado mudou bastante nos últimos dois anos e quem não se adaptar vai perder espaço. Não é questão de se, mas de quando.

**Evitar em PT-BR:**
- Palavra isolada como parágrafo ("Radicalmente.", "Literalmente.", "Ponto.")
- Mais de um fragmento dramático por texto
- Fragmento + ponto final para criar "peso" artificial

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

---

### Hedging com Preamble (Minimiza → Infla)

**Problema:** Padrão de IA de 2025/2026 onde o texto admite que o assunto é simples ou já conhecido, mas imediatamente em seguida usa linguagem inflada para compensar. É um hedging disfarçado de humildade — "sei que parece óbvio, mas na verdade é TRANSFORMADOR". Humanos ou dizem que é simples (e tratam como simples), ou dizem que é importante (e explicam por quê com dados). Não fazem os dois na mesma frase.

**Antes (IA):**
> Embora pareça um conceito simples, a consistência na publicação de conteúdo representa um dos pilares mais fundamentais e transformadores de qualquer estratégia de marketing digital moderna.
>
> À primeira vista, essa pode parecer uma mudança incremental, mas na verdade constitui uma transformação paradigmática na forma como organizações interagem com seus stakeholders.

**Depois (humano):**
> Publicar com consistência funciona. Não é insight novo — mas quase ninguém faz direito.
>
> A mudança parece pequena. O efeito não é.

**Evitar em PT-BR:**
- "Embora pareça simples, na verdade é [superlativo]"
- "À primeira vista... mas na verdade constitui..."
- "Pode parecer óbvio, porém [inflação]"
- "Apesar de ser um conceito básico, representa um dos mais [superlativo]"
- Qualquer estrutura que minimiza no preamble e infla na main clause
