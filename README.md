# Coding Exercise Drills — MoJ Senior Data Engineer Prep

These are **practice problems modelled on the style of exercise described in the interview
invite** (Python, GitHub Codespaces, data-cleaning/ETL flavour, tested with pytest, no AI
tools, talk-through-your-approach). They are not the actual MoJ exercise — there's no way to
know that in advance — but they're deliberately built to rehearse the same underlying skills:
reading a written brief fast, handling messy real-world data, writing a testable function
under a 30-minute clock, and narrating your reasoning out loud the whole time.

## How to use these

Each `drillN_*/` folder is self-contained:

- `README.md` — the brief, written as the interviewer's instructions. Read this first, and only this.
- `data/` — the input file(s).
- `starter.py` — a stub with the function signature and a `TODO`. This is what you edit.
- `test_starter.py` — run `pytest test_starter.py` from inside the drill folder once you think
  you're done, to check your work.
- `solution/solution.py` — the model answer. **Don't open this until you've either finished, or
  the clock has run out.** The value of these drills is in the unaided attempt, not the answer.
- `solution/NOTES.md` — talking points: the things worth saying out loud in the real interview
  about *why* the solution is shaped the way it is, not just what it does.

## Suggested order (matches the six-day execution plan)

1. **Drill 1 — Clean and Validate a Transaction Extract** (Day 1 baseline): straightforward
   validation and normalisation. Good for finding your true unaided starting point.
2. **Drill 2 — Aggregate Orders Without pandas** (Day 2): pure `dict`/`defaultdict`/`Counter`
   fluency, no validation complexity, to build that muscle in isolation.
3. **Drill 3 — Validate and Aggregate a Case Records Extract** (Day 4): combines validation and
   aggregation in one function, closer to full exercise complexity, MoJ-flavoured.
4. **Drill 4 — Merge and Deduplicate Customer Records** (Day 5 full mock): the least scaffolded
   of the four, with a genuinely ambiguous corner case you have to make a judgement call on —
   treat this one exactly like the real thing.

## Running any drill

```bash
cd drillN_*
python starter.py        # once you've implemented clean_transactions/aggregate_orders/etc.
pytest test_starter.py   # -v for more detail
```

No extra packages are required beyond the Python standard library and pytest.
