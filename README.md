
# Expense Tracker & Analytics Dashboard

A personal finance dashboard built with Python, Streamlit, Pandas, and SQLite. The application allows users to record expenses, explore spending patterns, and manage transaction history through an interactive interface.

## Features

- Add expenses with an amount, category, description, and date
- Store transactions persistently using SQLite
- Filter expenses by category
- View total spending, transaction counts, and average expenses
- Visualize spending by category and over time
- View transaction history
- Export transactions to CSV
- Delete individual expenses

## Tech Stack

- Python
- Streamlit
- Pandas
- SQLite
- Git and GitHub

## Project Structure

```text
expense-tracker-dashboard/
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
└── README.md
```

The SQLite database is generated locally and excluded from Git.

## Installation

1. Clone the repository.
2. Navigate into the project folder.
3. Create and activate a Python virtual environment.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Start the dashboard:

```bash
streamlit run app.py
```

6. Open the local URL displayed in your terminal.

## How It Works

The application uses Streamlit to provide the user interface, SQLite to store expense records, and Pandas to process transaction data and calculate spending summaries.

When a user adds or deletes an expense, the database is updated and the dashboard refreshes to display the latest information.

## Future Improvements

- Monthly budget limits
- Date-range filtering
- Expense editing
- Additional analytics and visualizations
- Automated tests
