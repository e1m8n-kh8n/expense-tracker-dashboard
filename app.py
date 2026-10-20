
import streamlit as st
import pandas as pd
from datetime import date

from database import init_db, add_expense, get_expenses, delete_expense

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)

init_db()

st.title("💰 Expense Tracker & Analytics Dashboard")
st.write("Track your expenses, explore spending patterns, and manage your budget.")

# ADD EXPENSE
st.subheader("Add a New Expense")

with st.form("expense_form", clear_on_submit=True):
    col1, col2 = st.columns(2)

    with col1:
        amount = st.number_input(
            "Amount ($)", min_value=0.01, value=10.00, step=0.01
        )
        category = st.selectbox(
            "Category",
            ["Food", "Shopping", "Transportation",
             "Entertainment", "Bills", "Health", "Other"]
        )

    with col2:
        description = st.text_input("Description")
        expense_date = st.date_input("Date", value=date.today())

    submitted = st.form_submit_button("Add Expense")

    if submitted:
        add_expense(
            round(amount, 2),
            category,
            description,
            expense_date.isoformat()
        )
        st.success("Expense added successfully!")
        st.rerun()

# LOAD EXPENSES
records = get_expenses()

if records:
    df = pd.DataFrame(
        records,
        columns=["ID", "Amount", "Category", "Description", "Date"]
    )

    df["Date"] = pd.to_datetime(df["Date"])

    st.divider()
    st.subheader("Filter Expenses")

    categories = ["All"] + sorted(df["Category"].unique().tolist())
    selected_category = st.selectbox("Filter by category", categories)

    filtered_df = df.copy()

    if selected_category != "All":
        filtered_df = filtered_df[
            filtered_df["Category"] == selected_category
        ]

    # SUMMARY METRICS
    st.subheader("Spending Overview")

    total_spending = filtered_df["Amount"].sum()
    transaction_count = len(filtered_df)
    average_expense = filtered_df["Amount"].mean() if transaction_count else 0

    m1, m2, m3 = st.columns(3)

    m1.metric("Total Spending", f"${total_spending:,.2f}")
    m2.metric("Transactions", transaction_count)
    m3.metric("Average Expense", f"${average_expense:,.2f}")

    # CHARTS
    st.divider()
    st.subheader("Spending Analytics")

    chart1, chart2 = st.columns(2)

    with chart1:
        st.write("Spending by Category")
        category_totals = (
            filtered_df.groupby("Category")["Amount"].sum()
            if not filtered_df.empty else pd.Series(dtype=float)
        )
        st.bar_chart(category_totals)

    with chart2:
        st.write("Spending Over Time")
        daily_totals = (
            filtered_df.groupby("Date")["Amount"].sum()
            if not filtered_df.empty else pd.Series(dtype=float)
        )
        st.line_chart(daily_totals)

    # TRANSACTION HISTORY
    st.divider()
    st.subheader("Transaction History")

    st.dataframe(
        filtered_df.sort_values("Date", ascending=False),
        use_container_width=True,
        hide_index=True
    )

    # DOWNLOAD CSV
    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Expenses as CSV",
        data=csv,
        file_name="expenses.csv",
        mime="text/csv"
    )

    # DELETE EXPENSE
    st.divider()
    st.subheader("Delete an Expense")

    expense_id = st.selectbox(
        "Select Expense ID",
        filtered_df["ID"].tolist(),
        disabled=filtered_df.empty
    )

    if st.button("Delete Selected Expense", disabled=filtered_df.empty):
        delete_expense(int(expense_id))
        st.success("Expense deleted successfully!")
        st.rerun()

else:
    st.info("No expenses yet. Add your first expense above!")
