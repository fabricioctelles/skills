---
title: "Plural rules and grammatical number"
category: i18n
status: recommended
updated: "2026-05-29T18:54:03.000Z"
sources:
  - title: "Unicode CLDR — Language Plural Rules"
    url: "https://cldr.unicode.org/index/cldr-spec/plural-rules"
    publisher: "Unicode"
  - title: "MDN — Intl.PluralRules"
    url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules"
    publisher: "MDN"
  - title: "W3C — Internationalization Quick Tips for the Web"
    url: "https://www.w3.org/International/quicktips/"
    publisher: "W3C"
licence: CC-BY-4.0
---

# Plural rules and grammatical number

> Most languages don't pluralise like English. Use CLDR plural categories — zero, one, two, few, many, other — via Intl.PluralRules instead of hard-coded 'item' vs 'items' logic.

## What it is

Grammatical number is how a language changes a word to reflect how many things it refers to. English has two forms — "1 item", "0 items", "2 items", "1.5 items" — and most developers write `count === 1 ? "item" : "items"` without thinking about it. That logic is wrong for most of the world's languages.

The [Unicode Common Locale Data Repository (CLDR)](https://cldr.unicode.org/index/cldr-spec/plural-rules) defines up to six plural *categories* that a language may use: `zero`, `one`, `two`, `few`, `many`, and `other`. Each language picks a subset and a rule that maps a number to one of them. Arabic uses all six. Russian, Polish and Ukrainian use `one` / `few` / `many` / `other`, switching on the last digit of the number ("1 файл", "2 файла", "5 файлов"). Welsh uses six. Japanese, Chinese, Korean and Vietnamese have no grammatical number at all — every count uses `other`.

`Intl.PluralRules` exposes CLDR's rules to the runtime, so you never have to encode the logic yourself.

## Why it matters

Hard-coded English plural logic produces broken sentences in every locale it cannot describe. A Russian user seeing "5 файла" instead of "5 файлов" reads it the way an English reader reads "5 file" — visibly wrong and visibly machine-translated. Translation memory and review costs go up because translators have to fight the code, and copy quality drops because there is no place to put the right forms.

## How to implement

Store strings *by category*, not by number, and let `Intl.PluralRules` pick the category.

```js
const ar = new Intl.PluralRules("ar");
ar.select(0);   // "zero"
ar.select(1);   // "one"
ar.select(2);   // "two"
ar.select(3);   // "few"
ar.select(11);  // "many"
ar.select(100); // "other"

const messages = {
  zero: "لا توجد ملفات",
  one: "ملف واحد",
  two: "ملفان",
  few: "{n} ملفات",
  many: "{n} ملفاً",
  other: "{n} ملف",
};
const text = messages[ar.select(n)].replace("{n}", n);
```

Use `Intl.PluralRules` with `{ type: "ordinal" }` for "1st / 2nd / 3rd / 4th" — these follow a different CLDR rule set from cardinals. Pair the result with `Intl.NumberFormat` so digits are rendered for the locale too (Arabic-Indic digits in `ar-EG`, Latin digits in `ar-SA`).

Any serious translation file format already encodes this: ICU MessageFormat (`{count, plural, one {1 file} other {# files}}`), Fluent, and gettext's `Plural-Forms` header all map a number to a category at runtime. Use one of those formats so translators can author the forms their language needs without touching code.

## Common mistakes

- `count === 1 ? "item" : "items"` — only works for English-like languages.
- Detecting the category by string-matching the number ("if it ends in 1…") — that is reinventing CLDR badly, and different languages have different rules.
- Concatenating strings like `"You have " + count + " items"`. Even with the right plural, word order differs by language. Use a template with a placeholder.
- Forgetting ordinals — "1st place" does not translate via cardinal rules.
- Adding a `zero` form to English. CLDR says English has no `zero` category; "0 items" uses `other`.
