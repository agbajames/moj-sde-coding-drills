# Drill 3 — Validate and Aggregate a Case Records Extract

**Style:** combined validation + aggregation, closer to full exercise complexity.
**Suggested time:** 30 minutes, including reading this brief — this one is meant to feel tight.

## Brief

You're given a daily extract of case records from an operational system
(`data/case_records.csv`). Each row has `case_id`, `court`, `status`, and `received_date`.
Some rows are malformed and must not reach the aggregate counts.

Write a function:

```python
def process_case_records(rows: list[dict]) -> dict:
    """
    Returns a dict with four keys:
      - "valid": list of clean dicts (case_id, court, status, received_date as ISO string)
      - "quarantined": list of dicts (case_id, reason)
      - "counts_by_court": dict mapping court -> count of valid records
      - "counts_by_status": dict mapping status -> count of valid records
    """
```

### Validation rules

- `status` must be one of `{"received", "in_progress", "closed"}` (case-insensitive, but
  normalise to lowercase in the output). Anything else: reason `"invalid status"`.
- `received_date` must parse as `YYYY-MM-DD`. Anything else: reason `"invalid date"`.
- `court` must be non-empty after stripping whitespace. Anything else: reason `"missing court"`.
- `case_id` must be non-empty — if it's missing, still quarantine the row, using `"UNKNOWN"` as
  the id in the quarantine record (don't crash on a missing key).
- Check in this order: case_id present → status valid → date valid → court present. Stop at the
  first failure per row.

### What "done" looks like

- The function runs cleanly against the extract and produces sensible valid/quarantined output
  plus both count dictionaries.
- At least one test in `test_starter.py` passes.
- You can narrate, in real time, why you check fields in that specific order (structural
  problems — a record you can't even identify — before content problems).

This is the closest of the four drills to what the real 30-minute exercise is likely to feel
like: multiple rules, multiple outputs, and a deliberately tight clock.
