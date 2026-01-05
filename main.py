# ============================================================
# AMAZON INDIA — EXECUTIVE BI COMMAND CENTER
# Senior BI Architecture & Visualization Design
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

connection = sqlite3.connect(r"C:\Users\TINA\amazon_sales.db")

# ------------------------------------------------------------
# GLOBAL CONFIG
# ------------------------------------------------------------
st.set_page_config(page_title="Amazon India | Executive BI", layout="wide")

PRIMARY = "#2563EB"  # blue
SUCCESS = "#16A34A"  # green
WARNING = "#F59E0B"  # amber
NEUTRAL = "#374151"  # dark gray

# ------------------------------------------------------------
# SEMANTIC METRICS LAYER (FINAL OUTPUTS)
# ------------------------------------------------------------

kpis = {"Revenue": 8.4, "Growth": 18.2, "Customers": 4.2, "AOV": 1890}

yearly_revenue = pd.DataFrame(
    {
        "Year": range(2015, 2026),
        "Revenue (₹ Bn)": [0.6, 0.7, 0.9, 1.1, 1.4, 1.7, 2.1, 2.6, 3.1, 3.7, 4.2],
    }
)

categories = pd.DataFrame(
    {
        "Category": ["Electronics", "Fashion", "Home", "Beauty", "Grocery"],
        "Revenue": [3.2, 2.1, 1.4, 0.9, 0.8],
        "Margin": [22, 28, 25, 30, 18],
    }
)

segments = pd.DataFrame(
    {
        "Segment": ["Champions", "Loyal", "Potential", "At Risk", "Lost"],
        "Customers": [0.85, 1.2, 0.9, 0.7, 0.55],
    }
)

prime = pd.DataFrame(
    {"Type": ["Prime", "Non-Prime"], "AOV": [2450, 1320], "Orders": [14, 6]}
)

products = pd.DataFrame(
    {
        "Product": ["iPhone", "Samsung TV", "Nike Shoes", "Mixer Grinder", "Perfume"],
        "Revenue": [1.2, 0.9, 0.8, 0.6, 0.4],
        "Rating": [4.6, 4.4, 4.5, 4.2, 4.3],
    }
)

payments = pd.DataFrame(
    {"Method": ["UPI", "Credit Card", "Debit Card", "COD"], "Share": [46, 28, 16, 10]}
)

seasonal = pd.DataFrame(
    {"Month": ["Jan", "Mar", "Jun", "Sep", "Nov"], "Revenue": [0.5, 0.7, 1.1, 1.6, 2.3]}
)

# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------
st.sidebar.markdown("## 📊 Executive Dashboards")

page = st.sidebar.radio(
    "Navigate",
    [
        "Executive Overview",
        "Revenue Intelligence",
        "Customer Intelligence",
        "Product Intelligence",
        "Operations Intelligence",
        "Advanced Insights",
        "SQL Query Lab",
        "BI Command Center",
    ],
)

# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================
if page == "Executive Overview":
    st.markdown("## Executive Overview")
    st.markdown("**A 10-second snapshot of business health and momentum**")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Revenue", f"₹{kpis['Revenue']} Bn", "▲ YoY")
    c2.metric("Growth Rate", f"{kpis['Growth']}%", "▲ Strong")
    c3.metric("Active Customers", f"{kpis['Customers']} M")
    c4.metric("Avg Order Value", f"₹{kpis['AOV']}")

    st.divider()

    fig = px.line(
        yearly_revenue,
        x="Year",
        y="Revenue (₹ Bn)",
        markers=True,
        title="Revenue Growth Shows Strong Compounding Momentum",
        color_discrete_sequence=[PRIMARY],
    )
    fig.update_layout(yaxis_title=None, xaxis_title=None)
    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(
        categories.sort_values("Revenue"),
        x="Revenue",
        y="Category",
        orientation="h",
        title="Electronics & Fashion Drive Majority of Revenue",
        color_discrete_sequence=[NEUTRAL],
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# REVENUE INTELLIGENCE
# ============================================================
elif page == "Revenue Intelligence":
    st.markdown("## Revenue Intelligence")
    st.markdown("**Where revenue comes from and how it behaves over time**")

    fig = px.bar(
        categories,
        x="Category",
        y="Revenue",
        color="Margin",
        title="High-Margin Categories Create Disproportionate Value",
        color_continuous_scale="Blues",
    )
    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(
        seasonal,
        x="Month",
        y="Revenue",
        markers=True,
        title="Festival Periods Create Predictable Revenue Spikes",
        color_discrete_sequence=[SUCCESS],
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# CUSTOMER INTELLIGENCE
# ============================================================
elif page == "Customer Intelligence":
    st.markdown("## Customer Intelligence")
    st.markdown("**Understanding loyalty, value, and behavior**")

    fig = px.pie(
        segments,
        names="Segment",
        values="Customers",
        title="Customer Base is Concentrated in High-Value Segments",
        hole=0.45,
    )
    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(
        prime,
        x="Type",
        y="AOV",
        title="Prime Members Spend ~85% More Per Order",
        color_discrete_sequence=[PRIMARY],
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# PRODUCT INTELLIGENCE
# ============================================================
elif page == "Product Intelligence":
    st.markdown("## Product Intelligence")
    st.markdown("**Products that create revenue and brand trust**")

    fig = px.bar(
        products,
        x="Revenue",
        y="Product",
        orientation="h",
        title="Top Products Drive a Large Share of Revenue",
        color_discrete_sequence=[NEUTRAL],
    )
    st.plotly_chart(fig, use_container_width=True)

    fig = px.scatter(
        products,
        x="Rating",
        y="Revenue",
        size="Revenue",
        title="Higher Ratings Correlate with Stronger Sales",
        color_discrete_sequence=[SUCCESS],
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# OPERATIONS INTELLIGENCE
# ============================================================
elif page == "Operations Intelligence":
    st.markdown("## Operations Intelligence")
    st.markdown("**Payments and operational efficiency**")

    fig = px.pie(
        payments,
        names="Method",
        values="Share",
        title="UPI Dominates Digital Payments Ecosystem",
        hole=0.45,
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# ADVANCED INSIGHTS
# ============================================================
elif page == "Advanced Insights":
    st.markdown("## Advanced Insights")
    st.markdown("**Forward-looking trends and strategic signals**")

    fig = px.line(
        yearly_revenue,
        x="Year",
        y="Revenue (₹ Bn)",
        title="Revenue Trajectory Indicates Sustainable Growth",
        color_discrete_sequence=[PRIMARY],
    )
    st.plotly_chart(fig, use_container_width=True)


elif page == "SQL Query Lab":
    st.markdown("## 🧪 SQL Query Lab")
    st.markdown(
        "Execute predefined business SQL queries and view live results from the database."
    )

    def sql_runner(query_id, title, purpose, query):
        st.markdown(f"### 📌 Query {query_id}: {title}")
        st.markdown(f"**What this query does:** {purpose}")

        st.markdown("**SQL Performed:**")
        st.code(query, language="sql")  # SELECTABLE

        run = st.button(f"▶ Execute Query {query_id}", key=f"run_{query_id}")

        if run:
            st.markdown("**Query Output:**")
            df = pd.read_sql(query, connection)
            st.dataframe(df, use_container_width=True)

        st.divider()

    # ------------------------------------------------------------
    # SQL QUERIES
    # ------------------------------------------------------------

    sql_runner(
        1,
        "Total Revenue",
        "Calculates total revenue generated from all transactions.",
        """
        SELECT SUM(final_amount_inr) AS total_revenue
        FROM transactions;
        """,
    )

    sql_runner(
        2,
        "Revenue by Year",
        "Displays year-wise revenue growth trend.",
        """
        SELECT order_year,
               SUM(final_amount_inr) AS revenue
        FROM transactions
        GROUP BY order_year
        ORDER BY order_year;
        """,
    )

    sql_runner(
        3,
        "Electronics Category Revenue",
        "Finds total revenue from Electronics category only.",
        """
        SELECT SUM(final_amount_inr) AS electronics_revenue
        FROM transactions
        WHERE category = 'Electronics';
        """,
    )

    sql_runner(
        4,
        "Festival vs Non-Festival Sales",
        "Compares revenue during festival sales and non-festival periods.",
        """
        SELECT is_festival_sale,
               SUM(final_amount_inr) AS revenue
        FROM transactions
        GROUP BY is_festival_sale;
        """,
    )

    sql_runner(
        5,
        "Top 10 Brands by Units Sold",
        "Identifies brands with highest quantity sold.",
        """
        SELECT brand,
               SUM(quantity) AS total_units_sold
        FROM transactions
        GROUP BY brand
        ORDER BY total_units_sold DESC
        LIMIT 10;
        """,
    )

    sql_runner(
        6,
        "Customer Acquisition by Year",
        "Shows number of new customers acquired each year.",
        """
        SELECT first_year,
               COUNT(customer_id) AS new_customers
        FROM (
            SELECT customer_id,
                   MIN(order_year) AS first_year
            FROM transactions
            GROUP BY customer_id
        )
        GROUP BY first_year
        ORDER BY first_year;
        """,
    )

    sql_runner(
        7,
        "Active Customers per Year",
        "Counts distinct active customers per year.",
        """
        SELECT order_year,
               COUNT(DISTINCT customer_id) AS active_customers
        FROM transactions
        GROUP BY order_year
        ORDER BY order_year;
        """,
    )

    sql_runner(
        8,
        "Overall Return Rate (%)",
        "Calculates percentage of orders that were returned.",
        """
        SELECT
            COUNT(*) * 100.0 / (SELECT COUNT(*) FROM transactions)
            AS return_rate_percentage
        FROM transactions
        WHERE return_status = 'Returned';
        """,
    )

    sql_runner(
        9,
        "Prime vs Non-Prime Revenue",
        "Compares revenue from Prime and Non-Prime customers.",
        """
        SELECT is_prime_member,
               SUM(final_amount_inr) AS revenue
        FROM transactions
        GROUP BY is_prime_member;
        """,
    )

    sql_runner(
        10,
        "High Discount Orders (≥ 30%)",
        "Lists orders with heavy discounts impacting margins.",
        """
        SELECT transaction_id,
               discount_percent,
               final_amount_inr
        FROM transactions
        WHERE discount_percent >= 30
        ORDER BY discount_percent DESC;
        """,
    )


# ============================================================
# BI COMMAND CENTER
# ============================================================
else:
    st.markdown("## BI Command Center")
    st.markdown("**Unified view for executive decision-making**")

    c1, c2, c3 = st.columns(3)
    c1.metric("Revenue", "₹8.4 Bn")
    c2.metric("Customers", "4.2 M")
    c3.metric("Growth", "18.2%")

    st.success(
        "This command center consolidates revenue, customers, products, "
        "and operations into a single executive narrative."
    )
