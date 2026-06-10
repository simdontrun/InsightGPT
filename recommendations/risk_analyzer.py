def analyze_risk(results):

    if not results:
        return None

    highest_loss_product = min(
        results,
        key=lambda x: x[2]
    )

    highest_discount_product = max(
        results,
        key=lambda x: x[3]
    )

    risk_summary = {
        "highest_loss_product":
            highest_loss_product[0],

        "highest_loss":
            highest_loss_product[2],

        "highest_discount_product":
            highest_discount_product[0],

        "highest_discount":
            highest_discount_product[3]
    }

    return risk_summary