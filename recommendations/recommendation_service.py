from root_cause.root_cause_detailed_engine import (
    get_loss_product_details
)

from recommendations.recommendation_engine import (
    generate_recommendations
)


def get_recommendations():

    results = get_loss_product_details()

    if not results:
        return None

    recommendations = generate_recommendations(
        results
    )

    return recommendations