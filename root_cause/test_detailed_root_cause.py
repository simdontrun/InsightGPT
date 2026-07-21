from root_cause.root_cause_detailed_engine import (
    get_loss_product_details
)


results = get_loss_product_details()

print("\n📊 DETAILED LOSS ANALYSIS\n")

for row in results:
    print(row)