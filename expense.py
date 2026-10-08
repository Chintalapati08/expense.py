import csv
from datetime import datetime

# ---------------------------
# Load previous expenses
# ---------------------------
def load_expenses(filename="expenses.csv"):
    expenses = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                expenses.append({
                    "date": row[0],
                    "category": row[1],
                    "amount": float(row[2])
                })
    except FileNotFoundError:
        pass
    return expenses

# ---------------------------
# Save expenses to file
# ---------------------------
def save_expenses(expenses, filename="expenses.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])
        for exp in expenses:
            writer.writerow([exp["date"], exp["category"], exp["amount"]])

# ---------------------------
# Add new expense
# ---------------------------
def add_expense(expenses):
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    amount = float(input("Enter amount: "))
    date = datetime.now().strftime("%Y-%m-%d")

    expenses.append({
        "date": date,
        "category": category,
        "amount": amount
    })

    save_expenses(expenses)
    print("Expense added successfully!\n")

# ---------------------------
# View all expenses
# ---------------------------
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet!\n")
        return

    print("\n--- Expense List ---")
    for exp in expenses:
        print(f"Date: {exp['date']} | Category: {exp['category']} | Amount: ₹{exp['amount']}")
    print()

# ---------------------------
# View total
# ---------------------------
def view_total(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Money Spent: ₹{total}\n")

# ---------------------------
# Main Program
# ---------------------------
def main():
    expenses = load_expenses()

    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spending")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            print("Exiting... Goodbye!")
            save_expenses(expenses)
            break
        else:
            print("Invalid choice! Try again.\n")


# Run the program
if __name__ == "__main__":
    main()
