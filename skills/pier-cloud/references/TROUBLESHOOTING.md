## Troubleshooting

### Erro 401 - Credenciais Inválidas

**Problema**: Autenticação falha com erro 401

**Sintomas**:
```json
{
  "code": "failed",
  "message": "invalid or expired token"
}
```

**Causas Comuns**:
- `client_id` ou `client_secret` incorretos
- Credenciais não cadastradas na plataforma Pier Cloud
- Variáveis de ambiente não carregadas corretamente

**Soluções**:
1. Verificar credenciais no arquivo `.env`
2. Confirmar que as variáveis estão sendo carregadas
3. Validar credenciais com o time da Pier Cloud
4. Verificar se o cliente HTTP está cadastrado na plataforma

### Erro 403 - Acesso Negado

**Problema**: Token válido mas sem permissão para acessar recurso

**Sintomas**:
```json
{
  "code": "authorization/forbidden",
  "message": "Access denied"
}
```

**Causas**:
- Conta sem permissões adequadas
- `tenancy_id` incorreto
- Recurso não pertence ao tenant especificado

**Soluções**:
1. Verificar permissões da conta na plataforma Pier Cloud
2. Confirmar `tenancy_id` correto
3. Contatar administrador para solicitar permissões

### Erro 404 - Recurso Não Encontrado

**Problema**: Endpoint ou recurso não existe

**Sintomas**:
```json
{
  "code": "workspace/not-found",
  "message": "Workspace not found"
}
```

**Causas**:
- `workspace_id` incorreto ou não existe
- `tenancy_id` inválido
- URL do endpoint incorreta

**Soluções**:
1. Listar todos os workspaces primeiro para verificar IDs disponíveis
2. Confirmar URL do endpoint está correta
3. Validar tenancy_id

### Token Expirado

**Problema**: Token JWT expirou após ~1 hora

**Sintomas**:
- Requisições que funcionavam começam a retornar 401
- Erro "invalid or expired token"

**Solução**:

Use o cliente robusto que implementa renovação automática:

```bash
python scripts/pier_cloud_client.py --action list-contexts
```

O cliente `pier_cloud_client.py` renova o token automaticamente antes de expirar.

### Timeout de Conexão

**Problema**: Requisição demora muito ou não responde

**Sintomas**:
- Timeout após 30+ segundos
- Conexão não estabelecida
- Erro de rede

**Soluções**:
1. Verificar conectividade com a internet
2. Testar disponibilidade da API: `curl -I https://api.piercloud.io/auth`
3. Verificar se há proxy ou firewall bloqueando
4. Tentar novamente após alguns minutos

### Rate Limiting (Muitas Requisições)

**Problema**: API retorna erro 429 (Too Many Requests)

**Sintomas**:
- Erro 429 após várias requisições rápidas
- Mensagem sobre limite de taxa

**Soluções**:
1. Usar o cliente robusto que implementa retry automático
2. Reduzir frequência de requisições
3. Implementar delays entre requisições
4. Usar paginação com `page_size` menor se necessário
