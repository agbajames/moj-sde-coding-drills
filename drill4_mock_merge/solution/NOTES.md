# Talking points for Drill 4

- **The match key is a normalised email, never the name** — names collide (two "Chidi Umeh"s
  are plausible; two identical email addresses are effectively the same person). Say this out
  loud if asked why you didn't match on name: it's a data-quality judgement call, and being able
  to justify it is worth more than the code itself.
- **"Prefer A on conflict" needed to survive either ingestion order.** The obvious-looking
  approach — "just ingest A first, so its values are already in place" — quietly breaks the
  rule if a caller ever needs to ingest B first (e.g. B arrives before A in a real pipeline).
  The solution encodes the preference explicitly with `tag == "A"` checks rather than relying
  on call order, which is a more defensible design if asked "what if the sources arrived in
  the other order?"
- **`sources` as a `set` internally, sorted list on output** — sets make "did we see this
  customer in A, B, or both" trivial to accumulate, and converting to a sorted list right
  before returning keeps the output deterministic and testable.
- **This drill has a deliberately underspecified corner** (what "differ only in casing" means
  exactly) — the real exercise will have similar grey areas. State the assumption you're
  making, keep moving, and don't spend your clock trying to find a "perfect" rule.
