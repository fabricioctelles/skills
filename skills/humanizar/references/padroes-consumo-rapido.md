# Padrões de Consumo Rápido — Perfis de Escaneabilidade

Padrões específicos para os perfis **Direto**, **Enxuto** e **Resumo**. Esses perfis otimizam para **consumo** (absorção rápida pelo leitor), não para **autoria** (texto que alguém vai assinar). A distinção é fundamental: perfis autorais preservam voz e estilo; perfis de consumo priorizam transferência eficiente de informação.

> **TRAVA FACTUAL neste arquivo:** brevidade comprime *forma*, não *conteúdo*. Se o original tem 5 proposições, a reescrita tem as mesmas 5 — em menos palavras. Cortar molduras e transições; preservar toda proposição, relação causal, número, qualificação de escopo e aviso. Quando um trecho protegido conflitar com a brevidade, a brevidade cede.

---

## Quando Usar Cada Perfil

| Perfil | Público | Formato típico | Otimiza para |
|---|---|---|---|
| ➡️ **Direto** | Tomador de decisão, leitor com atenção fragmentada | E-mail, Slack, briefing, resposta técnica | Escaneabilidade — quem lê só o bold entende |
| 🔹 **Enxuto** | Dev em flow, operador em troubleshooting | Terminal, chat técnico, instrução | Densidade máxima — uma linha quando basta |
| 📋 **Resumo** | Gestor, equipe em standup, stakeholder | Status update, notas de reunião, sprint review | Legibilidade — board de estado, não parágrafo |

**Regra de seleção rápida:**
- Leitor precisa **agir** → Enxuto
- Leitor precisa **decidir** → Direto
- Leitor precisa **acompanhar** → Resumo

---

## Formatação por Perfil

### Marcadores: → vs - vs *

| Contexto | Marcador | Exemplo |
|---|---|---|
| Fluxo ou consequência | → | `→ Resultado: deploy bem-sucedido` |
| Lista comum sem hierarquia | - | `- Item 1` |
| Ênfase em lista | * com negrito | `* **Ponto crítico:** descrição` |

**Regra:** usar `→` apenas para indicar **resultado, consequência ou próximo passo**. Para listas simples, `-` é suficiente. Misturar `→` e `-` no mesmo bloco é sinal de inconsistência.

### Negrito: Funcional vs Decorativo

| Uso | Exemplo | Veredicto |
|---|---|---|
| Lead-in de ponto | **Use PostgreSQL.** App social é... | ✅ Funcional |
| Termo-chave de decisão | ...correto para **~90% de apps** | ✅ Funcional |
| Número crítico | Timeout de **30s** | ✅ Funcional |
| Aviso/warning | **Armadilha comum:** | ✅ Funcional |
| Substantivo comum | A **plataforma** oferece **integração**... | ❌ Decorativo |
| Toda palavra importante | **PostgreSQL** é **bom** para **apps** | ❌ Decorativo |

**Regra:** negrito marca **hierarquia de escaneabilidade** — quem lê só o bold deve entender a resposta completa, a decisão principal e qualquer aviso. Se remover o negrito não prejudica a compreensão rápida, ele é decorativo.

### Emojis: Estado vs Decoração

| Emoji | Função | Perfil |
|---|---|---|
| ✅ | Feito/concluído | 📋 Resumo |
| 🟡 | Em andamento | 📋 Resumo |
| ⬜ | Não iniciado | 📋 Resumo |
| ❔ | Desconhecido | 📋 Resumo |
| 🔴 | Bloqueio/risco | 📋 Resumo |
| 🚀💡🎯✨ | Decoração | ❌ Nenhum |

**Regra:** emojis de estado são **notação funcional** — cada um indica um status específico. Emojis decorativos (🚀💡🎯) não têm função comunicativa e são sinal de IA em qualquer perfil.

### Estrutura do Perfil Resumo

```markdown
**TL;DR:** [Uma linha com resultado + bloqueio principal]

**[Categoria]:**
✅ **Item 1:** status
🟡 **Item 2:** status
⬜ **Item 3:** status

🔴 **Bloqueio:** [Descrição do impedimento]

**Sua vez:**
1. Opção 1
2. Opção 2
3. Opção 3
```

