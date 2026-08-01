from starter import aggregate_orders, load_orders


def test_revenue_by_region():
    result = aggregate_orders(load_orders())
    rbr = result["revenue_by_region"]
    assert rbr["London"] == 458.75   # 120.50 + 210.25 + 40.00 + 88.00
    assert rbr["Manchester"] == 226.25  # 75.00 + 95.75 + 55.50
    assert rbr["Leeds"] == 215.00    # 60.00 + 130.00 + 25.00


def test_top_products():
    result = aggregate_orders(load_orders())
    top = result["top_products"]
    assert len(top) == 3
    # Gizmo: 210.25+130.00+55.50=395.75, Widget: 120.50+60+95.75+88=364.25, Gadget: 75+40+25=140
    assert top[0] == ("Gizmo", 395.75)
    assert top[1] == ("Widget", 364.25)
    assert top[2] == ("Gadget", 140.00)
