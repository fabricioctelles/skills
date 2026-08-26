#!/usr/bin/env bash

set -euo pipefail

readonly upstream_url="https://github.com/cursor/plugins.git"
readonly upstream_branch="main"
readonly upstream_path="pstack"
readonly skill_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
readonly state_file="${skill_dir}/UPSTREAM_COMMIT"
readonly cache_base="${XDG_CACHE_HOME:-${HOME}/.cache}"
readonly upstream_cache="${PSTACK_UPSTREAM_CACHE_DIR:-${cache_base}/pstack-skill/upstream.git}"

usage() {
  printf '%s\n' \
    "Uso:" \
    "  $0 [check [<commit>]]" \
    "  $0 review-prompt" \
    "  $0 accept <commit>"
}

fail() {
  printf 'Erro: %s\n' "$1" >&2
  exit 2
}

validate_commit() {
  [[ "$1" =~ ^[0-9a-f]{40}$ ]] || fail "commit inválido: $1"
}

read_reference() {
  local reference
  [[ -f "$state_file" ]] || fail "arquivo de referência ausente: $state_file"
  reference="$(tr -d '[:space:]' < "$state_file")"
  validate_commit "$reference"
  printf '%s\n' "$reference"
}

prepare_cache() {
  if [[ ! -d "$upstream_cache" ]]; then
    mkdir -p -- "$(dirname -- "$upstream_cache")"
    git init --quiet --bare "$upstream_cache"
    git -C "$upstream_cache" remote add origin "$upstream_url"
  fi

  git -C "$upstream_cache" rev-parse --is-bare-repository >/dev/null 2>&1 \
    || fail "cache Git inválido: $upstream_cache"

  local configured_url
  configured_url="$(git -C "$upstream_cache" remote get-url origin 2>/dev/null)" \
    || fail "o cache não possui o remoto origin: $upstream_cache"
  [[ "$configured_url" == "$upstream_url" ]] \
    || fail "o cache aponta para outro remoto: $configured_url"

  git -C "$upstream_cache" fetch --quiet --filter=blob:none --no-tags origin \
    "+refs/heads/${upstream_branch}:refs/remotes/origin/${upstream_branch}"
}

latest_path_commit() {
  git -C "$upstream_cache" log -1 --format='%H' \
    "refs/remotes/origin/${upstream_branch}" -- "$upstream_path"
}

validate_upstream_reference() {
  local reference="$1"
  git -C "$upstream_cache" cat-file -e "${reference}^{commit}" 2>/dev/null \
    || fail "commit não encontrado no upstream: $reference"
  git -C "$upstream_cache" merge-base --is-ancestor \
    "$reference" "refs/remotes/origin/${upstream_branch}" \
    || fail "commit não pertence ao histórico atual de ${upstream_branch}: $reference"

  local path_commit
  path_commit="$(git -C "$upstream_cache" log -1 --format='%H' "$reference" -- "$upstream_path")"
  [[ "$path_commit" == "$reference" ]] \
    || fail "o commit não altera ${upstream_path}/: $reference"
}

check_updates() {
  local reference="$1"
  local latest
  validate_commit "$reference"
  validate_upstream_reference "$reference"
  latest="$(latest_path_commit)"

  if [[ "$reference" == "$latest" ]]; then
    printf 'Sem atualização em %s/. Referência: %s\n' "$upstream_path" "$reference"
    return 0
  fi

  printf '%s\n' \
    "Atualização upstream detectada em ${upstream_path}/." \
    "Referência reconhecida: ${reference}" \
    "Último commit:          ${latest}" \
    "" \
    "Commits pendentes:"
  git -C "$upstream_cache" log --reverse --date=short \
    --format='  %h  %ad  %s' "${reference}..${latest}" -- "$upstream_path"
  printf '%s\n' "" "Arquivos alterados:"
  git -C "$upstream_cache" diff --name-status \
    "${reference}..${latest}" -- "$upstream_path"
  printf '%s\n' "" "Após adaptar e validar o porte:" \
    "  $0 accept ${latest}"
  return 10
}