**Regras:**
- TL;DR deve se sustentar sozinho — quem lê só ele entende o essencial
- Um item por linha, negritar o assunto
- Bloqueio sempre em linha própria com 🔴
- "Sua vez" com opções numeradas para o leitor escolher por número
- Nunca inventar status — se desconhecido, marcar ❔

---

## Regras de Corte

### O que SEMPRE Cortar

| Padrão | Exemplo | Por que cortar |
|---|---|---|
| Preâmbulo | "Para responder à sua pergunta..." | Atrasa a resposta |
| Reafirmação da pergunta | "Você perguntou sobre bancos de dados..." | Redundante |
| Filler openers | "Ótima pergunta!", "Com certeza!" | Zero informação |
| Resumo final | "Em resumo, PostgreSQL é a melhor opção" | Repete o que já foi dito |
| Narração de ação | "Vou agora verificar o arquivo..." | Fazer, não narrar |
| Transições mecânicas | "Além disso", "Por outro lado", "Nesse sentido" | Padding |
| Ressalva genérica | "É importante considerar diversos fatores" | Não diz nada |
| Despedida | "Espero que isso ajude!" | Filler |

### O que NUNCA Cortar

| Elemento | Por que preservar |
|---|---|
| Warning/aviso | Omissão pode causar erro do leitor |
| Número exato | "~30s" não é igual a "alguns segundos" |
| Condição de escopo | "Apenas para workspaces < 14 dias" não vira "para workspaces" |
| Modalidade | "Pode causar" não vira "causa" |
| Fonte/atribuição | Quem disse ou de onde veio |
| Exceção mencionada | Restrição faz parte do fato |

**Regra mestre:** se omitir o trecho faz o leitor agir errado, o trecho fica — mesmo que quebre a brevidade.

### Padrões de IA que CONTINUAM se Aplicando

Mesmo em modo conciso, estes padrões denunciam texto de IA:

| Padrão | Descrição | Referência |
|---|---|---|
| Conclusão sinalizada | "Em conclusão", "Em resumo" no final | `padroes-composicao.md` |
| Metáfora morta | "Ecossistema", "jornada", "cenário" repetidos | `padroes-composicao.md` |
| Ressalva vazia | "É importante considerar" sem dizer o quê | `padroes-tom.md` |
| Vocabulário genérico | "Impacto", "contexto", "solução" sem especificidade | `padroes-linguagem.md` |
| Autorreferência | "Como assistente de IA..." | `padroes-tom.md` |

### Padrões SUSPENSOS Nestes Perfis

| Padrão | Suspenso em | Justificativa |
|---|---|---|
| Negrito excessivo | ➡️ Direto, 🔹 Enxuto | Negrito em lead-in é hierarquia, não decoração |
| Fragmentos curtos | 🔹 Enxuto | Uma linha é o formato, não fragmento dramático |
| Decoração Unicode (→) | ➡️ Direto | Seta indica fluxo/consequência, não decora |
| Emoji em cada item | 📋 Resumo | Emojis de estado são notação funcional |
| Listicle disfarçado | 📋 Resumo | Lista É o formato declarado, não disfarce |

---

## Integração com TRAVA FACTUAL

### Princípio: Brevidade por Compressão, não Ablação

```
CORRETO:
  Original (50 palavras) → Reescrita (25 palavras)
  Mesmas 5 proposições, metade das palavras
  
ERRADO:
  Original (50 palavras) → Reescrita (25 palavras)
  3 proposições, 2 foram cortadas
```

### Regra "Cortar Elaboração, Nunca Warning"

```python
para cada trecho do original:
    se trecho é warning/aviso:
        manter integralmente
    se trecho é número/threshold:
        manter exato
    se trecho é condição de escopo:
        manter completo
    se trecho é elaboração/exemplo:
        comprimir ou cortar
    se trecho é transição/filler:
        cortar
```

### Verificação Específica para Perfis de Brevidade

| # | Verificação | ✓/✗ |
|---|---|---|
| 1 | Toda proposição do original permanece, ainda que compactada? | |
| 2 | Nenhum aviso/warning foi removido? | |
| 3 | Nenhuma condição de escopo foi generalizada? | |
| 4 | Modalidade preservada? ("pode" não virou afirmação) | |
| 5 | Números e thresholds permanecem exatos? | |

---

