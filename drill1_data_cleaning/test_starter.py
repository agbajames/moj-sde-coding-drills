from starter import clean_transactions, load_rows


def test_counts():
    rows = load_rows()
    clean, rejected = clean_transactions(rows)
    # 10 input rows: T001, T002, T006, T009 are genuinely clean (4).
    # T003, T005, T007, T008, T010 have a bad amount (5).
    # T004 has a bad date (1).
    assert len(clean) == 4
    assert len(rejected) == 6


def test_date_normalised_to_iso():
    rows = load_rows()
    clean, _ = clean_transactions(rows)
    t002 = next(r for r in clean if r["transaction_id"] == "T002")
    assert t002["date"] == "2026-01-05"


def test_whitespace_stripped():
    rows = load_rows()
    clean, _ = clean_transactions(rows)
    t006 = next(r for r in clean if r["transaction_id"] == "T006")
    assert t006["category"] == "groceries"
    assert t006["amount"] == 33.10


def test_rejection_reasons():
    rows = load_rows()
    _, rejected = clean_transactions(rows)
    reasons = {r["transaction_id"]: r["reason"] for r in rejected}
    assert reasons["T004"] == "invalid date"
    assert reasons["T003"] == "invalid amount"
    assert reasons["T008"] == "missing category"
