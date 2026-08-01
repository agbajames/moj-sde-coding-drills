"""
Drill 1 starter. Read README.md first.

Run this file directly to see your clean/rejected output:
    python starter.py

Run the tests with:
    pytest test_starter.py
"""
import csv


def load_rows(path="data/transactions.csv"):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def clean_transactions(rows):
    """
    TODO: implement this.

    rows: list[dict] as read from the CSV (all values are strings).
    Returns: (clean, rejected) — see README.md for the exact shape and rules.
    """
    raise NotImplementedError


if __name__ == "__main__":
    rows = load_rows()
    clean, rejected = clean_transactions(rows)
    print(f"{len(clean)} clean, {len(rejected)} rejected")
    for r in rejected:
        print("  rejected:", r)
