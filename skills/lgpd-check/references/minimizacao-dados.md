# Minimização de Dados — Checks LGPD

## Checks obrigatórios

### Coleta (formulários e APIs)
- [ ] Cada campo de formulário tem finalidade documentada
- [ ] Nenhum campo coleta dados além do necessário para a finalidade declarada
- [ ] Newsletter pede apenas email (não nome, telefone, CPF, cargo)
- [ ] Formulário de contato pede apenas o necessário para responder
- [ ] CPF/RG/documentos de identidade coletados APENAS quando legalmente exigido (ex: emissão de NF)
- [ ] Campos opcionais claramente marcados como opcionais
- [ ] Data de nascimento coletada apenas se há requisito de idade, seguro ou obrigação legal
- [ ] Telefone coletado apenas se há necessidade real de ligação

### Dados sensíveis (Art. 11)
- [ ] Dados sensíveis (raça, religião, opinião política, saúde, biometria, genética, vida sexual) coletados APENAS com consentimento explícito ou exceção legal específica
- [ ] Se coletados: finalidade específica documentada e separada dos dados comuns
- [ ] Dados de saúde tratados apenas por profissionais de saúde ou entidades sanitárias (quando aplicável)

### Armazenamento
- [ ] Identificadores separados de dados comportamentais onde possível
- [ ] Hash ou tokenização aplicados onde o valor bruto não é necessário
- [ ] Dados sensíveis criptografados em repouso
- [ ] Campos de texto livre tratados com expectativa de conter dados pessoais

### Logs e registros técnicos
- [ ] Logs de requisição NÃO registram URLs completas com query strings contendo tokens/dados pessoais
- [ ] Bodies de requisição NÃO são logados em texto plano em produção
- [ ] CPF, dados de saúde e identificadores biométricos NUNCA aparecem em logs
- [ ] IPs anonimizados ou truncados em logs de longa retenção
- [ ] Retenção de logs definida e aplicada automaticamente (não apenas documentada)

### Retenção e eliminação
- [ ] Prazo máximo de retenção definido para cada categoria de dados
- [ ] Job automatizado de eliminação implementado (não apenas política em wiki)
- [ ] Eliminação flui para backups (com prazo de expiração próprio)
- [ ] Critérios de término do tratamento respeitados (Art. 15): finalidade alcançada, período expirado, solicitação do titular, determinação da ANPD
- [ ] Exceções de retenção documentadas (Art. 16): obrigação legal, pesquisa com anonimização, transferência com base legal, uso exclusivo anonimizado

### Privacy by Design (Art. 46)
- [ ] Formulários iniciam com zero campos opcionais — cada adição é justificada
- [ ] Configurações padrão minimizam exposição de dados (ex: perfis privados por padrão)
- [ ] Retenção automatizada — não depende de processos manuais
- [ ] Revisão periódica do mapeamento de dados (trimestral recomendado)
- [ ] RIPD (Relatório de Impacto) preparado para tratamentos de alto risco ou grande volume

### Proporcionalidade
- [ ] Dropdown de país usado em vez de endereço completo quando apenas país importa
- [ ] Endereço de entrega coletado apenas para produtos físicos
- [ ] Dados de localização precisos coletados apenas quando funcionalidade exige
- [ ] Nenhum dado coletado "para uso futuro" sem finalidade definida

## Referências legais

- LGPD Art. 6, II (adequação) e III (necessidade)
- LGPD Art. 11 (dados sensíveis)
- LGPD Art. 15 (término do tratamento)
- LGPD Art. 16 (eliminação de dados)
- LGPD Art. 38 (RIPD — Relatório de Impacto)
- LGPD Art. 46 (medidas de segurança e privacy by design)
- Prioridades de fiscalização ANPD 2026–2027 (privacy by design and by default)
