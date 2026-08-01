# Drill 4 — Merge and Deduplicate Customer Records Across Two Sources

**Style:** the Day 5 full mock. Treat this one as the real thing: 30 minutes, no AI, timer on,
narrate out loud, and don't look at the other drills' solutions first.

## Brief

Two systems each export a customer contact list independently: `data/source_a.csv` and
`data/source_b.csv`. The same customer sometimes appears in both, but formatted slightly
differently — different case, stray whitespace, a phone number present in one export and
missing in the other.

Write a function:

```python
def merge_customer_records(source_a: list[dict], source_b: list[dict]) -> list[dict]:
    """
    Each input record has: name, email, phone (phone may be an empty string).

    Match records across the two sources on a *normalised* email address:
    lowercase, stripped of surrounding whitespace.

    Returns a list of dicts, one per unique customer (by normalised email), each with:
      - name: prefer the longer of the two names if both sources have this customer and they
        differ only in casing/whitespace-trimmed length; otherwise prefer source A's version.
      - email: the normalised email.
      - phone: prefer whichever source has a non-empty phone; if both do and they differ,
        prefer source A's.
      - sources: a sorted list containing "A", "B", or both — whichever source(s) this
        customer appeared in.
    """
```

### What "done" looks like

- The function runs against both CSVs and produces one merged, deduplicated list.
- At least one test in `test_starter.py` passes.
- You can explain, out loud, in under 90 seconds, how you chose to normalise the match key and
  why email rather than name (names collide far more easily than email addresses).

This is deliberately the least scaffolded of the four drills — the real exercise brief will
have gaps you need to make a reasonable, defensible judgement call on, exactly like the "prefer
source A's version" and "differ only in casing" language above. State your assumption out loud
and move on, don't freeze on it.
