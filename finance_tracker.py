from transaction import Transaction

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, description):
        transaction = Transaction(amount, description, "income")
        self.transactions.append(transaction)
        print("Income added successfully.")

    def add_expense(self, amount, description):
        transaction = Transaction(amount, description, "expense")
        self.transactions.append(transaction)
        print("Expense added successfully.")

    def get_balance(self):
        balance = 0.0
        for transaction in self.transactions:
            if transaction.type == "income":
                balance += transaction.amount
            elif transaction.type == "expense":
                balance -= transaction.amount
        return balance

    def view_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)
