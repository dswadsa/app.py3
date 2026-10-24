import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------------
# 1. Title with team name
# ---------------------------------------------------------------
st.set_page_config(page_title="Superstore Sales Dashboard", layout="wide")

st.title("📊 Superstore Sales Dashboard | Team Retail Analytics")

# 2. One-line caption: who uses it + what decision it supports
st.caption(
    "Interactive dashboard for the Regional Sales Manager to plan monthly "
    "sales targets, promotions and product mix for their region."
)

# ---------------------------------------------------------------
# Load & clean the real data
# ---------------------------------------------------------------
df = pd.read_csv("supermarket.csv")
df.columns = df.columns.str.strip()                      # strip hidden spaces in column names
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)   # dd/mm/yyyy format
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df = df.dropna(subset=["Sales"])

# ---------------------------------------------------------------
# 5. Filters the decision-maker actually needs (Region only)
# ---------------------------------------------------------------
selected_region = st.selectbox(
    "Select your region",
    options=sorted(df["Region"].unique()),
)
region_df = df[df["Region"] == selected_region]

# ---------------------------------------------------------------
# 3. Headline metrics with st.metric (at most 3)
# ---------------------------------------------------------------
col1, col2, col3 = st.columns(3)

total_sales = region_df["Sales"].sum()
n_orders = region_df["Order ID"].nunique()
avg_order = total_sales / n_orders if n_orders else 0

with col1:
    st.metric("Total Sales", f"${total_sales:,.0f}")
with col2:
    st.metric("Number of Orders", f"{n_orders:,}")
with col3:
    st.metric("Avg Order Value", f"${avg_order:,.2f}")

# ---------------------------------------------------------------
# 4. Supporting charts
# ---------------------------------------------------------------
# Chart 1: Monthly sales trend (line)
st.subheader("Monthly Sales Trend")
monthly = (
    region_df.resample("MS", on="Order Date")["Sales"]
    .sum()
    .reset_index()
)
fig1 = px.line(
    monthly,
    x="Order Date",
    y="Sales",
    title=f"Monthly Sales — {selected_region}",
    markers=True,
)
fig1.update_layout(xaxis_title="Month", yaxis_title="Sales ($)")
st.plotly_chart(fig1, width="stretch")

# Chart 2: Sales by product category (bar)
st.subheader("Sales by Product Category")
cat_sales = region_df.groupby("Category")["Sales"].sum().reset_index().sort_values("Sales", ascending=True)
fig2 = px.bar(
    cat_sales,
    x="Sales",
    y="Category",
    orientation="h",
    title=f"Sales by Category — {selected_region}",
)
fig2.update_layout(xaxis_title="Sales ($)", yaxis_title="")
st.plotly_chart(fig2, width="stretch")

# Chart 3 (supporting): Sales by sub-category (horizontal bar)
st.subheader("Sales by Sub-Category")
sub_sales = region_df.groupby("Sub-Category")["Sales"].sum().reset_index().sort_values("Sales", ascending=True)
fig3 = px.bar(
    sub_sales,
    x="Sales",
    y="Sub-Category",
    orientation="h",
    title=f"Sales by Sub-Category — {selected_region}",
)
fig3.update_layout(xaxis_title="Sales ($)", yaxis_title="")
st.plotly_chart(fig3, width="stretch")

# ---------------------------------------------------------------
# 6. Data period + refresh frequency (Step 4)
# ---------------------------------------------------------------
st.divider()
st.markdown(
    """
**Data Period**: Jan 2015 – Dec 2018 (Tableau Superstore dataset, 9,800 rows).

**Refresh frequency plan**: The sales table refreshes **monthly** from the ERP/CRM
system. The Regional Sales Manager reviews this dashboard every month when setting
the coming month's sales target. Real-time refresh would add cost without changing
any monthly decision.

> ⚠️ **Warning**: This dataset is a static 4-year snapshot. Seasonal patterns
> (high in Sep & Nov–Dec, low in Jan–Feb) are visible but should not be extrapolated
> beyond the period shown.
"""
)
#（注：内容由AI生成）
