from finance_tracker import FinanceTracker

def main():
    tracker = FinanceTracker()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            tracker.add_income(amount, description)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            tracker.add_expense(amount, description)
        elif choice == '3':
            print(f"Current balance: ${tracker.get_balance():.2f}")
        elif choice == '4':
            tracker.view_transaction_history()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
