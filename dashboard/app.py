import streamlit as st
import pandas as pd
import plotly.express as px

from analytics.kpi_service import get_kpis
from analytics.region_service import get_region_data
from analytics.category_service import get_category_data
from analytics.product_service import get_product_data


# Page Title
st.set_page_config(
    page_title="InsightGPT",
    page_icon="📊",
    layout="wide"
)


# Dashboard Header
st.title("📊 InsightGPT")
st.subheader("AI-Powered Decision Intelligence Platform")


# Fetch KPI Data
kpis = get_kpis()

if not kpis:
    st.error("Database connection failed")
    st.stop()


# Create 3 KPI Columns
col1, col2, col3 = st.columns(3)


# Revenue KPI
with col1:
    st.metric(
        label="Total Revenue",
        value=f"${kpis['revenue']:,.2f}"
    )


# Profit KPI
with col2:
    st.metric(
        label="Total Profit",
        value=f"${kpis['profit']:,.2f}"
    )


# Margin KPI
with col3:
    st.metric(
        label="Profit Margin",
        value=f"{kpis['margin']:.2f}%"
    )

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