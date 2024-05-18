class Bank:
    def __init__(self, account_number, customer_name, initial_balance):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid withdrawal amount. Check balance or amount.")

    def get_balance(self):
        return self.__balance

account = Bank("123456789", "John Doe", 1000.0)
print(account.get_balance())

account.deposit(500)
print(account.get_balance())

account.withdraw(200)
print(account.get_balance())

account.withdraw(1500)
print(account.get_balance())
