from root_cause.root_cause_detailed_engine import (
    get_loss_product_details
)

from root_cause.evidence_explainer import (
    explain_evidence
)


def get_root_cause_analysis():

    results = get_loss_product_details()

    if not results:
        return None, None

    analysis = explain_evidence(results)

    return results, analysis