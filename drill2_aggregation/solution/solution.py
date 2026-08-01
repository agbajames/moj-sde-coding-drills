"""Model solution for Drill 2."""
import json
from collections import defaultdict
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "orders.json"


def load_orders(path=DATA_PATH):
    with open(path) as f:
        return json.load(f)


def aggregate_orders(orders):
    revenue_by_region = defaultdict(float)
    revenue_by_product = defaultdict(float)

    for order in orders:
        revenue_by_region[order["region"]] += order["revenue"]
        revenue_by_product[order["product"]] += order["revenue"]

    revenue_by_region = {k: round(v, 2) for k, v in revenue_by_region.items()}
    revenue_by_product = {k: round(v, 2) for k, v in revenue_by_product.items()}

    # Sort descending by revenue, tie-break alphabetically by product name.
    top_products = sorted(
        revenue_by_product.items(),
        key=lambda item: (-item[1], item[0]),
    )[:3]

    return {
        "revenue_by_region": revenue_by_region,
        "top_products": top_products,
    }


if __name__ == "__main__":
    print(aggregate_orders(load_orders()))
