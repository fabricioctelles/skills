# Implement Web Bot Auth

Use Web Bot Auth so your site can identify itself when it sends bot or agent requests, per the
[IETF WebBotAuth WG](https://datatracker.ietf.org/wg/webbotauth/about/).

## Requirements

- Publish a JWKS (JSON Web Key Set) at `/.well-known/http-message-signatures-directory`
- The JWKS must contain at least one public key for signature verification
- Sign requests sent by your bot or agent so receiving sites can verify them
- Include `Signature-Agent` and `Signature-Input` headers on those signed requests

## Cloudflare

[Web Bot Auth on Cloudflare](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/)
provides built-in support for verifying bot request signatures.

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.botAccessControl.webBotAuth.status` is `"pass"`.
