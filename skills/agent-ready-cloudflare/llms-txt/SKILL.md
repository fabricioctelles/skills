---
name: agent-ready-llms-txt
description: >
  Sub-skill de agent-ready-cloudflare: Implement llms.txt
---
# Implement llms.txt

Publish an LLM-friendly overview of your site per
[llmstxt.org](https://llmstxt.org/).

## Requirements

- Serve `/llms.txt` as plain text (UTF-8) with HTTP 200
- Start with an H1 (`# Site Name`) title line
- Include a short summary paragraph describing your site
- Link to the most important content sections for agents
- Optionally link to `/llms-full.txt` for expanded content

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Confirm your deployed site serves `/llms.txt` exactly as intended.
