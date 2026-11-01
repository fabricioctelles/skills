# Statechart

Cheque com TLC um modelo TLA+ de um sistema que muda de estado e desenhe o resultado como um statechart Mermaid. O relatório mostra o caminho mais curto até cada regra de estado quebrada. Para propriedades temporais, mostra o contraexemplo do TLC, que pode conter um ciclo.

Escreva os estados e as transições nas palavras da pessoa que lê o gráfico. Essa pessoa decide se o comportamento está correto.

## Executar

Trabalhe em uma pasta temporária fora do repositório. Escreva a especificação TLA+ e seu arquivo de configuração. Execute:

```sh
TLA2TOOLS=/caminho/absoluto/tla2tools.jar JAVA=/caminho/absoluto/java \
  <pstack-skill>/scripts/statechart/statechart SPEC.tla \
  [--config ARQUIVO] [--view ARQUIVO] [--out PASTA]
```

O launcher POSIX escolhe o primeiro runtime compatível disponível no `PATH`. Aceita Node 22.18 a 22.x, Node 23.6 ou posterior, Bun 1.1.5 ou posterior, ou Deno 2.0 ou posterior. Não exige compilação nem pacotes npm para executar. O runtime e o launcher usam `/bin/sh` para encerrar os processos filhos e limpar os temporários; use um ambiente POSIX.

Instale TLC e Java separadamente. Defina `TLA2TOOLS` como o caminho do `tla2tools.jar`. `JAVA` é opcional quando `java` já está no `PATH`; requer Java 11 ou posterior. O upstream usa TLC 1.7.4, cujo jar oficial tem SHA-256 `936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88`. Este porte não instala dependências automaticamente e pode funcionar sem rede com essas dependências locais.

O comando só publica arquivos em uma pasta nova ou vazia. O padrão é `SPEC-chart`; prefira um novo `--out` em cada execução. As saídas são `report.md`, `chart.mmd`, `tlc.out` e, quando necessário, `tlc-REGRA.out`. O status é `0` quando todas as regras passam, `1` quando uma regra quebra e `2` quando não foi possível checar. SIGINT e SIGTERM retornam `130` e `143`. Erros e interrupções não publicam saídas parciais.

`--view` importa e executa um módulo JavaScript ou TypeScript com as permissões do runtime. Leia esse módulo antes de executá-lo e use somente código confiável. A view não é uma configuração isolada nem uma sandbox. O launcher Deno concede leitura, escrita, execução de subprocessos e acesso a variáveis de ambiente.

O compilador substitui os comandos antigos `from-spec` e `from-chart`. Não existe conversão automática de Mermaid para TLA+ neste fluxo. Para começar de um gráfico, escreva o modelo que representa o comportamento acordado e cheque-o com o mesmo comando.

## Escrever o modelo

- Escreva cada regra acordada com o leitor como um `INVARIANT`. Pode tratar de uma tela, um resultado, um valor persistido ou uma mensagem. Se falta uma variável para expressar uma regra, acrescente a variável. Nunca enfraqueça uma regra para fazê-la passar.
- Defina `Next` como uma disjunção das ações, por exemplo `YouPressPlay \/ YouPressStop`. Caso contrário, o TLC pode chamar todas as transições de `Next`.
- Um estado sem saída quebra `NoDeadlock`, mesmo quando representa um término correto. Se um `INVARIANT` ou uma `PROPERTY` já tiver esse nome, a regra de deadlock recebe o nome `CHECK_DEADLOCK`. Para um término correto, acrescente a `Next` uma ação verdadeira somente nos estados finais, sem alterar variáveis, por exemplo `Done == phase \in {"paid", "failed"} /\ UNCHANGED vars`. Dê um rótulo a ela em `step()`.
- Se houver uma especificação do código, comece de uma cópia dela. Preserve as regras existentes. Relacione cada variável e ação ao código que um revisor pode abrir. Modele cada ação como um passo indivisível do código.

## Escolher os rótulos

Coloque o título, os rótulos e as cores em um módulo passado por `--view`. A exportação `state(vars)` determina a forma do gráfico:

- Uma string gera um gráfico plano. Exemplo `export const state = (v) => v.paid ? "Pago" : "Pagando";`.
- Um array gera estados pais. Exemplo `export const state = (v) => v.main.split(".");`.
- Um objeto gera uma região paralela por chave. Exemplo `export const state = (v) => ({ Reprodução: v.playback, Volume: v.volume });`.

Nomeie os estados pelo que o leitor vê ou precisa entender, como “Pagando” ou “Lease adquirido, escrita pendente”. Evite nomes de variáveis. Em `vars`, uma sequência TLA+ é um objeto com chaves a partir de `1`; `v.pc[1]` corresponde a `pc[1]`. Um conjunto é um array.

A view também pode exportar `step(action, from, to)`. Ela recebe o nome da ação do TLC e os valores antes e depois da transição. Retorne o rótulo da seta na linguagem do leitor, como “você aperta play” ou “a conexão falha”. Ações com o mesmo efeito visível recebem o mesmo rótulo e compartilham uma seta.

Quando uma transição depende de uma condição, acrescente-a entre colchetes, por exemplo “você aperta play [enquanto o arquivo carrega]”. Em gráficos com regiões, o compilador já escreve condições sobre outras regiões, como `[when Offline]`. Seus colchetes substituem essa condição automática. Por isso, não escreva colchetes para uma condição sobre outra região. Quando um valor que nenhum rótulo mostra decide o destino, nomeie o resultado da ação, como “a leitura da lista falha”.

