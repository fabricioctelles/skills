### Autopilot-stack

Execute [Autopilot-full](autopilot-full.md), sem merge. Use quando o operador recebe os PRs verificados para integrar, inclusive para “autopilot, don't merge”, “stack them, don't ship” e “build the stack, I'll land it”.

1. **Substitua o passo 5 pela entrega em verificado.** Pare quando cada PR estiver verificado e verde no head atual. Entregue os PRs ao operador. Depois da entrega, ninguém faz push sem autorização do operador. Todo prompt de checkpoint cita este arquivo para preservar a regra de não integrar.
2. **Empilhe só PRs dependentes.** Essa é a exceção ao passo 3. Um PR que depende de outro usa a branch dele como base, conforme **Size and stacks** de [opening-a-pr](opening-a-pr.md). O owner faz rebase sobre a branch pai. A raiz faz rebase sobre trunk. Um head novo no PR inferior exige restack dos dependentes pelos respectivos owners. Um patch-id estável preserva os resultados nos termos de [shipping](shipping.md). PRs independentes continuam baseados em trunk.

**Resposta:** abra com o objetivo do usuário. Liste cada PR com link, dependências e veredito no head atual. Informe gates e follow-ups. Substitua a lista do que integrou pela lista do que foi entregue para integração.
