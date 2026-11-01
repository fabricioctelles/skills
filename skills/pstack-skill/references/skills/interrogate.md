# Interrogate

Adversários tentam quebrar uma mudança ou um design. Só mantenha um achado quando uma execução o comprovar. Reporte os achados. Não aplique correções.

## Delimite

Use o escopo indicado pelo usuário. Caso contrário, examine o diff desde o merge base com a branch base até a árvore de trabalho, incluindo mudanças não commitadas e arquivos novos relevantes. Reafirme a intenção com [in-your-own-words](in-your-own-words.md), a partir do pedido, dos commits e da descrição do PR. Pergunte ao usuário se a intenção continuar incerta depois de examinar as fontes disponíveis.

## Distribua

Siga a fase A, passos 3 e 4, e a fase B de [arena](arena.md). Escolha adversários com os papéis `judge` e `peer`, conforme [setup-pstack](setup-pstack.md), em vez de candidatos a implementação. Use agentes de propósito geral com escrita restrita ao próprio worktree, pois precisam executar reproduções. Copie as mudanças não commitadas e os arquivos novos do escopo para cada worktree. Sem subagentes, faça passes independentes sequenciais em cópias isoladas, registrando a limitação. Cada adversário recebe o mesmo escopo, a intenção e este brief:

> Quebre esta mudança. Comprove cada achado com uma execução contra o código real, como um teste que falha, um script de reprodução ou a saída de um comando que mostre o comportamento errado. Para um design ou plano, execute um protótipo ou uma sondagem da árvore atual. Mantenha reproduções no seu próprio worktree. Reporte cada achado com título, comando exato, saída observada e saída exigida pela intenção. Omita o que não executou, incluindo críticas de estilo, nomes ou estrutura sem falha demonstrada e riscos que só existiriam após uma mudança futura. Não encontrar achados também é um resultado válido.

## Verifique

Verifique cada achado conforme arena, fase F, executando seu comando novamente. Mantenha-o quando a saída demonstrar uma falha que contrarie a intenção. Descarte os demais. Una achados com a mesma causa raiz.

Pule as fases C, D e E de arena. Os adversários encontram falhas diferentes. O veredito mantém todos os achados comprovados, em vez de escolher a lista de um adversário.

## Entregue

- **Intenção.** O objetivo reafirmado.
- **Achados.** Para cada achado comprovado, o comando, sua saída, como a falha contraria a intenção e quais adversários a encontraram. Diga “nenhum achado comprovado” quando nenhum sobreviver.
- **Descartados.** Para cada adversário, a quantidade de achados descartados e os motivos.
