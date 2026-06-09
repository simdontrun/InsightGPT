from root_cause.root_cause_detailed_engine import (
    get_loss_product_details
)

from recommendations.recommendation_engine import (
    generate_recommendations
)


results = get_loss_product_details()

print("\n📊 BUSINESS EVIDENCE\n")

for row in results:
    print(row)

print("\n💡 RECOMMENDATIONS\n")

recommendations = generate_recommendations(
    results
)

print(recommendations)