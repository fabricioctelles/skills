---
title: "/.well-known/webfinger"
category: well-known
status: optional
updated: "2026-05-29T09:13:20.000Z"
sources:
  - title: "RFC 7033 — WebFinger"
    url: "https://www.rfc-editor.org/rfc/rfc7033"
    publisher: "IETF"
  - title: "IANA — Well-Known URIs Registry"
    url: "https://www.iana.org/assignments/well-known-uris/well-known-uris.xhtml"
    publisher: "IANA"
  - title: "ActivityPub — W3C Recommendation"
    url: "https://www.w3.org/TR/activitypub/"
    publisher: "W3C"
licence: CC-BY-4.0
---

# /.well-known/webfinger

> WebFinger (RFC 7033) resolves an account identifier such as acct:user@example.com to a set of links. The Fediverse uses it to discover ActivityPub actors.

## What it is

WebFinger is a discovery protocol defined in **RFC 7033**. A client asks `/.well-known/webfinger` for information about a resource identifier — typically an account in the form `acct:user@example.com` — and the server returns a JSON Resource Descriptor (JRD) describing that resource and where to find more.

It is the protocol that lets you type `@alice@mastodon.example` into any Fediverse client and have it resolve to Alice's ActivityPub profile, regardless of which server she lives on.

## Why it matters

- **Federation depends on it.** Mastodon, Pleroma, Misskey, GoToSocial, PeerTube, Lemmy and every other ActivityPub-speaking platform use WebFinger as step one of "who is this user".
- **It abstracts the URL.** A handle like `acct:joost@example.com` is human-friendly. The actual ActivityPub actor URL might be `https://example.com/users/joost`. WebFinger maps one to the other.
- **It works across protocols.** WebFinger is not tied to ActivityPub. It can advertise any kind of link relation for any kind of resource.

If your site does not host accounts that need to federate, you do not need this URL.

## How to implement

Accept GET requests with a `resource` query parameter. Return `application/jrd+json`.

```http
GET /.well-known/webfinger?resource=acct:joost@example.com HTTP/1.1
Host: example.com
Accept: application/jrd+json
```

A typical response for a Fediverse account:

```json
{
  "subject": "acct:joost@example.com",
  "aliases": [
    "https://example.com/@joost",
    "https://example.com/users/joost"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://example.com/@joost"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://example.com/users/joost"
    }
  ]
}
```

Rules:

- Serve over **HTTPS**, and respond on the host that matches the right-hand side of the `acct:` URI. A query for `joost@example.com` must be answered by `example.com`, not `social.example.com`.
- Return `404` for unknown resources, `400` for a missing or malformed `resource` parameter.
- Accept the `rel` query parameter and filter the `links` array accordingly. Clients use it to reduce payload size.
- Set permissive `Access-Control-Allow-Origin: *` so browser-based clients can fetch the response.

## Common mistakes

- Answering on the wrong host. If user identifiers look like `@alice@example.com` but WebFinger lives on `social.example.com`, federation breaks. Fix this by serving WebFinger from `example.com` and redirecting or proxying as needed.
- Returning `text/plain` or `application/json` instead of `application/jrd+json`.
- Leaking the existence of accounts via different responses for "user exists but private" and "user does not exist". Pick one behaviour and apply it consistently.
- Ignoring the `rel` filter and always returning every link.

## Verification

```
curl -s "https://example.com/.well-known/webfinger?resource=acct:joost@example.com" | jq .
```

Then try to follow your account from a Mastodon server you do not control. If federation fails, WebFinger is almost always the first thing to check.
