# Talking points for Drill 2

- **`defaultdict(float)`** removes the need for `if key not in dict: dict[key] = 0` boilerplate —
  a small thing, but it's exactly the kind of idiom panels notice under time pressure.
- **Two passes, one loop**: both aggregations (by region, by product) happen in the same
  single pass over `orders`, rather than iterating the list twice. Worth saying out loud —
  it shows you're thinking about scanning cost even on a small list.
- **Sorting with a composite key** `(-item[1], item[0])` gives you "descending by revenue,
  then ascending alphabetically" in one `sorted()` call — a pattern worth having ready
  any time a tie-break rule is mentioned.
- **Rounding only at the output boundary**, not during accumulation, avoids compounding
  floating-point rounding error across many additions.
