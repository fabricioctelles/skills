# Goal Rubric

Use this when shaping the user's loop goal.

## Good Goal Shape

- Names the concrete outcome, not only the activity.
- Defines the artifact or state that proves the loop finished.
- Sets scope boundaries: included work, excluded work, and maximum depth.
- Names context sources the host must gather instead of assumptions it may make.
- Identifies the user, customer, system, or reviewer who will consume the result.

## Critique Prompts

- What would count as done if two competent agents disagreed?
- Which terms are subjective and need a measurable proxy?
- What context must be read before the host drafts a plan?
- What is explicitly out of scope for this loop?
- Can the goal be split into plan, delivery, and verification artifacts?

## Anti-Patterns

- "Improve the project" without a target artifact.
- "Make it good" without criteria.
- "Research X" without the decision the research supports.
- Goals where success depends on information the loop never gathers.
- Goals that require endless polishing with no stop condition.

## Better Examples

Weak: "Make our onboarding better."

Better: "Produce a 5-step onboarding workflow map for new enterprise users,
with each step assigned to a product surface, email, human owner, or missing
capability, and with no unresolved TBDs."

Weak: "Fix the flaky tests."

Better: "Identify and patch the root cause of the checkout test flake, prove it
with 20 local repeats or a CI rerun, and leave a short note explaining the
failure mode and the verification evidence."

