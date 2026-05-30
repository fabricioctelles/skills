---
title: "Internationalised Domain Names (IDN)"
category: i18n
status: optional
updated: "2026-05-29T18:54:03.000Z"
sources:
  - title: "RFC 5891 — IDNA 2008: Protocol"
    url: "https://www.rfc-editor.org/rfc/rfc5891"
    publisher: "IETF"
  - title: "RFC 5890 — IDNA 2008: Definitions and Document Framework"
    url: "https://www.rfc-editor.org/rfc/rfc5890"
    publisher: "IETF"
  - title: "Unicode TR #46 — Unicode IDNA Compatibility Processing"
    url: "https://unicode.org/reports/tr46/"
    publisher: "Unicode"
  - title: "Chromium — IDN in Google Chrome"
    url: "https://chromium.googlesource.com/chromium/src/+/main/docs/idn.md"
    publisher: "Chromium project"
licence: CC-BY-4.0
---

# Internationalised Domain Names (IDN)

> IDNs let domain names contain non-ASCII characters. They are encoded as Punycode on the wire and rendered as Unicode in the browser, subject to anti-spoofing rules.

## What it is

Internationalised Domain Names allow labels in a hostname to contain characters outside ASCII — Cyrillic, Greek, Han, Arabic, accented Latin, and so on. `münchen.de`, `日本語.jp`, and `παράδειγμα.gr` are all valid.

DNS itself only carries ASCII, so each non-ASCII label is encoded with [Punycode](https://www.rfc-editor.org/rfc/rfc3492) and prefixed with `xn--`. The browser shows the Unicode form to the user; the resolver, certificate, and `Host` header see the ASCII form.

```
User sees:    münchen.de
On the wire:  xn--mnchen-3ya.de
```

The current standard is **IDNA 2008** ([RFC 5890–5894](https://www.rfc-editor.org/rfc/rfc5891)), with [Unicode TR #46](https://unicode.org/reports/tr46/) defining the compatibility processing browsers actually use.

## Why it matters

For users outside the ASCII-Latin world, a domain in their own script is more memorable, more brandable, and easier to type than a transliteration. For everyone, the security implications matter: visually similar characters across scripts ("paypal" written with a Cyrillic "а" instead of Latin "a") enable **homograph attacks**, where a malicious domain impersonates a real one. Browsers therefore apply display rules that decide when to show the Unicode form and when to fall back to Punycode in the address bar.

## How to implement

Most sites only consume IDNs; few operate them. Either way, get the basics right.

**If you own an IDN:**

- Register both the IDN and an ASCII fallback, and `301` between them so links and analytics consolidate.
- Get a TLS certificate that covers both forms. Modern CAs handle this automatically when you submit the A-label (`xn--…`); verify the certificate's `dNSName` SAN entries include the encoded form.
- Set `<link rel="canonical">` to one form (typically the Unicode form) so search engines pick a single representation.
- Test mail flow. Local-part Internationalised Email ([RFC 6531](https://www.rfc-editor.org/rfc/rfc6531)) is a separate spec and patchily supported.

**If your site accepts hostnames as input (email, URLs, webhooks):**

- Normalise with **IDNA 2008 + UTS #46** before storing. Use a library (`idna` in Python, `url.domainToASCII` in Node, `IDN` in the JDK) rather than hand-rolling the algorithm.
- Store the A-label (`xn--…`) as the canonical key and display the U-label (Unicode) to users.
- Apply your platform's spoofing protection: mixed-script detection, confusable-character checks, and the [Unicode confusables data](https://www.unicode.org/Public/security/latest/confusables.txt).

**Browser display rules.** Chromium, Firefox, and Safari each maintain a policy: show Unicode if the label is in a single script (with a few mixed exceptions), or if the user's configured languages include that script. Otherwise show Punycode. You cannot override this from a website, and you should not try — it is the user's protection against homograph attacks. Test your IDN in each browser and accept that some users will see `xn--mnchen-3ya.de`.

## Common mistakes

- Comparing hostnames as raw Unicode strings, missing case folding, NFC normalisation, and IDNA mapping. Always normalise to the A-label first.
- Accepting an IDN at registration but not on login because two libraries normalise differently.
- Assuming the address bar always shows Unicode. Browser policy may downgrade to Punycode, which is fine.
- Issuing a certificate only for the U-label. Certificates must cover the A-label encoding.
- Treating IDN as a green-light for arbitrary Unicode. IDNA 2008 disallows many code points (symbols, emoji, joiners) for safety.
