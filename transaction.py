class Transaction:
    def __init__(self, amount, description, trans_type):
        self.amount = amount
        self.description = description
        self.type = trans_type

    def __str__(self):
        return f"{self.type.capitalize()}: ${self.amount:.2f} - {self.description}"
