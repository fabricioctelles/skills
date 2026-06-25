# AI Workflow Mapping Example

This example shows the Looper artifact shape for mapping customer process notes
into an agent-ready workflow.

Compile after editing:

```bash
python ../../scripts/looper.py compile loop.yaml --out loop.resolved.json --render LOOP.md --session-prompt RUN_IN_SESSION.md
```

The easy path is to ask the current LLM session to follow `RUN_IN_SESSION.md`.

Use the Python runner only when you want to run the loop outside the LLM
session, after reviewing model invocations and privacy egress:

```bash
python run-loop.py
```
