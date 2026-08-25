# Architect

Design before implementing. Sketch types, function signatures, class shapes, and module boundaries with `not implemented` bodies; fill in code against the chosen sketch afterward. If implementation proves the sketch wrong, throw it out and redesign. Use whenever code crosses a function boundary and the shape is not already obvious.

Open a todolist with one entry per phase.

1. Ground
2. Sketch
3. Agree
4. Implement
5. Scrap

## Phase A: Ground

Build a traced mental model of every system the new code touches: run the `how` procedure over the relevant subsystems, critique mode when existing structure is the constraint. Naming a file is not grounding. If the design redefines ownership or layering, also run `why` so the rationale becomes a constraint, not a guess.

Skip only for genuinely greenfield work with nothing to integrate.

## Phase B: Sketch

Run the arena procedure on the design-sketch task with Phase A artifacts as shared grounding. Require at least two structurally distinct candidates before synthesis, whole-shape alternatives rather than point fixes inside one shape ([exhaust-the-design-space](../principles.md#exhaust-the-design-space)). Each candidate writes: caller usage first, then type sketch, signatures, module map, prose rationale derived from it.

Screen every candidate against these red flags before synthesis: shallow modules that leak what they should hide, information leaking across boundaries, temporal decomposition (phase-named modules repeating domain rules), pass-through methods that add layers without compression. Prefer the candidate that hides more complexity behind a smaller public surface.

Arena returns one synthesized package plus a synthesis-decision note.

## Phase C: Agree

Default: proceed straight to implementation. Pause for sign-off only when the invoker explicitly asks. The sketch can land as its own scaffold-first commit; planned, scoped breakage during fill-in is fine ([outcome-oriented-execution](../principles.md#outcome-oriented-execution)). For adversarial pressure before implementing, run interrogate on the sketch.

Human pushback on the shape, at a checkpoint or after the fact, is Phase A evidence: re-ground and re-run Phase B before writing more code.

## Phase D: Implement against the sketch

The sketch is the contract. Deviations are signal, not friction to absorb silently: if a function needs an unanticipated parameter, decide whether the sketch was wrong, the requirement was missed, or the implementation overreaches, and surface it.

## Phase E: Scrap when the architecture is wrong

The trigger is a *pattern* of friction, not single instances: the same workaround shape recurring across unrelated code, unrelated edge cases all needing special branches, types needing escape hatches to compile, callers having to know internal rules, two or more independent same-shaped deviations during fill-in.

When you scrap: re-run `how` over what has been built so lessons enter as inputs; redesign as if the new constraints were day-one assumptions ([redesign-from-first-principles](../principles.md#redesign-from-first-principles)); subtract before adding, so the new sketch starts smaller than the old one; return to Phase B.
