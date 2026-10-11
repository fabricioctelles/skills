#!/usr/bin/env python3
"""
measure.py — Descriptive English prose metrics.

Usage:
    echo "some text" | python3 measure.py
    python3 measure.py --file path/to/text.txt

Calculates linguistic metrics (TTR, burstiness, entropy, sentence/paragraph
variation, passive voice, contractions, etc.) for editorial inspection. These measurements do not determine authorship.
Passive voice, contraction rate, and noun density use approximate heuristics.

Requires Python 3.10+. No external dependencies.
"""

import argparse
import json
import math
import re
import statistics
import sys
from collections import Counter


# Common contractions and their expanded forms
CONTRACTION_PAIRS = {
    "i'm": "i am", "i've": "i have", "i'll": "i will", "i'd": "i would",
    "you're": "you are", "you've": "you have", "you'll": "you will", "you'd": "you would",
    "he's": "he is", "he'll": "he will", "he'd": "he would",
    "she's": "she is", "she'll": "she will", "she'd": "she would",
    "it's": "it is", "it'll": "it will", "it'd": "it would",
    "we're": "we are", "we've": "we have", "we'll": "we will", "we'd": "we would",
    "they're": "they are", "they've": "they have", "they'll": "they will", "they'd": "they would",
    "that's": "that is", "there's": "there is", "here's": "here is",
    "what's": "what is", "who's": "who is", "where's": "where is",
    "won't": "will not", "can't": "cannot", "couldn't": "could not",
    "wouldn't": "would not", "shouldn't": "should not", "doesn't": "does not",
    "don't": "do not", "didn't": "did not", "isn't": "is not",
    "aren't": "are not", "wasn't": "was not", "weren't": "were not",
    "hasn't": "has not", "haven't": "have not", "hadn't": "had not",
    "let's": "let us", "that'll": "that will", "who'll": "who will",
}

# Expanded forms to detect (when NOT contracted)
EXPANDED_FORMS = set(CONTRACTION_PAIRS.values())

# Common concrete nouns (physical, tangible objects)
CONCRETE_PATTERNS = re.compile(
    r"\b(table|chair|car|house|tree|dog|cat|book|phone|door|window|wall|"
    r"road|water|stone|hand|face|eye|foot|head|body|room|floor|glass|"
    r"box|bag|cup|plate|knife|pen|paper|shirt|shoe|hat|bed|desk|"
    r"computer|screen|keyboard|mouse|bottle|lamp|clock|mirror|bridge|"
    r"river|mountain|ocean|sun|moon|star|cloud|rain|snow|fire|smoke|"
    r"bread|meat|fruit|flower|grass|sand|iron|gold|silver|wood|rock|"
    r"truck|bus|train|plane|boat|ship|bicycle|wheel|engine|hammer|"
    r"needle|rope|chain|brick|coin|ring|bell|drum|guitar|piano)\b",
    re.IGNORECASE,
)

# Abstract nouns (concepts, ideas, qualities)
ABSTRACT_PATTERNS = re.compile(
    r"\b(freedom|justice|love|beauty|truth|wisdom|knowledge|power|"
    r"happiness|sadness|anger|fear|hope|faith|courage|patience|"
    r"democracy|philosophy|theory|concept|idea|thought|belief|"
    r"understanding|experience|opportunity|challenge|strategy|"
    r"approach|methodology|framework|perspective|consideration|"
    r"implementation|optimization|functionality|capability|"
    r"efficiency|effectiveness|sustainability|innovation|"
    r"transformation|development|improvement|enhancement|"
    r"complexity|simplicity|diversity|integrity|creativity)\b",
    re.IGNORECASE,
)


def tokenize(text: str) -> list[str]:
    """Split text into lowercase word tokens."""
    return re.findall(r"[a-z']+", text.lower())


