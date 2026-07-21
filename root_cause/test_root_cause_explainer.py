from root_cause.root_cause_engine import (
    get_loss_making_products
)

from root_cause.root_cause_explainer import (
    explain_loss_products
)


results = get_loss_making_products()

print("\n🚨 LOSS MAKING PRODUCTS\n")

for row in results:
    print(row)

print("\n🤖 ROOT CAUSE ANALYSIS\n")

analysis = explain_loss_products(
    results
)

print(analysis)