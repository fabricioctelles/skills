# TypeScript best practices

Apply [type-system-discipline](../principles.md#type-system-discipline) first; this grounds it in TS syntax.

| Rule | Summary |
|------|---------|
| Discriminated unions | Model variants with a `kind` literal discriminant so impossible states cannot be represented. No optional-field bags. |
| Branded types | Brand primitives with `& { readonly __brand: "X" }`; validate once at creation. |
| Constructive modeling | Build the shape so the illegal value cannot be constructed: `[T, ...T[]]` non-empty, `start` + `duration` range. Not runtime guards. |
| Simplest total type | Keep `T[]` while operations stay total; strengthen to `NonEmpty<T>` only where the loose type forces `!`, casts, or throws. |
| `unknown` over `any` | External data is `unknown`. `any` disables checking everywhere it touches. |
| No `as` casts | Every `as` is a runtime crash waiting. Cast only after validation. |
| Narrowing hierarchy | Discriminant switch > `in` > `typeof`/`instanceof` > user-defined guard > `as`. |
| Type guards | Must verify the claim; a lying guard hides behind a safe-looking name. Name `isX` / `hasX`. |
| Exhaustiveness | Inline `const _exhaustive: never = x;` in default arms so adding a variant fails compilation. |
| `satisfies` over `as` | Validates without widening literal types. |
| Boundary validation | Parse incoming data once into a named domain type ([boundary-discipline](../principles.md#boundary-discipline)); trust types inside. |
| Schema-derived types | Reach for `Pick`/`Omit`/`Parameters`/`ReturnType`/`Awaited`/`typeof` before declaring new interfaces. |
| Object args | Pass objects over positionals on non-hot paths so order self-documents. |
| Real tests | Do not mock what you can run; verify UI in a running build. Mock only what cannot run locally. |
| Structured telemetry | Structured logs debuggable from an id. No `console.log` in shipped code. |
