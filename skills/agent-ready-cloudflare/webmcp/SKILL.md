---
name: agent-ready-webmcp
description: >
  Sub-skill de agent-ready-cloudflare: Implement WebMCP
---
# Implement WebMCP

Expose site tools to AI agents via the browser using the
[WebMCP API](https://webmachinelearning.github.io/webmcp/)
([Chrome blog](https://developer.chrome.com/blog/webmcp-epp),
[declarative API](https://github.com/webmachinelearning/webmcp/blob/main/declarative-api-explainer.md)).

## Requirements

- Call `document.modelContext.registerTool()` for each tool you want to expose; it returns a Promise
- Each tool needs `name`, `description`, `inputSchema` (JSON Schema), and an `execute` callback
- Tools should expose your site's key actions (search, navigation, data retrieval)
- Pass an `AbortController` signal in the options to unregister tools when no longer needed
- For existing HTML forms, add `toolname` and `tooldescription` to the `<form>` and `toolparamdescription` to its inputs to expose them declaratively
- Older Chrome builds expose the API on `navigator.modelContext`; feature-detect `document.modelContext` first and fall back to it if needed
- The API is detected by loading the page in a browser — ensure the script runs on page load

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.discovery.webMcp.status` is `"pass"`.
