# Talking points for Drill 3

- **Structural checks before content checks**: a missing `case_id` means you can't even name
  the record in a quarantine log, so it's checked first, before anything about its content.
  This is the same instinct as Part Six's "quarantine, don't drop" whiteboarding structure —
  say that connection out loud if you get the chance.
- **`continue` per branch** keeps each validation rule readable as its own small block rather
  than nesting `if/elif/else` four deep — worth mentioning if asked why you structured it
  this way rather than one large conditional.
- **Aggregation happens inline, in the same loop as validation**, rather than as a second pass
  over `valid` afterwards — one read of the input, not two, which is the same efficiency
  instinct as Drill 2.
- **`dict(counts_by_court)`** at the end converts the `defaultdict` back to a plain `dict`
  before returning it — a small, easy-to-forget detail that stops a caller accidentally
  inserting new zero-count keys just by looking one up.
