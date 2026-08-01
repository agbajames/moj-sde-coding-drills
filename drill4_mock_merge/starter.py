"""
Drill 4 starter — the Day 5 full mock. Read README.md first.
Run: python starter.py
Test: pytest test_starter.py
"""
import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"


def load_source(filename):
    with open(DATA_DIR / filename, newline="") as f:
        return list(csv.DictReader(f))


def merge_customer_records(source_a, source_b):
    """TODO: implement. See README.md for the exact matching and conflict rules."""
    raise NotImplementedError


if __name__ == "__main__":
    merged = merge_customer_records(load_source("source_a.csv"), load_source("source_b.csv"))
    for record in merged:
        print(record)
