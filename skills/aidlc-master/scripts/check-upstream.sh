#!/usr/bin/env bash

set -euo pipefail

readonly upstream_url="https://github.com/awslabs/aidlc-workflows.git"
readonly upstream_branch="main"
readonly upstream_paths=(
  "aidlc-rules"
  "docs/WORKING-WITH-AIDLC.md"
  "docs/GENERATED_DOCS_REFERENCE.md"
  "docs/writing-inputs"
)
readonly mirror_path="aidlc-rules/aws-aidlc-rule-details"
readonly skill_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
readonly state_file="${skill_dir}/UPSTREAM_COMMIT"
readonly cache_base="${XDG_CACHE_HOME:-${HOME}/.cache}"
readonly upstream_cache="${AIDLC_UPSTREAM_CACHE_DIR:-${cache_base}/aidlc-master/upstream.git}"

# Arquivos adicionados por este porte (não existem em aws-aidlc-rule-details/).
readonly -a mirror_exclusions=(
  "working-with-aidlc.md"
  "generated-docs-reference.md"
  "inputs"
)

usage() {
  printf '%s\n' \
    "Uso:" \
    "  $0 [check [<commit>]]      # há mudanças upstream desde UPSTREAM_COMMIT?" \
    "  $0 mirror-diff [<commit>]  # references/ ainda é espelho 1:1 do upstream?" \
    "  $0 review-prompt           # prompt de revisão do porte" \
    "  $0 accept <commit>         # reconhece o commit revisado"
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

  git -C "$upstream_cache" fetch --quiet --no-tags origin \
    "+refs/heads/${upstream_branch}:refs/remotes/origin/${upstream_branch}"
}

latest_path_commit() {
  git -C "$upstream_cache" log -1 --format='%H' \
    "refs/remotes/origin/${upstream_branch}" -- "${upstream_paths[@]}"
}

validate_upstream_reference() {
  local reference="$1"
  git -C "$upstream_cache" cat-file -e "${reference}^{commit}" 2>/dev/null \
    || fail "commit não encontrado no upstream: $reference"
  git -C "$upstream_cache" merge-base --is-ancestor \
    "$reference" "refs/remotes/origin/${upstream_branch}" \
    || fail "commit não pertence ao histórico atual de ${upstream_branch}: $reference"

  # A referência precisa ser um commit que TOCA os caminhos portados, senão
  # `check` acusaria atualização fantasma a cada commit de CI do upstream.
  local path_commit
  path_commit="$(git -C "$upstream_cache" log -1 --format='%H' "$reference" -- "${upstream_paths[@]}")"
  [[ "$path_commit" == "$reference" ]] \
    || fail "o commit não altera os caminhos portados: $reference (use $path_commit)"
}

check_updates() {
  local reference="$1"
  local latest
  validate_commit "$reference"
  validate_upstream_reference "$reference"
  latest="$(latest_path_commit)"

  if [[ "$reference" == "$latest" ]]; then
    printf 'Sem atualização nos caminhos portados. Referência: %s\n' "$reference"
    return 0
  fi

  printf '%s\n' \
    "Atualização upstream detectada." \
    "Referência reconhecida: ${reference}" \
    "Último commit:          ${latest}" \
    "" \
    "Commits pendentes:"
  git -C "$upstream_cache" log --reverse --date=short \
    --format='  %h  %ad  %s' "${reference}..${latest}" -- "${upstream_paths[@]}"
  printf '%s\n' "" "Arquivos alterados:"
  git -C "$upstream_cache" diff --name-status \
    "${reference}..${latest}" -- "${upstream_paths[@]}"
  printf '%s\n' "" "Versão upstream declarada:"
  git -C "$upstream_cache" show "${latest}:aidlc-rules/VERSION" 2>/dev/null | sed 's/^/  /' || true
  printf '%s\n' "" "Para revisar o porte:" "  $0 review-prompt" \
    "" "Depois de portar e validar:" "  $0 accept ${latest}"
  return 10
}

