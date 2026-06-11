from analytics.kpi_service import (
    get_kpis
)

from root_cause.root_cause_service import (
    get_root_cause_analysis
)

from recommendations.recommendation_service import (
    get_recommendations
)


def generate_executive_report():

    kpis = get_kpis()

    loss_products, analysis = (
        get_root_cause_analysis()
    )

    recommendations = (
        get_recommendations()
    )

    report = f"""
==================================================
INSIGHTGPT EXECUTIVE BUSINESS REPORT
==================================================

EXECUTIVE SUMMARY

Total Revenue:
{kpis['revenue']:,.2f}

Total Profit:
{kpis['profit']:,.2f}

Profit Margin:
{kpis['margin']:.2f}%


==================================================
ROOT CAUSE ANALYSIS
==================================================

{analysis}


==================================================
AI RECOMMENDATIONS
==================================================

{recommendations}

==================================================
END OF REPORT
==================================================
"""

    return report