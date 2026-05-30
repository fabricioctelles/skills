# Consentimento de Cookies — Checks LGPD

## Checks obrigatórios

### Modelo de consentimento
- [ ] Modelo opt-in implementado — nenhum cookie não essencial é setado antes do aceite
- [ ] Consentimento é prévio, livre, informado e inequívoco
- [ ] Nenhuma caixa pré-marcada (Art. 8, §4 — consentimento genérico é nulo)
- [ ] Scroll ou navegação NÃO são tratados como consentimento
- [ ] Cookie walls restritos — acesso ao conteúdo não é condicionado ao aceite de cookies

### Banner de consentimento (primeira camada)
- [ ] Banner exibido antes de qualquer cookie não essencial ser setado
- [ ] Resumo conciso das finalidades apresentado
- [ ] Botão "Aceitar Todos" presente
- [ ] Botão "Rejeitar Todos" presente com **mesma proeminência visual** (tamanho, cor, posição)
- [ ] Link "Gerenciar Preferências" disponível
- [ ] Link para Política de Privacidade incluído
- [ ] Banner em **português** para visitantes brasileiros
- [ ] Sem dark patterns (cores manipulativas, linguagem tendenciosa, botão de rejeitar escondido)

### Modal de preferências (segunda camada)
- [ ] Toggles granulares por categoria de finalidade (analytics, marketing, personalização)
- [ ] Cookies estritamente necessários identificados e não desativáveis
- [ ] Base legal por finalidade indicada (se aplicável)
- [ ] Lista de cookies/tecnologias específicas por categoria (recomendado)
- [ ] Botão de salvar preferências funcional

### Comportamento pós-consentimento
- [ ] "Rejeitar" efetivamente bloqueia todos os cookies não essenciais
- [ ] Nenhum fallback de fingerprinting quando cookies são rejeitados
- [ ] Scripts de analytics/marketing só carregam após aceite explícito
- [ ] Google Analytics, Meta Pixel, Hotjar etc. NÃO carregam antes do consentimento

### Revogação e renovação
- [ ] Link/ícone persistente no rodapé para reabrir preferências a qualquer momento
- [ ] Revogar consentimento é tão fácil quanto concedê-lo (1 clique)
- [ ] Consentimento renovado a cada **6 meses** (requisito LGPD)
- [ ] Re-solicitação apenas quando finalidades mudam, não a cada visita

### Registro de consentimento
- [ ] Timestamp (ISO 8601) registrado para cada ação de consentimento
- [ ] Escolhas feitas (quais finalidades aceitas/rejeitadas) armazenadas
- [ ] Versão da política vigente no momento do consentimento registrada
- [ ] Jurisdição detectada registrada (para sites multi-região)
- [ ] Registros mantidos por no mínimo **18 meses**
- [ ] Controlador consegue comprovar que consentimento válido foi obtido (ônus da prova — Art. 8, §2)

### Cookies estritamente necessários (isentos de consentimento)
- [ ] Apenas cookies genuinamente necessários são isentos: sessão, login, carrinho, segurança, load balancing
- [ ] Analytics, A/B testing, social embeds e marketing NÃO são classificados como "necessários"

### Proteção de crianças
- [ ] Se o site pode ser acessado por menores: mecanismos de consentimento adequados à idade
- [ ] Consentimento parental implementado para dados de crianças (Art. 14)

## Referências legais

- LGPD Art. 7, I (consentimento como base legal)
- LGPD Art. 8 (requisitos de consentimento: livre, informado, inequívoco, específico, revogável)
- LGPD Art. 8, §4 (consentimento genérico é nulo)
- LGPD Art. 8, §5 (revogação a qualquer momento)
- LGPD Art. 14 (dados de crianças e adolescentes)
- Orientação ANPD 2023 sobre cookies e rastreadores
- Prioridades de fiscalização ANPD 2026–2027 (publicidade direcionada)