mirror_diff() {
  local reference="$1"
  local workdir
  local -a exclude_flags=()
  local name

  validate_commit "$reference"
  validate_upstream_reference "$reference"

  workdir="$(mktemp -d)"
  # O path é expandido agora: `workdir` é local e já saiu de escopo quando o trap roda.
  trap "rm -rf -- '$workdir'" EXIT HUP INT TERM

  git -C "$upstream_cache" archive "$reference" "$mirror_path" | tar -x -C "$workdir" \
    || fail "não foi possível extrair ${mirror_path} de ${reference}"

  for name in "${mirror_exclusions[@]}"; do
    exclude_flags+=(-x "$name")
  done

  printf 'Espelho 1:1 — upstream %s vs %s/references\n\n' "${reference:0:8}" "$skill_dir"
  if diff -r -u "${exclude_flags[@]}" "$workdir/$mirror_path" "$skill_dir/references"; then
    printf '\nSem divergências.\n'
    return 0
  fi

  printf '%s\n' "" \
    "Divergências acima. Esperado: apenas a adaptação A5 em common/process-overview.md" \
    "(nota de duplicação apontando para o README desta skill)." \
    "Qualquer outra divergência é deriva do porte — ver README.md, seção Adaptations."
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
    printf 'Sem atualização nos caminhos portados. Não há revisão pendente.\n'
    return 0
  fi

  pending_commits="$(git -C "$upstream_cache" log --reverse --date=short \
    --format='- %h (%ad) %s' "${reference}..${latest}" -- "${upstream_paths[@]}")"
  changed_files="$(git -C "$upstream_cache" diff --name-status \
    "${reference}..${latest}" -- "${upstream_paths[@]}")"
  repository_root="$(git -C "$skill_dir" rev-parse --show-toplevel)" \
    || fail "a skill local não está em um repositório Git: $skill_dir"
  prompt="$(cat <<'EOF'
# Revisão da sincronização aidlc-master

Esta skill é um **espelho 1:1** dos steering rules do AWS AI-DLC, com seis adaptações
documentadas (A1–A6 no `README.md`). O default é **adotar o texto upstream verbatim**;
divergir exige justificativa.

## Contexto verificável

- Skill local: `__SKILL_DIR__`
- Repositório upstream: `__UPSTREAM_URL__`
- Caminhos portados: `aidlc-rules/`, `docs/WORKING-WITH-AIDLC.md`, `docs/GENERATED_DOCS_REFERENCE.md`, `docs/writing-inputs/`
- Referência já revisada: `__REFERENCE__`
- Último commit relevante: `__LATEST__`

Commits pendentes:

__PENDING_COMMITS__

Arquivos upstream alterados:

__CHANGED_FILES__

## Contrato do porte

- `references/**` é cópia literal de `aidlc-rules/aws-aidlc-rule-details/**`. Ao sincronizar,
  **substitua** o arquivo pela versão upstream; não reescreva, não condense, não traduza.
- `SKILL.md` é `aidlc-rules/aws-aidlc-rules/core-workflow.md` com as adaptações A1–A4 e A6:
  frontmatter da skill (A1), resolução do diretório de rule details com `references/` como
  fallback garantido (A2), escopo do header de prioridade ao tempo de vida da skill (A3),
  a seção *Host-agnostic answering* (A4) e a seção *Gotchas* (A6). Reaplique-as sobre o novo core-workflow.
- `references/common/process-overview.md` carrega a adaptação A5 (nota de duplicação
  apontando para o README da skill). Reaplique após substituir o arquivo.
- Nenhum nome de tool proprietário de agente entra na skill. O mecanismo canônico de
  perguntas continua o arquivo `.md` com tags `[Answer]:`.
- Arquivos novos em `aws-aidlc-rule-details/**` entram no espelho. Arquivos removidos upstream
  saem daqui também.
- Mudanças upstream em `scripts/aidlc-evaluator/**`, CI, ou nos dois exemplos completos de
  `docs/writing-inputs/` estão fora do escopo do porte — registre e ignore.
- Não avance `UPSTREAM_COMMIT`. Isso acontece só após revisão humana, via
  `./scripts/check-upstream.sh accept <sha>`.

## Evidência obrigatória

```bash
git -C "__UPSTREAM_CACHE__" diff --find-renames "__REFERENCE__..__LATEST__" -- aidlc-rules docs
git -C "__UPSTREAM_CACHE__" show "__LATEST__:aidlc-rules/VERSION"
git -C "__UPSTREAM_CACHE__" show "__LATEST__:aidlc-rules/aws-aidlc-rules/core-workflow.md"
"__SKILL_DIR__/scripts/check-upstream.sh" mirror-diff "__LATEST__"
```

## Decisão por arquivo alterado

| Arquivo upstream | Tipo de mudança | Destino local | Ação | Adaptação a reaplicar |
| --- | --- | --- | --- | --- |

## Execução e validação

Restrinja as edições a `__SKILL_DIR__`. Depois:

```bash
bash -n "__SKILL_DIR__/scripts/check-upstream.sh"
"__SKILL_DIR__/scripts/check-upstream.sh" mirror-diff "__LATEST__"
git -C "__REPOSITORY_ROOT__" diff --check
```

E verifique que toda referência do tipo `common/x.md`, `inception/x.md`, `construction/x.md`,
`extensions/.../x.md` citada em qualquer arquivo portado resolve para um arquivo existente
sob `references/`.

Entregue a tabela de decisões, os arquivos locais alterados, a evidência de validação, e o SHA
a reconhecer: `__LATEST__`.
EOF
 )"
  prompt="${prompt//__SKILL_DIR__/$skill_dir}"
  prompt="${prompt//__REPOSITORY_ROOT__/$repository_root}"
  prompt="${prompt//__UPSTREAM_URL__/$upstream_url}"
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
    || fail "use o último commit dos caminhos portados: $latest"

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
    mirror-diff)
      [[ $# -le 2 ]] || { usage >&2; exit 2; }
      prepare_cache
      mirror_diff "${2:-$(read_reference)}"
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
