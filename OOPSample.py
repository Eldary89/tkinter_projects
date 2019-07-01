class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"Ownew is:{self.owner} has a balance {self.balance}"

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Sorry you don't have enough balance")


acct1 = Account("Jose", 100)

print(acct1)

print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)
acct1.withdraw(75)
print(acct1.balance)
