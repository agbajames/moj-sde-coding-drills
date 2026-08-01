"""Model solution for Drill 3."""
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "case_records.csv"
ALLOWED_STATUSES = {"received", "in_progress", "closed"}


def load_rows(path=DATA_PATH):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def process_case_records(rows):
    valid = []
    quarantined = []
    counts_by_court = defaultdict(int)
    counts_by_status = defaultdict(int)

    for row in rows:
        case_id = (row.get("case_id") or "").strip()
        if not case_id:
            quarantined.append({"case_id": "UNKNOWN", "reason": "missing case_id"})
            continue

        status = (row.get("status") or "").strip().lower()
        if status not in ALLOWED_STATUSES:
            quarantined.append({"case_id": case_id, "reason": "invalid status"})
            continue

        raw_date = (row.get("received_date") or "").strip()
        try:
            received_date = datetime.strptime(raw_date, "%Y-%m-%d").date().isoformat()
        except ValueError:
            quarantined.append({"case_id": case_id, "reason": "invalid date"})
            continue

        court = (row.get("court") or "").strip()
        if not court:
            quarantined.append({"case_id": case_id, "reason": "missing court"})
            continue

        valid.append({
            "case_id": case_id,
            "court": court,
            "status": status,
            "received_date": received_date,
        })
        counts_by_court[court] += 1
        counts_by_status[status] += 1

    return {
        "valid": valid,
        "quarantined": quarantined,
        "counts_by_court": dict(counts_by_court),
        "counts_by_status": dict(counts_by_status),
    }


if __name__ == "__main__":
    result = process_case_records(load_rows())
    print(f"{len(result['valid'])} valid, {len(result['quarantined'])} quarantined")
    print("by court:", result["counts_by_court"])
    print("by status:", result["counts_by_status"])
