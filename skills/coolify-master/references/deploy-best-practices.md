# Boas praticas de deploy no Coolify

## Escolha do build pack

### Dockerfile

Prefira `Dockerfile` quando:
- a app usa SSR ou modo hybrid
- voce precisa de runtime controlado
- a porta, imagem ou comando de start precisam ser explicitos
- health check confiavel e importante
- rolling update importa

### Static

Prefira `Static` quando:
- a aplicacao gera apenas artefato estatico final
- nao existe endpoint server-side no mesmo deploy
- a saida publicada e um diretorio como `dist` ou `out`

### Nixpacks

Prefira `Nixpacks` quando:
- o projeto segue convencoes comuns do ecossistema
- voce quer menos manutencao de imagem
- nao ha necessidade clara de Dockerfile customizado

### Docker Compose

Prefira `Docker Compose` quando:
- ha varios servicos que precisam subir juntos
- a stack depende de definicao compose real

Evite `Docker Compose` quando:
- existe apenas uma app web simples
- o objetivo e tirar proveito de rolling updates da aplicacao principal

## Variaveis de ambiente

Separe por fase:
- **build variable**: so o que precisa existir durante o build
- **runtime variable**: segredos e configuracoes lidas pela app em execucao

Regras:
- segredo de runtime nao deve entrar no build sem necessidade real
- se o segredo for realmente de build, prefira recursos seguros do Docker/BuildKit quando disponiveis
- mantenha `HOST=0.0.0.0` e `PORT` coerente com a app

## Porta e binding

Checklist minimo:
- a app escuta em `0.0.0.0`
- a app escuta na mesma porta cadastrada no recurso
- o proxy aponta para a porta certa

## Health checks

Boas praticas:
- usar endpoint simples como `/healthz` ou `/api/healthz`
- retornar `200` quando a instancia esta apta a receber trafego
- nao depender de integracao externa instavel para o health principal

Observacoes:
- health checks controlam trafego no proxy
- health checks corretos melhoram confiabilidade do deploy

## Rolling updates

Rolling updates dependem de:
- health check valido
- container saudável
- configuracao compativel com o modelo de update

Nao presuma rolling update em deploy com `Docker Compose`.

## Domains, HTTPS e DNS

Regras:
- cadastrar FQDN completo, por exemplo `https://app.exemplo.com`
- confirmar DNS antes de concluir que o certificado falhou
- definir estrategia clara para `www` vs `non-www`

Se aparecer certificado self-signed, suspeite primeiro de DNS ou falha na emissao do Let's Encrypt.

## Persistencia

Padrao:
- trate apps web como stateless

Use storage persistente apenas quando:
- a app realmente grava estado em disco
- o dado nao pode ser descartado entre deploys

Evite compartilhar bind mounts entre varios containers sem necessidade real.

## Self-hosted

Em ambiente self-hosted, inclua no checklist:
- firewall
- patching do host
- espaco em disco
- backups
- observabilidade minima

## Fontes oficiais recomendadas

- Dockerfile: https://coolify.io/docs/applications/build-packs/dockerfile
- Static: https://coolify.io/docs/applications/build-packs/static
- Environment Variables: https://coolify.io/docs/knowledge-base/environment-variables
- Domains: https://coolify.io/docs/knowledge-base/domains
- Health Checks: https://coolify.io/docs/knowledge-base/health-checks
- Rolling Updates: https://coolify.io/docs/knowledge-base/rolling-updates
- Persistent Storage: https://coolify.io/docs/knowledge-base/persistent-storage
