# 🛒 Superstore Management System — EDA & Dashboard

> **From raw data to business intelligence** — a complete end-to-end data analysis project covering synthetic data generation, exploratory analysis, and interactive Power BI dashboards.

---

## 📖 The Story

Every business generates data. But raw data alone means nothing — it needs to be *asked the right questions*.

This project simulates a real-world retail analytics workflow. Starting from scratch (no pre-built Kaggle dataset), I **created my own synthetic business dataset** of 1000+ records, then applied structured EDA techniques to extract actionable insights across sales, customers, inventory, and delivery performance.

The result: three fully interactive Power BI dashboards that allow business stakeholders to explore KPIs without ever touching the raw data.

---

## 🗂️ Project Structure

```
superstore-eda/
│
├── data/
│   └── Superstore_Management_System.csv     # Synthetic dataset (1000+ rows, 25 cols)
│
├── notebooks/
│   └── superstore_analysis.py               # Full EDA pipeline
│
├── dashboards/
│   ├── superstore_performance_dashboard.png  # Sales & KPI dashboard
│   ├── inventory_supplier_dashboard.png      # Inventory & reorder dashboard
│   └── customer_delivery_dashboard.png       # Customer & delivery insights
│
├── outputs/
│   └── eda_analysis_summary.csv             # Exported key metrics
│
└── README.md
```

---

## Phase 1 — Data Generation 🏗️

**Goal:** Build a realistic retail dataset from scratch.

Instead of downloading an existing dataset, I used `Faker`, `NumPy`, and `Pandas` to generate 1000 synthetic orders with realistic distributions across:

| Column Group | Fields |
|---|---|
| Order Info | Order ID, Order Date, Ship Date |
| Customer | Customer ID, Name, Segment (Home Office / Consumer / Corporate) |
| Product | Product ID, Name, Category, Unit Price, Cost Price |
| Transaction | Sales Amount, Quantity, Discount (%), Profit |
| Fulfillment | Region, Payment Mode, Delivery Status |
| Inventory | Stock Left, Reorder Quantity, Auto Reorder flag |

**Key design decision:** Inventory logic was built in — if `Stock Left < threshold`, the `Auto Reorder` flag activates and a `Reorder Quantity` is suggested automatically. This mirrors real supply chain systems.

---

## Phase 2 — Data Preparation 🧹

```python
# No missing values, no duplicates — clean dataset confirmed
df.isnull().sum()      # → Series([], dtype: int64)
df.duplicated().sum()  # → 0

# Date conversion
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')
df['Ship Date']  = pd.to_datetime(df['Ship Date'],  format='%d-%m-%Y')

# Feature engineering
df['Order Month'] = df['Order Date'].dt.to_period('M')
df['Order Year']  = df['Order Date'].dt.year
```

---

## Phase 3 — Exploratory Data Analysis 🔍

### Univariate Analysis
Examined distribution of all categorical and numerical variables individually.

- **Customer Segments:** Home Office (354) > Consumer (347) > Corporate (299)
- **Payment Modes:** UPI, Net Banking, Credit Card, Cash — nearly equal distribution (~25% each)
- **Delivery Status:** Returned, Cancelled, Delivered, Pending — roughly balanced (by design)
- **Numerical variables:** Profit, Sales Amount, Discount % analyzed via histograms + boxplots

### Bivariate Analysis
Compared variables against each other to surface performance differences.

| Dimension | Top Performer |
|---|---|
| Sales by Category | Electronics ($3.3M) |
| Profit by Category | Grocery ($0.85M) |
| Sales by Region | West (27.2%) |
| Profit by Region | North ($0.87M) |

### Time Series Analysis
Monthly trend analysis revealed:
- **Peak months:** July ($1.26M), January ($1.13M)
- **Trough months:** April ($0.79M), September ($0.94M)
- Seasonal pattern: mid-year dip followed by Q3 recovery

### Correlation Analysis

```
High positive correlations found:
  Sales Amount  ↔  Cost Price   (expected — cost drives price)
  Sales Amount  ↔  Profit       (higher sales = higher absolute profit)

Low correlation:
  Discount (%) ↔  Profit       (discount strategy not hurting profit significantly)
```

---

## Phase 4 — Power BI Dashboards 📊

### Dashboard 1: Superstore Performance Dashboard
**Focus:** Sales, profit, and product/regional KPIs

- Total Sales: **$12.74M** | Total Profit: **$3.19M** | Avg Discount: **10.20%**
- Top product by sales: **Stapler ($0.80M)**
- Sales by region: West leads at 27.2%, followed by East (26.3%)
- Monthly trend line showing full-year seasonality
- Filters: Region slicer for drill-down

### Dashboard 2: Inventory & Supplier Dashboard
**Focus:** Stock health and reorder management

- Total Stock Left: **25K units** | Low Stock Items: **194** | Avg Reorder: **6.96**
- 80.6% of items do NOT need reorder — inventory is healthy overall
- 19.4% (194 items) flagged for auto-reorder
- Stock distribution: Furniture holds the most stock, Office Supplies the least
- Reorder trend peaks in December — signals seasonal demand surge

### Dashboard 3: Customer & Delivery Insights
**Focus:** Customer behavior and fulfillment performance

- 989 unique customers
- Most common payment: **UPI**
- Average items per order: **5.46**
- Profit by segment: Corporate (35.54%) > Home Office (34.09%) > Consumer (30.37%)
- Profit by region: North ($0.87M) leads
- Sales split near-equal across all 4 delivery statuses (~$3M each)

---

## 🔑 Key Insights

1. **Electronics drives volume; Grocery drives margin** — Electronics has highest sales ($3.3M) but Grocery has the best profit margin.
2. **North region is most profitable** despite West having highest sales share — margin efficiency matters more than volume.
3. **Home Office segment is the largest** by order count but Corporate yields the highest profit contribution per order.
4. **UPI dominates payment methods** — digital payment preference is strong.
5. **19.4% inventory is at reorder threshold** — auto-reorder logic successfully catches low-stock items before stockout.
6. **Discount rate has weak correlation with profit** — the 10.2% average discount is not significantly eroding margins.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Data generation, EDA, analysis |
| Pandas | Data wrangling |
| NumPy | Numerical operations |
| Matplotlib / Seaborn | Visualization |
| Faker | Synthetic data generation |
| Power BI | Interactive dashboard |

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/superstore-eda.git
cd superstore-eda

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn faker

# 3. Run the analysis
python notebooks/superstore_analysis.py

# Output: eda_analysis_summary.csv saved to working directory
```

---

## 📌 What I Learned

- How to **design a synthetic dataset** with realistic business logic (inventory thresholds, segment distributions)
- Structuring a complete **EDA pipeline** from quality check → univariate → bivariate → time series → correlation
- Building **multi-page Power BI dashboards** with cross-filtering slicers
- The difference between **revenue leaders** (Electronics) and **margin leaders** (Grocery) — a core business intelligence concept
- How **inventory auto-reorder logic** can be embedded directly in data design

---

## 👤 Author

**Sohel Rahmn** — Data Analyst & Python Developer
> Connect on [LinkedIn](https://www.linkedin.com/in/sohel-rahman-a02b7429b/) | [GitHub](https://github.com/sohelrahman2)

---


