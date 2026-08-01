from starter import process_case_records, load_rows


def test_valid_and_quarantined_counts():
    result = process_case_records(load_rows())
    assert len(result["valid"]) == 6
    assert len(result["quarantined"]) == 4


def test_status_normalised_lowercase():
    result = process_case_records(load_rows())
    c1006 = next(r for r in result["valid"] if r["case_id"] == "C1006")
    assert c1006["status"] == "in_progress"


def test_missing_case_id_uses_unknown():
    result = process_case_records(load_rows())
    unknown = [q for q in result["quarantined"] if q["case_id"] == "UNKNOWN"]
    assert len(unknown) == 1
    assert unknown[0]["reason"] == "missing case_id"


def test_counts_by_court_and_status():
    result = process_case_records(load_rows())
    assert result["counts_by_court"]["Manchester Crown Court"] == 3
    assert result["counts_by_court"]["Leeds Magistrates Court"] == 2
    assert result["counts_by_court"]["Birmingham Crown Court"] == 1
    assert result["counts_by_status"]["received"] == 2
    assert result["counts_by_status"]["closed"] == 2
    assert result["counts_by_status"]["in_progress"] == 2


def test_quarantine_reasons():
    result = process_case_records(load_rows())
    reasons = {q["case_id"]: q["reason"] for q in result["quarantined"] if q["case_id"] != "UNKNOWN"}
    assert reasons["C1004"] == "missing court"
    assert reasons["C1005"] == "invalid status"
    assert reasons["C1007"] == "invalid date"
