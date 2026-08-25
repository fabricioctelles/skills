# Blast radius

Find what a small-looking change breaks elsewhere before it ships, beyond the diff, and prove the one fact it is safe because of by running code. Companion to `how` and `why`: how tells you what it does, why tells you why it is shaped that way, blast radius tells you what it breaks somewhere else.

Listing callers is not the job; grep does that in seconds. The job is the breakage grep will not show you.

## Do not trust your own writeup

A blast-radius writeup sounds convincing whether or not it is true; that is the trap. Find the one or two facts everything depends on and prove them by running code. Words are where you start, not what you ship.

Certainty ladder for each safety fact; get it as far down as cheaply possible and say where it stopped:

1. You said so. Worthless.
2. You pointed at the line. Real `file:line` or the library's source.
3. You showed the bad case cannot happen. Walked the failure step by step.
4. You ran it. A script or test calling the real code, failing loud if wrong.
5. You reproduced it in the running app.

Any fact short of step 4 gets said out loud as unproven. Step 4 is usually one small script importing the same library the app ships and calling the exact function in question.

## Steps

1. Read the change: diff, symbols added/changed/deleted, behavior differences including the part the diff does not spell out.
2. Find the one fact it is safe because of. Most scary-looking changes rest on a single fact ("this call only drops already-dead cache entries"). Find it; most scary cases die at once. Spend time here, not on a long maybe-list.
3. Look where grep stops. Library source at its pinned version plus local patches. Execution timing (microtasks, teardown). What symbol search misses: JSON payloads, DB columns, wire formats, another language reading the same bytes, feature flags, three hops downstream.
4. Be honest per risk: real chance, real cost, `file:line`. Confirmed risks listed; checked-and-cleared listed separately. Never invent a caller or API.
5. Prove the one fact: script or test running the real code, pasted output. Cannot prove cheaply: mark unproven, never round up.
6. Big or wide change: run it as an arena; different models catch different real bugs.

## Handback

What changed including the non-obvious part; the one safety fact with its ladder step and proof (or "unproven"); real risks with likelihood, cost, and how to check; cleared items; the cheapest test catching the real bug. Written through [unslop](unslop.md), citing real code, private data stripped.
