#!/usr/bin/env bash
# OKF Bundle Validator v0.2
# Usage: validate.sh <bundle-path>
# Checks conformance with OKF v0.2 spec:
#   E1: All non-reserved .md files have YAML frontmatter
#   E2: All frontmatter has non-empty 'type' field
#   E3: Reserved files follow structure rules
#   E4: Attested Computation concepts have required 'runtime' field
#
# Also reports v0.2 features: trust fields, lifecycle, provenance, staleness

set -euo pipefail

BUNDLE="${1:-.}"
ERRORS=0
WARNINGS=0
TOTAL=0
CONCEPTS=0
ATTESTED_COMPUTATIONS=0
WITH_GENERATED=0
WITH_VERIFIED=0
HUMAN_VERIFIED=0
MACHINE_VERIFIED=0
WITH_SOURCES=0
WITH_STATUS=0
STALE_COUNT=0
DEPRECATED_COUNT=0
DRAFT_COUNT=0

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

if [ ! -d "$BUNDLE" ]; then
  echo -e "${RED}Error: '$BUNDLE' is not a directory${NC}"
  exit 1
fi

echo "Validating OKF bundle: $BUNDLE"
echo "Spec version: v0.2"
echo "---"

# Get current timestamp for staleness check
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)

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
          echo -e "${YELLOW}W5: $relative — log.md has no ISO 8601 date headings${NC}"
          WARNINGS=$((WARNINGS + 1))
        fi
      fi
    fi
    continue
  fi

  CONCEPTS=$((CONCEPTS + 1))

  # E1: Check for YAML frontmatter
  if ! head -1 "$file" | grep -q "^---$"; then
    echo -e "${RED}E1: $relative — no YAML frontmatter${NC}"
    ERRORS=$((ERRORS + 1))
    continue
  fi

  # Extract frontmatter (between first --- and second ---)
  frontmatter=$(sed -n '2,/^---$/p' "$file" | sed '$d')

  # E2: Check for non-empty type field
  # `|| true` is required: under `set -euo pipefail` a non-matching grep would
  # abort the whole script instead of letting the emptiness check below report E2.
  type_value=$(echo "$frontmatter" | grep -E "^type:" | sed 's/^type:\s*//' | tr -d '"' | tr -d "'" | xargs) || true
  if [ -z "$type_value" ]; then
    echo -e "${RED}E2: $relative — missing or empty 'type' field${NC}"
    ERRORS=$((ERRORS + 1))
    continue
  fi

  # E4: Attested Computation must have runtime
  if [[ "$type_value" == "Attested Computation" ]]; then
    ATTESTED_COMPUTATIONS=$((ATTESTED_COMPUTATIONS + 1))
    if ! echo "$frontmatter" | grep -qE "^runtime:"; then
      echo -e "${RED}E4: $relative — Attested Computation missing required 'runtime' field${NC}"
      ERRORS=$((ERRORS + 1))
    fi
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

  # v0.2 Trust fields check
  if echo "$frontmatter" | grep -qE "^generated:"; then
    WITH_GENERATED=$((WITH_GENERATED + 1))
  else
    # Check for legacy timestamp field
    if echo "$frontmatter" | grep -qE "^timestamp:"; then
      echo -e "${YELLOW}W3: $relative — using legacy 'timestamp' field, consider migrating to 'generated'${NC}"
      WARNINGS=$((WARNINGS + 1))
    fi
  fi

  if echo "$frontmatter" | grep -qE "^verified:"; then
    WITH_VERIFIED=$((WITH_VERIFIED + 1))
    # Check if human-verified
    if echo "$frontmatter" | grep -qE "human:"; then
      HUMAN_VERIFIED=$((HUMAN_VERIFIED + 1))
    else
      MACHINE_VERIFIED=$((MACHINE_VERIFIED + 1))
    fi
  fi

  # v0.2 Provenance check
  if echo "$frontmatter" | grep -qE "^sources:"; then
    WITH_SOURCES=$((WITH_SOURCES + 1))
    # Check that sources entries have resource field
    # This is a simplified check - full YAML parsing would be better
    sources_block=$(echo "$frontmatter" | sed -n '/^sources:/,/^[a-z]/p' | sed '$d')
    if echo "$sources_block" | grep -q "^\s*-" && ! echo "$sources_block" | grep -qE "resource:"; then
      echo -e "${YELLOW}W6: $relative — sources entry may be missing 'resource' field${NC}"
      WARNINGS=$((WARNINGS + 1))
    fi
  fi

  # v0.2 Lifecycle check
  if echo "$frontmatter" | grep -qE "^status:"; then
    WITH_STATUS=$((WITH_STATUS + 1))
    status_value=$(echo "$frontmatter" | grep -E "^status:" | sed 's/^status:\s*//' | tr -d '"' | tr -d "'" | xargs)
    case "$status_value" in
      draft)
        DRAFT_COUNT=$((DRAFT_COUNT + 1))
        ;;
      deprecated)
        DEPRECATED_COUNT=$((DEPRECATED_COUNT + 1))
        ;;
      stable)
        # Default, nothing special
        ;;
      *)
        echo -e "${YELLOW}W: $relative — unknown status value '$status_value' (expected: draft|stable|deprecated)${NC}"
        WARNINGS=$((WARNINGS + 1))
        ;;
    esac
  fi

  # v0.2 Staleness check
  if echo "$frontmatter" | grep -qE "^stale_after:"; then
    stale_date=$(echo "$frontmatter" | grep -E "^stale_after:" | sed 's/^stale_after:\s*//' | tr -d '"' | tr -d "'" | xargs)
    # Simple string comparison works for ISO 8601 dates
    if [[ "$NOW" > "$stale_date" ]] || [[ "$NOW" == "$stale_date" ]]; then
      STALE_COUNT=$((STALE_COUNT + 1))
      echo -e "${YELLOW}W7: $relative — content is STALE (stale_after: $stale_date)${NC}"
      WARNINGS=$((WARNINGS + 1))
    fi
  fi

