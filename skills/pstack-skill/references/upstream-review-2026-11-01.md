# Revisão upstream do pstack em 01/11/2026

O objetivo é incorporar as melhorias úteis dos 22 commits pendentes, preservando o catálogo como uma pasta portátil e revisando o novo runtime antes de executá-lo.

O catálogo partiu da versão 1.5 e de `eb4db2b55b2b7dec3d9282754cddf0a56bf4ff10` (pstack 0.15.28). Esta revisão cobre até `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`, de 27/10/2026. A versão local passa a 1.6. O SHA em `UPSTREAM_COMMIT` permanece na referência anterior até o reconhecimento humano pelo comando `accept`.

As fontes foram obtidas de `https://github.com/cursor/plugins.git`, caminho `pstack/`, com o verificador local. O histórico, o diff e os arquivos finais foram comparados com as adaptações existentes. A instalação de `~/.agents/skills/pstack-skill` estava em 1.4; esta tarefa modifica o catálogo, sem atualizar instalações locais.

## Decisões por mudança

| Mudança upstream | Intenção | Contraparte local | Decisão | Justificativa e ação local |
| --- | --- | --- | --- | --- |
| #776 `7698375`, #779 `4ec7ffa`, #791 `076f4b2` | Corrigir o fluxo antigo e melhorar a renderização | [statechart](skills/statechart.md), `scripts/statechart/` | Adaptar | A versão final substitui o fluxo antigo. Removidos `.mjs` e modelo legado; preservada a referência de renderização Pele. |
| #977 `34b1b7c`, #982 `740d2c0`, #981 `519d36a` | Compilar TLA+ para Mermaid, preservar ações qualificadas e testar encerramento de processos | `scripts/statechart/` | Adaptar | Portados compilador TS, launcher POSIX, testes e corpus. Removida a instalação automática de Java/TLC via mise. Testes de renderização exigem opt-in e usam `--ignore-scripts`. |
| #794 `00d5dec` | Ler cada resultado formal TLA+ com statechart | [create-formal-verification-skill](skills/create-formal-verification-skill.md) | Adotar | A skill gerada encaminha cada resultado TLA+ para o procedimento empacotado. |
| #797 `3c0fdb4` | Entregar ketchup como vídeo legendado | [ketchup-video](skills/ketchup-video.md), [poteto-help](skills/poteto-help.md), `SKILL.md` | Adaptar | Procedimento autocontido, ativado por pedido explícito. Detecta renderizador disponível, como FFmpeg. Sem ele ou em falha, entrega as decisões em texto. Não exige serviço de geração, pacote irmão ou upload. |
| #1043 `c742dd6` | Orquestração conduzida pelo agente e remoção de `orch` | [Orchestrate](../playbooks/orchestrate.md) | Adaptar | Agentes nativos e arquivos TSV/Markdown substituem Task e Project tracker. O catálogo já não continha `orch`; simplificado o protocolo local. Sem subagentes, unidades sequenciais em Autonomous run. |
| #986 `ab1f702`, objetivo do usuário | Preservar intenção entre mensagens e agentes | `SKILL.md`, [opening-a-pr](../playbooks/opening-a-pr.md), [autonomous-run](../playbooks/autonomous-run.md), Orchestrate | Adotar | Objetivo reaparece na primeira mensagem, briefs, abertura de `Why` e relatórios finais, sem confirmação adicional. |
| #986 `ab1f702`, interrogate e arena | Manter achados comprovados e diversidade real | [interrogate](skills/interrogate.md), [arena](skills/arena.md) | Adaptar | Achados exigem reprodução, refeita pelo coordenador. As quatro references removidas upstream já não existiam no catálogo. Arena tenta outra família; se indisponível, preserva revisão em contexto novo e declara a ausência de diversidade. |
| #986 `ab1f702`, autopilots e plano | Reduzir verificações repetidas e empilhar só dependências | [autopilot-full](../playbooks/autopilot-full.md), [autopilot-stack](../playbooks/autopilot-stack.md), [multi-phase-plan](../playbooks/multi-phase-plan.md), [babysit](../playbooks/babysit.md) | Adaptar | Stack herda full sem merge. Só dependências formam stack. Findings bloqueiam quando demonstram bug, gate falho ou documentação incorreta. Preservados forge e drivers neutros. |
| #986 `ab1f702`, delegação e medição | Evitar chamadas bloqueantes, slugs rejeitados e números sem decisão | `SKILL.md`, arena, [swarm](skills/swarm.md), [princípios](principles.md#explain-the-number) | Adaptar | Fallbacks usam modelos realmente disponíveis. Briefs de medição nomeiam SHAs e método; decisão e ruído são definidos antes da medição. O validador usa o papel `worker`, sem slug proprietário. |
| #807 `e73df47` | Corrigir numeração e referência à tabela do swarm | [swarm](skills/swarm.md) | Adotar | A numeração local já era sequencial. O relatório agora nomeia explicitamente a tabela de resultados. |
| #805 `f83fbe6` | Ler mtime com GNU e BSD | `scripts/worktree-audit.sh` | Adotar | Detecta `stat -c`/`date -d` ou `stat -f`/`date -r` uma vez. Mantidas as adaptações locais de consulta ao forge. |
| #803 `86c2448` | Reconhecer delimitadores de código inline pareados | `scripts/check-plan.mjs`, `scripts/check-plan.test.mjs` | Adotar | Expressão upstream e regressões CLI portadas para `node:test`, sem exigir Bun. |
| #800 `7054003` | Impedir edições perdidas no cache do plugin | [reflect](skills/reflect.md) | Adaptar | Edita a origem mantida ou uma cópia persistente fora do cache. Respeita autorização já concedida na sessão. |
| #806 `a0b0ad9` | Explicar auto-update no Claude Code | [adaptador Claude Code](harness/claude-code.md#atualização-do-plugin-upstream) | Adaptar | Nota datada e restrita ao plugin upstream. Não apresenta configuração de marketplace como atualizador desta pasta. |
| #801 `96dec8e`, #802 `fe096ef` | Corrigir descoberta de forks e deadline de polling em watch-pr | [babysit](../playbooks/babysit.md), sem script `watch-pr` local | Rejeitar | Os scripts específicos não são distribuídos neste porte. As consultas seguem o forge e os PRs indicados. Não foi introduzida uma nova camada de polling. |
| #804 `3c596e7` | Preferir PR ativo no runtime orch | Orchestrate, sem runtime `orch` local | Rejeitar | Runtime ausente no catálogo e removido pelo próprio #1043. Estado de PR vem da consulta ao forge. |
| #792 `642289e`, #798 `b1a1298`, #978 `7c7bde7`, #983 `164ced1`; manifests e guias do plugin | Versionar e documentar a distribuição Cursor | `SKILL.md`, [README](../README.md) | Adaptar | Versão própria 1.6 e documentação do comportamento portado. Não copiar manifests, árvores geradas nem versões do plugin. |

