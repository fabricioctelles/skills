# Scripts de Terceiros e Analytics — Checks LGPD

## Checks obrigatórios

### Inventário de scripts de terceiros
- [ ] Todos os domínios externos contactados pelo site estão mapeados
- [ ] Cada script de terceiro tem finalidade documentada e justificada
- [ ] Classificação por necessidade: estritamente necessário / funcional / analytics / marketing
- [ ] Base legal identificada para cada script que processa dados pessoais (Art. 7)

### Carregamento condicional (consent-gated)
- [ ] Scripts não essenciais carregam APENAS após consentimento opt-in
- [ ] Google Analytics / GA4 não carrega antes do aceite
- [ ] Meta Pixel / Facebook SDK não carrega antes do aceite
- [ ] Hotjar / session replay não carrega antes do aceite
- [ ] YouTube embeds / social embeds não carregam antes do aceite (ou usam modo privacy)
- [ ] Tag Manager configurado para respeitar estado de consentimento
- [ ] Nenhum script de marketing/analytics no `<head>` sem gate de consentimento

### Sinal GPC (Global Privacy Control)
- [ ] Sinal `Sec-GPC: 1` / `navigator.globalPrivacyControl` detectado
- [ ] Quando GPC presente: tratado como "rejeitar todos" para cookies não essenciais
- [ ] Comportamento com GPC documentado na política de privacidade

### Analytics com privacidade
- [ ] Se analytics sem cookies (Plausible, Fathom, Cloudflare Web Analytics): documentar que não requer consentimento
- [ ] Se analytics com cookies (GA4, Matomo com cookies): consentimento opt-in implementado
- [ ] IP anonimizado antes do armazenamento
- [ ] Retenção de dados de analytics definida e limitada
- [ ] Renovação de consentimento a cada 6 meses para analytics com cookies
- [ ] Ferramenta de analytics nomeada na política de privacidade
- [ ] Base legal documentada (consentimento ou legítimo interesse com teste tripartite)

### Transferência internacional via scripts
- [ ] Scripts que enviam dados para fora do Brasil/UE identificados
- [ ] Mecanismo de transferência documentado para cada um (SCCs, consentimento, adequação)
- [ ] Decisão de adequação Brasil-UE (Resolução 32/2026) cobre scripts com servidores na UE
- [ ] Scripts com servidores nos EUA requerem SCCs (Resolução 19/2024) ou consentimento específico

### Controles técnicos de segurança
- [ ] Content Security Policy (CSP) implementada com `script-src` restritivo
- [ ] Subresource Integrity (SRI) para scripts de terceiros com URL estável
- [ ] Referrer-Policy configurada como `strict-origin-when-cross-origin` ou mais restritiva
- [ ] Fontes e bibliotecas self-hosted quando possível (elimina contato com terceiro)

### Responsabilidade do controlador
- [ ] Controlador reconhece responsabilidade pelos dados processados por scripts de terceiros
- [ ] DPA (Data Processing Agreement) executado com cada fornecedor de script que processa dados pessoais
- [ ] Cláusulas LGPD nos contratos: Art. 39, notificação de incidentes em 3 dias úteis, assistência em DSARs
- [ ] Revisão periódica de scripts (trimestral recomendado) — fornecedores mudam práticas
- [ ] Sub-processadores dos fornecedores conhecidos e aprovados

### Session replay e ferramentas de UX
- [ ] Se usa session replay (Hotjar, FullStory, etc.): verificar o que é gravado
- [ ] Campos de senha e cartão de crédito mascarados por padrão
- [ ] CPF e dados sensíveis excluídos da gravação
- [ ] Consentimento explícito obtido antes da gravação
- [ ] Retenção das gravações limitada e documentada

### IA e chatbots de terceiros
- [ ] Chatbots/assistentes de IA embutidos: verificar se processam/armazenam dados pessoais das conversas
- [ ] Verificar se dados de interação NÃO são usados para treinamento de modelos sem consentimento específico
- [ ] ANPD Technology Radar No. 3 (2024): web scraping e IA generativa sob escrutínio
- [ ] Base legal específica para uso de dados em IA (consentimento recomendado)

### Divulgação na política de privacidade
- [ ] Cada ferramenta de analytics nomeada na política
- [ ] Dados coletados por cada ferramenta descritos
- [ ] Período de retenção por ferramenta informado
- [ ] Base legal por ferramenta documentada
- [ ] Transferências internacionais por ferramenta declaradas

## Referências legais

- LGPD Art. 6 (princípios: finalidade, adequação, necessidade, transparência, segurança)
- LGPD Art. 7, I (consentimento como base legal para tracking)
- LGPD Art. 39 (obrigações do operador)
- LGPD Art. 46 (medidas de segurança)
- LGPD Art. 20 (decisões automatizadas — relevante para IA)
- Resolução CD/ANPD No. 19/2024 (transferência internacional)
- Resolução CD/ANPD No. 32/2026 (adequação Brasil-UE)
- ANPD Technology Radar No. 3 (2024) — IA generativa e proteção de dados
- Prioridades de fiscalização ANPD 2026–2027 (publicidade direcionada, IA)
