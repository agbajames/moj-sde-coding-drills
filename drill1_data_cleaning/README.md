# Drill 1 — Clean and Validate a Transaction Extract

**Style:** data cleaning / validation. **Suggested time:** 30 minutes, including reading this brief.

## Brief (read this as the interviewer's instructions)

You've been given a CSV export of transaction events from a legacy system (`data/transactions.csv`).
The export is messy: some rows have missing amounts, some dates are in an inconsistent format,
some fields have stray whitespace, and some rows are invalid in other ways.

Write a function:

```python
def clean_transactions(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    rows: a list of dicts as read directly from the CSV (all values are strings).

    Returns a tuple (clean, rejected):
      - clean: list of dicts with keys transaction_id, date (ISO 'YYYY-MM-DD' string),
        amount (float), category (str), for every row that passes validation.
      - rejected: list of dicts with keys transaction_id, reason (str), for every row
        that fails validation.
    """
```

### Validation rules

- `date` may arrive as `YYYY-MM-DD` or `DD/MM/YYYY`. Normalise it to `YYYY-MM-DD` in the output.
  If it doesn't parse in either format, reject with reason `"invalid date"`.
- `amount` must parse as a positive number. Missing, non-numeric, or non-positive amounts are
  rejected with reason `"invalid amount"`.
- `category` must be non-empty after stripping whitespace. Reject empty categories with reason
  `"missing category"`.
- Strip leading/trailing whitespace from every string field before validating or returning it.
- If a row fails more than one rule, report whichever reason you hit first — there's no single
  right order, just be consistent and be able to explain your choice out loud.

### What "done" looks like

- `clean_transactions` runs against `data/transactions.csv` and produces sensible clean/rejected lists.
- At least one test in `test_starter.py` passes.
- You can explain, out loud, in under 60 seconds, how you handled the two date formats and why.

Do this one without looking at `solution/` first. Time yourself.