done < <(find "$BUNDLE" -name "*.md" -type f -print0 | sort -z)

# Summary
echo ""
echo "---"
echo -e "${CYAN}Summary${NC}"
echo "Files scanned: $TOTAL"
echo "Concept files: $CONCEPTS"
echo ""

if [ $ERRORS -eq 0 ]; then
  echo -e "${GREEN}✅ Bundle is OKF v0.2 conformant${NC}"
else
  echo -e "${RED}❌ $ERRORS error(s) — bundle is NOT conformant${NC}"
fi

if [ $WARNINGS -gt 0 ]; then
  echo -e "${YELLOW}⚠  $WARNINGS warning(s)${NC}"
fi

echo ""
echo -e "${CYAN}v0.2 Features${NC}"

# Trust summary
echo ""
echo "Trust:"
if [ $WITH_GENERATED -gt 0 ]; then
  echo -e "  ${BLUE}ℹ${NC}  $WITH_GENERATED concepts with 'generated' field"
fi
if [ $WITH_VERIFIED -gt 0 ]; then
  echo -e "  ${BLUE}ℹ${NC}  $WITH_VERIFIED concepts with 'verified' field"
  if [ $HUMAN_VERIFIED -gt 0 ]; then
    echo -e "      ${GREEN}✓${NC} $HUMAN_VERIFIED human-reviewed"
  fi
  if [ $MACHINE_VERIFIED -gt 0 ]; then
    echo -e "      ${BLUE}○${NC} $MACHINE_VERIFIED machine-confirmed only"
  fi
fi
UNVERIFIED=$((CONCEPTS - WITH_VERIFIED))
if [ $UNVERIFIED -gt 0 ]; then
  echo -e "      ${YELLOW}○${NC} $UNVERIFIED unverified"
fi

# Provenance summary
echo ""
echo "Provenance:"
if [ $WITH_SOURCES -gt 0 ]; then
  echo -e "  ${BLUE}ℹ${NC}  $WITH_SOURCES concepts with 'sources' field"
else
  echo -e "  ${YELLOW}○${NC} No concepts with provenance tracking"
fi

# Lifecycle summary
echo ""
echo "Lifecycle:"
if [ $WITH_STATUS -gt 0 ]; then
  echo -e "  ${BLUE}ℹ${NC}  $WITH_STATUS concepts with explicit 'status'"
fi
if [ $DRAFT_COUNT -gt 0 ]; then
  echo -e "      ${YELLOW}○${NC} $DRAFT_COUNT draft"
fi
if [ $DEPRECATED_COUNT -gt 0 ]; then
  echo -e "      ${YELLOW}○${NC} $DEPRECATED_COUNT deprecated"
fi
if [ $STALE_COUNT -gt 0 ]; then
  echo -e "  ${RED}⚠${NC}  $STALE_COUNT concepts are STALE (past stale_after)"
fi

# Attested Computations
if [ $ATTESTED_COMPUTATIONS -gt 0 ]; then
  echo ""
  echo "Attested Computations:"
  echo -e "  ${BLUE}ℹ${NC}  $ATTESTED_COMPUTATIONS Attested Computation concept(s)"
fi

echo ""
exit $ERRORS
