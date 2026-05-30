# Transferência Internacional de Dados — Checks LGPD

## Checks obrigatórios

### Mapeamento de transferências
- [ ] Todos os serviços/ferramentas que recebem dados pessoais estão mapeados
- [ ] País de destino de cada transferência identificado
- [ ] Finalidade de cada transferência documentada
- [ ] Categorias de dados transferidos identificadas por destinatário

### Mecanismos de proteção (Art. 33)
- [ ] Cada transferência internacional possui mecanismo legal válido:
  - **Decisão de adequação**: UE/EEA (Resolução 32/2026, jan 2026) — transferência direta permitida
  - **SCCs da ANPD** (Resolução 19/2024): texto exato e inalterado, obrigatório desde ago/2025
  - **Consentimento específico e destacado**: informando ao titular sobre riscos e caráter internacional
  - **Normas corporativas globais** (BCRs): aprovadas pela ANPD
  - **Autorização específica da ANPD**: para casos não cobertos acima
- [ ] Não há transferência sem mecanismo documentado

### Adequação Brasil-UE (Resolução 32/2026)
- [ ] Transferências para UE/EEA/EFTA identificadas e documentadas como cobertas pela adequação
- [ ] Limitações conhecidas: não cobre segurança pública, defesa nacional, investigação criminal
- [ ] Monitoramento de eventual revisão da decisão (prazo de 4 anos)

### SCCs brasileiras (Resolução 19/2024)
- [ ] Para transferências fora do eixo Brasil-UE: SCCs da ANPD executadas
- [ ] Texto das SCCs utilizado na íntegra (sem alterações)
- [ ] Tanto controlador quanto operador são responsáveis por comprovar conformidade
- [ ] Avaliação de impacto da transferência (TIA) realizada para destinos sem adequação
- [ ] Sub-processadores no exterior cobertos pelas SCCs

### Serviços comuns que transferem dados internacionalmente
- [ ] Google Analytics / GA4 → verificar se dados vão para EUA (requer SCCs ou consent)
- [ ] AWS / Azure / GCP → verificar região dos servidores e se dados saem do Brasil/UE
- [ ] Mailchimp / SendGrid / HubSpot → EUA (requer SCCs)
- [ ] Stripe / PayPal → EUA (requer SCCs)
- [ ] Intercom / Zendesk → EUA (requer SCCs)
- [ ] Cloudflare → verificar configuração de região
- [ ] Meta Pixel / Google Ads → EUA (requer consentimento + SCCs)

### Divulgação na política de privacidade
- [ ] Transferências internacionais declaradas na política de privacidade
- [ ] Mecanismo de proteção utilizado informado ao titular
- [ ] Países/regiões de destino identificados
- [ ] Não afirma "dados permanecem no Brasil" se usa SaaS com servidores no exterior

### Contratos com operadores internacionais
- [ ] DPA (Data Processing Agreement) executado com cada operador estrangeiro
- [ ] Cláusulas LGPD incluídas: Art. 39, notificação de incidentes em 3 dias úteis, assistência em DSARs, eliminação no término
- [ ] Direito de auditoria previsto no contrato
- [ ] Sub-processadores aprovados e documentados

## Referências legais

- LGPD Art. 33 (hipóteses de transferência internacional)
- LGPD Art. 34 (avaliação do nível de proteção do país destinatário)
- LGPD Art. 35 (cláusulas contratuais e normas corporativas)
- LGPD Art. 36 (autorização específica da ANPD)
- Resolução CD/ANPD No. 19/2024 (regulamento de transferência internacional e SCCs)
- Resolução CD/ANPD No. 32/2026 (decisão de adequação Brasil-UE)
