class Customer():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.accounts = {}

    def create_bank(self, type, id):
        if id not in self.accounts:
            if type == "Checking":
                self.accounts[id] = CheckingAccount(id)
            elif type == "Credit":
                self.accounts[id] = CreditAccount(id)


class Account():
    def __init__(self, id):
        self.id = id
        self.transactions = []


class CheckingAccount(Account):
    def __init__(self, id):
        super().__init__(id)
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append('+' + amount)

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append('-' + amount)


class CreditAccount(Account):
    def __init__(self, id, creditLine):
        super().__init__(id)
        self.creditLine = creditLine
        self.balanceOwed = 0

    def deposit(self, amount):
        if amount > 0:
            self.balanceOwed -= amount
            self.creditLine += amount
            self.transactions.append('+' + amount)

    def withdraw(self, amount):
        if amount <= self.creditLine:
            self.creditLine -= amount
            self.balanceOwed += amount
            self.transactions.append('-' + amount)
