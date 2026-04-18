# Implement llms-full.txt

Publish expanded LLM content per
[llmstxt.org](https://llmstxt.org/).

## Requirements

- Serve `/llms-full.txt` as plain text (UTF-8) with HTTP 200
- Include structured, detailed content suitable for LLM ingestion
- Cover the key topics, APIs, and documentation from your site
- Link to it from your `/llms.txt` file

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Confirm your deployed site serves `/llms-full.txt` exactly as intended.
