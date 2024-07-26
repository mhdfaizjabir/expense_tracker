# Personal Finance Tracker

This is a Personal Finance Tracker developed using Python. It allows users to load, manage, and visualize financial transactions stored in a CSV file.

## Features

- **Add Transactions**: Add new transactions with date, type, category, amount, and description.
- **View Summary**: Display a summary of total income, expenses, savings, and debt.
- **Visualize Data**: Generate visual reports using Matplotlib and Seaborn to show income and expenses over time.
- **Expense Distribution**: Show a pie chart of expenses categorized by type.

##Functions 
### load_data(): Loads transactions from transactions.csv. If the file doesn't exist, it creates an empty DataFrame.
### save_data(data): Saves the given DataFrame to transactions.csv.
### get_date(): Prompts the user to enter a date in YYYY-MM-DD format.
### get_type(): Prompts the user to enter the type of transaction (Income/Expense).
### get_category(): Prompts the user to enter the category of the transaction.
### get_amount(): Prompts the user to enter the amount of the transaction.
### get_description(): Prompts the user to enter a description for the transaction.
### add_transaction(data): Adds a new transaction to the DataFrame.
### get_date_range(): Prompts the user to enter a date range for filtering transactions.
### show_summary(data): Displays a summary of total income, expenses, savings, and debt.
### show_graphs(data): Generates line plots for income and expenses over time.
### show_expense_distribution(data): Displays a pie chart of expenses categorized by type.


## Requirements

- Python 3.x
- Pandas
- Matplotlib
- Seaborn

##Clone the repository : 
-git clone https://github.com/yourusername/personal-finance-tracker.git
-cd personal-finance-tracker
##Run the application :
- python main.py