## Exemplos Antes/Depois

### Perfil Direto

**Contexto:** Resposta sobre escolha de banco de dados

**Antes (IA — 87 palavras):**
> Para responder à sua pergunta sobre qual banco de dados utilizar para seu novo aplicativo social, é importante considerar diversos fatores relevantes. PostgreSQL é uma excelente opção para aplicações que necessitam de relacionamentos complexos entre entidades. Por outro lado, MongoDB pode ser mais adequado para cenários específicos onde a flexibilidade de schema é prioritária. Em resumo, a escolha final depende das suas necessidades específicas e do contexto do projeto.

**Depois (Direto — 52 palavras):**
> **Use PostgreSQL.** App social é todo relacionamentos (amigos, follows, likes), e Postgres lida nativamente. Correto para ~90% de apps sociais novos.
>
> **MongoDB só se:** dados sem schema que mudam toda semana, ou volume de escrita que justifique o trade-off.
>
> **Armadilha comum:** começar com Mongo e gastar meses migrando quando precisar de JOIN.

### Perfil Enxuto

**Contexto:** Troubleshooting de erro

**Antes (IA — 54 palavras):**
> Para corrigir esse erro que você está enfrentando, você precisará verificar o arquivo de configuração do seu projeto. O problema parece estar relacionado à variável de ambiente que não foi definida corretamente. Recomendo que você abra o arquivo .env e verifique se a chave DATABASE_URL está presente. Espero que isso ajude a resolver o problema.

**Depois (Enxuto — 12 palavras):**
> Falta `DATABASE_URL` no `.env`. Adicione a linha e reinicie o server.

### Perfil Resumo

**Contexto:** Status de processo de contratação

**Antes (IA — 62 palavras):**
> Com relação ao andamento do projeto de contratação, gostaria de informar que recebemos 20 candidatos até o momento. Destes, 5 foram triados e 2 entrevistas estão agendadas. Ainda não fizemos nenhuma oferta. Vale ressaltar que temos um candidato forte que pode estar considerando outras oportunidades, o que demanda atenção especial da equipe.

**Depois (Resumo — 58 palavras, mas escaneável):**
> **TL;DR:** Pipeline saudável no topo, linha de chegada travada. Candidato forte escorregando.
>
> **Funil:**
> ✅ **Candidatos:** 20 recebidos
> ✅ **Triagem:** 5 de 20
> 🟡 **Entrevistas:** 2 agendadas, não realizadas
> ⬜ **Oferta:** não rascunhada
>
> 🔴 **Bloqueio:** Candidato forte com outras propostas — janela de ~5 dias.
>
> **Sua vez:**
> 1. Fast-track o candidato forte
> 2. Rodar as 2 entrevistas esta semana
> 3. Rascunhar oferta agora

---

## Diferença entre Perfis de Consumo e Perfis Autorais

| Aspecto | Perfis Autorais | Perfis de Consumo |
|---|---|---|
| **Foco** | Voz, estilo, autenticidade | Transferência eficiente de informação |
| **Público** | Leitor que vai ler tudo | Leitor que vai escanear |
| **Formatação** | Mínima, a serviço da voz | Estruturada para navegação |
| **Negrito** | Evitar excesso | Usar para hierarquia |
| **Listas** | Quando natural | Quando facilita consumo |
| **Tom** | Varia por perfil | Consistentemente direto |
| **Exemplos** | Crônica, Jornalístico, Acadêmico | Direto, Enxuto, Resumo |
| **Pergunta-guia** | "Como o autor diria isso?" | "O que o leitor precisa saber?" |

---

## Checklist de Verificação

Antes de entregar texto em perfil de consumo rápido:

- [ ] Primeira frase carrega a resposta/decisão principal?
- [ ] Quem lê só o bold entende o essencial?
- [ ] Nenhum warning/aviso foi cortado?
- [ ] Números e thresholds estão exatos?
- [ ] Condições de escopo estão completas?
- [ ] Zero filler (preâmbulo, despedida, "espero que ajude")?
- [ ] Emojis têm função (estado) ou são decoração?
- [ ] Negrito marca hierarquia ou decora substantivos?
- [ ] TL;DR se sustenta sozinho? (perfil Resumo)
- [ ] Status não foi inventado? (perfil Resumo)
