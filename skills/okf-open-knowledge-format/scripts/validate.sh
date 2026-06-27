#!/usr/bin/env bash
# OKF Bundle Validator v0.1
# Usage: validate.sh <bundle-path>
# Checks conformance with OKF v0.1 spec:
#   E1: All non-reserved .md files have YAML frontmatter
#   E2: All frontmatter has non-empty 'type' field
#   E3: Reserved files follow structure rules

set -euo pipefail

BUNDLE="${1:-.}"
ERRORS=0
WARNINGS=0
TOTAL=0

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

if [ ! -d "$BUNDLE" ]; then
  echo -e "${RED}Error: '$BUNDLE' is not a directory${NC}"
  exit 1
fi

echo "Validating OKF bundle: $BUNDLE"
echo "---"

# Find all .md files
while IFS= read -r -d '' file; do
  TOTAL=$((TOTAL + 1))
  relative="${file#$BUNDLE/}"
  basename=$(basename "$file")

  # Skip reserved files (validate separately)
  if [[ "$basename" == "index.md" || "$basename" == "log.md" ]]; then
    # E3: Check reserved file structure
    if [[ "$basename" == "index.md" ]]; then
      # index.md should NOT have frontmatter (except bundle root may have okf_version)
      if head -1 "$file" | grep -q "^---$"; then
        # Allow only if it's bundle root and contains okf_version
        if [[ "$relative" != "index.md" ]]; then
          echo -e "${RED}E3: $relative — index.md should not have frontmatter${NC}"
          ERRORS=$((ERRORS + 1))
        fi
      fi
    fi
    if [[ "$basename" == "log.md" ]]; then
      # log.md should have date headings in YYYY-MM-DD format
      if ! grep -qE "^## [0-9]{4}-[0-9]{2}-[0-9]{2}" "$file" 2>/dev/null; then
        if [ -s "$file" ]; then
          echo -e "${YELLOW}W: $relative — log.md has no ISO 8601 date headings${NC}"
          WARNINGS=$((WARNINGS + 1))
        fi
      fi
    fi
    continue
  fi

  # E1: Check for YAML frontmatter
  if ! head -1 "$file" | grep -q "^---$"; then
    echo -e "${RED}E1: $relative — no YAML frontmatter${NC}"
    ERRORS=$((ERRORS + 1))
    continue
  fi

  # Extract frontmatter (between first --- and second ---)
  frontmatter=$(sed -n '2,/^---$/p' "$file" | sed '$d')

  # E2: Check for non-empty type field
  type_value=$(echo "$frontmatter" | grep -E "^type:" | sed 's/^type:\s*//' | tr -d '"' | tr -d "'" | xargs)
  if [ -z "$type_value" ]; then
    echo -e "${RED}E2: $relative — missing or empty 'type' field${NC}"
    ERRORS=$((ERRORS + 1))
    continue
  fi

  # Warnings for recommended fields
  if ! echo "$frontmatter" | grep -qE "^title:"; then
    echo -e "${YELLOW}W1: $relative — missing recommended 'title' field${NC}"
    WARNINGS=$((WARNINGS + 1))
  fi
  if ! echo "$frontmatter" | grep -qE "^description:"; then
    echo -e "${YELLOW}W1: $relative — missing recommended 'description' field${NC}"
    WARNINGS=$((WARNINGS + 1))
  fi

done < <(find "$BUNDLE" -name "*.md" -type f -print0 | sort -z)

# Summary
echo "---"
echo "Files scanned: $TOTAL"
if [ $ERRORS -eq 0 ]; then
  echo -e "${GREEN}✅ Bundle is OKF v0.1 conformant${NC}"
else
  echo -e "${RED}❌ $ERRORS error(s) — bundle is NOT conformant${NC}"
fi
if [ $WARNINGS -gt 0 ]; then
  echo -e "${YELLOW}⚠  $WARNINGS warning(s)${NC}"
fi

exit $ERRORS
