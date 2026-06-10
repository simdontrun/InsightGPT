import streamlit as st
import pandas as pd
import plotly.express as px

from dashboard.theme_loader import (
    load_css
)

from analytics.kpi_service import get_kpis
from analytics.region_service import get_region_data
from analytics.category_service import get_category_data
from analytics.product_service import get_product_data

from nl_sql.gemini_sql_generator import generate_sql
from nl_sql.sql_validator import validate_sql
from nl_sql.sql_executor import execute_query
from nl_sql.explanation_generator import generate_explanation

from root_cause.root_cause_service import (
    get_root_cause_analysis
)

from recommendations.recommendation_service import (
    get_recommendations
)

st.set_page_config(
    page_title="InsightGPT",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# APP STATE
# -----------------------------

if "page" not in st.session_state:
    st.session_state.page = "landing"

if "theme" not in st.session_state:
    st.session_state.theme = "light"

st.markdown(
    load_css(
        st.session_state.theme
    ),
    unsafe_allow_html=True
)

# -----------------------------
# THEME PICKER
# -----------------------------

if "theme" not in st.session_state:
    st.session_state.theme = "light"

dark_mode = st.toggle(
    "🌙 Dark Mode",
    key="dark_toggle",
    value=(st.session_state.theme == "dark")
)

st.session_state.theme = (
    "dark"
    if dark_mode
    else "light"
)

st.divider()

# ----------------------------------
# SIDEBAR
# ----------------------------------

with st.sidebar:

    st.title("📊 InsightGPT")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "AI Analytics",
            "Root Cause",
            "Recommendations"
        ]
    )

    st.markdown("---")

    dark_mode = st.toggle(
        "🌙 Dark Mode",
        value=(st.session_state.theme == "dark")
    )

    st.session_state.theme = (
        "dark"
        if dark_mode
        else "light"
    )


# ----------------------------------
# HEADER
# ----------------------------------

st.title("📊 InsightGPT")
st.caption(
    "AI-Powered Decision Intelligence Platform"
)


# ----------------------------------
# KPI SECTION
# ----------------------------------

kpis = get_kpis()

if not kpis:
    st.error("Database connection failed")
    st.stop()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Revenue",
        value=f"${kpis['revenue']:,.2f}"
    )

with col2:
    st.metric(
        label="Total Profit",
        value=f"${kpis['profit']:,.2f}"
    )

with col3:
    st.metric(
        label="Profit Margin",
        value=f"{kpis['margin']:.2f}%"
    )


# ----------------------------------
# REGION CHART
# ----------------------------------

st.divider()

st.subheader("🌍 Regional Revenue Analysis")

region_data = get_region_data()

region_df = pd.DataFrame(region_data)

fig = px.bar(
    region_df,
    x="Region",
    y="Revenue",
    title="Revenue by Region"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ----------------------------------
# CATEGORY CHART
# ----------------------------------

st.divider()

st.subheader("📦 Category Revenue Analysis")

category_data = get_category_data()

category_df = pd.DataFrame(category_data)

fig = px.bar(
    category_df,
    x="Category",
    y="Revenue",
    title="Revenue by Category"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ----------------------------------
# PRODUCT CHART
# ----------------------------------

st.divider()

st.subheader("🏆 Top Product Performance")

product_data = get_product_data()

product_df = pd.DataFrame(product_data)

fig = px.bar(
    product_df,
    x="Product",
    y="Revenue",
    title="Top Products by Revenue"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ----------------------------------
# AI ANALYTICS SECTION
# ----------------------------------

st.divider()

st.subheader("🤖 Ask InsightGPT")

question = st.text_input(
    "Ask a business question"
)

if st.button("Analyze"):

    if not question:
        st.warning("Please enter a question.")
        st.stop()

    # Generate SQL
    sql_query = generate_sql(question)

    if not sql_query:
        st.error(
            "Gemini quota exceeded or service temporarily unavailable. Please try again later."
        )
        st.stop()

    st.write("### Generated SQL")

    st.code(sql_query)

    # Validate SQL
    if not validate_sql(sql_query):
        st.error("SQL validation failed")
        st.stop()

    # Execute SQL
    results = execute_query(sql_query)

    if results is None:
        st.error("Database query failed")
        st.stop()

    # Display Results
    st.write("### Results")

    if len(results) == 1:

        value = results[0][0]

        if isinstance(value, (int, float)):
            st.success(f"${value:,.2f}")
        else:
            st.success(str(value))

    else:
        st.write(results)

    # AI Explanation
    st.write("### 🤖 AI Business Interpretation")

    try:

        explanation = generate_explanation(
            question,
            results
        )

        if explanation:
            st.info(explanation)
        else:
            st.warning("Explanation unavailable.")

    except Exception:
        st.warning(
            "Explanation unavailable (Gemini quota exceeded or service unavailable)."
        )

st.divider()

st.subheader("🚨 Root Cause Analysis")

loss_products, analysis = get_root_cause_analysis()
st.write("Analysis Debug:")
st.write(analysis)

if loss_products:

    root_df = pd.DataFrame(
        loss_products,
        columns=[
            "Product",
            "Revenue",
            "Profit",
            "Avg Discount",
            "Quantity"
        ]
    )

    st.dataframe(
        root_df,
        use_container_width=True
    )

    st.write("### Executive Analysis")

    if analysis:
        st.info(analysis)

else:
    st.warning(
        "Root cause analysis unavailable."
    )

st.divider()

st.subheader("💡 AI Recommendations")

recommendations = get_recommendations()
st.write("Recommendations Debug:")
st.write(recommendations)

if recommendations:

    st.success(recommendations)

else:

    st.warning(
        "Recommendations unavailable."
    )
