### Orchestrate

**Você conduz o programa e verifica o que os agentes produzem. Os owners escrevem o código.** Use para um projeto contínuo de vários dias, com muitos PRs e subagentes, entregue a um coordenador. Uma tarefa conduzida até um predicado pertence a Autonomous run. Uma execução que precisa de um fluxo próprio pertence a figure-it-out. Se um agente consegue terminar no orçamento da sessão, use Autonomous run.

Use o mecanismo nativo de subagentes do harness. Sem subagentes, reduza a execução a unidades sequenciais em Autonomous run. Não instale um runtime de orquestração. Prefira notificações de conclusão e assinaturas de eventos de PR e CI quando disponíveis. Sem eventos, confira o estado nos checkpoints e use apenas um watcher em background com intervalo limitado. Não crie um segundo loop de polling nem retransmita mensagens de status entre agentes.

#### Estado persistente

Guarde o estado em `orchestrate/<projeto>/`, sob o diretório de trabalho. Use arquivos legíveis sem ferramentas específicas. Cada arquivo tem um único responsável pela escrita.

- `preferences.md` registra o objetivo do usuário e as ordens permanentes. Cada novo brief leva essas ordens e todo o contexto necessário.
- `units.tsv` registra unidade, owner, estado, branch, PR, head SHA e caminho do brief.
- `ledger.tsv` registra os vereditos e as evidências por PR e head SHA. Um novo head exige um novo veredito.
- `decisions.tsv` mantém a trilha de [show-me-your-work](../references/skills/show-me-your-work.md).
- `gates.md` registra as decisões que dependem do usuário. `status.md` resume o estado atual a partir dos registros e da consulta ao forge.

Use o tracker nativo do harness se ele existir, mantendo referências aos artefatos persistentes. Sem tracker, os arquivos acima bastam. Não mantenha cópias concorrentes do mesmo estado.

#### Topologia

- **Um owner por PR.** Ele é o único escritor da branch e acompanha o PR da construção ao merge, dentro da autorização do usuário. Só ele faz push, rebase ou retarget. Fechar ou retargetar um PR base pode deixar descendentes sem base, por isso exige a decisão do coordenador. O coordenador não escreve código. Conflitos, rebases da cadeia e correções voltam aos owners.
- **Um agente novo por tarefa independente.** O brief reafirma o objetivo do usuário e inclui os relatórios anteriores de que a unidade depende. Workers não veem seus irmãos. Dê a cada escritor um worktree ou checkout isolado. Trabalho que usa autenticação local, simulador, transcrições ou a superfície real executa onde esses recursos existem. Use os papéis de [setup-pstack](../references/skills/setup-pstack.md).
- **Um subcoordenador só quando uma área tiver muitos workers.** Ele mantém os briefs da área e devolve um resumo consolidado. Limite a árvore a coordenador, subcoordenadores e workers. Respeite o limite de concorrência do harness e reponha a janela conforme cada agente termina, sem esperar uma onda inteira.
- **Preserve estado de agente só quando necessário.** Use fork ou retome um agente apenas quando a tarefa precisa do checkout, das alterações não commitadas ou de um processo que ele ainda executa. Caso contrário, crie um agente novo com o escopo consolidado. Mensagens ao worker servem para direcionar o trabalho em andamento. Nunca envie uma mensagem só para verificar se está vivo.
- **Cada PR tem um verificador que não o escreveu.** Use outra família de modelo quando disponível. Sem essa diversidade, registre a limitação e faça uma verificação independente com contexto novo. O owner só integra após um passe no head atual e dentro da autorização vigente. Na falta de merge autorizado, para em merge-ready.
- **Comece com uma unidade.** Passe por brief, owner, verificação e merge autorizado ou entrega em merge-ready antes de ampliar a execução. Para unidades baratas e semelhantes, a primeira unidade já é esse teste.

#### Supervisão

- **Cada brief nomeia a evidência de conclusão.** Dê o comando e a saída esperada, a verificação na superfície real ou o artefato exigido. Inclua o objetivo, os caminhos permitidos e proibidos e as ações vedadas. Sem evidência definida, a unidade ainda não tem escopo.
- **Leia o diff ou o artefato.** A síntese do worker e CI verde não substituem verificação. Comportamento exige mais que typecheck. Cada veredito vale para um head SHA. Examine uma amostra dos briefs dos subcoordenadores enquanto seus workers executam e corrija as instruções quando a amostra falhar.
- **Devolva trabalho que sai do escopo.** Corrija só o que bloqueia o programa. Registre o restante como follow-up.
- **Consulte o estado real antes de reportar.** Use `gh pr view` e `gh pr checks`, ou os equivalentes do forge. Reconcilie cada agente iniciado como concluído, substituído ou absorvido por outra unidade.
- **Substitua agentes que travam ou repetem tentativas sem progresso.** Observe commits, pushes, PRs e evidências, em vez do texto de status. Após limite de contexto ou memória, reduza o escopo. Após queda de conexão, tente o mesmo brief. Após erro de ferramenta, use outro modelo disponível. Depois de duas tentativas, descarte a unidade e reprograme. Um agente aguardando uma decisão sua ou do usuário precisa de resposta. Se um agente encerrado retornar tarde, compare sua saída com o head atual e transfira achados únicos para um agente novo.
- **Leve ao usuário só decisões reais ou bloqueios.** Inclua ações irreversíveis fora da autorização vigente, escolhas de produto que nenhum experimento resolve e impasses que sobreviveram a uma revisão do plano. Rebase, flake de CI, triagem e “devo continuar?” ficam com o coordenador.

**Resposta:** abra com o objetivo e o que foi entregue. Liste cada PR com link, estado consultado no forge e veredito no head atual. Informe o que foi descartado, por quê, as decisões pendentes e os caminhos do estado persistente e da trilha.
