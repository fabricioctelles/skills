# Architect

Before writing code, trace every system the change touches, then sketch two structurally different shapes for it (types, signatures, module boundaries, with `not implemented` bodies) and pick the one where each piece of state has one owner, each task has one way to do it, and callers need to know least. Write caller usage first, then the types. Naming a file is not grounding. If the design redefines ownership or layering, run `why` first so the rationale is a constraint, not a guess.

For a large or contested design, run the **arena** procedure instead of sketching alone, with the traced systems as shared grounding.

Reject a shape with shallow modules that leak what they should hide, phase-named modules that repeat domain rules, or pass-through layers. Proceed to implementation by default. Pause for sign-off only when the invoker asks ("with checkpoint"), and run `interrogate` on the sketch when it needs adversarial pressure.

The sketch is the contract. Surface every deviation. Redesign instead of patching when workarounds repeat: the same workaround in unrelated code, types that need escape hatches, or callers that must know internal rules. Redesign as if the new constraints were there from day one ([redesign-from-first-principles](../principles.md#redesign-from-first-principles)), starting smaller than the old sketch.
