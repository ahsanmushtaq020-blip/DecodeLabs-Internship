total = 0

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Total Spent")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Add Expense
    if choice == "1":
        expense = float(input("Enter expense amount: "))

        total = total + expense

        print(f"Expense added: {expense}")

    # View Total
    elif choice == "2":
        print(f"Total Spent: {total}")

    # Exit
    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
