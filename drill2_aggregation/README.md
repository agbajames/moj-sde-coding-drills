# Drill 2 — Aggregate Orders Without pandas

**Style:** aggregation / dict and collections fluency. **Suggested time:** 30 minutes.

## Brief

You're given a JSON export of orders (`data/orders.json`), a list of objects like:

```json
{"order_id": "O001", "region": "London", "product": "Widget", "revenue": 120.50}
```

You do **not** have pandas available in this environment — build the aggregation with plain
dictionaries, `collections.Counter`, or `collections.defaultdict`.

Write a function:

```python
def aggregate_orders(orders: list[dict]) -> dict:
    """
    Returns a dict with two keys:
      - "revenue_by_region": dict mapping region -> total revenue (float), rounded to 2 dp.
      - "top_products": list of (product, total_revenue) tuples, the 3 highest-revenue
        products overall, sorted descending by revenue. If there's a tie, break it
        alphabetically by product name.
    """
```

### Notes

- Revenue values are already valid floats in this file — no cleaning required, this drill is
  about aggregation, not validation (that was Drill 1).
- Round every revenue total to 2 decimal places in the output.
- Don't import pandas even if it happens to be installed in your environment — the point of
  this drill is fluency with `dict`/`Counter`/`defaultdict`, which is what you'll have if the
  real exercise's environment doesn't include pandas.

### What "done" looks like

- `aggregate_orders` runs against `data/orders.json` and produces a plausible-looking
  `revenue_by_region` and a 3-item `top_products` list.
- At least one test in `test_starter.py` passes.
- You can explain out loud, in under 60 seconds, why you chose `defaultdict` (or plain `dict`
  with `.get`) over building a list and scanning it repeatedly.
