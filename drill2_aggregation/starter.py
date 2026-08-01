"""
Drill 2 starter. Read README.md first.
Run: python starter.py
Test: pytest test_starter.py
"""
import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "orders.json"


def load_orders(path=DATA_PATH):
    with open(path) as f:
        return json.load(f)


def aggregate_orders(orders):
    """TODO: implement. See README.md for the exact return shape."""
    raise NotImplementedError


if __name__ == "__main__":
    result = aggregate_orders(load_orders())
    print(result)
