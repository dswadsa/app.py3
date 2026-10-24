# Superstore Sales Dashboard (Streamlit)
**Team**: Retail Analytics
**Dataset**: Tableau Superstore (US retail), `supermarket.csv` (9,800 rows, 2015–2018)

## Step 1 — Dataset & Decision-Maker
- **Dataset**: Superstore US retail transaction data, Jan 2015 – Dec 2018.
- **Each row**: one order line (product purchased in an order).
- **Key fields**: `Order Date`, `Region` (West/East/Central/South), `Segment`
  (Consumer/Corporate/Home Office), `Category` (Furniture/Office Supplies/Technology),
  `Sub-Category`, `Sales`.
- **Decision-maker**: **Regional Sales Manager** — each manager is accountable for
  one Region's sales performance.
- **Purpose**: set monthly sales targets, plan promotions and adjust product mix for
  their region.

## Step 2 — Why a Dashboard
1. **Who looks, how often**: The Regional Sales Manager opens the dashboard each month,
   before setting the next month's sales target.
2. **Decision sentence**: *If the manager sees a region's monthly sales falling and a
   product category's share shrinking, they will launch a category promotion and re-allocate
   marketing spend to that category.*
3. **What they do today without it**: manually merge ERP/CRM exports and build a monthly
   report in Excel — a 2–3 hour manual task each month, causing slow reaction to declining
   sales and missed promotion windows.
4. **Why dashboard, not email / static report / alert**: the manager must explore by
   region and by category every month. Static reports cannot filter by region; alerts only
   fire on emergencies. The dashboard supports repeated exploratory planning.

## Step 3 — What Matters
### ✅ Shown (at most 3 headline metrics)
- **Total Sales** (region revenue)
- **Number of Orders**
- **Average Order Value**

### ✅ Supporting charts
- **Monthly Sales Trend** (line) — shows whether sales are rising/falling and the seasonality
  (high in Sep & Nov–Dec, low in Jan–Feb).
- **Sales by Category** (bar) — which product lines drive revenue.
- **Sales by Sub-Category** (bar) — deeper product-mix detail for promotion planning.

### ✅ Filter
- **Region selector** — the manager handles one region at a time.

### ❌ Deliberately cut
1. **City / State level detail**: too granular for a monthly regional target decision; adds
   clutter without changing the plan.
2. **Exact product names / SKU rows**: order-line detail is irrelevant to the monthly
   category-level planning shown here.

### ⚠️ What can mislead & mitigation
- The dataset is a **static 4-year snapshot**; seasonal patterns should not be extrapolated
  beyond 2015–2018.
- Mitigation: a warning caption is embedded at the bottom of the dashboard.

## Step 4 — Refresh Frequency
- The sales table refreshes **monthly** from the ERP/CRM system.
- The manager reviews **monthly** when setting the next month's target.
- **Trigger**: if a category's monthly sales drop **>20% vs the prior month**, the manager
  investigates and launches a targeted promotion.
- **Cost of stale data**: 1-month-old numbers lead to wrong targets — under-investing in
  rising categories and over-investing in declining ones.

## Step 5 — App & Deployment
- **File**: `app.py`
- **Dependencies**: `requirements.txt`
- **Deploy**: Streamlit Community Cloud (set Python 3.14 in Advanced Settings)
- **Run locally**: `uv init` → add files → `streamlit run app.py`
