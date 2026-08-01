# Talking points for Drill 1

- **Order of checks matters and is worth stating out loud**: date first, then amount, then
  category — pick an order, say why, and be consistent. Here the order roughly follows "most
  structurally broken first" (a date that doesn't parse at all vs a field that's simply empty).
- **`strptime` with a tuple of formats** is the cleanest way to handle "may arrive in either of
  two shapes" without writing brittle regex — this is a pattern worth having ready for any
  date-normalisation question.
- **Reject, don't crash**: every bad row produces a structured rejection with a reason, rather
  than raising an exception or silently dropping it — this is the "quarantine, don't drop"
  instinct from the whiteboarding structure in Part Six of the main prep pack.
- **Whitespace stripping happens before validation, not after** — a value of `" "` (just spaces)
  needs to be treated as empty, which only works if you strip first.
