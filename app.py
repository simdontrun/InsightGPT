import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import tempfile, os

from dashboard.theme_loader import load_css

# --------------------------------------------------
# PAGE CONFIG  (must be first Streamlit call)
# --------------------------------------------------
st.set_page_config(
    page_title="InsightGPT",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# --------------------------------------------------
# HANDLE NAV CLICKS via query params
# nav links carry both ?nav=PageName&theme=dark so
# theme survives the full-page reload that anchors cause
# --------------------------------------------------
params = st.query_params
if "nav" in params or "theme" in params:
    valid_pages = ["Dashboard", "AI Analytics", "Root Cause",
                   "Recommendations", "Forecast", "Documents"]
    # Restore theme first so it's set before anything renders
    if "theme" in params and params["theme"] in ("light", "dark"):
        st.session_state.theme = params["theme"]
    # Then restore page
    if "nav" in params and params["nav"] in valid_pages:
        st.session_state.page = params["nav"]
    st.query_params.clear()
    st.rerun()

# --------------------------------------------------
# CSS INJECTION (theme + global overrides)
# --------------------------------------------------
st.markdown(load_css(st.session_state.theme), unsafe_allow_html=True)

dark = st.session_state.theme == "dark"

# Sidebar background, text, accent colours
SB_BG       = "#10121A" if dark else "#EDEAE1"
LOGO_BG     = "#C8F169" if dark else "#1A1814"
LOGO_FG     = "#111"    if dark else "#F5F0E8"
LOGO_TXT    = "#EEF0F5" if dark else "#1A1814"
SUB_TXT     = "#8B90A8" if dark else "#7A7060"
DEFAULT_FG  = "#8B90A8" if dark else "#4A4540"
ACTIVE_BG   = "rgba(200,241,105,0.14)" if dark else "#1A1814"
ACTIVE_FG   = "#C8F169" if dark else "#F5F0E8"
HOVER_BG    = "rgba(255,255,255,0.07)"  if dark else "rgba(26,24,20,0.08)"
HOVER_FG    = "#EEF0F5" if dark else "#1A1814"
DIVIDER     = "#262C3E" if dark else "#E2D9C8"

st.markdown(f"""
<!-- Tabler Icons CDN (pinned version) -->
<link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.11.0/dist/tabler-icons.min.css">

<style>
/* ---- Global font ---- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] {{ font-family: 'Inter', sans-serif !important; }}

/* ---- Sidebar shell ---- */
[data-testid="stSidebar"] > div:first-child {{
    background: {SB_BG} !important;
    padding: 1.2rem 0.85rem 1rem !important;
}}

/* ---- Nav anchor reset ---- */
.ig-nav a {{
    text-decoration: none !important;
    display: block;
    margin-bottom: 3px;
    color: inherit !important;
}}

/* ---- Nav item pill ---- */
.ig-nav-item {{
    display: flex;
    align-items: center;
    gap: 11px;
    padding: 8px 11px;
    border-radius: 10px;
    cursor: pointer;
    font-size: 13.5px;
    font-weight: 500;
    color: {DEFAULT_FG} !important;
    transition: background 0.15s, color 0.15s;
    line-height: 1;
}}
.ig-nav-item * {{
    color: inherit !important;
}}
.ig-nav-item:hover {{
    background: {HOVER_BG} !important;
    color: {HOVER_FG} !important;
}}
.ig-nav-item:hover * {{
    color: {HOVER_FG} !important;
}}

/* ---- Active pill ---- */
.ig-nav-item.active {{
    background: {ACTIVE_BG} !important;
    color: {ACTIVE_FG} !important;
}}
.ig-nav-item.active * {{
    color: {ACTIVE_FG} !important;
}}

/* ---- Icon sizing ---- */
.ig-nav-item .ig-icon {{
    font-size: 17px;
    width: 22px;
    text-align: center;
    flex-shrink: 0;
    opacity: 0.65;
}}
.ig-nav-item.active .ig-icon {{
    opacity: 1;
}}
.ig-nav-item:hover .ig-icon {{
    opacity: 0.9;
}}

/* ---- Theme toggle button ---- */
.ig-theme-wrap {{
    margin-top: 18px;
    padding-top: 14px;
    border-top: 1px solid {DIVIDER};
}}
[data-testid="stSidebar"] .stButton > button {{
    width: 100% !important;
    background: transparent !important;
    border: 1px solid {DIVIDER} !important;
    color: {DEFAULT_FG} !important;
    border-radius: 9px !important;
    font-size: 12.5px !important;
    font-weight: 500 !important;
    padding: 7px 12px !important;
    box-shadow: none !important;
    transition: background 0.15s !important;
    font-family: 'Inter', sans-serif !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    justify-content: center !important;
}}
[data-testid="stSidebar"] .stButton > button p,
[data-testid="stSidebar"] .stButton > button span {{
    color: {DEFAULT_FG} !important;
}}
[data-testid="stSidebar"] .stButton > button:hover {{
    background: {HOVER_BG} !important;
    color: {HOVER_FG} !important;
    transform: none !important;
}}
[data-testid="stSidebar"] .stButton > button:hover p,
[data-testid="stSidebar"] .stButton > button:hover span {{
    color: {HOVER_FG} !important;
}}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PLOTLY HELPERS
# --------------------------------------------------
CHART_COLORS_LIGHT = ["#1A1814", "#6B5E4E", "#A0927E", "#D4C5B0", "#EDE8DC"]
CHART_COLORS_DARK  = ["#C8F169", "#8AB8FF", "#FF9F6B", "#C084FC", "#34D399"]

def plotly_layout():
    is_dark = st.session_state.theme == "dark"
    text_color  = "#EEF0F5" if is_dark else "#1A1814"
    muted_color = "#9BA3BC" if is_dark else "#7A7060"
    grid_color  = "#262C3E" if is_dark else "#E2D9C8"
    bg_color    = "#161923" if is_dark else "#F5F0E8"

    axis_common = dict(
        gridcolor=grid_color,
        showgrid=False,
        zeroline=False,
        tickfont=dict(color=text_color, size=11),
        title_font=dict(color=muted_color, size=11),
        linecolor=grid_color,
    )

    return dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor=bg_color,
        font=dict(
            color=text_color,
            family="Inter, sans-serif",
            size=12,
        ),
        title_font=dict(size=14, color=text_color),
        margin=dict(l=0, r=0, t=40, b=0),
        xaxis=axis_common,
        yaxis=axis_common,
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color=text_color, size=11),
        ),
        coloraxis_colorbar=dict(
            tickfont=dict(color=text_color),
            title_font=dict(color=text_color),
        ),
    )

def bar_colors():
    return CHART_COLORS_DARK if st.session_state.theme == "dark" else CHART_COLORS_LIGHT

def make_bar(df, x, y, title, color_col=None):
    colors = bar_colors()
    fig = px.bar(
        df, x=x, y=y, title=title,
        color=color_col if color_col else x,
        color_discrete_sequence=colors,
    )
    fig.update_layout(**plotly_layout())
    fig.update_traces(marker_line_width=0)
    return fig

def make_line_forecast(df):
    is_dark = st.session_state.theme == "dark"
    line_col = "#C8F169" if is_dark else "#1A1814"
    band_col  = "rgba(200,241,105,0.15)" if is_dark else "rgba(26,24,20,0.08)"

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["ds"], y=df["yhat_upper"],
        mode="lines", line=dict(width=0),
        showlegend=False, name="Upper bound",
    ))
    fig.add_trace(go.Scatter(
        x=df["ds"], y=df["yhat_lower"],
        mode="lines", line=dict(width=0),
        fill="tonexty", fillcolor=band_col,
        showlegend=False, name="Lower bound",
    ))
    fig.add_trace(go.Scatter(
        x=df["ds"], y=df["yhat"],
        mode="lines", name="Forecast",
        line=dict(color=line_col, width=2.5),
    ))
    fig.update_layout(title="30-Day Sales Forecast", **plotly_layout())
    return fig

# --------------------------------------------------
# NAV DEFINITION
# icon names from tabler-icons.io
# --------------------------------------------------
NAV_ITEMS = [
    ("Dashboard",       "ti-layout-dashboard"),
    ("AI Analytics",    "ti-message-chatbot"),
    ("Root Cause",      "ti-zoom-exclamation"),
    ("Recommendations", "ti-bulb"),
    ("Forecast",        "ti-chart-line"),
    ("Documents",       "ti-file-description"),
]

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    current = st.session_state.page

    # ---- Logo block ----
    theme_class = "theme-dark" if dark else "theme-light"
    st.markdown(f"""
    <div class="sidebar-logo">
      <div class="sidebar-logo-icon {theme_class}">
        <i class="ti ti-chart-dots-3"></i>
      </div>
      <div>
        <div class="sidebar-logo-text {theme_class}">InsightGPT</div>
        <div class="sidebar-logo-sub" style="color:{SUB_TXT};">Analytics Platform</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ---- Section label ----
    st.markdown(f"""
    <div style="font-size:10px;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;
                color:{SUB_TXT};padding:0 4px;margin-bottom:8px;">Navigation</div>
    """, unsafe_allow_html=True)

    # ---- Nav items (HTML anchors carrying both nav target and current theme) ----
    nav_html = '<div class="ig-nav">'
    for label, icon in NAV_ITEMS:
        active_class = " active" if label == current else ""
        nav_key = label.replace(" ", "+")
        theme_val = "dark" if dark else "light"
        nav_html += f"""
        <a href="?nav={nav_key}&theme={theme_val}" target="_self">
          <div class="ig-nav-item{active_class}">
            <i class="ti {icon} ig-icon"></i>
            <span>{label}</span>
          </div>
        </a>"""
    nav_html += "</div>"
    st.markdown(nav_html, unsafe_allow_html=True)

    # ---- Divider + theme toggle ----
    st.markdown(f'<div class="ig-theme-wrap"></div>', unsafe_allow_html=True)
    theme_icon = "🌙" if not dark else "☀️"
    theme_label = f"{theme_icon}  Switch to {'Dark' if not dark else 'Light'} Mode"
    if st.button(theme_label, key="theme_toggle"):
        st.session_state.theme = "dark" if not dark else "light"
        st.rerun()

# --------------------------------------------------
# CURRENT PAGE
# --------------------------------------------------
page = st.session_state.page

# --------------------------------------------------
# PAGE HEADER HELPER
# --------------------------------------------------
def page_header(title, subtitle):
    st.markdown(f"# {title}")
    st.caption(subtitle)
    st.divider()

# --------------------------------------------------
# PAGE: DASHBOARD
# --------------------------------------------------
if page == "Dashboard":
    page_header("Dashboard", "Live business performance at a glance")

    from analytics.kpi_service import get_kpis
    from analytics.region_service import get_region_data
    from analytics.category_service import get_category_data
    from analytics.product_service import get_product_data

    with st.spinner("Loading data…"):
        kpis = get_kpis()

    if not kpis:
        st.error("Database connection failed. Run `streamlit run app.py` from the project root.")
        st.stop()

    k1, k2, k3 = st.columns(3)
    k1.metric("Total Revenue",  f"${kpis['revenue']:,.0f}")
    k2.metric("Total Profit",   f"${kpis['profit']:,.0f}")
    k3.metric("Profit Margin",  f"{kpis['margin']:.1f}%")

    st.markdown("#### Regional & Category Breakdown")
    left, right = st.columns(2)

    with left:
        region_df = pd.DataFrame(get_region_data())
        if not region_df.empty:
            st.plotly_chart(make_bar(region_df, "Region", "Revenue", "Revenue by Region"),
                            use_container_width=True)
        else:
            st.info("No region data available.")

    with right:
        cat_df = pd.DataFrame(get_category_data())
        if not cat_df.empty:
            st.plotly_chart(make_bar(cat_df, "Category", "Revenue", "Revenue by Category"),
                            use_container_width=True)
        else:
            st.info("No category data available.")

    st.markdown("#### Top Products")
    prod_df = pd.DataFrame(get_product_data())
    if not prod_df.empty:
        st.plotly_chart(make_bar(prod_df, "Product", "Revenue", "Top Products by Revenue"),
                        use_container_width=True)
    else:
        st.info("No product data available.")

# --------------------------------------------------
# PAGE: AI ANALYTICS
# --------------------------------------------------
elif page == "AI Analytics":
    page_header("AI Analytics",
                "Ask business questions in plain English — get SQL, results, and a written explanation")

    from nl_sql.gemini_sql_generator import generate_sql
    from nl_sql.sql_validator import validate_sql
    from nl_sql.sql_executor import execute_query
    from nl_sql.explanation_generator import generate_explanation

    st.markdown("**Your question**")
    question = st.text_input(
        "question",
        placeholder="e.g. What is the total revenue for each region?",
        label_visibility="collapsed",
    )

    col_btn, _ = st.columns([1, 5])
    run = col_btn.button("Analyze →", use_container_width=True)

    if run:
        if not question.strip():
            st.warning("Please enter a question first.")
            st.stop()

        with st.spinner("Generating SQL…"):
            sql_query = generate_sql(question)

        if not sql_query:
            st.error("Could not generate SQL — Gemini quota may be exceeded. Try again shortly.")
            st.stop()

        with st.expander("Generated SQL", expanded=True):
            st.code(sql_query, language="sql")

        if not validate_sql(sql_query):
            st.error("SQL validation failed. The query may reference unknown tables or columns.")
            st.stop()

        with st.spinner("Running query…"):
            results = execute_query(sql_query)

        if results is None:
            st.error("Database query failed.")
            st.stop()

        st.markdown("**Results**")
        if len(results) == 1 and len(results[0]) == 1:
            value = results[0][0]
            st.success(f"**${value:,.2f}**" if isinstance(value, (int, float)) else str(value))
        else:
            results_df = pd.DataFrame(results)
            st.dataframe(results_df, use_container_width=True)

        st.markdown("**AI Interpretation**")
        with st.spinner("Generating explanation…"):
            try:
                explanation = generate_explanation(question, results)
                if explanation:
                    st.info(explanation)
                else:
                    st.warning("Explanation unavailable.")
            except Exception:
                st.warning("Explanation unavailable (Gemini quota exceeded).")

# --------------------------------------------------
# PAGE: ROOT CAUSE
# --------------------------------------------------
elif page == "Root Cause":
    page_header("Root Cause Analysis",
                "Identify loss-making products and the reasons behind them")

    from root_cause.root_cause_service import get_root_cause_analysis

    with st.spinner("Analysing loss-making products…"):
        loss_products, analysis = get_root_cause_analysis()

    if loss_products:
        root_df = pd.DataFrame(
            loss_products,
            columns=["Product", "Revenue", "Profit", "Avg Discount", "Quantity"],
        )
        st.markdown("**Loss-making products**")
        st.dataframe(root_df, use_container_width=True)

        if analysis:
            st.markdown("**Executive Analysis**")
            st.info(analysis)
    else:
        st.info("No loss-making products found.")

# --------------------------------------------------
# PAGE: RECOMMENDATIONS
# --------------------------------------------------
elif page == "Recommendations":
    page_header("AI Recommendations",
                "Strategic actions generated from your sales data")

    from recommendations.recommendation_service import get_recommendations

    with st.spinner("Generating recommendations…"):
        recommendations = get_recommendations()

    if recommendations:
        st.success(recommendations)
    else:
        st.warning("Recommendations unavailable — check your Gemini API key.")

# --------------------------------------------------
# PAGE: FORECAST
# --------------------------------------------------
elif page == "Forecast":
    page_header("Forecast Center", "30-day sales outlook with confidence intervals")

    from forecasting.forecast_engine import generate_forecast

    with st.spinner("Building forecast model…"):
        forecast_df = generate_forecast()

    if forecast_df is not None:
        st.plotly_chart(make_line_forecast(forecast_df), use_container_width=True)

        c1, c2 = st.columns(2)
        c1.metric("Forecast peak",  f"${forecast_df['yhat'].max():,.0f}")
        c2.metric("30-day avg",     f"${forecast_df['yhat'].tail(30).mean():,.0f}")

        with st.expander("Forecast data table"):
            display_df = forecast_df[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(30).copy()
            display_df.columns = ["Date", "Forecast", "Lower bound", "Upper bound"]
            display_df["Date"] = display_df["Date"].dt.strftime("%b %d, %Y")
            for col in ["Forecast", "Lower bound", "Upper bound"]:
                display_df[col] = display_df[col].map("${:,.0f}".format)
            st.dataframe(display_df, use_container_width=True)

        csv = forecast_df.to_csv(index=False).encode()
        st.download_button("📥  Download forecast CSV",
                           data=csv, file_name="forecast.csv", mime="text/csv")
    else:
        st.warning("Forecast unavailable. Ensure Prophet is installed and forecast CSV exists.")

# --------------------------------------------------
# PAGE: DOCUMENTS
# --------------------------------------------------
elif page == "Documents":
    page_header("Document Intelligence",
                "Upload a PDF report and ask questions about it")

    from rag.rag_engine import ask_document

    uploaded = st.file_uploader(
        "Upload a PDF report",
        type=["pdf"],
        help="Upload any business report. The system will read and index it so you can ask questions.",
    )

    if uploaded:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded.read())
            tmp_path = tmp.name
        st.session_state["rag_doc_path"] = tmp_path
        st.success(f"✅ **{uploaded.name}** uploaded and indexed.")

    doc_path = st.session_state.get(
        "rag_doc_path",
        "data/documents/InsightGPT_Quarterly_Report.pdf"
    )
    if "rag_doc_path" not in st.session_state:
        st.caption("Using the default quarterly report. Upload a PDF above to use your own.")

    st.markdown("**Ask a question about the document**")
    rag_question = st.text_input(
        "rag_q",
        placeholder="e.g. What were the key risks mentioned in the report?",
        label_visibility="collapsed",
    )

    col_btn2, _ = st.columns([1, 5])
    ask = col_btn2.button("Ask →", use_container_width=True)

    if ask:
        if not rag_question.strip():
            st.warning("Please enter a question first.")
        else:
            with st.spinner("Searching document…"):
                try:
                    answer = ask_document(rag_question)
                    st.info(answer)
                except Exception as e:
                    st.error(f"Document QA failed: {e}")

    st.divider()
    st.markdown("**Executive Report**")
    report_path = "reports/Executive_Report.pdf"
    if os.path.exists(report_path):
        with open(report_path, "rb") as pdf_file:
            st.download_button(
                "📥  Download Executive Report",
                data=pdf_file,
                file_name="Executive_Report.pdf",
                mime="application/pdf",
            )
    else:
        st.info("No executive report found at `reports/Executive_Report.pdf`.")
