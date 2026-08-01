"""Model solution for Drill 1. Read this only after attempting starter.py unaided."""
import csv
from datetime import datetime
from pathlib import Path

DATE_FORMATS = ("%Y-%m-%d", "%d/%m/%Y")
DEFAULT_DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "transactions.csv"


def load_rows(path=DEFAULT_DATA_PATH):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def _parse_date(raw):
    raw = raw.strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(raw, fmt).date().isoformat()
        except ValueError:
            continue
    return None


def _parse_amount(raw):
    raw = (raw or "").strip()
    if not raw:
        return None
    try:
        value = float(raw)
    except ValueError:
        return None
    if value <= 0:
        return None
    return value


def clean_transactions(rows):
    clean, rejected = [], []

    for row in rows:
        tx_id = row["transaction_id"].strip()
        category = (row.get("category") or "").strip()

        date = _parse_date(row["date"])
        if date is None:
            rejected.append({"transaction_id": tx_id, "reason": "invalid date"})
            continue

        amount = _parse_amount(row.get("amount"))
        if amount is None:
            rejected.append({"transaction_id": tx_id, "reason": "invalid amount"})
            continue

        if not category:
            rejected.append({"transaction_id": tx_id, "reason": "missing category"})
            continue

        clean.append({
            "transaction_id": tx_id,
            "date": date,
            "amount": amount,
            "category": category,
        })

    return clean, rejected


if __name__ == "__main__":
    rows = load_rows()
    clean, rejected = clean_transactions(rows)
    print(f"{len(clean)} clean, {len(rejected)} rejected")
    for r in rejected:
        print("  rejected:", r)
