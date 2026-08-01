"""Model solution for Drill 4."""
import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_source(filename):
    with open(DATA_DIR / filename, newline="") as f:
        return list(csv.DictReader(f))


def _normalise_email(raw):
    return raw.strip().lower()


def merge_customer_records(source_a, source_b):
    by_email = {}

    def ingest(records, tag):
        for row in records:
            email = _normalise_email(row["email"])
            name = row["name"].strip()
            phone = (row.get("phone") or "").strip()

            if email not in by_email:
                by_email[email] = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "sources": {tag},
                }
                continue

            existing = by_email[email]
            existing["sources"].add(tag)

            # Prefer the longer name (a reasonable proxy for "more complete"),
            # falling back to whichever came from source A on an exact tie.
            if tag != "A" and len(name) > len(existing["name"]):
                existing["name"] = name
            elif tag == "A":
                # Re-ingesting A after B already set the record (order-independent):
                # A's name wins on a length tie, and A's phone wins if both are present.
                if len(name) >= len(existing["name"]):
                    existing["name"] = name

            if not existing["phone"] and phone:
                existing["phone"] = phone
            elif tag == "A" and phone:
                existing["phone"] = phone  # A wins on a genuine conflict

    # Ingest A first so that, on a conflict, "prefer A" is the natural default;
    # the tag == "A" branches above make this correct even if the call order changes.
    ingest(source_a, "A")
    ingest(source_b, "B")

    merged = []
    for record in by_email.values():
        record["sources"] = sorted(record["sources"])
        merged.append(record)

    return sorted(merged, key=lambda r: r["email"])


if __name__ == "__main__":
    merged = merge_customer_records(load_source("source_a.csv"), load_source("source_b.csv"))
    for record in merged:
        print(record)
