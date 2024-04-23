class BankAccount:
    def __init__(self, accNumber, balance):
        self.accNumber = accNumber
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds")

acc1 = BankAccount("123456", 1000)
acc1.deposit(500)
acc1.withdraw(200)
acc1.withdraw(1500)
