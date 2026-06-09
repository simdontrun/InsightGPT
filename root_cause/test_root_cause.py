from root_cause.root_cause_engine import (
    get_loss_making_products
)


results = get_loss_making_products()

print("\n🚨 LOSS-MAKING PRODUCTS\n")

for row in results:
    print(row)