def split_sentences(text: str) -> list[str]:
    """Split text into sentences using punctuation boundaries."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s for s in sentences if s.strip()]


def split_paragraphs(text: str) -> list[str]:
    """Split text into paragraphs by blank lines."""
    paragraphs = re.split(r'\n\s*\n', text.strip())
    return [p for p in paragraphs if p.strip()]


def calc_ttr(tokens: list[str]) -> float:
    """Type-Token Ratio: unique tokens / total tokens."""
    if not tokens:
        return 0.0
    return len(set(tokens)) / len(tokens)


def calc_burstiness(sentences: list[str]) -> float:
    """Standard deviation of sentence lengths (word count per sentence)."""
    lengths = [len(s.split()) for s in sentences]
    if len(lengths) < 2:
        return 0.0
    return statistics.stdev(lengths)


def calc_shannon_entropy(tokens: list[str]) -> float:
    """Shannon entropy: -sum p(x)*log2(p(x)) over vocabulary."""
    if not tokens:
        return 0.0
    total = len(tokens)
    counts = Counter(tokens)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy


def calc_sentence_length_cov(sentences: list[str]) -> float:
    """Coefficient of variation of sentence lengths: std/mean."""
    lengths = [len(s.split()) for s in sentences]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    if mean == 0:
        return 0.0
    return statistics.stdev(lengths) / mean


def calc_mean_sentence_length(sentences: list[str]) -> float:
    """Mean sentence length in words."""
    lengths = [len(s.split()) for s in sentences]
    if not lengths:
        return 0.0
    return statistics.mean(lengths)


def calc_paragraph_length_cov(paragraphs: list[str]) -> float:
    """Coefficient of variation of paragraph lengths (in sentences)."""
    if len(paragraphs) < 2:
        return 0.0
    lengths = [len(split_sentences(p)) for p in paragraphs]
    mean = statistics.mean(lengths)
    if mean == 0:
        return 0.0
    return statistics.stdev(lengths) / mean


def calc_ly_adverbs_per_100(tokens: list[str]) -> float:
    """Count adverbs ending in -ly per 100 words."""
    if not tokens:
        return 0.0
    # Exclude common non-adverb -ly words
    exceptions = {
        "only", "early", "likely", "family", "really", "actually",
        "finally", "fly", "supply", "apply", "reply", "holy",
        "ugly", "belly", "jelly", "bully", "ally", "rally",
    }
    ly_count = sum(
        1 for t in tokens
        if t.endswith("ly") and len(t) > 3 and t not in exceptions
    )
    return (ly_count / len(tokens)) * 100


def calc_passive_voice_pct(text: str) -> float:
    """Approximate passive voice: was/were/been/being + past participle pattern."""
    sentences = split_sentences(text)
    if not sentences:
        return 0.0
    passive_pattern = re.compile(
        r'\b(was|were|been|being|is|are|am)\s+(\w+ed|(\w+en))\b',
        re.IGNORECASE,
    )
    passive_count = sum(1 for s in sentences if passive_pattern.search(s))
    return passive_count / len(sentences)


def calc_contraction_rate(text: str) -> float:
    """Percentage of contractable phrases that ARE contracted."""
    text_lower = text.lower()
    tokens_raw = re.findall(r"[a-z']+", text_lower)
    text_joined = " ".join(tokens_raw)

    contracted_count = 0
    expanded_count = 0

    # Count contractions present
    for contraction in CONTRACTION_PAIRS:
        contracted_count += text_joined.count(contraction)

    # Count expanded forms present (not contracted)
    for expanded in EXPANDED_FORMS:
        expanded_count += text_joined.count(expanded)

    total = contracted_count + expanded_count
    if total == 0:
        return 0.0
    return contracted_count / total


def calc_concrete_noun_density(tokens: list[str]) -> float | None:
    """Ratio of concrete nouns to (concrete + abstract) nouns found."""
    text = " ".join(tokens)
    concrete_matches = len(CONCRETE_PATTERNS.findall(text))
    abstract_matches = len(ABSTRACT_PATTERNS.findall(text))
    total = concrete_matches + abstract_matches
    if total == 0:
        return None  # no matching nouns; density was not measured
    return concrete_matches / total


def analyze(text: str) -> dict:
    """Run full analysis on input text."""
    tokens = tokenize(text)
    sentences = split_sentences(text)
    paragraphs = split_paragraphs(text)

    noun_density = calc_concrete_noun_density(tokens)
    metrics = {
        "ttr": round(calc_ttr(tokens), 4),
        "burstiness": round(calc_burstiness(sentences), 4),
        "shannon_entropy": round(calc_shannon_entropy(tokens), 4),
        "sentence_length_cov": round(calc_sentence_length_cov(sentences), 4),
        "mean_sentence_length": round(calc_mean_sentence_length(sentences), 2),
        "paragraph_length_cov": round(calc_paragraph_length_cov(paragraphs), 4),
        "ly_adverbs_per_100": round(calc_ly_adverbs_per_100(tokens), 4),
        "passive_voice_pct": round(calc_passive_voice_pct(text), 4),
        "contraction_rate": round(calc_contraction_rate(text), 4),
        "concrete_noun_density": round(noun_density, 4) if noun_density is not None else None,
    }

    return {
        "metrics": metrics,
        "limitations": [
            "Descriptive metrics do not establish authorship or editorial quality.",
            "Passive voice, contractions, and noun density use approximate heuristics.",
            "Sentence splitting and lexical metrics depend on text length and genre.",
        ],
        "meta": {
            "total_tokens": len(tokens),
            "unique_tokens": len(set(tokens)),
            "total_sentences": len(sentences),
            "total_paragraphs": len(paragraphs),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Measure descriptive English prose metrics without authorship classification.",
    )
    parser.add_argument(
        "--file", "-f",
        type=str,
        help="Path to text file to analyze (reads stdin if omitted)",
    )
    args = parser.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    if not text.strip():
        print(json.dumps({"error": "Empty input"}), file=sys.stdout)
        sys.exit(1)

    result = analyze(text)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
