
import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "expenses.xlsx"

def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_excel(FILE_NAME)
    else:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])

def save_data(df):
    df.to_excel(FILE_NAME, index=False)

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc.): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note (optional): ")

    df = load_data()
    new_entry = pd.DataFrame([[date, category, amount, note]], columns=df.columns)
    df = pd.concat([df, new_entry], ignore_index=True)
    save_data(df)
    print("✅ Expense added successfully!")

def view_expenses():
    df = load_data()
    if df.empty:
        print("No expenses found.")
    else:
        print("\n--- All Expenses ---")
        print(df)

def show_pie_chart(df):
    summary = df.groupby("Category")["Amount"].sum()
    summary.plot.pie(autopct="%1.1f%%", figsize=(6, 6), title="Expense Breakdown by Category")
    plt.ylabel("")
    plt.show()

def show_line_graph(df):
    df_sorted = df.sort_values("Date")
    df_grouped = df_sorted.groupby("Date")["Amount"].sum()
    df_grouped.plot(kind="line", marker='o', title="Expenses Over Time", figsize=(8, 5))
    plt.xlabel("Date")
    plt.ylabel("Total Amount")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def show_bar_graph(df):
    summary = df.groupby("Category")["Amount"].sum()
    summary.plot(kind="bar", color="skyblue", title="Expenses by Category", figsize=(7, 4))
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def expense_summary():
    df = load_data()
    if df.empty:
        print("No data to display.")
        return

    print("\n--- Summary Menu ---")
    print("1. Pie Chart")
    print("2. Line Graph (Daily Total)")
    print("3. Bar Graph (By Category)")
    choice = input("Enter your choice: ")

    if choice == '1':
        show_pie_chart(df)
    elif choice == '2':
        show_line_graph(df)
    elif choice == '3':
        show_bar_graph(df)
    else:
        print("❌ Invalid choice.")

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Graphical Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            expense_summary()
        elif choice == '4':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