## Revisão do runtime

Foram lidos os fontes TypeScript de execução e o launcher antes dos testes. Não apareceu exfiltração, coleta de credenciais, comando de instalação oculto ou comportamento suspeito.

- O launcher verifica versões no `PATH`, segue symlinks e usa `exec` para Node 22.18 a 22.x, Node 23.6+, Bun 1.1.5+ ou Deno 2+. Ele não baixa runtimes.
- O compilador upstream instala Java/TLC via mise quando `TLA2TOOLS` falta. Esse comportamento foi removido. O porte exige `TLA2TOOLS` e usa `JAVA` ou `java` no `PATH`.
- Os subprocessos recebem argumentos separados. Os comandos de `/bin/sh` usam texto estático e parâmetros posicionais entre aspas. Encerram o grupo de processos e removem os temporários criados pelo comando.
- A saída é preparada fora do destino e publicada por rename somente após uma execução concluída. O destino precisa ser novo ou vazio. Falha ou interrupção não publica resultado parcial.
- `--view` executa código com as permissões do runtime. A documentação exige leitura prévia e código confiável. Deno recebe permissões de leitura, escrita, subprocessos e ambiente; a view não é sandbox.
- Executar o compilador não exige pacotes npm. `fast-check` é dependência de desenvolvimento. Os testes de renderização só instalam Pele/Mermaid/jsdom com `PSTACK_RENDER_TESTS=1`, fora do repositório e com `--ignore-scripts`.
- O jar oficial TLC 1.7.4 usado na validação foi conferido contra SHA-256 `936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88`.

## Validação executada

| Verificação | Resultado |
| --- | --- |
| Suíte completa do compilador com TLC 1.7.4 e Java 25 | 367 testes passaram; nenhum skip ou falha. Executada em cópia do porte com o runtime já sem mise. |
| Testes finais locais de dependência e renderização com opt-in | 75 passaram. Cobrem as mudanças posteriores no caminho da referência e no opt-in do renderer. |
| Mesmos arquivos sem opt-in | 2 passaram e 73 testes de renderer foram pulados, sem instalar renderers. |
| Modelo Counter pelo launcher local | Node 26.12.1, Bun 1.4.4 e Deno 2.9.8 produziram o relatório com 4 estados e status 0. |
| Modelo CounterRules pelo launcher local | Status 1 e caminhos mínimos para três regras violadas; preservada a ação qualificada `M!Jump`. |
| Encerramento SIGINT/SIGTERM/SIGKILL | A suíte CLI confirmou limpeza, encerramento de filhos e ausência de saída parcial em Linux com `/bin/sh`. |
| `node --test scripts/check-plan.test.mjs` | 7 testes passaram, incluindo delimitadores múltiplos, não pareados e pontuação fora do span. |
| Skeleton de multi-phase-plan extraído e validado | `1 PR sections, 0 problems`. |
| worktree-audit com repositório/worktree/transcrição temporários | GNU coreutils leu `LAST_CHAT=2026-10-01` do mtime fixado no fixture. Não houve exclusão de worktree do usuário. |
| Viabilidade de ketchup-video | FFmpeg gerou MP4 H.264 silencioso, 960×540, 8,5 s, com dois slides conectados, transição e legendas. ffprobe confirmou a mídia; um frame de cada slide foi inspecionado. |
| Sintaxe shell, links Markdown locais e whitespace do diff | Validados. |

Os logs, o fixture de vídeo e o jar de teste desta sessão estão em `/tmp/pstack-port.OEwj13/`. São evidências temporárias. Os testes reproduzíveis do compilador e do validador acompanham a skill.

Para repetir as verificações do compilador, siga [Validar o compilador](skills/statechart.md#validar-o-compilador). Os limites mínimos dos três runtimes seguem o upstream; os smokes desta sessão usaram as versões listadas, não todas as versões aceitas pelo launcher. A variante BSD do audit não foi executada neste host Linux.

Uma revisão independente dos documentos encontrou uma frase ambígua sobre ausência de achados e uma contradição entre o fallback de arena e o contrato de degradação. Ambas foram corrigidas. Nenhuma referência executável ao CLI antigo da statechart permaneceu.

## Reconhecimento da referência

Após a revisão humana do diff, o mantenedor pode reconhecer o SHA coberto:

```sh
./scripts/check-upstream.sh accept c742dd61706fbacc1b95f1a20b7b988cf096ce6c
```

Esse comando só funcionará se o SHA ainda for a última alteração upstream em `pstack/`. Se houver uma versão posterior, revise o delta adicional antes de reconhecê-la.