Exportações opcionais:

- `group(vars)` retorna o nome de uma fase. Um estado recebe a cor da fase somente quando todos os estados de modelo que ele agrupa pertencem à mesma fase.
- `colors` atribui a cada nome de grupo uma classe entre `blue`, `orange`, `purple`, `yellow`, `teal`, `tan` e `pink`.
- `title` é uma string exibida no topo do gráfico.

Cada função depende somente de seus argumentos. O compilador chama `state()` e `group()` no máximo uma vez por estado de modelo e `step()` no máximo uma vez por transição. O gráfico e o relatório usam essas mesmas respostas.

O gráfico omite transições que ficam no mesmo rótulo. Separe o rótulo quando o leitor precisar enxergar essa transição.

Busque cerca de 20 setas ou menos. Primeiro agrupe valores com o mesmo comportamento e omita detalhes irrelevantes, como uma chamada em andamento cujo retorno não altera nada. Preserve os estados dos caminhos de bugs e suas marcas. Se um agrupamento troca `breaks` por `mayBreak`, ele esconde onde a regra quebra. Não agrupe estados que quebram regras diferentes.

Se ainda houver setas demais, `step()` pode retornar `null` para ocultar transições que não ajudam o leitor. Preserve estas condições:

- Cada estado desenhado continua alcançável por setas desde um estado inicial.
- Cada estado com uma saída no modelo mantém ao menos uma saída no gráfico.
- Oculte todas as transições de uma seta ou nenhuma delas. Ocultar apenas algumas estreita sua condição.
- Informe na entrega quais transições foram ocultadas.

## Ler o resultado

- Um estado que quebra uma regra recebe a classe `breaks`. Quando somente parte dos estados de modelo agrupados nele quebra a regra, recebe `mayBreak`. A legenda nomeia as regras de cada marca. Quando uma marca representa várias regras, explique quais estados quebram quais regras. Em regiões paralelas, uma combinação que quebra uma regra deve ter ao menos uma marca; as marcas podem representar condições combinadas.
- A exploração do gráfico continua depois de um estado que quebra uma regra. O gráfico pode mostrar o que acontece depois do bug.
- Use constantes pequenas ou uma `CONSTRAINT` para limitar modelos infinitos.
- Com `VIEW` ou `SYMMETRY`, TLC agrupa estados equivalentes. O gráfico desenha o representante. Uma seta pode levar ao representante em vez do estado literal alcançado; o relatório informa essa redução.
- TLC checa regras em estados além de uma `CONSTRAINT` ou `ACTION_CONSTRAINT`, mas não os explora nem os checa para deadlock. O gráfico inclui esses estados e transições quando encerram o caminho mais curto de uma regra quebrada. Outros estados além do limite não aparecem. TLC também pode checar regras depois de uma transição que `ACTION_CONSTRAINT` exclui, mesmo quando já chegou ao mesmo estado por outro caminho.
- O comando checa as regras com o arquivo de configuração como escrito e um worker. Quando uma regra quebra, remove essa regra e roda TLC de novo até nenhuma quebrar. Depois da primeira quebra, cada execução para em 100.000 estados distintos. Um limite ou erro deixa as regras pendentes em “Rules not checked”. Não trate uma regra não checada como aprovada. Para checá-la, remova as regras quebradas da configuração ou reduza o modelo. O módulo que limita estados pode alterar a ordem de variáveis do TLC e produzir um contraexemplo temporal diferente.
- `tlc.out` contém a saída da checagem com a configuração original. Quando uma regra quebra fora do gráfico ou uma propriedade temporal quebra, `tlc-REGRA.out` preserva o contraexemplo correspondente. Com `-XX:+UseParallelGC`, o TLC puro pode repetir o primeiro aviso; `tlc.out` o mostra uma vez, conforme o protocolo que o comando lê.

## Mostrar e entregar

Mostre `chart.mmd` em um bloco `mermaid`. O limite do gráfico completo é de 500 estados contados pelo TLC na configuração original. Acima disso, o gráfico mostra somente caminhos de regras quebradas. Se nenhuma regra quebra, não há `chart.mmd`. O relatório ainda contém a contagem e os caminhos encontrados. Reduza o modelo para visualizar o grafo completo.

Quando o usuário pedir uma imagem, ou o gráfico ficar grande demais como texto, siga [Renderizar um gráfico](statechart/render.md). O procedimento usa Pele. Use outro renderer somente se o usuário pedir.

Entregue o gráfico e seu Mermaid a quem precisa decidir. Para cada bug, informe a regra, sua frase na linguagem do leitor e o caminho numerado no relatório. Explique o que o modelo omite e dê o comando de reprodução com um novo `--out`.

Quando o modelo descreve código, reproduza cada caminho no código real, por teste ou execução ao vivo, com um passo por ação do modelo. Se o bug não ocorrer, assuma que o modelo está errado até demonstrar o contrário. Corrija o modelo, não a regra.

## Validar o compilador

Para executar os testes Node, instale explicitamente as dependências de desenvolvimento de `scripts/statechart/package.json` com `npm install --ignore-scripts`. Depois execute `npm test` nessa pasta. Os testes que precisam de TLC são pulados quando `TLA2TOOLS` não está definido. Os testes de renderização instalam Pele, Mermaid e jsdom em um cache fora do repositório somente quando `PSTACK_RENDER_TESTS=1`; essa opção exige rede no primeiro uso. Sem ela, `npm test` não instala renderers. O teste do tema CSS continua local.
