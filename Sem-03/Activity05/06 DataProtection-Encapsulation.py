'''
How Encapsulation Enhances Data Protection:
Hides Internal State: Encapsulation hides the internal state of an object from the outside world. Only the object's methods can interact with its internal state.
Controlled Access: Through getter and setter methods, encapsulation provides a controlled way of accessing and modifying the data, allowing for validation and error checking.
Prevents Unauthorized Access: By making attributes private, encapsulation prevents direct access to and modification of the data from outside the class.
'''

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount!")

account = BankAccount("123456789", 1000)

print("Initial balance:", account.get_balance()) 

account.deposit(500)
print("Balance after deposit:", account.get_balance())

account.withdraw(2000)

account.withdraw(300)
print("Balance after withdrawal:", account.get_balance())
