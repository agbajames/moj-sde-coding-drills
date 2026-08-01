from starter import merge_customer_records, load_source


def _by_email(records):
    return {r["email"]: r for r in records}


def test_unique_customer_count():
    merged = merge_customer_records(load_source("source_a.csv"), load_source("source_b.csv"))
    # 5 in A, 5 in B, 3 overlap (alice, chidi, diana) -> 7 unique customers
    assert len(merged) == 7


def test_matched_in_both_sources():
    merged = _by_email(merge_customer_records(load_source("source_a.csv"), load_source("source_b.csv")))
    alice = merged["alice.whitfield@example.com"]
    assert alice["sources"] == ["A", "B"]
    assert alice["phone"] == "07700 900123"  # only A has a phone for Alice


def test_email_normalised():
    merged = _by_email(merge_customer_records(load_source("source_a.csv"), load_source("source_b.csv")))
    assert "chidi.umeh@example.com" in merged
    chidi = merged["chidi.umeh@example.com"]
    assert chidi["sources"] == ["A", "B"]


def test_phone_conflict_prefers_a_when_both_present():
    merged = _by_email(merge_customer_records(load_source("source_a.csv"), load_source("source_b.csv")))
    diana = merged["diana.petrescu@example.com"]
    assert diana["phone"] == "07700 900789"  # A's number, not B's 07700 900999


def test_single_source_customers_flagged():
    merged = _by_email(merge_customer_records(load_source("source_a.csv"), load_source("source_b.csv")))
    assert merged["fatima.khan@example.com"]["sources"] == ["B"]
    assert merged["ewan.mcallister@example.com"]["sources"] == ["A"]
