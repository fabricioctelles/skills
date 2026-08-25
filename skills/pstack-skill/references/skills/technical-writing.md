# Technical writing

Write documentation a tired engineer understands on the first read: docs, RFCs, readmes, PR descriptions, commit messages. Four layers, one question each: what kind of document is this, how do sentences address the reader, how much does each sentence carry, can any sentence be read two ways.

Three rules sit above the layers:

- **Cut every word that does no work.** "In order to" is "to". "It is important to note that" is nothing.
- **Use the short everyday word.** "Use", not "utilize". "Do", not "perform".
- **When a rule makes a sentence worse, fix the sentence another way or leave it alone.**

The codebase is the word list: write the real symbol, file, flag, command. Do not invent jargon; if you need a named pattern, define it at first use.

Vary rhythm so the doc does not read machine-clipped: mix sentence lengths on purpose, split sentences carrying two thoughts, have a view where the mode allows it, prefer specific over sterile ("a column rename fails the build", not "schema changes can cause issues").

## Pick the mode first (Diataxis)

One document, one mode. Action+learning: tutorial. Action+work: how-to. Understanding+work: reference. Understanding+learning: explanation. No mixing; split and link instead.

- **Tutorial.** You are the teacher. Open with what the learner will build. Every step produces visible results early and often; tell them what they should see.
- **How-to.** Steps to a goal for a competent person. No digressions, no background. Name it by task: "How to calibrate the radar array".
- **Reference.** Describe, only describe. Dry, complete, sure. Mirror the structure of the thing described.
- **Explanation.** One bounded topic anchored on a real why question. Context, decisions, alternatives. Opinion lives here and nowhere else.

## Write to the reader

Present tense, "you", active voice naming the actor. Instructions as commands. Condition before instruction ("To delete the document, click Delete"). Common case first. Headings carry the point, not just the topic; sentence case. Numbered lists for sequences, bullets otherwise, introduced by a complete sentence. Never "simply", "easy", or "please" in a procedure. Links say where they go.

## One statement per sentence

One instruction per sentence; split instructions past ~20 words. Warning before the step it guards. Keep articles ("Remove the backup file", not "Remove backup file"). One meaning per word; one verb per action everywhere. Procedures as direct commands, never narration or passive. Prefer "-ing"-free constructions.

## Leave no sentence open to two readings

"Only" and "not" sit next to what they change. Break long noun strings. Every "it" and "this" points at one obvious thing; repeat the noun when in doubt. No dropped verbs in series. Keep structural small words ("that"). Disambiguate joins ("both...and", "either...or"). Periods, not semicolons. Parenthetical text is a full grammatical unit. No "(s)" plurals, no slashes-for-or. One name per thing across the whole doc. Skip idioms and Latin abbreviations; plain constructions parse best for non-native readers and agents alike.

PR descriptions and commit messages follow every layer except Diataxis. Apply [unslop](unslop.md) to everything this procedure touches.