render_review_prompt() {
  local reference="$1"
  local latest
  local pending_commits
  local changed_files
  local repository_root
  local prompt
  validate_commit "$reference"
  validate_upstream_reference "$reference"
  latest="$(latest_path_commit)"

  if [[ "$reference" == "$latest" ]]; then
    printf 'Sem atualização em %s/. Não há revisão pendente.\n' "$upstream_path"
    return 0
  fi

  pending_commits="$(git -C "$upstream_cache" log --reverse --date=short \
    --format='- %h (%ad) %s' "${reference}..${latest}" -- "$upstream_path")"
  changed_files="$(git -C "$upstream_cache" diff --name-status \
    "${reference}..${latest}" -- "$upstream_path")"
  repository_root="$(git -C "$skill_dir" rev-parse --show-toplevel)" \
    || fail "a skill local não está em um repositório Git: $skill_dir"
  prompt="$(cat <<'EOF'
# Revisão da adaptação pstack-skill

Você mantém uma skill portátil inspirada no pstack. Ela **não é um espelho** do plugin Cursor. Avalie as mudanças upstream com julgamento de engenharia antes de alterar qualquer arquivo local.

## Contexto verificável

- Skill local: `__SKILL_DIR__`
- Repositório upstream: `__UPSTREAM_URL__`
- Caminho upstream: `__UPSTREAM_PATH__/`
- Referência já revisada: `__REFERENCE__`
- Última mudança relevante: `__LATEST__`

Commits pendentes:

__PENDING_COMMITS__

Arquivos upstream alterados:

__CHANGED_FILES__

## Contrato da versão local

- Preserve a skill como uma pasta autocontida e portável para agentes que leem `SKILL.md`.
- Preserve as adaptações locais que removem dependências de Cursor, Graphite, cloud agents, modelos proprietários e comandos exclusivos de plugins.
- Não busque paridade textual nem copie manifests, automações ou integrações específicas do Cursor sem uma equivalência portátil comprovada.
- Prefira uma adaptação menor que preserve a intenção e os invariantes do upstream.
- Preserve comportamentos locais que sejam deliberadamente diferentes quando eles atendem melhor ao ambiente portátil.
- Não avance `UPSTREAM_COMMIT`. Esse reconhecimento só acontece depois da revisão humana, via `./scripts/check-upstream.sh accept <sha>`.

## Evidência obrigatória

Leia o diff completo antes de decidir. Use estes comandos, sem assumir que nomes ou caminhos upstream tenham um correspondente local direto:

```bash
git -C "__UPSTREAM_CACHE__" diff --find-renames "__REFERENCE__..__LATEST__" -- "__UPSTREAM_PATH__"
git -C "__UPSTREAM_CACHE__" log --reverse --format=fuller "__REFERENCE__..__LATEST__" -- "__UPSTREAM_PATH__"
rg -n --glob '*.md' --glob '*.sh' 'multi-phase|plan|check-plan|<termo relevante>' "__SKILL_DIR__"
```

Leia cada arquivo upstream afetado com `git -C "__UPSTREAM_CACHE__" show "__LATEST__:<caminho>"`. Depois localize o comportamento correspondente na skill local e compare intenção, não apenas texto.

## Decisão por mudança

Para cada mudança upstream, produza uma linha com:

| Mudança upstream | Intenção | Contraparte local | Decisão | Justificativa | Ação local |
| --- | --- | --- | --- | --- | --- |

Use apenas estas decisões:

- **Adotar** quando a mudança já é portátil e melhora a skill local.
- **Adaptar** quando a intenção é útil, mas a implementação upstream depende do Cursor ou conflita com a arquitetura local.
- **Rejeitar** quando a mudança não oferece valor à versão portátil ou reduz sua compatibilidade.

Não trate ausência de correspondência como defeito. Ela pode ser uma adaptação intencional.

## Execução e validação

Implemente somente os itens decididos como **Adotar** ou **Adaptar**. Restrinja as edições a `__SKILL_DIR__`. Não altere `UPSTREAM_COMMIT`.

Valide o resultado com:

```bash
bash -n "__SKILL_DIR__/scripts/check-upstream.sh"
python3 /home/fabricio/.codex/skills/.system/skill-creator/scripts/quick_validate.py "__SKILL_DIR__"
git -C "__REPOSITORY_ROOT__" diff --check
```

Na resposta, entregue a tabela de decisões, os arquivos locais alterados, a evidência de validação e o SHA que o mantenedor deve reconhecer depois de revisar o resultado: `__LATEST__`.
EOF
 )"
  prompt="${prompt//__SKILL_DIR__/$skill_dir}"
  prompt="${prompt//__REPOSITORY_ROOT__/$repository_root}"
  prompt="${prompt//__UPSTREAM_URL__/$upstream_url}"
  prompt="${prompt//__UPSTREAM_PATH__/$upstream_path}"
  prompt="${prompt//__UPSTREAM_CACHE__/$upstream_cache}"
  prompt="${prompt//__REFERENCE__/$reference}"
  prompt="${prompt//__LATEST__/$latest}"
  prompt="${prompt//__PENDING_COMMITS__/$pending_commits}"
  prompt="${prompt//__CHANGED_FILES__/$changed_files}"
  printf '%s\n' "$prompt"
}

accept_reference() {
  local candidate="$1"
  local latest
  validate_commit "$candidate"
  validate_upstream_reference "$candidate"
  latest="$(latest_path_commit)"
  [[ "$candidate" == "$latest" ]] \
    || fail "use o último commit de ${upstream_path}/: $latest"

  local temporary_state
  temporary_state="$(mktemp "${state_file}.XXXXXX")"
  trap 'rm -f -- "$temporary_state"' EXIT HUP INT TERM
  printf '%s\n' "$candidate" > "$temporary_state"
  mv -- "$temporary_state" "$state_file"
  trap - EXIT HUP INT TERM
  printf 'Referência atualizada para %s.\n' "$candidate"
}

main() {
  local command="${1:-check}"

  case "$command" in
    check)
      [[ $# -le 2 ]] || { usage >&2; exit 2; }
      prepare_cache
      check_updates "${2:-$(read_reference)}"
      ;;
    review-prompt)
      [[ $# -eq 1 ]] || { usage >&2; exit 2; }
      prepare_cache
      render_review_prompt "$(read_reference)"
      ;;
    accept)
      [[ $# -eq 2 ]] || { usage >&2; exit 2; }
      prepare_cache
      accept_reference "$2"
      ;;
    -h|--help|help)
      usage
      ;;
    *)
      usage >&2
      exit 2
      ;;
  esac
}

main "$@"
