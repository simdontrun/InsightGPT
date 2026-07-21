from root_cause.root_cause_detailed_engine import (
    get_loss_product_details
)

from root_cause.evidence_explainer import (
    explain_evidence
)


results = get_loss_product_details()

print("\n📊 ROOT CAUSE EVIDENCE\n")

for row in results:
    print(row)

print("\n🤖 EXECUTIVE ANALYSIS\n")

analysis = explain_evidence(results)

print(analysis)