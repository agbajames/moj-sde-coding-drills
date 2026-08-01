"""
Drill 3 starter. Read README.md first.
Run: python starter.py
Test: pytest test_starter.py
"""
import csv
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "case_records.csv"


def load_rows(path=DATA_PATH):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def process_case_records(rows):
    """TODO: implement. See README.md for the exact rules and return shape."""
    raise NotImplementedError


if __name__ == "__main__":
    result = process_case_records(load_rows())
    print(f"{len(result['valid'])} valid, {len(result['quarantined'])} quarantined")
    print("by court:", result["counts_by_court"])
    print("by status:", result["counts_by_status"])
