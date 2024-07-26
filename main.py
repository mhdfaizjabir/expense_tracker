import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

CSV_FILE = "transactions.csv"

def load_data():
    if os.path.exists(CSV_FILE):
        try: 
            data = pd.read_csv(CSV_FILE) 
            if data.empty:
                raise pd.errors.EmptyDataError
        except pd.errors.EmptyDataError:
            data = pd.DataFrame(columns=['Date', 'Type', 'Category', 'Amount', 'Description'])
    else:
        data = pd.DataFrame(columns=['Date', 'Type', 'Category', 'Amount', 'Description'])
    return data

def save_data(data):
    data.to_csv(CSV_FILE, index=False)

def get_date():
    while True:
        date_str = input("Enter the date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_type():
    while True:
        trans_type = input("Enter the type (Income/Expense): ").capitalize()
        if trans_type.lower() in ["income", "expense"]:
            return trans_type.capitalize()
        print("Type must be either 'Income' or 'Expense'.")

def get_category():
    while True:
        category = input("Enter the category: ")
        if category.isalpha():
            return category
        print("Category must contain only letters.")

def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            return amount
        except ValueError:
            print("Amount must be a number.")

def get_description():
    while True:
        description = input("Enter the description: ")
        if all(char.isalpha() or char.isspace() for char in description):
            return description
        print("Description must contain only letters and spaces.")

def add_transaction(data):
    date = get_date()
    trans_type = get_type()
    amount = get_amount()
    
    if trans_type == 'Income':
        category = 'Income'
        description = 'Income'
    else:
        category = get_category()
        description = get_description()
    
    new_transaction = pd.DataFrame({
        'Date': [date],
        'Type': [trans_type],
        'Category': [category],
        'Amount': [amount],
        'Description': [description]
    })
    
    data = pd.concat([data, new_transaction], ignore_index=True)
    save_data(data)
    print("Transaction added successfully.")
    return data

def get_date_range():
    start_date_str = input("Enter the start date (YYYY-MM-DD) or press Enter to include all: ")
    end_date_str = input("Enter the end date (YYYY-MM-DD) or press Enter to include all: ")
    
    start_date = None
    end_date = None

    if start_date_str:
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid start date format. Please use YYYY-MM-DD.")
            return get_date_range()
    
    if end_date_str:
        try:
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid end date format. Please use YYYY-MM-DD.")
            return get_date_range()

    return start_date, end_date

def show_summary(data):
    start_date, end_date = get_date_range()
    
    if start_date and end_date:
        mask = (pd.to_datetime(data['Date']) >= start_date) & (pd.to_datetime(data['Date']) <= end_date)
        data = data.loc[mask]
    elif start_date:
        mask = pd.to_datetime(data['Date']) >= start_date
        data = data.loc[mask]
    elif end_date:
        mask = pd.to_datetime(data['Date']) <= end_date
        data = data.loc[mask]

    total_income = data[data['Type'] == 'Income']['Amount'].sum()
    total_expense = data[data['Type'] == 'Expense']['Amount'].sum()
    savings = total_income - total_expense
    debt = 0
    if savings < 0:
        debt = abs(savings)
        savings = 0
    
    print("\nSummary")
    print(f"Total Income: {total_income} QAR")
    print(f"Total Expense: {total_expense} QAR")
    print(f"Savings: {savings} QAR")
    if debt > 0:
        print(f"Debt: {debt} QAR")
    if total_expense > total_income:
        print("Warning: Your expenses exceed your income!")

def show_graphs(data):
    start_date, end_date = get_date_range()

    if start_date and end_date:
        mask = (pd.to_datetime(data['Date']) >= start_date) & (pd.to_datetime(data['Date']) <= end_date)
        data = data.loc[mask]
    elif start_date:
        mask = pd.to_datetime(data['Date']) >= start_date
        data = data.loc[mask]
    elif end_date:
        mask = pd.to_datetime(data['Date']) <= end_date
        data = data.loc[mask]

    if data.empty:
        print("No data available to display graphs.")
        return
    
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data = data.dropna(subset=['Date'])

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Amount', hue='Type', data=data, estimator=sum)
    plt.title('Income and Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount (QAR)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def show_expense_distribution(data):
    expense_data = data[data['Type'] == 'Expense']
    
    if expense_data.empty:
        print("No expense data available to display.")
        return
    
    expense_summary = expense_data.groupby('Category')['Amount'].sum()
    
    plt.figure(figsize=(10, 6))
    plt.pie(expense_summary, labels=expense_summary.index, autopct='%1.1f%%', startangle=140)
    plt.title('Expense Distribution by Category')
    plt.legend(expense_summary.index, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.tight_layout()
    plt.show()

def main():
    data = load_data()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add a transaction")
        print("2. Show summary")
        print("3. Show graphs")
        print("4. Show expense distribution")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            data = add_transaction(data)
        elif choice == '2':
            show_summary(data)
        elif choice == '3':
            show_graphs(data)
        elif choice == '4':
            show_expense_distribution(data)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
