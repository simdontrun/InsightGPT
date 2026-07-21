from root_cause.root_cause_detailed_engine import (
    get_loss_product_details
)

from recommendations.risk_analyzer import (
    analyze_risk
)


results = get_loss_product_details()

print(
    "\n📊 LOSS PRODUCT DATA\n"
)

for row in results:
    print(row)

risk_summary = analyze_risk(
    results
)

print(
    "\n🚨 RISK SUMMARY\n"
)

print(risk_summary)